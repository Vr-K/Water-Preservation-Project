#####
# Rough version of the training . used locally. CSC version needs some information changed 
#####

if __name__ == '__main__':
    from ultralytics import YOLO
    model = YOLO('runs/segment/yolo8m_seg_custom3/weights/best.pt')          # or if starting the training and you dont have best, use just the chosen YOLO version
    results = model.train(
        data='LandscapeSegmentation.v3i.yolov8/data.yaml',                   # get data.yaml file, i think you can also get just use the dataset folder location here
        imgsz=768,                                                           # can be ignored, otherwise resizes the image size
        epochs=50,                                                           # epoch is how many completed runs
        batch=8,                                                             # batch is how many files per segction
        name='yolo8m_seg_custom'                                             # name of the given model
    )
