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
| `2024-qwen2-vl-wang` | Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution | arXiv 2024 | `DYNAMIC-RESOLUTION-VISUAL-TOKENIZATION`, `MULTIMODAL-ROTARY-POSITION-EMBEDDING`, `SPACE-TIME-PATCH-EMBEDDING`, `PATCH-EMBEDDING` | — | noted |
| `2024-llava-onevision-li` | LLaVA-OneVision: Easy Visual Task Transfer | arXiv 2024 | `DYNAMIC-RESOLUTION-VISUAL-TOKENIZATION`, `VISUAL-INSTRUCTION-TUNING`, `SPACE-TIME-PATCH-EMBEDDING`, `PATCH-EMBEDDING` | — | noted |
| `2022-blip-li` | BLIP: Bootstrapping Language-Image Pre-training for Unified VL Understanding and Generation | ICML 2022 | `CAPTIONING-DATA-BOOTSTRAPPING`, `FROZEN-BACKBONE-BRIDGE-TO-LLM`, `CONTRASTIVE-IMAGE-TEXT-PRETRAINING` | — | noted |
| `2024-internvl-chen` | InternVL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks | CVPR 2024 | `FROZEN-BACKBONE-BRIDGE-TO-LLM`, `CONTRASTIVE-IMAGE-TEXT-PRETRAINING`, `MASKED-IMAGE-MODELING` | — | noted |
| `2023-eva-clip-sun` | EVA-CLIP: Improved Training Techniques for CLIP at Scale | arXiv 2023 | `CONTRASTIVE-IMAGE-TEXT-PRETRAINING`, `MASKED-IMAGE-MODELING` | — | noted |
| `2022-coca-yu` | CoCa: Contrastive Captioners are Image-Text Foundation Models | arXiv 2022 | `CONTRASTIVE-IMAGE-TEXT-PRETRAINING`, `VISUAL-INSTRUCTION-TUNING` | — | noted |
| `2022-flamingo-alayrac` | Flamingo: a Visual Language Model for Few-Shot Learning | NeurIPS 2022 | `FROZEN-BACKBONE-BRIDGE-TO-LLM` | — | noted |
| `2023-instructblip-dai` | InstructBLIP: Towards General-purpose Vision-Language Models with Instruction Tuning | NeurIPS 2023 | `FROZEN-BACKBONE-BRIDGE-TO-LLM`, `VISUAL-INSTRUCTION-TUNING` | — | noted |
| `2023-llava-1.5-liu` | Improved Baselines with Visual Instruction Tuning (LLaVA-1.5) | arXiv 2023 | `FROZEN-BACKBONE-BRIDGE-TO-LLM`, `DYNAMIC-RESOLUTION-VISUAL-TOKENIZATION`, `VISUAL-INSTRUCTION-TUNING` | — | noted |
| `2024-internvideo2-wang` | InternVideo2: Scaling Foundation Models for Multimodal Video Understanding | ECCV 2024 | `CAPTIONING-DATA-BOOTSTRAPPING`, `MASKED-IMAGE-MODELING`, `TUBE-MASKING-FOR-VIDEO-MIM`, `FROZEN-BACKBONE-BRIDGE-TO-LLM` | — | noted |
| `2024-llava-next-interleave-li` | LLaVA-NeXT-Interleave: Tackling Multi-image, Video, and 3D in Large Multimodal Models | arXiv 2024 | `VISUAL-INSTRUCTION-TUNING`, `DYNAMIC-RESOLUTION-VISUAL-TOKENIZATION` | — | noted |
| `2021-lora-hu` | LoRA: Low-Rank Adaptation of Large Language Models | ICLR 2022 | `LORA-LOW-RANK-ADAPTATION` | — | noted |
| `2023-cogagent-hong` | CogAgent: A Visual Language Model for GUI Agents | CVPR 2024 | `FROZEN-BACKBONE-BRIDGE-TO-LLM` | — | noted |
| `2023-grounding-dino-liu` | Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection | arXiv 2023 | `OPEN-VOCABULARY-DETECTION-VIA-TEXT-GROUNDING`, `CONTRASTIVE-IMAGE-TEXT-PRETRAINING` | — | noted |
| `2023-label-free-cbm-oikarinen` | Label-free Concept Bottleneck Models | ICLR 2023 | `VLM-SUPERVISED-CONCEPT-GENERATION`, `CONCEPT-BOTTLENECK-ARCHITECTURE`, `CONTRASTIVE-IMAGE-TEXT-PRETRAINING` | — | noted |
| `2021-dino-caron` | Emerging Properties in Self-Supervised Vision Transformers (DINO) | ICCV 2021 | `STUDENT-TEACHER-SELF-DISTILLATION` | — | noted |
| `2023-minigpt4-zhu` | MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models | arXiv 2023 | `CAPTIONING-DATA-BOOTSTRAPPING`, `FROZEN-BACKBONE-BRIDGE-TO-LLM` | — | noted |
| `2025-qwen2.5-vl-bai` | Qwen2.5-VL Technical Report | arXiv 2025 | `ABSOLUTE-TIME-POSITION-ENCODING`, `MULTIMODAL-ROTARY-POSITION-EMBEDDING`, `DYNAMIC-RESOLUTION-VISUAL-TOKENIZATION` | — | noted |
| `2024-nvila-liu` | NVILA: Efficient Frontier Visual Language Models | arXiv 2024 | `DYNAMIC-RESOLUTION-VISUAL-TOKENIZATION`, `FROZEN-BACKBONE-BRIDGE-TO-LLM` | — | noted |

**Status:** `queued` → `reading` → `noted` → `built`

- `noted` = atomic concept nodes exist in EMDEE citing this slug
- `built` = at least one folder in `../experiments/` references this slug

## Concept nodes live in EMDEE, not here

The atomic notes are children of `knowledge/COMPUTER-VISION-VLM-VLA.md` in the EMDEE vault. One node per **concept** (not per paper) — a single paper typically feeds 2–5 concept nodes, and a single concept node accretes citations from many papers over time.

Each EMDEE concept node cites papers by slug (e.g., `[2021-clip-radford]`) so `grep` across the vault finds every note that touches a given paper.
