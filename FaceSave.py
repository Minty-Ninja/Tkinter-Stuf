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

---------------------------------------------------------------------------------------------------------------------
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

count = 0
#Looping program for capturing 30 images
while count<30: 
    (_, im) = webcam.read() # Capturing one single frame from the video
    x= cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    fc = face_cascade.detectMultiScale(im, 1.3, 4)
    for (x, y, w, h) in fc: 
        cv2.rectangle(im, (x,y), (x+w, y+h), (255,255,255), 2)
        face = x[y:y+h, x:x+w] 
        res = cv2.resize(face, (width,height))
        cv2.imwrite('%s/%s.png' % (path,count) , res)
    count+=1
    cv2.imshow("OOf", im)
    key = cv2.waitKey(10)
    if key == 27: 
        break

