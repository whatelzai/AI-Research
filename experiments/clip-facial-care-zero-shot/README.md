# CLIP Zero-Shot on Facial-Care Images

**Slug references:** `[2021-clip-radford]`, `[2020-vit-dosovitskiy]`
**Concept nodes tested:** `CONTRASTIVE-IMAGE-TEXT-PRETRAINING`, `ZERO-SHOT-CLASSIFICATION-VIA-TEXT-PROMPTS`

## Goal

Concretely stress-test the hypothesis (from CLIP paper + SNAIC notes) that CLIP is **strong on coarse category recognition but weak on fine-grained axes** — the exact regime SNAIC's concept-driven video understanding must handle for consumer facial-care.

## Setup

- Model: `openai/clip-vit-base-patch32` (~150M params, ViT-B/32 + text transformer)
- Images: 8 fetched from Wikimedia Commons via keyword search
- 4 concept axes tested per image:
  - **product_category** (10 prompts): moisturizer / shampoo / lipstick / sunscreen / eye cream / etc.
  - **application_region** (7 prompts): cheek / lips / eye area / hair / neck / etc.
  - **action_verb** (8 prompts): applying / washing / patting / rubbing / etc.
  - **skin_state** (6 prompts): oily / dry / clear / red / smooth / etc.

Softmax over each axis's prompts → predicted label + confidence.

## Data quality caveat (surprise finding #1)

Wikimedia keyword search returned **4 correctly-matched images and 4 completely off-topic images** whose filenames contained the query keyword but content did not:

| Query | Fetched | Match? |
|---|---|---|
| `woman applying lipstick` | *Applying red lipstick — model Eve Casini* | ✅ correct |
| `man shaving face` | *Wellcome illustration of a barber shaving* | ✅ correct (historical) |
| `man face wash` | *Wellcome illustration of face-washing* | ✅ correct (historical) |
| `woman washing hair shampoo` | *School hair-washing class* | ✅ correct |
| `eye cream application` | *Oak Street Ice Cream Hot Dogs Interior* | ❌ "cream" |
| `facial mask sheet` | *Macedonian tomb of Aghia Paraskevi* | ❌ "mask" |
| `sunscreen sun cream applying` | *Hanig Ice Cream Parlor Ruins* | ❌ "cream" |
| `skincare cream face` | *India Alternative Medicine Market Report* | ❌ "cream" |

**This is itself the SNAIC data-pipeline problem in miniature.** Keyword-matched web scraping produces noisy corpora — the exact motivation for DINOv2's [[AUTOMATED-DATA-CURATION-FOR-SSL]] (embed → dedupe → nearest-neighbor retrieval against a curated seed set). CLIP embeddings themselves can filter this: score each candidate image against `"a photo of {query}"` and drop below-threshold matches.

## Findings on the 4 correctly-matched images

### Modern color photo (lipstick) — CLIP performs very well

`03_woman_applying_lipstick.jpg`:
- product_category: `lipstick being applied` **88.5%** ✅
- application_region: `touching their lips` **67.7%** ✅
- action_verb: `applying cream` **84.4%** ✅ (correct verb, wrong noun — verb axis worked)

**All three axes correct with high confidence.** This is CLIP's home turf: single-subject color photo, canonical action, clean composition.

### Historical illustrations (Wellcome shaving + face wash) — CLIP breaks down

Both are B&W 19th-century medical illustrations, well outside CLIP's training distribution (mostly modern web photos):

`02_man_shaving_face.jpg`:
- product_category: `eye cream being applied` 27.3% ❌ (should be shaving)
- application_region: `touching their neck` 50.3% ❌
- action_verb: `patting skin` 33.5% ❌ (should be shaving/rubbing)

`06_man_face_wash.jpg`:
- product_category: `eye cream being applied` 23.9% ❌
- application_region: `touching their neck` 24.3% ❌
- action_verb: `patting skin` 26.2% ❌

**Confidences all in the 20-33% range** — CLIP is *appropriately uncertain* about out-of-distribution imagery, which is actually a useful signal. Both images collapse to "eye cream + touching neck + patting" — plausibly the coarsest visual features (person + face touching) dominate.

### School hair-washing class — CLIP misses the fine-grained target

`01_shampoo_hair_washing.jpg` (real photo but complex multi-person scene):
- product_category: `face wash being used` 38.9% ❌ (should be shampoo — face wash is #1, shampoo is #2 at 21.5%)
- application_region: `touching their neck` 51.3% ❌ (should be hair — hair only 12.4%)
- action_verb: `patting skin` 37.4% ❌

The wrong product+region combo is instructive: CLIP conflates "face wash" and "shampoo" (both watery + head-adjacent), and misses "hair" despite the query explicitly being hair washing. **Multi-person composition confuses the region prediction** — the model latches on a wrong body area.

## Skin state axis — mostly noise

Confidences hover 25-50%, top picks feel random (irritated skin for lipstick model? dry skin for shampoo?). CLIP has no meaningful zero-shot skin-condition classifier out of the box. This aligns with the fine-grained-weakness hypothesis: subtle skin descriptors are exactly the visual regime where CLIP fails.

## Takeaways

1. **Confirmed: coarse-and-canonical works, fine-grained-and-composed doesn't.** Single-subject product-application shots work well; multi-person scenes, out-of-distribution styles, and subtle skin descriptors do not.
2. **Confirmed: skin-state zero-shot is unusable** without fine-tuning or a domain-specific concept bottleneck ([[CONCEPT-BOTTLENECK-ARCHITECTURE]]).
3. **The keyword-search noise problem is real** — this is exactly the case for LVL-142M-style curation ([[AUTOMATED-DATA-CURATION-FOR-SSL]]) using CLIP embeddings themselves as a filter.
4. **CLIP's uncertainty on OOD images is a feature, not a bug** — confidences drop from 88% → 25%, giving a usable signal for "this image doesn't match any of my prompts well."
5. **Historical / non-photorealistic imagery** (Wellcome illustrations) collapses hard — SNAIC's proprietary consumer footage is at least in the right modality (modern color video), but style-of-recording matters.

## Suggested next iteration

- Swap the 4 off-topic images for actual facial-care content (better queries, or curated seed set).
- Add ~5-10 real YouTube facial-care thumbnails or frames for realistic input distribution.
- Compare against a video-VLM (Video-LLaMA or LLaVA-NeXT-Video) on the same axes — image CLIP is only the baseline.
- Test *composite* prompts (e.g., "a woman applying moisturizer to her cheek with her right hand") to probe compositional understanding — likely another axis of failure.

## Files

- `run.py` — the experiment
- `images/` — 8 test images + `manifest.json` with source URLs and Wikimedia titles
- `results/clip_scores.json` — full per-image, per-axis, top-3 scores
- `results/analysis.md` — this file's findings in briefer form (mirrored)
