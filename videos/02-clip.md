# Video #2 — CLIP: how the internet became labeled training data

**Concept nodes:** `edmund/research/ai/cv/CONTRASTIVE-IMAGE-TEXT-PRETRAINING.md`, `edmund/research/ai/cv/ZERO-SHOT-CLASSIFICATION-VIA-TEXT-PROMPTS.md`
**Papers cited:** `[2021-clip-radford]`
**Length target:** 5:00 (≈750 spoken words)
**Format:** talking head, with occasional cutaways to a diagram of the contrastive matrix and the CLIP paper's prompt-template figure.

---

## Working title options
1. **CLIP — how the internet became labeled training data** — my pick, ambiguity in the title pulls the click
2. **The paper that killed ImageNet** — provocative, high-stakes, may over-promise
3. **How OpenAI taught AI to see, without labels** — safe, keyword-strong, less distinctive

*My pick:* option 1 for the thumbnail. It reframes the paper as a data story rather than an architecture story, and "the internet as training data" is a hook most technical viewers haven't heard phrased that directly.

---

## Script

### [0:00 – 0:25] Cold open + hook

> Before 2021, if you wanted a computer vision model that could recognize a thousand classes of objects, you needed a thousand-class labeled dataset. Someone had to sit down and label millions of images by hand. That's how ImageNet was built. Fifteen years of academic labor.
>
> Then OpenAI released a paper called CLIP. And CLIP said: **what if we don't do that.** What if we use the internet — where every image already comes with text next to it — as the training signal?
>
> Four hundred million image-text pairs later, they had a model that could classify anything you could describe in English. No labels. No fixed categories. Just: scrape the internet, and train.
>
> This is video 2 of a series on modern computer vision — how it actually works, from the primitives up. If you missed video 1 on patch embedding, it's linked below. Let's go.

### [0:25 – 1:15] Setup — what was the problem

> Old computer vision had two big problems, both about labels.
>
> **First:** labels are expensive. ImageNet has 1.4 million images across a thousand classes, and it took years and a small army of workers. Scaling that to ten thousand classes is not really feasible.
>
> **Second:** a labeled dataset defines a fixed vocabulary. Train a model on ImageNet's thousand classes, and it can only ever output one of those thousand things. Show it a "digital camera" and it might say "reflex camera" because that's the closest class. Show it something completely new — a specific breed of dog it never saw — and it just guesses wrong.
>
> Meanwhile, sitting right next to us on the internet, was every image humans had ever posted — with a caption, or alt text, or a filename, or a nearby paragraph. Free labels. Fuzzy, noisy, wrong sometimes — but free. And billions of them.
>
> The question CLIP asked was: can we actually use this?

### [1:15 – 3:00] The trick — contrastive matching

> Here's what CLIP does. It has two networks — an image encoder, and a text encoder. Both output vectors of the same size. Think of the vector as a point in a high-dimensional space.
>
> During training, you grab a batch — say, 32,000 image-text pairs from the web. Encode all the images. Encode all the texts. Now you have 32,000 image vectors and 32,000 text vectors.
>
> Then you build a 32,000-by-32,000 matrix of similarities. Every image compared to every text. The diagonal — where each image meets its own caption — should score high. Every off-diagonal cell — image compared to someone else's caption — should score low.
>
> That's the whole training objective. Pull matching pairs together in the embedding space, push non-matching pairs apart. Do this for four hundred million pairs.
>
> *[Diagram cutaway: the N-by-N similarity matrix, diagonal highlighted]*
>
> Once you're done, images and text live in the same space. A photo of a golden retriever ends up near the words "a golden retriever." A photo of a sunset ends up near "a sunset over the ocean."
>
> Now the trick that makes this actually useful: **zero-shot classification.**
>
> Say you want to classify an image into one of a thousand categories. You don't retrain the model. You take each category name, wrap it in a template like *"a photo of a {class name}"* — encode that with the text encoder, and now you have a thousand text vectors. Encode the image. Whichever text vector is closest — that's your prediction.
>
> The classes are just text. You can change them on the fly. Add "vintage car" tomorrow, remove "sedan" — no retraining. The model classifies whatever you can describe.

### [3:00 – 3:50] Why it mattered

> CLIP did three things at once, which is why it's the most-cited computer vision paper of the last five years.
>
> **One:** it proved you can turn web-scraped noise into world-class visual features. Weak supervision at scale beats clean supervision at small scale. This is the philosophical core of foundation models.
>
> **Two:** it produced a joint image-text embedding space that everything downstream now uses. Stable Diffusion uses CLIP's text encoder to understand your prompts. Every open-source vision-language model — LLaVA, BLIP-2, Qwen — starts from a CLIP or CLIP-descendant vision encoder. If you're using AI to look at images today, you're almost certainly using CLIP somewhere in the stack.
>
> **Three:** it made zero-shot the default expectation. Before CLIP, if you needed a classifier for a new task, you built a dataset. After CLIP, you write a prompt.

### [3:50 – 4:35] Where CLIP falls short

> One honest note, because CLIP isn't magic.
>
> It's coarse. It's great at "is this a dog or a cat" — it's bad at "is this a Golden Retriever or a Labrador." Same failure mode for fine-grained scenes: it can tell you someone is applying makeup, it struggles to tell you which product or which technique. It's a wide-net classifier, not a fine-grained one.
>
> It also has a weird quirk: **on many tasks, CLIP's zero-shot performance is actually better than its few-shot performance.** If you take CLIP's image features and train a small classifier on twenty labeled examples, it often does worse than just writing text prompts. Which is counterintuitive, and one of the open puzzles in the field.
>
> I actually ran a small experiment on this — code's on my GitHub if you want to see it. Skin-state classification with prompts basically at chance. The fine-grained weakness is very real.

### [4:35 – 5:00] Close + hook to next

> Next up: **MAE — Masked Autoencoders.** Which asks the opposite question CLIP asked. CLIP said "let's use text as supervision." MAE says "what if we don't need any supervision at all — just cover up random parts of the image and make the model fill them back in?" It's the other major direction in modern computer vision, and the direct ancestor of every video-understanding model we have.
>
> If this was useful, subscribe — one of these most days through August. Learning in public, so wrong-in-public is part of the deal. See you tomorrow.

---

## YouTube description

Before CLIP, if you wanted a computer to recognize a thousand things, someone had to label a thousand kinds of images. CLIP asked a different question: what if we use the internet — where every image already has text next to it — as the training signal? Four hundred million image-text pairs later, they had a model that classifies anything you can describe in English, no labels required. In this video I break down how contrastive image-text pretraining actually works, why it produced the joint embedding space that powers every modern vision-language model, and where it still breaks down.

I'm learning modern computer vision in public — one concept per video, roughly through August 2026.

📚 Paper: Learning Transferable Visual Models From Natural Language Supervision (arXiv:2103.00020)
🗺️ My concept-node graph: [link to GitHub repo]
🔬 Reproducible code + experiments: [link to GitHub repo]

Chapters:
0:00 - The question
0:25 - Why labels were the bottleneck
1:15 - How contrastive matching works
3:00 - Why it mattered
3:50 - Where CLIP falls short
4:35 - What's next

---

## Suggested tags
`CLIP, contrastive learning, computer vision, openai, zero-shot classification, vision language model, foundation models, deep learning, ai research, machine learning`

---

## Delivery notes

**Script pacing**
- 780 words at ~150 wpm = 5:12. Trim 30 words if you speak slower. Cut candidate: the "vintage car / remove sedan" example at [2:50] — teacherly, not load-bearing.
- Slow down on the contrastive matrix explanation ("32,000 by 32,000... diagonal high, off-diagonal low"). This is the mechanism — viewers need a beat to picture it.
- Pause after "*What if we don't do that*" and after "*After CLIP, you write a prompt.*" Both are hook lines that need silence.
- Retake trigger: if you stumble on "pull matching pairs together... push non-matching pairs apart" — retake. It's the load-bearing sentence.

**Talking-head practical**
- Same setup as video #1 — mid-chest framing, camera at eye level, natural window light. Skip re-reading video #1's checklist if you've already batch-set-up.
- For batch recording, shoot both videos in the same shirt or change deliberately — random wardrobe changes across daily uploads look inconsistent.

**Cutaway plan**
- [2:00] cutaway to a static diagram of the contrastive matrix — the N-by-N grid with the diagonal highlighted. Draw it yourself in Keynote / Figma in 5 min, or use the CLIP paper's Figure 1.
- [2:30] optional freeze on the prompt-template idea: text overlay of `"a photo of a {class name}"` — reinforces the visual.
- [4:00] cutaway to your experiment's terminal output or JSON, showing the actual skin-state chance-level scores — turns "I ran a small experiment" from a claim into evidence.
- Everything else: stay on face.

**Publishing checklist**
- Thumbnail featuring the phrase "CLIP" and either a matrix visual or "400M" as a number
- Chapter markers pasted into description
- End screen linking video #1 (patch embedding) — the prerequisite
- First pinned comment: link to the CLIP paper + link to the GitHub experiment folder

**Cross-video continuity**
- The line *"if you missed video 1 on patch embedding, it's linked below"* at [0:25] assumes video 1 exists and is linked. Verify before publishing.
- The [4:00] mention of the GitHub experiment assumes the repo is public. Verify.
