# YOLOv5 – OBJECT_MAIN Project

## Project Overview
This project trains a YOLOv5 model to detect:
- screwdriver
- wrench

All preparation steps (Parts 1–4) are assumed completed:
1. Use case defined and theory written
2. Images collected and organized in OBJECT_MAIN
3. Annotated in YOLO format with OpenLabeling
4. Dataset structure verified

---

## Checking dataset preparation (Parts 1–4)

### 1. Verify folder structure
tree ~/objects_detector/OBJECT_MAIN -L 3

### 2. Verify images and labels are empty
ls -l ~/objects_detector/OBJECT_MAIN/dataset/images/train
ls -l ~/objects_detector/OBJECT_MAIN/dataset/images/val
ls -l ~/objects_detector/OBJECT_MAIN/dataset/labels/train
ls -l ~/objects_detector/OBJECT_MAIN/dataset/labels/val

### 3. Verify YAML file
cat ~/objects_detector/OBJECT_MAIN/yolov5_data/custom_dataset.yaml

### 4. Verify dataset consistency
python ~/objects_detector/OBJECT_MAIN/scripts/verify_dataset.py

### 5. Check project instructions
cat ~/objects_detector/OBJECT_MAIN/docs/project_rules.md
cat ~/objects_detector/OBJECT_MAIN/docs/split_plan.md

---

## Training and Testing YOLOv5 (Part 5)

### 1. Activate YOLOv5 environment
cd ~/yolov5
source ~/yolov5_env/bin/activate

### 2. Copy dataset YAML
cp ~/objects_detector/OBJECT_MAIN/yolov5_data/custom_dataset.yaml ~/yolov5/data/custom_dataset.yaml

### 3. Start training
python train.py --img 640 --batch 16 --epochs 30 --data data/custom_dataset.yaml --weights yolov5s.pt --cache

### 4. Resume training if needed
python train.py --weights runs/train/exp/weights/last.pt --resume

### 5. Run detection on validation images
python detect.py --weights runs/train/exp/weights/best.pt --img 640 --conf 0.25 --source ~/objects_detector/OBJECT_MAIN/dataset/images/val

### 6. Run detection on webcam (optional)
python detect.py --weights runs/train/exp/weights/best.pt --source 0 --conf-thres 0.4 --img 640 --device 0

### Notes
- Image and label filenames must match exactly.
- Use 80/20 split for train/val datasets.
- Annotate images in YOLO format: `class_id x_center y_center width height`.
- Ensure `class_list.txt` in OpenLabeling matches the classes (screwdriver, wrench).
