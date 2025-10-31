
#### Install YOLOv8

The AI used to detect the objects, in AI Vision.
Needs Python 3.8 to 3.11

1) in terminal:
    pip install torch torch-vision opencv-python 

2) install YOLO on windows:
    - Open Command Prompt (not PowerShell).
    - Create a virtual environment (recommended):
        python -m venv yolov8-env
        yolov8-env\Scripts\activate
    - Upgrade pip and install YOLOv8
        pip install --upgrade pip
    OR
        python.exe -m pip install --upgrade pip 
        pip install ultralytics
    - Verify installation:
        yolo

3) Installation Guide for Ubuntu 20.04+ (I have not tested this one since using windows machine)
    - Update your system:
        sudo apt update && sudo apt upgrade
    - Install Python and pip:
        sudo apt install python3-pip python3-venv
    - Set up a virtual environment:
        python3 -m venv yolov8-env
        source yolov8-env/bin/activate
    - Install YOLOv8 via pip:
        pip install ultralytics

4) the terminal should read (yolov8-env). this is your CLI.

5) Commands
    task    detect tells YOLOv8 that you want to perform object detection.
    mode    predict indicates that you’re using the model for prediction (as opposed to training).
    model   yolov8n.pt specifies which pre-trained model you want to use.
    source  ’path/to/your/image.jpg’ points to the image or video you want to analyze.

6) YOLO COMMANDS:
- You can Close the env with
    deactivate
in shell command menu.
- And reactivate with
    yolov8-env\Scripts\activate
command line.

## above yolo tut is unusable since jakub is making a special AI that combines YOLOv8 and svin transform into one super ai /joke

#### Install Label Studio

A Youtube tutorial if you are a more visual learner:
https://www.youtube.com/watch?v=R1ozTMrujOE

This is what we will use to make our custom dataset. Using Label Studio.
Python needs to be version 3.8 or newer up to 3.11. So set up an env with python 3.11

1) pip install
    pip install label-studio
    - and if the first does not work try:
    pip install --only-binary=all label-studio
    - otherwise check error report.
2) 
- set up the env
    C:\Python311_location -m venv labelstudio_env
- activates the env
    labelstudio_env\Scripts\activate
- install label studio
    pip install label-studio

3) CLI for this is (labelstudio_env)

congrats! you've created a working label studio .env

#### How to Label data in Label Studio and make a image object dataset

1) open the Labelstudio_env
    labelstudio_env\Scripts\activate

2) run
    label-studio

3) open browser and move over to localhost:8000/projects
    - if you do not have account for label studio, you need to make one

NOTE: you can create multiple types of datasets. this tutorial will focus on making a object detection dataset for this tut.

4) create project and import images

5) choose Label All Tasks. aka the big blue button

6) choose template, in this case:
    - "Object detection with bounding boxes"

7) Next we need to specify classes.
    - Like Dog, Plate, Spoon, Cat etc. the thing we are identifying.
    - remove classes irrelevant to the dataset
    - save

8) Start labeling
    - return to previous page
    - once again. choose the big blue button with the words Label All Tasks

9) To label object
    - Click Class
    - Click and drag the bounding box over the object
    - Submit

NOTE you can have multiple objects in the same image

11) Keep labeling objects until satisfied

12) Once finished Export as either:

    - YOLO
    - YOLO with images
    - YOLOv8
    - YOLOv8 with images
    - YOLOv8 OBB
    - YOLOv8 OBB with images
    - COCO

our project uses *COCO* files
    
with images datasets are just datasets that can be applied more easily

AND CONGRATS! you have created a labeled dataset that can be used in training a AI
