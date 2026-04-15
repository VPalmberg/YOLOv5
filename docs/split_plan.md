# Dataset split plan

## Split ratio
- train = 80%
- val = 20%

## Planned numbers
- total images: about 90
- train images: 72
- val images: 18

## Split rule
Use a simple fixed rule for consistency:
- every 5th image goes to validation
- all other images go to training

## Important rule
The same filename must be used for:
- image file
- label file

Examples:
- images/train/001.jpg ↔ labels/train/001.txt
- images/val/005.jpg ↔ labels/val/005.txt

## Final check
After splitting the dataset:
1. count train images
2. count val images
3. check that each image has a matching label
4. run:
   python scripts/verify_dataset.py
