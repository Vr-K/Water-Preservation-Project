from ultralytics import YOLO
import matplotlib.pyplot as plt

model = YOLO('yolov8m-seg.pt')  # Load a segmentation-capable YOLOv8 model
results = model.predict(source='https://ultralytics.com/images/bus.jpg')  # Run inference

# Get image with masks and bounding boxes drawn
img_with_masks = results[0].plot()

plt.imshow(img_with_masks)
plt.axis('off')
plt.show()
