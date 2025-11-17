from ultralytics import YOLO

# Load the pretrained YOLOv8 segmentation model
model = YOLO('runs/segment/yolo8m_seg_custom/weights/best.pt')

# Run inference on the image
results = model.predict(source='D:/Jakub/datasets/Niinijärvi29092023/DJI_0630.JPG', imgsz=768)

# Show each result
for result in results:
    result.show()  # visualize detected objects and masks

    # Access segmentation masks data
    masks = result.masks.data
