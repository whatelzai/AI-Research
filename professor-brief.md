# SNAIC / P&G Research Fellow — Conversation Brief

*Prep for the pre-application conversation with the professor. Application closes 2026-08-09.*

## Where I've been putting the time

Working through the substrate of concept-driven video understanding — 13 papers across five phases (image foundations → VLMs → video → concept & weak supervision → generative), structured as a knowledge graph of ~18 reusable concept nodes I can pull into any specific problem. One small experiment (CLIP zero-shot on facial-care images) grounded the reading in the fine-grained regime the JD describes. This isn't a claim of expertise — it's the map I built so we can talk in specifics rather than vocabulary.

## My reading of what SNAIC × P&G is actually working on

*Please correct me — this is my best guess before the conversation.*

Concept-driven video understanding of consumer-recorded facial-care videos isn't standard action recognition or captioning. The videos are noisy, unlabeled, single-subject, long-form, and the interesting content is subtle: which product, applied where, how, over what skin state, in what step of a routine. Off-the-shelf VLMs (CLIP, LLaVA, Video-LLaMA) are trained on caption-heavy web data and are documented weak at exactly this fine-grained regime — I ran a small CLIP zero-shot test on 8 facial-care images and the fine-grained axes (region, gesture, skin state) confirmed this, with skin-state prompts essentially at chance.

That suggests the research question is less "which SOTA VLM do we bolt on" and more "what supervision + architecture combination makes concept-driven understanding tractable on a domain-specific corpus."

## A candidate pipeline I've been thinking about

Curious how close or far this is from what you have in mind:

1. **Domain corpus** — LVD-142M-style automated curation (DINOv2), seeded with P&G's proprietary set, retrieving nearest-neighbour clips from raw web video (facial-care tutorials, product reviews). Turns a small proprietary corpus into a much larger curated pretraining substrate.
2. **Self-supervised video encoder** — VideoMAE (tube-masked MIM at 90-95% ratio) trained on that curated corpus. VideoMAE's data-efficiency finding is important here: they got SOTA on SSv2 from ~3.5k in-domain clips with no external data, and in-domain always beat larger out-of-domain — which changes the calculus for a P&G-scale corpus.
3. **Concept bottleneck** — route predictions through a named-concept intermediate layer (`product-category`, `application-region`, `gesture-type`, `skin-state`, `routine-step`). Test-time intervention comes free. Concept supervision can be bootstrapped from a VLM rather than requiring hand labels.
4. **Optional synthetic augmentation** — Video-LDM's freeze-image-add-temporal-layers recipe for generating targeted synthetic training clips (rare skin conditions, edge-case demographics, uncommon techniques). Closes the data-scarcity loop that curation opens.
5. **Optional audio channel** — most video-VLMs discard it. Consumer facial-care video usually has voice-over (product name, technique, step). ImageBind-style shared-embedding bridging gets zero-shot audio understanding without needing paired audio-text data.

Each step is one design choice; each has documented tradeoffs; none of it is settled.

## Open questions I'd love to work through with you

1. **What's the right concept vocabulary for facial-care?** Product-driven, behaviour-driven, skin-state-driven, routine-step-driven — probably a hybrid, but which axes matter for P&G's downstream applications determines everything upstream.
2. **How noisy can VLM-generated concept labels be before concept bottleneck breaks?** The paper only tests clean human labels. VLM-supervised extensions are the direction the field is going, but empirically the noise threshold is under-studied.
3. **Is temporal concept drift a solved problem, or a research direction?** Image CBM literature is mature; video CBM is thin. Whether a gesture is "applying" vs "massaging" changes across the same clip.
4. **Consent & synthetic imagery.** If the pipeline includes generating consumer-face video for augmentation, the ethics call-out from the LDM paper (deepfake / misuse) applies. Worth naming a plan up front rather than being asked about it later.
5. **What does P&G actually want to do with the outputs?** Search, dashboarding, product recommendation, agentic tutoring — the downstream use case would sharpen the concept vocabulary in (1).

## What I'd bring

Not a research CV, so being honest — a systems background that ships. What I've done this week (map + code + hypotheses) is the mode I default to; I'd expect the first weeks of the role to look similar, just deeper. Warm path is real: I trust you'd tell me quickly if the fit isn't right, and I'd rather have that conversation now than after applying.

---

*If useful, the concept-node graph is in my EMDEE vault under `edmund/research/ai/cv/` — happy to walk through any node in more detail. The experiment code is in a GitHub repo I can share on request.*
