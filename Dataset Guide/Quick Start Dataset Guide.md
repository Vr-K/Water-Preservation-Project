yolov8 env is to run the working AI

labelstudio env is to run annonation tools

# the dataset type

i dont know which dataset we are going to go from the following:
    - YOLO
    - YOLO with images
    - YOLOv8
    - YOLOv8 with images
    - YOLOv8 OBB
    - YOLOv8 OBB with images
    - COCO
with images datasets are just datasets that can be applied more easily

# Create new environment (use python 3.11 or 3.12)
python3.11 -m venv labelstudio_env
labelstudio_env\Scripts\activate
pip install label-studio

# Launch Label Studio
label-studio

# close env
deactivate

# links to helpful things in relating to labeling:

label studio tutorial:
https://www.youtube.com/watch?v=R1ozTMrujOE

docker for i forget where this could be used. it's needed for WebODM though, which might become relevant in future
https://www.docker.com/products/docker-desktop/

