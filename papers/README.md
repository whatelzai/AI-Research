# Papers

PDF library + index. The **slug** (filename without `.pdf`) is the join key across this repo and EMDEE.

## Naming

`YYYY-shortname-firstauthor.pdf` — lowercase, hyphens.

Examples:
- `2021-clip-radford.pdf`
- `2020-vit-dosovitskiy.pdf`
- `2023-llava-liu.pdf`

## Index

| Slug | Title | Venue | EMDEE concept nodes | Experiments | Status |
|------|-------|-------|---------------------|-------------|--------|
| `2020-vit-dosovitskiy` | An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale | ICLR 2021 | `PATCH-EMBEDDING`, `INDUCTIVE-BIAS-VS-SCALE-TRADEOFF` | — | noted |
| `2021-clip-radford` | Learning Transferable Visual Models From Natural Language Supervision | ICML 2021 | `CONTRASTIVE-IMAGE-TEXT-PRETRAINING`, `ZERO-SHOT-CLASSIFICATION-VIA-TEXT-PROMPTS`, `INDUCTIVE-BIAS-VS-SCALE-TRADEOFF` | `clip-facial-care-zero-shot` | built |
| `2021-mae-he` | Masked Autoencoders Are Scalable Vision Learners | CVPR 2022 | `MASKED-IMAGE-MODELING`, `PATCH-EMBEDDING` | — | noted |
| `2023-blip2-li` | BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and LLMs | ICML 2023 | `FROZEN-BACKBONE-BRIDGE-TO-LLM`, `VISUAL-INSTRUCTION-TUNING` | — | noted |
| `2023-llava-liu` | Visual Instruction Tuning | NeurIPS 2023 | `VISUAL-INSTRUCTION-TUNING`, `FROZEN-BACKBONE-BRIDGE-TO-LLM` | — | noted |
| `2023-siglip-zhai` | Sigmoid Loss for Language Image Pre-Training | ICCV 2023 | `SIGMOID-VS-SOFTMAX-CONTRASTIVE-LOSS`, `CONTRASTIVE-IMAGE-TEXT-PRETRAINING`, `ZERO-SHOT-CLASSIFICATION-VIA-TEXT-PROMPTS` | — | noted |
| `2021-timesformer-bertasius` | Is Space-Time Attention All You Need for Video Understanding? | ICML 2021 | `DIVIDED-SPACE-TIME-ATTENTION`, `SPACE-TIME-PATCH-EMBEDDING`, `INDUCTIVE-BIAS-VS-SCALE-TRADEOFF`, `PATCH-EMBEDDING` | — | noted |
| `2022-videomae-tong` | VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training | NeurIPS 2022 | `TUBE-MASKING-FOR-VIDEO-MIM`, `MASKED-IMAGE-MODELING`, `SPACE-TIME-PATCH-EMBEDDING`, `DIVIDED-SPACE-TIME-ATTENTION`, `PATCH-EMBEDDING` | — | noted |
| `2023-video-llama-zhang` | Video-LLaMA: An Instruction-tuned Audio-Visual Language Model for Video Understanding | EMNLP 2023 | `CROSS-MODAL-BRIDGING-VIA-SHARED-EMBEDDING-SPACE`, `FROZEN-BACKBONE-BRIDGE-TO-LLM` | — | noted |
| `2023-dinov2-oquab` | DINOv2: Learning Robust Visual Features without Supervision | TMLR 2024 | `STUDENT-TEACHER-SELF-DISTILLATION`, `AUTOMATED-DATA-CURATION-FOR-SSL`, `MASKED-IMAGE-MODELING`, `CONTRASTIVE-IMAGE-TEXT-PRETRAINING` | — | noted |
| `2020-concept-bottleneck-koh` | Concept Bottleneck Models | ICML 2020 | `CONCEPT-BOTTLENECK-ARCHITECTURE` | — | noted |
| `2021-latent-diffusion-rombach` | High-Resolution Image Synthesis with Latent Diffusion Models | CVPR 2022 | `LATENT-DIFFUSION`, `CROSS-ATTENTION-CONDITIONING-FOR-DIFFUSION`, `INDUCTIVE-BIAS-VS-SCALE-TRADEOFF` | — | noted |
| `2023-video-ldm-blattmann` | Align your Latents: High-Resolution Video Synthesis with Latent Diffusion Models | CVPR 2023 | `FREEZE-IMAGE-BACKBONE-ADD-TEMPORAL-LAYERS`, `LATENT-DIFFUSION`, `FROZEN-BACKBONE-BRIDGE-TO-LLM` | — | noted |

**Status:** `queued` → `reading` → `noted` → `built`

- `noted` = atomic concept nodes exist in EMDEE citing this slug
- `built` = at least one folder in `../experiments/` references this slug

## Concept nodes live in EMDEE, not here

The atomic notes are children of `knowledge/COMPUTER-VISION-VLM-VLA.md` in the EMDEE vault. One node per **concept** (not per paper) — a single paper typically feeds 2–5 concept nodes, and a single concept node accretes citations from many papers over time.

Each EMDEE concept node cites papers by slug (e.g., `[2021-clip-radford]`) so `grep` across the vault finds every note that touches a given paper.
