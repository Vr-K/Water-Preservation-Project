import cv2
import numpy as np
from ultralytics import YOLO
import matplotlib.pyplot as plt
import os


MODEL_PATH = "yolov8n.pt"  
DATA_ROOT = r"C:/Users/acer/Desktop/Heatmap/data"  
GAUSSIAN_SIZE = 75
ALPHA = 0.6                 # this is for transparency
MAX_DISPLAY = 3             # Maximum number of image that can be displayed at one time


# Load YOLOv8 model
model = YOLO(MODEL_PATH)

# this creates output folder for the generated heatmaps
OUTPUT_ROOT = os.path.join(DATA_ROOT, "heatmaps")
os.makedirs(OUTPUT_ROOT, exist_ok=True)

display_count = 0

# Walk through all subfolders and images
for root, dirs, files in os.walk(DATA_ROOT):
    for file in files:
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            image_path = os.path.join(root, file)
            print(f"Processing: {image_path}")

            # Load image
            img = cv2.imread(image_path)
            if img is None:
                print(f"Failed to load {image_path}, skipping.")
                continue

            height, width = img.shape[:2]
            heatmap = np.zeros((height, width), dtype=np.float32)

            # Run YOLO detection
            results = model.predict(source=image_path)

            # this generates gaussian blobs for detected objects
            for box in results[0].boxes.xyxy:
                x1, y1, x2, y2 = box.cpu().numpy()
                cx = int((x1 + x2) / 2)
                cy = int((y1 + y2) / 2)

                blob = np.zeros_like(heatmap, dtype=np.float32)
                cv2.circle(blob, (cx, cy), GAUSSIAN_SIZE, 1, -1)
                blob = cv2.GaussianBlur(blob, (0, 0),
                                        sigmaX=GAUSSIAN_SIZE/2,
                                        sigmaY=GAUSSIAN_SIZE/2)
                heatmap += blob

            # Normalize heatmap to normal size i.e(0-255)
            if np.max(heatmap) > 0:
                heatmap = np.clip(heatmap / np.max(heatmap) * 255, 0, 255).astype(np.uint8)
            else:
                heatmap = heatmap.astype(np.uint8)

            # Apply color map
            heatmap_color = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)

            # Overlay heatmap on original image
            blended = cv2.addWeighted(img, 1 - ALPHA, heatmap_color, ALPHA, 0)

            # Save heatmap, maintaining folder structure
            relative_path = os.path.relpath(root, DATA_ROOT)
            output_folder = os.path.join(OUTPUT_ROOT, relative_path)
            os.makedirs(output_folder, exist_ok=True)
            output_path = os.path.join(output_folder, f"heatmap_{file}")
            cv2.imwrite(output_path, blended)
            print(f"Saved heatmap: {output_path}")

            # Display the heatmap (limited to MAX_DISPLAY)
            if display_count < MAX_DISPLAY:
                plt.figure(figsize=(10, 6))
                plt.imshow(cv2.cvtColor(blended, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.title(f"Heatmap: {file}")
                plt.show()
                display_count += 1

print("All images processed!")
