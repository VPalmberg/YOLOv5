from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
dirs = {
    "train_images": ROOT / "dataset" / "images" / "train",
    "val_images": ROOT / "dataset" / "images" / "val",
    "train_labels": ROOT / "dataset" / "labels" / "train",
    "val_labels": ROOT / "dataset" / "labels" / "val",
}

def stem_set(path: Path, suffix: str):
    return {p.stem for p in path.glob(f"*{suffix}")}

train_img = stem_set(dirs["train_images"], ".jpg")
val_img = stem_set(dirs["val_images"], ".jpg")
train_lab = stem_set(dirs["train_labels"], ".txt")
val_lab = stem_set(dirs["val_labels"], ".txt")

missing_train_labels = sorted(train_img - train_lab)
missing_val_labels = sorted(val_img - val_lab)
orphan_train_labels = sorted(train_lab - train_img)
orphan_val_labels = sorted(val_lab - val_img)

print("Train images:", len(train_img))
print("Val images:", len(val_img))
print("Train labels:", len(train_lab))
print("Val labels:", len(val_lab))
print()

if missing_train_labels:
    print("Missing train labels for:", missing_train_labels)
if missing_val_labels:
    print("Missing val labels for:", missing_val_labels)
if orphan_train_labels:
    print("Orphan train labels:", orphan_train_labels)
if orphan_val_labels:
    print("Orphan val labels:", orphan_val_labels)

if not any([missing_train_labels, missing_val_labels, orphan_train_labels, orphan_val_labels]):
    print("Dataset structure looks consistent.")
