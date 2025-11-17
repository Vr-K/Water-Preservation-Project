## TO run

if __name__ == '__main__':
    from ultralytics import YOLO
    model = YOLO('runs/segment/yolo8m_seg_custom3/weights/best.pt')
    results = model.train(
        data='LandscapeSegmentation.v3i.yolov8/data.yaml', 
        imgsz=768,
        epochs=50,
        batch=8,
        name='yolo8m_seg_custom'
    )