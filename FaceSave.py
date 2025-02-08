import cv2
import numpy as np
import os, sys

#Storage
stor = "haarcascade_frontalface_default.xml"
datasets = "datasets"
sub_data= "Idhant"

path= os.path.join(datasets, sub_data)
if not os.path.isdir(path):
    os.mkdir(path) 

#Defining Image size
(width,height)= (100, 100)
face_cascade = cv2.CascadeClassifier(stor)
webcam = cv2.VideoCapture(0)
