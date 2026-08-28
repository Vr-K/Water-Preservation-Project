# albumentation using https://albumentations.ai/docs/3-basic-usage/bounding-boxes-augmentations/ tutorial

##############################################
# this is only for one image at a time, currently, need to clean up and add loop folder function
# ONLY WORKS FOR YOLO DATASET FORMAT
##############################################

# pip install albumentations
# command window > python > select python interpeter

import albumentations as A
import cv2
import numpy as np
import array
import random

#SEED_NUM = random.random()

# how to handle bboxes
train_transform = A.Compose([
    #A.RandomCrop(width=450, height=450, p=1.0),         # add more transforms here when needed
    A.HorizontalFlip(p=1)
    #A.RandomBrightnessContrast(p=0.2),
], bbox_params=A.BboxParams(
    format='yolo',
    label_fields=['class_labels'],
    min_visibility=0.1,              # Keep boxes even if slightly cropped
    min_area=0,                   # keep small boxes
), seed = 333)

# load image and prep bboxes as numpy array
image = cv2.imread("C:/Users/korke/Wetlands AI/1c0dde26-DJI_0946.JPG")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
h, w = image.shape[:2]              # 

bboxes = []      # [x_center, y_center, width, height]
class_labels = []   # int label

# open and read txt file and turn to array
# while line:
#     print(line.strip())
#     line = file.readline()
#     array2 = file.read(0)
#     with open("C:/Users/korke/Wetlands AI/1c0dde26-DJI_0946.txt", "rb") as file:      # open in binary
#         file.seek(2, 2)                                                             # from 2 to end
#         array3 = file.read().decode("utf-8")                                       # read until end
#     array4 = array3 + " " + array2              # needs to be in specific order in albumentation
#     master_array.append(array4)

# with open("C:/Users/korke/Wetlands AI/1c0dde26-DJI_0946.txt") as f:
#     array2 = f.read(0)
#     line = f.readline()
#     array3 = line[2:]
#     array4 = array3, " ", array2
#     array4 = float(array4)
#     master_array.append(array4)

with open("C:/Users/image/location/path/image.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) != 5:
            continue
        cls_id = int(parts[0])
        x_c = float(parts[1])
        y_c = float(parts[2])
        width = float(parts[3])
        height = float(parts[4])
        bboxes.append([x_c, y_c, width, height])
        class_labels.append(cls_id)

bboxes = np.array(bboxes, dtype=np.float32)    # bboxes
class_labels = np.array(class_labels, dtype=np.int32)  # labels

# this one actually needs to be EVERY SINGLE BBOX IN THE IMAGE
# class_labels = np.array(['Lupiini', 'Kurtturuusu', 'Jattiputki', 'Jattipalsami', 'Piisku', 'Tatar', 'Terttuselja', 'Valkokarhunkoynnos', 'Viitapihlaja-angervo'])

result = train_transform(image = image, bboxes = bboxes, class_labels = class_labels)

# results
augmented_image = result['image']
augmented_bboxes = result['bboxes']             # Returns as numpy array if input was array
augmented_labels = result['class_labels']

cv2.imwrite("augmented_image.jpg", cv2.cvtColor(augmented_image, cv2.COLOR_RGB2BGR))

with open("augmented_labels.txt", "w") as f:
    for box, label in zip(augmented_bboxes, augmented_labels):
        f.write(f"{int(label)} {box[0]} {box[1]} {box[2]} {box[3]}\n")
