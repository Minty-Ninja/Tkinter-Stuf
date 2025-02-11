import cv2
import os,sys
import numpy as np

size= 4
stor  = "haarcascade_frontalface_default.xml"
datasets = "datasets"

print("Recognizing face. Please ensure sufficient lighting")

#Creating a list of images and corresponding names
(images, labels, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(datasets):
    for subdir in dirs: 
        names[id] = subdir
        x  = os.path.join(datasets, subdir)





        
