# Project rules

## Selected classes
- 0 = screwdriver
- 1 = wrench

## Class order
The class order must always stay the same:
1. screwdriver
2. wrench

## Image format
- All images must be in `.jpg` format
- Filenames must not contain spaces or special symbols

## Label format
- All labels must be in YOLO format
- Each image must have a matching `.txt` label file with the same filename stem

## Naming rule
Examples:
- `001.jpg` ↔ `001.txt`
- `002.jpg` ↔ `002.txt`

## Dataset split
- train/val split = 80/20
- For about 90 images:
  - 72 images for training
  - 18 images for validation

## Important rule
After annotation starts, image filenames must not be changed.

## Final dataset structure
dataset/
├── images/
│   ├── train/
│   └── val/
└── labels/
    ├── train/
    └── val/
