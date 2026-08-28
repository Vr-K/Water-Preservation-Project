######
# file used for specifically python
# works for whole folder
######

from ultralytics.data.converter import yolo_bbox2segment
from ultralytics import SAM

# 1. Convert boxes to segments automatically
yolo_bbox2segment(
    im_dir="C:/Users/input/dir/path/for/images/images/",                                           # images to segment
    sam_model="sam2_b.pt"                                                                          # The model used to generate masks
    #device="cuda"                                                                                 # Use "cpu" if you don't have a GPU, can also be ignored completely, mine doesnt work
)

# 2. Visualize a result using SAM 2's native prediction (avoids Unpack Error)
model = SAM("sam2_b.pt")
results = model.predict(
    source="C:/Users/input/dir/path/for/images/images/",                                           # original directory
    labels="C:/Users/output/dir/path/file_for_labels.txt"                                          # labels-segment folder
    # show=True
)
