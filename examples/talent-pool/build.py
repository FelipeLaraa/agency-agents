#!/usr/bin/env python3
"""Gera examples/talent-pool/index.html: o banco de talentos visual dos agentes.

Uso (na raiz do repositório):  python3 examples/talent-pool/build.py

Junta três fontes:
  1. os arquivos de agente (frontmatter + seções) -> habilidades, entregáveis, tamanho
  2. curation.txt -> bloco, hierarquia, acesso, escopo e resumo de negócio (julgamento humano)
  3. similaridade TF-IDF entre os textos -> agentes parecidos e grupos sugeridos
"""
import collections
import glob
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SKIP = ("integrations", "strategy", "examples", "scripts")

BLOCOS = {
    "dir": ("Direção & Estratégia", "#b4532a"),
    "mkt": ("Marketing & Conteúdo", "#c2410c"),
    "ads": ("Mídia Paga", "#a16207"),
    "ven": ("Vendas & Receita", "#047857"),
    "cx": ("Atendimento & Sucesso", "#4d7c0f"),
    "prd": ("Produto", "#a21caf"),
    "des": ("Design & UX", "#be185d"),
    "eng": ("Engenharia de Software", "#1d4ed8"),
    "dia": ("Dados & IA", "#0e7490"),
    "ops": ("Infra & Confiabilidade", "#0369a1"),
    "sec": ("Segurança", "#b91c1c"),
    "qa": ("Qualidade & Testes", "#b45309"),
    "agt": ("Agentes & Automação", "#4338ca"),
    "fin": ("Finanças", "#15803d"),
    "pop": ("Pessoas & Operações", "#6d28d9"),
    "pm": ("Gestão de Projetos", "#0284c7"),
    "jur": ("Jurídico & Privacidade", "#57534e"),
    "vert": ("Setores específicos", "#0f766e"),
    "game": ("Games", "#7e22ce"),
    "gis": ("Geoespacial (GIS)", "#0d9488"),
    "xr": ("XR & Espacial", "#0891b2"),
    "acad": ("Pesquisa & Academia", "#7c3aed"),
}

# Grupos sugeridos: agentes com função parecida. `acao` é a recomendação.
GRUPOS = [
    ("QA com evidência", ["testing-evidence-collector", "testing-reality-checker"], "fundir",
     "O par mais parecido do repositório. Os dois exigem prova antes de aprovar. Um coleta, o outro decide. Dá para ser um agente só com dois modos."),
    ("Performance de CMS", ["engineering-drupal-performance", "engineering-wordpress-performance"], "fundir",
     "Mesma estrutura e mesmo roteiro, só troca a plataforma. Um agente de performance com um capítulo por CMS resolve."),
    ("Loja em CMS", ["engineering-drupal-shopping-cart", "engineering-wordpress-shopping-cart"], "fundir",
     "Mesmo caso do par acima: catálogo, pagamento e checkout, mudando só Drupal ou WooCommerce."),
    ("Acessibilidade", ["testing-accessibility-auditor", "engineering-section-508-specialist"], "lider",
     "O auditor WCAG cobre o geral. O de Section 508 só importa para quem vende ao governo dos EUA."),
    ("Atendimento ao cliente", ["customer-service", "support-support-responder", "healthcare-customer-service",
                                "hospitality-guest-services", "retail-customer-returns"], "lider",
     "Um atendente genérico mais variações por setor. Escolha o genérico e só puxe o do seu setor, se existir."),
    ("Analistas financeiros", ["finance-financial-analyst", "finance-fpa-analyst", "support-finance-tracker",
                               "chief-financial-officer"], "lider",
     "Três analistas com orçamento, previsão e fluxo de caixa sobrepostos, abaixo do CFO. Para empresa pequena, CFO mais um analista basta."),
    ("Pós-venda e retenção", ["sales-account-strategist", "customer-success-manager"], "fundir",
     "Os dois cuidam de expansão, reuniões de resultado e retenção de receita. Diferença é mais de nome do que de trabalho."),
    ("Prospecção ativa", ["sales-outbound-strategist", "sales-outreach"], "fundir",
     "Um desenha a sequência, o outro executa a abordagem. Na prática fazem o mesmo trabalho de prospecção B2B."),
    ("Gestão de projetos", ["project-management-studio-producer", "project-management-project-shepherd",
                            "project-management-studio-operations", "project-manager-senior"], "lider",
     "Quatro gerentes com prazo, recurso e risco em comum. Um líder de portfólio mais um condutor de projeto cobre quase tudo."),
    ("Infra e operação", ["engineering-devops-automator", "support-infrastructure-maintainer", "engineering-sre"], "lider",
     "Automação, manutenção e confiabilidade da mesma infraestrutura. Para time pequeno é uma pessoa só."),
    ("Privacidade e conformidade", ["data-privacy-officer", "support-legal-compliance-checker",
                                    "engineering-privacy-engineer"], "manter",
     "Tema igual, camadas diferentes: o encarregado define a política, o verificador confere, o engenheiro implementa no código."),
    ("Segurança de aplicação", ["security-architect", "security-appsec-engineer", "security-senior-secops",
                                "security-ai-generated-code-auditor"], "lider",
     "Todos revisam código e modelam ameaças. Um arquiteto mais um revisor de código é suficiente para a maioria."),
    ("Ser encontrado por IA", ["marketing-ai-citation-strategist", "marketing-aeo-foundations",
                               "marketing-agentic-search-optimizer"], "lider",
     "Três ângulos do mesmo assunto novo: ser citado, ser lido e ser usado por IAs. Comece pelo de citação."),
    ("Redes sociais por plataforma", ["marketing-social-media-strategist", "marketing-instagram-curator",
                                      "marketing-tiktok-strategist", "marketing-twitter-engager",
                                      "marketing-reddit-community-builder", "marketing-linkedin-content-creator",
                                      "marketing-video-optimization-specialist"], "lider",
     "Um estrategista geral e um agente por rede. Puxe só as redes em que a marca realmente atua."),
    ("Plataformas chinesas", ["marketing-china-market-localization-strategist", "marketing-xiaohongshu-specialist",
                              "marketing-wechat-official-account", "marketing-zhihu-strategist",
                              "marketing-weibo-strategist", "marketing-douyin-strategist",
                              "marketing-kuaishou-strategist", "marketing-bilibili-content-strategist",
                              "marketing-baidu-seo-specialist", "marketing-podcast-strategist",
                              "marketing-private-domain-operator", "marketing-china-ecommerce-operator",
                              "marketing-livestream-commerce-coach", "marketing-multi-platform-publisher"], "arquivar",
     "Catorze agentes só de marketing na China. Se você não vende lá, pode ignorar o bloco inteiro."),
    ("Podcast", ["marketing-global-podcast-strategist", "marketing-podcast-strategist"], "lider",
     "Mesmo trabalho em dois mercados. O global serve fora da China, o outro só lá."),
    ("Relatório de vendas em três peças", ["sales-data-extraction-agent", "data-consolidation-agent",
                                         "report-distribution-agent"], "fundir",
     "Três agentes curtos que formam uma única esteira: extrair, consolidar, distribuir. Sozinhos não fazem sentido."),
    ("Interface e UX", ["design-ui-designer", "design-ux-architect", "design-ui-finish-gate-reviewer"], "lider",
     "Sistema visual e fundação de UX se sobrepõem bastante. O revisor final é complementar."),
    ("Relação com desenvolvedores", ["specialized-developer-advocate", "marketing-developer-community-builder",
                                     "product-dx-engineer"], "lider",
     "Conteúdo, comunidade e experiência do dev. Só interessa se o seu cliente é desenvolvedor."),
    ("Banco de dados", ["engineering-database-optimizer", "engineering-database-reliability-engineer",
                        "engineering-gaussdb-expert"], "manter",
     "Otimização e confiabilidade são trabalhos diferentes. O de GaussDB é uma variação regional do otimizador."),
]

LANGS = {
    "python": "Python", "py": "Python", "javascript": "JavaScript", "js": "JavaScript", "jsx": "React",
    "typescript": "TypeScript", "ts": "TypeScript", "tsx": "React", "sql": "SQL", "bash": "Shell", "sh": "Shell",
    "shell": "Shell", "yaml": "YAML/Config", "yml": "YAML/Config", "json": "JSON", "html": "HTML", "css": "CSS",
    "scss": "CSS", "php": "PHP", "rust": "Rust", "go": "Go", "swift": "Swift", "kotlin": "Kotlin", "java": "Java",
    "csharp": "C#", "cs": "C#", "cpp": "C++", "c": "C", "lua": "Lua", "luau": "Lua", "gdscript": "GDScript",
    "glsl": "Shader", "hlsl": "Shader", "gdshader": "Shader", "solidity": "Solidity", "hcl": "Terraform",
    "terraform": "Terraform", "dockerfile": "Docker", "markdown": "Documento", "md": "Documento", "xml": "XML",
    "toml": "YAML/Config", "ini": "YAML/Config", "graphql": "GraphQL", "ruby": "Ruby", "dart": "Dart",
    "vue": "Vue", "twig": "PHP", "promql": "Monitoramento", "nginx": "YAML/Config", "mermaid": "Diagrama",
}


def clean(s):
    s = re.sub(r"[`*_#]", "", s)
    s = re.sub(r"[^\w\s.,:;/&()+'’\"%$€—–\-?!<>=@\[\]]", "", s, flags=re.UNICODE)
    return re.sub(r"\s+", " ", s).strip(" :-—–")


def parse(path):
    text = open(path, encoding="utf-8").read()
    if not text.startswith("---"):
        return None
    _, fm, body = text.split("---", 2)
    meta, services = {}, []
    for line in fm.splitlines():
        m = re.match(r"^([A-Za-z_-]+):\s*(.*)", line)
        if m:
            meta[m.group(1)] = m.group(2).strip().strip('"').strip("'")
        m = re.match(r"^\s+-\s+name:\s*(.+)", line)
        if m:
            services.append(m.group(1).strip().strip('"'))
    return meta, services, body


def sections(body):
    out, cur, in_fence = [], None, False
    for line in body.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        if not in_fence and line.startswith("## "):
            cur = [clean(line[3:]).lower(), []]
            out.append(cur)
        elif cur:
            cur[1].append(line)
    return out


def items(lines, cap=8):
    """Subtítulos ### de uma seção; se não houver, os tópicos de primeiro nível."""
    subs, bullets, in_fence = [], [], False
    for line in lines:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if line.startswith("### "):
            subs.append(clean(line[4:]))
        elif re.match(r"^[-*] ", line):
            b = line[2:]
            m = re.match(r"\*\*(.+?)\*\*", b)
            b = clean(m.group(1) if m and len(m.group(1)) > 12 else b)
            bullets.append(b if len(b) <= 90 else b[:87].rsplit(" ", 1)[0] + "…")
    picked = subs if len(subs) >= 2 else bullets
    seen, res = set(), []
    for p in picked:
        if p and p.lower() not in seen and len(p) > 3:
            seen.add(p.lower())
            res.append(p)
    return res[:cap]


def find(secs, *keys):
    for title, lines in secs:
        if any(k in title for k in keys):
            got = items(lines)
            if got:
                return got
    return []


def main():
    cur = {}
    for line in open(os.path.join(HERE, "curation.txt"), encoding="utf-8"):
        if line.strip() and not line.startswith("#"):
            stem, bloco, lvl, acc, scope, pt = line.rstrip("\n").split("|", 5)
            cur[stem] = (bloco, int(lvl), int(acc), scope, pt)

    divisions = json.load(open(os.path.join(ROOT, "divisions.json")))["divisions"]
    agents, bodies = [], {}
    for path in sorted(glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True)):
        rel = os.path.relpath(path, ROOT)
        if rel.split(os.sep)[0] in SKIP or os.sep not in rel:
            continue
        parsed = parse(path)
        if not parsed:
            continue
        meta, services, body = parsed
        stem = os.path.basename(rel)[:-3]
        if stem not in cur:
            sys.exit(f"ERRO: {rel} não está em curation.txt. Adicione uma linha para ele.")
        bloco, lvl, acc, scope, pt = cur[stem]
        secs = sections(body)
        titles = " | ".join(t for t, _ in secs)
        langs = collections.Counter(
            LANGS[l.lower()] for l in re.findall(r"^\s*```([A-Za-z]+)", body, re.M) if l.lower() in LANGS)
        words = len(body.split())
        bodies[stem] = body
        agents.append({
            "id": stem, "path": rel, "name": meta.get("name", stem), "emoji": meta.get("emoji", ""),
            "vibe": meta.get("vibe", ""), "desc": meta.get("description", ""),
            "div": divisions.get(rel.split(os.sep)[0], {}).get("label", rel.split(os.sep)[0]),
            "bloco": bloco, "lvl": lvl, "acc": acc, "scope": scope, "pt": pt,
            "skills": find(secs, "core mission", "core capabilit", "specialized skills", "domain expertise",
                           "core competenc", "capabilities"),
            "deliv": find(secs, "deliverable", "tooling", "tech stack"),
            "langs": [l for l, _ in langs.most_common(6)],
            "tools": [t.strip() for t in meta.get("tools", "").split(",") if t.strip()],
            "services": services, "words": words,
            "has": [int(k in titles) for k in ("rules", "workflow", "metrics", "deliverable", "when not to use")],
        })
    missing = set(cur) - {a["id"] for a in agents}
    if missing:
        sys.exit(f"ERRO: curation.txt cita agentes que não existem: {sorted(missing)}")

    # --- similaridade TF-IDF (ignora linhas que aparecem em 3+ arquivos) ---
    norm = lambda l: re.sub(r"[^a-z ]", "", l.lower()).strip()
    line_count = collections.Counter()
    for b in bodies.values():
        line_count.update({norm(x) for x in b.splitlines()})
    tf, df = {}, collections.Counter()
    for k, b in bodies.items():
        txt = " ".join(l for l in b.splitlines() if line_count[norm(l)] < 3)
        tf[k] = collections.Counter(re.findall(r"[a-z][a-z0-9+#.-]{2,}", txt.lower()))
        df.update(tf[k].keys())
    n = len(bodies)
    vec = {}
    for k, c in tf.items():
        v = {w: (1 + math.log(f)) * math.log(n / df[w]) for w, f in c.items() if df[w] < n * 0.5}
        length = math.sqrt(sum(x * x for x in v.values())) or 1
        vec[k] = {w: x / length for w, x in v.items()}
    keys = list(vec)
    sim = collections.defaultdict(dict)
    for i, a in enumerate(keys):
        for b in keys[i + 1:]:
            va, vb = (vec[a], vec[b]) if len(vec[a]) < len(vec[b]) else (vec[b], vec[a])
            s = sum(x * vb.get(w, 0) for w, x in va.items())
            sim[a][b] = sim[b][a] = s
    for a in agents:
        top = sorted(sim[a["id"]].items(), key=lambda kv: -kv[1])[:3]
        a["sim"] = [[k, round(s * 100)] for k, s in top if s >= 0.2]

    grupos = []
    for titulo, membros, acao, nota in GRUPOS:
        for m in membros:
            if m not in bodies:
                sys.exit(f"ERRO: grupo '{titulo}' cita agente inexistente: {m}")
        pares = [sim[x][y] for i, x in enumerate(membros) for y in membros[i + 1:]]
        grupos.append({"t": titulo, "m": membros, "a": acao, "n": nota,
                       "max": round(max(pares) * 100), "avg": round(sum(pares) / len(pares) * 100),
                       "words": sum(len(bodies[m].split()) for m in membros)})

    allp = [sim[a][b] for i, a in enumerate(keys) for b in keys[i + 1:]]
    stats = {"max": round(max(allp) * 100), "over40": sum(1 for s in allp if round(s * 100) >= 40)}
    data = {"agents": agents, "grupos": grupos, "stats": stats,
            "blocos": {k: {"n": v[0], "c": v[1]} for k, v in BLOCOS.items()}}
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
    out = os.path.join(HERE, "index.html")
    page = tpl.replace("/*__DATA__*/null", payload)
    head = ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n</head>\n<body>\n')
    open(out, "w", encoding="utf-8").write(head + page + "</body>\n</html>\n")
    if len(sys.argv) > 1:  # caminho opcional: só o miolo, para publicar onde o <head> já é fornecido
        open(sys.argv[1], "w", encoding="utf-8").write(page)
    print(f"{len(agents)} agentes, {len(grupos)} grupos -> {os.path.relpath(out, ROOT)} ({os.path.getsize(out) // 1024} KB)")
    no_sk = [a["id"] for a in agents if not a["skills"]]
    no_dl = [a["id"] for a in agents if not a["deliv"] and not a["langs"]]
    print(f"sem habilidades extraídas: {len(no_sk)} {no_sk[:12]}")
    print(f"sem entregáveis extraídos: {len(no_dl)} {no_dl[:12]}")


if __name__ == "__main__":
    main()
