# Video #1 — Patch Embedding: how transformers ate computer vision

**Concept node:** `edmund/research/ai/cv/PATCH-EMBEDDING.md`
**Papers cited:** `[2020-vit-dosovitskiy]`, `[2021-mae-he]`, `[2021-clip-radford]`
**Length target:** 5:00 (≈750 spoken words)
**Format:** talking head, with occasional cutaways to a diagram or the ViT paper Figure 1.

---

## Working title options
1. **How Transformers Ate Computer Vision (in 5 Minutes)** — hooky, broad
2. **Patch Embedding — the one trick that unlocked modern CV** — specific, keyword-strong
3. **CV Research Journal #1: Patch Embedding** — signals the series, lower ceiling

*My pick:* option 2 for the thumbnail — "Patch Embedding" is a Google-able term that pulls the right audience; "the one trick" is the hook. Save "CV Research Journal #1" as a text overlay on the video itself, so the series identity is there without hurting discoverability.

---

## Script

### [0:00 – 0:20] Cold open + hook

> Around 2020, transformers took over natural language processing. GPT was two years old, BERT had already changed search. And a lot of us watching from the sidelines were asking the same question: **why hasn't this happened to computer vision yet?**
>
> Because it did — in one paper, with one trick. And that trick — patch embedding — is the reason CLIP works, the reason Stable Diffusion works, the reason your phone can now describe a video to you.
>
> I've been reading through computer vision research this week. This is what I learned about that trick, in 5 minutes. Sharing as I go.

*[Optional overlay: your name / "CV Research Journal #1"]*

### [0:20 – 1:20] What was the problem

> Transformers were built for language. They take a sequence of word tokens, and they let every word attend to every other word. That's how they learn context: "bank" near "river" is different from "bank" near "money."
>
> That works for language because language *is* a sequence of tokens. Words come one after another. There's an order. There's a natural granularity.
>
> Images don't work like that. An image is a 2D grid of pixels. There's no natural "first word" in an image. A 512x512 photo has a quarter-million pixels — you can't attend every pixel to every other pixel, that's 60 billion pairs. And even if you could, individual pixels don't mean anything. A red pixel is just red. A word carries meaning; a pixel doesn't.
>
> So for years, computer vision used convolutions instead — small filters that scan across the image looking for edges, then textures, then shapes. It worked. But it meant vision and language were solved by completely different machinery.

### [1:20 – 3:00] The trick — patch embedding

> Here's what the Vision Transformer paper did — and it's almost embarrassingly simple.
>
> Take the image. Cut it into small squares — patches. Usually 16 by 16 pixels each. So a 224 by 224 image becomes a 14 by 14 grid of patches — 196 of them.
>
> Now, for each patch, flatten it. A 16 by 16 patch with 3 color channels is 768 numbers. Push those 768 numbers through a single linear layer. Out comes a vector. Call that vector a *token*.
>
> That's it. You now have 196 tokens per image. Feed them into a standard transformer — the same architecture as GPT — and let every patch attend to every other patch.
>
> *[Diagram cutaway: ViT Figure 1 — image → grid → tokens → transformer]*
>
> Two small details matter. First: transformers don't care about order — words could be shuffled and the attention would still work — so we add a *position embedding* to each token, a learnable vector that says "you are patch number 47, top-right area." That gives the model spatial awareness.
>
> Second: we prepend one extra "class token" — a learnable vector that isn't tied to any patch. After the transformer runs, we read out that token's final state and use it as the image's summary representation. Same trick BERT uses.
>
> And that's the whole thing. Patches as words. Position embeddings as location. Class token as summary. No convolutions anywhere.

### [3:00 – 3:50] Why it mattered so much

> Now — this looks like a small change. But it's the reason everything downstream became possible.
>
> Once images and text both come into the model as *token sequences*, you can train one model on both. That's exactly what CLIP does — image tokens on one side, text tokens on the other, learn to match them.
>
> Once you can mask random patches and ask the model to fill them back in — like BERT does for words — you get MAE, self-supervised pretraining on images with no labels needed.
>
> Once you can cut *video* into patches across space and time — call them cubelets — you get VideoMAE, and every modern video model.
>
> Patch embedding is the interface. Every modern computer vision system starts here.

### [3:50 – 4:35] Why I'm going deep on this

> The reason I'm going deep on this: I want to actually understand how modern AI systems that see and reason about the world work — not just at the API level, but from the primitives up.
>
> Every model doing anything interesting with images or video right now — CLIP, LLaVA, Stable Diffusion, Qwen2-VL — starts with patch embedding. Same trick, extended, layered, combined. If you don't understand this one, you're one level too shallow to reason about anything above it.
>
> So this is video 1 of a series. I'm walking through the concepts I'm learning, one per video, and by the end you'll have the same map I'm building — from patches all the way up to systems that reason across long-form video.

### [4:35 – 5:00] Close + hook to next

> Next up: **CLIP** — the paper that took patch embedding, added a text encoder, and taught a model to match images to captions from 400 million pairs scraped off the internet. That's the paper that made zero-shot image classification real.
>
> If this was useful, subscribe — I'm posting one of these most days through August. And if you spot something I've got wrong, tell me in the comments. I'm learning in public, so wrong-in-public is part of the deal. See you tomorrow.

---

## YouTube description

Patch embedding is the trick that let transformers take over computer vision — and it's simpler than you'd expect. In this first video I break down how the Vision Transformer (Dosovitskiy et al. 2020) reshapes images into token sequences, and why that one interface change unlocked CLIP, MAE, Stable Diffusion, and every modern video-language model.

I'm learning modern computer vision in public — one concept per video, roughly through August 2026.

📚 Paper: An Image is Worth 16x16 Words (arXiv:2010.11929)
🗺️ My concept-node graph: [link to GitHub repo]
🔬 Reproducible code + experiments: [link to GitHub repo]

Chapters:
0:00 - The question
0:20 - Why transformers didn't work on images
1:20 - The trick: patch embedding
3:00 - Why it mattered
3:50 - Why I'm going deep on this
4:35 - What's next

---

## Suggested tags
`computer vision, vision transformer, ViT, patch embedding, deep learning, ai research, transformers, machine learning, cv research, self-supervised learning`

---

## Delivery notes

**Script pacing**
- 750 words at ~150 wpm = 5:00 exactly. If you naturally speak faster (180 wpm), aim for ~900 words and cut later. Slower speakers should cut ~100 words.
- Slow down on the definition ("cut it into small squares... flatten... push through a linear layer"). Everything else can move fast.
- Pause after "*embarrassingly simple*" and after "*Patch embedding is the interface*." These are the lines that carry.
- Cut candidate if over time: the second half of the [0:20-1:20] block (the "individual pixels don't mean anything" tangent). Teacherly and not load-bearing.
- Retake trigger: if you stumble on "patch embedding is the interface" — retake. It's the load-bearing sentence of the video.

**Talking-head practical**
- Frame yourself from mid-chest up, camera at eye level. Below eye level makes you look unsure; above makes you look small.
- Look at the lens, not the screen. Cover the preview window with a Post-it if it pulls your eyes.
- Natural window light beats any indoor lamp — face the window, don't backlight yourself. If recording at night, one lamp above and slightly behind the camera.
- One take through, don't stop for small stumbles. Fix stumbles in one clean take of the individual line and cut it in.
- Wear something one shade darker than your background — separation matters more than what you wear.

**Cutaway plan (light editing)**
- [1:40] cutaway to ViT Figure 1 (the model diagram) — freeze on it for ~10s while you describe patches → tokens.
- [3:15] optional cutaway to a montage of paper titles (CLIP, MAE, VideoMAE, Qwen2-VL) as you name them.
- Everything else: stay on face.

**Publishing checklist before you hit upload**
- Thumbnail with the phrase "patch embedding" visible + a grid/patch visual
- Chapter markers pasted into description (already drafted above)
- End screen linking to your channel + a placeholder "video 2 coming tomorrow"
- First pinned comment: link to the ViT paper
