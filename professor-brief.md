# SNAIC / P&G Research Fellow — Conversation Brief

*Prep for the pre-application conversation with the professor. Application closes 2026-08-09.*

## Where I've been putting the time

Working through the substrate of concept-driven video understanding — 32 papers across seven phases (image foundations → VLMs → video → concept & weak supervision → generative → Sept-2024 SOTA → 2025 SOTA + adjacent recipes), structured as a knowledge graph of ~25 reusable concept nodes I can pull into any specific problem. One small experiment (CLIP zero-shot on facial-care images) grounded the reading in the fine-grained regime the JD describes. This isn't a claim of expertise — it's the map I built so we can talk in specifics rather than vocabulary.

## My reading of what SNAIC × P&G is actually working on

*Please correct me — this is my best guess before the conversation.*

Concept-driven video understanding of consumer-recorded facial-care videos isn't standard action recognition or captioning. The videos are noisy, unlabeled, single-subject, long-form, and the interesting content is subtle: which product, applied where, how, over what skin state, in what step of a routine. Off-the-shelf image-CLIP is documented weak at exactly this fine-grained regime — I ran a small CLIP zero-shot test on 8 facial-care images and the fine-grained axes (region, gesture, skin state) confirmed this, with skin-state prompts essentially at chance.

But the picture shifted meaningfully once I reached the 2024-2025 SOTA (Qwen2.5-VL, LLaVA-OneVision, InternVideo2). Open-source VLMs now match GPT-4o on multimodal benchmarks, handle 20+ min video via dynamic-resolution tokenization, and cross-scenario capabilities emerge from co-training without explicit supervision. Combined with automated concept generation (Label-Free CBM: GPT + CLIP replaces human concept annotation), the concept-driven paradigm is now practically deployable at foundation-model scale. **The research question has shifted from "how do we build this" to "which components dominate and how do we evaluate them."**

## A candidate pipeline

*Named components — the specific choices I'd defend, curious where you'd redirect.*

1. **Base VLM** — Qwen2.5-VL. Native-resolution ViT with window attention, absolute-time M-RoPE for second-level step localization in long routines, dynamic FPS handling, native visual grounding, agent-trajectory training data.
2. **Data bootstrapping** — CapFilt-style re-captioning of P&G footage with Qwen2.5-VL itself, producing structured concept-tagged descriptions at scale. The LLaVA-OneVision result (99.8% synthetic instruction data works) makes this credible.
3. **Concept bottleneck** — Label-Free CBM pipeline: Qwen2.5-VL generates concept vocabulary from a facial-care taxonomy, SigLIP scores frames against concepts, sparse elastic-net produces the final concept-to-task layer. First stage of the architecture that scales CBM beyond CUB-sized datasets. Human weight-editing property preserved for auditability.
4. **Detection primitive** — Grounding DINO for open-vocabulary product / region / gesture detection via text prompts. Eliminates per-SKU detector training.
5. **Fine-tuning mechanism** — LoRA adapters on Qwen2.5-VL. Cheap per-concept, swappable, no inference latency.
6. **Optional — audio channel via InternVideo2's tri-modal fusion** (video + voice-over + ASR → LLM-fused captions). Most video-VLMs discard audio; facial-care tutorials typically have narration that names products and steps.

Where does this pipeline *not* match what you have in mind?

## Open questions I'd want your steer on

1. **Which component is the research contribution vs. engineering integration?** My guess: the concept bottleneck design + evaluation methodology + audit workflow. The base model and detection primitive are engineering choices; the concept-driven layer is where original work lives.
2. **What's the right concept vocabulary for facial-care?** Product-driven, behaviour-driven, skin-state-driven, routine-step-driven — probably a hybrid. VLM-supervised generation gives a candidate set; humans must curate the final taxonomy. This is where your domain judgment matters most.
3. **How noisy can VLM-generated concept labels be before the bottleneck breaks?** Label-Free CBM only tested on CIFAR / CUB / ImageNet; noise threshold on messy consumer video is under-studied. Empirical question worth designing an early experiment around.
4. **What's the evaluation metric?** Concept-level accuracy? Downstream task performance? Intervention effectiveness (how often does human editing fix errors)? Auditability score? Choice of metric shapes the entire iteration loop.
5. **What does P&G actually want to do with the outputs?** Passive analysis / dashboarding / product recommendation / agent-style tutorial reasoning — the deployment shape sharpens everything upstream.

## What I'd bring

Not a research CV, so being honest — a systems background that ships. What I've done this week (map + code + hypotheses) is the mode I default to; I'd expect the first weeks of the role to look similar, just deeper. Warm path is real: I trust you'd tell me quickly if the fit isn't right, and I'd rather have that conversation now than after applying.

---

*Concept-node graph in my EMDEE vault under `edmund/research/ai/` — happy to walk through any node in more detail. Experiment code and reading notes are in a GitHub repo I can share on request. I'll also be posting short daily explainer videos on YouTube through the application window as a public-learning receipt.*
