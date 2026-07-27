"""CLIP zero-shot on facial-care images across 4 concept axes.

Tests the hypothesis (from `CONTRASTIVE-IMAGE-TEXT-PRETRAINING` and
`ZERO-SHOT-CLASSIFICATION-VIA-TEXT-PROMPTS` concept nodes) that CLIP is
strong on coarse category recognition but weak on fine-grained axes such
as action verbs and skin-state descriptors — the exact regime SNAIC's
concept-driven video understanding must handle.

Papers: [2021-clip-radford], [2020-vit-dosovitskiy]
"""
import json, os, sys
from pathlib import Path
from PIL import Image
import torch
from transformers import CLIPProcessor, CLIPModel

HERE = Path(__file__).parent
IMG_DIR = HERE / "images"
RES_DIR = HERE / "results"
MODEL_ID = "openai/clip-vit-base-patch32"

AXES = {
    "product_category": [
        "a photo of moisturizer being applied",
        "a photo of shampoo being used",
        "a photo of lipstick being applied",
        "a photo of sunscreen being applied",
        "a photo of shaving cream on the face",
        "a photo of eye cream being applied",
        "a photo of face wash being used",
        "a photo of a face mask sheet on the face",
        "a photo of foundation being applied",
        "a photo of mascara being applied",
    ],
    "application_region": [
        "a photo of a person touching their cheek",
        "a photo of a person touching their lips",
        "a photo of a person touching their eye area",
        "a photo of a person touching their hair",
        "a photo of a person touching their forehead",
        "a photo of a person touching their neck",
        "a photo of a person touching their chin",
    ],
    "action_verb": [
        "a photo of a person applying cream",
        "a photo of a person washing",
        "a photo of a person rinsing",
        "a photo of a person massaging skin",
        "a photo of a person patting skin",
        "a photo of a person rubbing skin",
        "a photo of a person spraying",
        "a photo of a person drying with a towel",
    ],
    "skin_state": [
        "a photo of oily skin",
        "a photo of dry skin",
        "a photo of clear healthy skin",
        "a photo of red irritated skin",
        "a photo of blemished skin",
        "a photo of smooth skin",
    ],
}

def load_model():
    print(f"loading {MODEL_ID} ...", flush=True)
    model = CLIPModel.from_pretrained(MODEL_ID)
    processor = CLIPProcessor.from_pretrained(MODEL_ID)
    model.eval()
    return model, processor

def score_image(model, processor, img, prompts):
    inputs = processor(text=prompts, images=img, return_tensors="pt", padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits_per_image[0]           # [len(prompts)]
    probs = logits.softmax(dim=-1).tolist()
    return probs

def main():
    RES_DIR.mkdir(exist_ok=True)
    model, processor = load_model()

    with open(IMG_DIR / "manifest.json") as f:
        manifest = json.load(f)

    results = []
    for entry in manifest:
        fname = entry["file"]
        fpath = IMG_DIR / fname
        try:
            img = Image.open(fpath).convert("RGB")
        except Exception as e:
            print(f"skip {fname}: {e}"); continue
        per_axis = {}
        for axis_name, prompts in AXES.items():
            probs = score_image(model, processor, img, prompts)
            ranked = sorted(zip(prompts, probs), key=lambda x: x[1], reverse=True)
            per_axis[axis_name] = {
                "top1": {"prompt": ranked[0][0], "prob": ranked[0][1]},
                "top3": [{"prompt": p, "prob": pr} for p, pr in ranked[:3]],
            }
        results.append({
            "file": fname,
            "query": entry["query"],
            "wikimedia_title": entry["title"],
            "axes": per_axis,
        })
        print(f"scored {fname}")

    out_path = RES_DIR / "clip_scores.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nwrote {out_path}")

if __name__ == "__main__":
    main()
