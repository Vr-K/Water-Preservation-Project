import cv2
import numpy as np
import matplotlib.pyplot as plt
from ultralytics import YOLO

model = YOLO('yolov8m-seg.pt')
results = model.predict(source='https://ultralytics.com/images/bus.jpg')

result = results[0]
orig_img = result.orig_img
names = result.names  # Class id to name mapping

# Get unique detected classes sorted for display order
unique_classes = sorted(set(result.boxes.cls.cpu().numpy().astype(int)))

for cls_id in unique_classes:
    class_name = names[cls_id]
    combined_mask = np.zeros(orig_img.shape[:2], dtype=np.uint8)

    for mask, detected_cls_id in zip(result.masks.xy, result.boxes.cls.cpu().numpy().astype(int)):
        if detected_cls_id == cls_id:
            pts = np.array(mask).astype(np.int32)
            combined_mask = cv2.fillPoly(combined_mask, [pts], 255)

    # Mask original image to show only current class objects
    output_img = cv2.bitwise_and(orig_img, orig_img, mask=combined_mask)

    plt.figure(figsize=(10, 10))
    plt.imshow(output_img)
    plt.axis('off')
    plt.title(f"Objects of class '{class_name}'")
    plt.show()
