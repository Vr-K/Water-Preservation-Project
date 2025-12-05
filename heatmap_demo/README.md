README – Heatmap Demo for Invasive Species Project

This folder contains a small demo that shows how we plan to use heatmaps (Grad-CAM) in our main invasive species detection project.

Right now, we don’t have our own trained model for invasive plants, so I made this demo using a pretrained ResNet152 model. The goal is to show how the heatmap will highlight the important part of an image that the AI uses to make a prediction.

Even though the model currently predicts normal ImageNet classes like “cat”, “dog”, “broccoli”, etc., the idea is the same. Once we train our invasive-species model, the heatmap will highlight leaves, stems, shapes, or textures that the model considers important.

What this demo does

Loads a pretrained ResNet152 model

Takes an input image

Runs Grad-CAM on the last convolutional layer

Generates a heatmap showing the most influential part of the image

Saves the results as:

gradcam_result.jpg (original image + heatmap)

gradcam_heatmap.jpg (heatmap only)

This is mainly for explainability. Later, when we classify invasive plants, we can show which parts of the plant caused the AI to identify it as invasive. This makes the model more trustworthy and helps users understand what the AI is “looking at.”

Files in this folder

grad_cam1_demo.py – main script for generating the heatmaps

test.jpg – sample image the script reads

outputs/ – optional output folder

venv/ – virtual environment (ignored in Git)

.gitignore – to avoid uploading unnecessary files

README.md – this explanation

How to run the demo

Install the required packages:

pip install torch torchvision pillow matplotlib opencv-python


Make sure your test image is named test.jpg (or change the filename inside the script).

Run the script:

python3 grad_cam1_demo.py


After running, check:

gradcam_result.jpg

gradcam_heatmap.jpg

These show how the heatmap looks.

Why this is relevant to our invasive species project

This demo is basically a preview of how our real model will work once it is trained.
The steps will be the same:

Input image of a plant

Model predicts whether it is invasive

Grad-CAM highlights the important region

