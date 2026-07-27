# SNAIC / P&G Research Fellow — Conversation Brief

*Prep for the pre-application conversation with the professor. Application closes 2026-08-09.*

## Where I've been putting the time

Working through the substrate of concept-driven video understanding — 15 papers across six phases (image foundations → VLMs → video → concept & weak supervision → generative → Sept-2024 SOTA), structured as a knowledge graph of ~20 reusable concept nodes I can pull into any specific problem. One small experiment (CLIP zero-shot on facial-care images) grounded the reading in the fine-grained regime the JD describes. This isn't a claim of expertise — it's the map I built so we can talk in specifics rather than vocabulary.

## My reading of what SNAIC × P&G is actually working on

*Please correct me — this is my best guess before the conversation.*

Concept-driven video understanding of consumer-recorded facial-care videos isn't standard action recognition or captioning. The videos are noisy, unlabeled, single-subject, long-form, and the interesting content is subtle: which product, applied where, how, over what skin state, in what step of a routine. Off-the-shelf image-CLIP is documented weak at exactly this fine-grained regime — I ran a small CLIP zero-shot test on 8 facial-care images and the fine-grained axes (region, gesture, skin state) confirmed this, with skin-state prompts essentially at chance.

But the picture shifted meaningfully once I read the Sept-2024 SOTA (Qwen2-VL, LLaVA-OneVision). Open-source VLMs now match GPT-4o on multimodal benchmarks, handle 20+ min video via dynamic-resolution tokenization, and — critically — LLaVA-OneVision demonstrates that video capability and multi-image reasoning **emerge** from image + video co-training without explicit multi-image supervision. That reframes the research question.

## The strategic fork I'd want your steer on

The Phase 1-5 reading pointed me toward a ground-up pipeline: automated curation → self-supervised video pretraining (VideoMAE) → concept bottleneck → task heads. The Phase 6 reading suggests a different order of operations may dominate:

**Option A — SOTA fine-tune first.** Take Qwen2-VL 72B as the substrate. Use it to re-caption P&G footage into structured concept labels (LLaVA-OneVision's 99.8%-synthetic-data trick shows this works at scale). Fine-tune a concept-bottleneck adapter on top. Ship the baseline in weeks.

**Option B — Ground-up domain pipeline.** Automated curation from raw web video, VideoMAE tube-masked pretraining on the curated corpus, concept bottleneck from scratch. VideoMAE's data-efficiency finding (SOTA on SSv2 from ~3.5k in-domain clips, in-domain always beating larger out-of-domain) makes this defensible even at P&G scale. Slower, but the model is fully owned and domain-adapted.

They're not mutually exclusive — A gives you a baseline to beat with B — but **which one is the right first bet** determines the entire team's compute and calendar. This is the question I'd most want your read on. Adjacent design choices (concept vocabulary, VLM-supervision noise threshold, audio channel, synthetic augmentation) fall out of that answer.

## Open questions I'd love to work through with you

1. **A or B first?** — as above.
2. **What's the right concept vocabulary for facial-care?** Product-driven, behaviour-driven, skin-state-driven, routine-step-driven — probably a hybrid, but which axes matter for P&G's downstream applications determines everything upstream.
3. **How noisy can VLM-generated concept labels be before concept bottleneck breaks?** The paper only tests clean human labels; VLM-supervision is the direction the field is going but empirically the noise threshold is under-studied.
4. **Consent & synthetic imagery.** If the pipeline includes generating consumer-face video for augmentation (Video LDM), the ethics call-out (deepfake / misuse) applies. Worth naming a plan up front rather than being asked about it later.
5. **What does P&G actually want to do with the outputs?** Search, dashboarding, product recommendation, agentic tutoring — the downstream use case would sharpen the concept vocabulary in (2) and the A-vs-B call in (1).

## What I'd bring

Not a research CV, so being honest — a systems background that ships. What I've done this week (map + code + hypotheses) is the mode I default to; I'd expect the first weeks of the role to look similar, just deeper. Warm path is real: I trust you'd tell me quickly if the fit isn't right, and I'd rather have that conversation now than after applying.

---

*Concept-node graph in my EMDEE vault under `edmund/research/ai/` — happy to walk through any node in more detail. Experiment code and reading notes are in a GitHub repo I can share on request. I'll also be posting short daily explainer videos on YouTube through the application window as a public-learning receipt.*
