# Banco de Talentos

Catálogo visual dos agentes do repositório. Abra `index.html` no navegador.

Cada agente tem uma ficha com: o que faz pelo negócio, hierarquia no bloco, nível de acesso,
para quem serve, habilidades, o que pode desenvolver, agentes parecidos e qualidade da ficha.

| Arquivo | Papel |
| --- | --- |
| `curation.txt` | Avaliação manual de cada agente: bloco, hierarquia, acesso, escopo e resumo. Edite aqui. |
| `build.py` | Lê os agentes e a curadoria, calcula similaridade e gera `index.html`. Também guarda os grupos sugeridos. |
| `template.html` | Layout e interação da página. |
| `index.html` | Página gerada. Não edite à mão. |

Depois de adicionar, remover ou reavaliar um agente:

```bash
python3 examples/talent-pool/build.py
```

O script para com erro se algum agente não tiver linha em `curation.txt`.

Hierarquia, acesso e escopo são avaliação editorial, não algo declarado nos arquivos dos agentes.
