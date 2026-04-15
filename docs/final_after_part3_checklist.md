# Final checklist after Parts 1–3

1. Collect all final images in one place
2. Collect all final YOLO label files in one place
3. Check that every image has a matching label file
4. Split files into train and val sets
5. Move training images to dataset/images/train
6. Move validation images to dataset/images/val
7. Move training labels to dataset/labels/train
8. Move validation labels to dataset/labels/val
9. Run dataset verification:
   python scripts/verify_dataset.py
10. Copy yolov5_data/custom_dataset.yaml into yolov5/data/custom_dataset.yaml
11. Run training
12. Run detection test on images
13. Run webcam detection if needed
14. Record the final video
15. Add links and final details to the report
