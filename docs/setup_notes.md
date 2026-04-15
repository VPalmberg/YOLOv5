# Local YOLOv5 setup notes

Recommended project layout:

project_root/
├── yolov5/
└── yolov5_project_repo/

Then copy:
- `yolov5_project_repo/yolov5_data/custom_dataset.yaml`
into
- `yolov5/data/custom_dataset.yaml`

Training command:
python train.py --img 640 --batch 16 --epochs 30 --data data/custom_dataset.yaml --weights yolov5s.pt --cache

CPU fallback:
python train.py --img 416 --batch 4 --epochs 10 --data data/custom_dataset.yaml --weights yolov5n.pt --device cpu
