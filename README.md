# YOLOv5 Tool Detection Project

This repository is prepared for a course project on object detection using YOLOv5.

## Selected classes
- screwdriver
- wrench

## Current status
Parts 1–3 are not finished yet.
This repository is prepared in advance so that Parts 4–5 can be completed quickly later.

## Repository structure
- `dataset/images/train` — training images
- `dataset/images/val` — validation images
- `dataset/labels/train` — YOLO labels for training images
- `dataset/labels/val` — YOLO labels for validation images
- `yolov5_data/custom_dataset.yaml` — YOLOv5 dataset configuration
- `docs/report_draft.md` — report draft template
- `docs/parts_and_tasks.md` — task division by parts
- `docs/part4_checklist.md` — preparation checklist for Part 4
- `docs/part5_checklist.md` — preparation checklist for Part 5
- `scripts/verify_dataset.py` — quick dataset consistency checker

## Class IDs
- 0 = screwdriver
- 1 = wrench

## What to do when Parts 1–3 are finished
1. Put training images into `dataset/images/train`
2. Put validation images into `dataset/images/val`
3. Put matching label files into `dataset/labels/train` and `dataset/labels/val`
4. Check that every image has a matching `.txt` label file
5. Clone YOLOv5 into a separate folder or next to this repository
6. Copy `yolov5_data/custom_dataset.yaml` into the `yolov5/data` folder
7. Run training

## Example training command
```bash
python train.py --img 640 --batch 16 --epochs 30 --data data/custom_dataset.yaml --weights yolov5s.pt --cache
```

## Example detection command
```bash
python detect.py --weights runs/train/exp/weights/best.pt --img 640 --conf 0.25 --source data/images
```
