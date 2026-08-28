Files regarding the project, only work as local, but can be added as CSC

- multiple files named heatmap example code on how to possibly generate a working attention/intensity heatmaps for YOLOv8. Has not been verified yet(have forgotten to verify, will get back to this when we have a working model).
- ***albumentation.py*** on how to implement albumentation, currently works on only one file per time, need to add "repeat until have gone each file in folder" capability.
- ***SAM2.py*** file to turn regular bbox dataset into segmented dataset 
- ***testSAM2.py*** to test how well the SAM2 managed to segement a given portion of dataset. currently very choppy, might be the wrong file uploaded to repo. need to double check.
- ***train.py*** to actually train the model(or reuse TrainSegModel, both should work)
- ***CSC_base.py*** hot to implement the code in CSC format file. Forgot to save an example
- ***CSC_base2.txt*** how to implement the code in CSC format copy paste    (uses SAM2.py as example)
