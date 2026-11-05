# 🎞️ Knowledge Module — Motion Graphics & Animated Objects (for a video-editor agent)

> **How to use this:** paste this whole block into your existing video-editor agent, under a heading like `## Motion Graphics & Animated Objects`. It is a *knowledge module*, not a standalone agent — it has no identity/frontmatter of its own, so it inherits your editor's persona. Tooling is **hybrid**: CapCut Pro for fast day-to-day cutting, After Effects / DaVinci Fusion for high-impact pieces. Optimized for short-form vertical video (Reels / TikTok / Shorts) in the **real-estate** niche, with retention as the north star.

---

## Animation Fundamentals (the non-negotiables)

- **Keyframes = start state + end state; the software interpolates between them.** You animate four core properties: position, scale, rotation, opacity. Everything else is a combination of these.
- **Easing is the soul.** Linear motion looks mechanical and cheap. Always apply ease-in / ease-out (Bezier curves). A graphic that accelerates in and decelerates to a stop reads as "professional"; a linear one reads as "template."
- **Overshoot & bounce add life.** Let an object slightly pass its endpoint and settle back (elastic/bounce). This is what makes a price tag "snap" in instead of sliding in dead.
- **Spacing = speed.** Tighter keyframe spacing = faster action; wider = slower. Control rhythm with spacing, not just duration.
- **Short-form timing rule:** keep each text/object animation to **0.3–0.5s** in and out. Slower drags the pace; faster is unreadable.
- **Motion serves the narrative and the retention, never the ego.** If a hard cut works, don't add a fancy transition. Every animated element must earn its place by directing attention to value or holding the viewer — decoration that does neither gets cut.
- **Respect readability and reduced motion.** Never block faces, never strobe, keep text legible against the footage, and don't over-animate business content into chaos.

---

## Animated Objects & Graphics ("objetos animados")

The core of what you're adding. Each is an on-screen element that animates in, holds, and animates out:

- **Lower-thirds** — agent name + CRECI, brokerage logo, listing title. Animate in with a slide + fade + subtle bar wipe; hold 3–5s; animate out before it overstays.
- **Callout tags** — price, m², bedrooms/baths, neighborhood — **pop/bounce in**, pinned near the on-screen element they describe. Use a connector line/arrow to the feature.
- **Running graphics / animated data** — **number counters** (price, ROI, % appreciation counting up), bar/pie reveals, progress bars, comparison bars (this listing vs. market avg). The count-up animation itself is a retention device.
- **Floating fonts / kinetic typography** — text that drifts with subtle parallax, tracks to a subject, or rotates in 3D (covered in its own section below).
- **Attention directors** — animated arrows, circles, highlights, blur-the-rest spotlight, zoom-punch onto a detail. Point the eye exactly where the value is.
- **Map & location** — pin drop with bounce, radius/coverage reveal, "X min to downtown" animated route.
- **Floor-plan reveal** — stroke draw-on of the plan lines + room labels fading in sequentially; great for "tour the layout" segments.
- **Before/After** — slider wipe, split-screen, or luma-mask reveal for renovations / virtual staging.
- **Stamps & stickers** — "VENDIDO / SOLD", "NOVO", "EXCLUSIVO" rubber-stamp slam-in with a shake and a sound effect.
- **Match-move / tracking** — lock a graphic to a moving element in the footage (corner-pin a logo to a wall, pin a price to a house). Done with CapCut keyframe tracking for simple moves, or AE Mocha / planar + 3D camera tracking for complex ones.

---

## Kinetic Typography & Floating Fonts

- **Entrances:** typewriter/character-by-character (suspense, tech feel), bounce-in (playful), handwriting/stroke draw-on (artisanal, educational), glitch + chromatic aberration (tech/urban), 3D rotate (premium feel).
- **Floating text:** subtle continuous drift + parallax depth (foreground text moves more than background) sells dimensionality; optionally track the text to a subject so it "sticks" to the scene.
- **Layering for legibility (always ≥2 layers):** bottom stroke/shadow → mid color fill → top highlight/gloss. Decorative text color must contrast the frame (bright text on dark frames; dark text + stroke on bright frames).
- **Keyword emphasis:** pop the key word in a hot color (red/yellow), with a shake or pulse-scale on the beat. In real estate, pop the **number** — price, m², % — never the filler words.
- **Burned-in captions (sound-off is the default viewing mode):** word-by-word karaoke highlight, big bold sans, high contrast, lower third, inside the safe zone. AI auto-caption → manual review for names/addresses/numbers.

---

## Transitions Engineered for Retention

- **Hook in the first 1–2 seconds** with a motion pattern-interrupt (a graphic slamming in, a whip-pan reveal, a number counting). Then re-hook with a visual change every 3–5s.
- **High-impact transition types:** whip-pan (motion-blur swipe between scenes), **mask transition** (use a doorframe, wall, or hand in-frame as the wipe — very high impact for property tours), zoom/warp punch, luma/gradient wipe, morph cut (seamless jump-cut for talking head).
- **Speed ramping (fast-slow-fast):** pre-action slow build → action at normal speed → slow-motion savor. Return to normal speed on the BGM downbeat. Shoot at 60/120fps for clean slow-mo — 24/30fps footage stutters when slowed.
- **Cut to the beat,** but only on strong beats and transition points — cutting on every beat causes rhythm fatigue.
- **Principle:** the transition serves the narrative. A mask wipe through a doorway earns its place; a random "fancy" transition between two static shots does not.

---

## Real-Estate Animated Kit (ready-made ideas)

- **Price reveal:** counter animating up to the value + bounce-in tag + optional "VENDIDO" slam.
- **Spec bar:** animated icon row — 🛏 3 · 🛁 2 · 📐 120m² · 🚗 2 — each icon popping in sequence.
- **Neighborhood intro:** map pin drop + "5 min do metrô" route animation + photo callouts of nearby landmarks.
- **Floor-plan tour:** line draw-on of the plan, room labels fading in as the camera/clip moves through each space.
- **Before/After renovation:** slider wipe or split with animated divider.
- **CTA lower-third:** "Agende a visita" + phone/WhatsApp + CRECI, pulsing gently to draw the tap.
- **Stills with life:** Ken Burns (slow push/pan) + parallax on photos so a static listing photo still moves.
- **Virtual-staging callouts:** arrows/tags pointing to "sala ampliada", "cozinha integrada".

---

## Tooling (hybrid — when to use which)

- **CapCut Pro (day-to-day, fast):** keyframe curves, mask animation, speed curves, built-in particle/sticker effects, one-tap transitions, AI auto-captions (95%+), AI smart cutout (no green screen). Use for 80% of cuts and anything on a tight turnaround. Limits: weak at complex VFX, less color precision.
- **After Effects (high-impact pieces):** Particular for particles, Mocha for planar tracking, **expressions** (`wiggle()` for organic float, `loopOut()` for cycles, time-based motion), shape layers for clean vector graphics, and **MOGRTs / Essential Graphics** to build reusable branded templates (price tag, lower-third, spec bar) that drop into Premiere.
- **DaVinci Fusion (free powerhouse):** node-based VFX + particle system, industry-standard color (DaVinci color panel), Fairlight audio. Use when you want AE-class compositing without the subscription.
- **Lottie / Bodymovin:** export lightweight vector animations for reuse across pieces and platforms; great for recurring brand graphics.
- **Rule of thumb:** build the **brand template once** (in AE/Fusion as MOGRT/Lottie or as a CapCut template) and reuse it — consistency + speed. Reach for AE/Fusion only when CapCut can't achieve the look.

---

## Particle & VFX (atmosphere, not the star)

- Common uses: light bokeh, dust motes, sparks, confetti (for "SOLD"), light leaks, soft glow on a premium listing.
- CapCut: built-in particle stickers (one-tap). AE/Fusion: Particular / Fusion particle system for custom.
- **Principle:** particles enhance atmosphere; they never steal the show. If the viewer notices the particles more than the property, cut them.

---

## Technical Specs & Guardrails

- **Canvas:** vertical 9:16, 1080×1920. Edit at 24–30fps; **shoot** 60/120fps for slow-mo headroom.
- **Platform safe zones:** keep key graphics and captions out of the bottom ~20% and right edge (platform UI covers them); captions in the lower third but inside a 10–15% margin from all edges.
- **Legibility:** every caption gets at least one of — semi-transparent backdrop bar, stroke, or drop shadow.
- **Discipline:** text animations 0.3–0.5s; don't animate more than ~2 elements at once; don't let effects slow the pace — pacing beats polish in short form.
- **Export:** H.264/H.265, high bitrate for vertical (≈10–16 Mbps at 1080p) to survive platform re-compression.

---

## Rules (paste-ready, numbered)

1. **Ease everything.** No linear keyframes — ease-in/out (Bezier) on every animated property, always.
2. **0.3–0.5s per text/object animation.** Snappy in, snappy out; never let a graphic drag the pace.
3. **Every animated element directs attention to value or holds the viewer.** If it does neither, delete it.
4. **If a hard cut works, don't add a transition.** Motion serves the narrative, not the ego.
5. **Hook in ≤2s with a motion pattern-interrupt,** then re-hook with a visual change every 3–5s.
6. **Pop the number, not the filler.** In real estate the price, m², and % are the stars of the typography.
7. **Captions are always on** (viewers watch sound-off); word-by-word highlight, high contrast, ≥2 legibility layers.
8. **Never block faces; stay inside the safe zone;** keep graphics out of the bottom 20% and right edge.
9. **Overshoot/bounce for life,** but keep it subtle on business content — liveliness, not chaos.
10. **Pin callouts to the feature they describe** with a connector; a floating tag with no anchor confuses.
11. **Build the brand template once and reuse it** (MOGRT / Lottie / CapCut template) — consistency and speed.
12. **CapCut by default; AE/Fusion only when CapCut can't get the look.** Don't over-engineer a 30-second cut.
13. **Shoot 60/120fps when slow-mo is planned;** never slow 24/30fps footage and expect smooth motion.
14. **Cut on strong beats only,** not every beat — rhythm fatigue kills retention.
15. **Particles and VFX enhance atmosphere, never steal the show.**
16. **Respect reduced motion and readability** — no strobing, no unreadable speed, no motion that induces nausea.
17. **Match-move graphics to moving footage** (corner-pin/track) so overlays feel part of the scene, not stuck on glass.
18. **One clear CTA per video,** animated to draw the tap ("Agende a visita" + contact), placed in the safe zone.
