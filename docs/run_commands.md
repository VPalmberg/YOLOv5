# Run commands

## Training (standard)
python train.py --img 640 --batch 16 --epochs 30 --data data/custom_dataset.yaml --weights yolov5s.pt --cache

## Training (CPU fallback)
python train.py --img 416 --batch 4 --epochs 10 --data data/custom_dataset.yaml --weights yolov5n.pt --device cpu

## Resume training
python train.py --weights runs/train/exp/weights/last.pt --resume

## Detection on images
python detect.py --weights runs/train/exp/weights/best.pt --img 640 --conf 0.25 --source data/images

## Detection on webcam
python detect.py --weights runs/train/exp/weights/best.pt --source 0 --conf-thres 0.4 --img 640 --device 0
