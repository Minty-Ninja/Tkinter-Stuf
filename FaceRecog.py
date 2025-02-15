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

-------------------------------------------------------------------------------------------------------
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
        #Loop through each image inside folder
        for filename in os.listdir(x):
            path = x+'/'+filename
            #Assign ID
            label = id
            images.append(cv2.imread(path, 0)) #Reading in greyscale
            labels.append(int(label))
        id+=1 #Iterating through id
(width, height) = (140, 100)
#Converting list into numpy arrays
(image, labels) = [np.array(list) for list in [images, labels]]

#Creating face recognizer model    
model = cv2.face.LBPHFaceRecognizer_create()

#Trainging the model
model.train(images, labels)

#Recognizing face from live camera
fc = cv2.CascadeClassifier(stor)

#Opening webcam
webcam= cv2.VideoCapture(0)

try: 
    while True:
        (_, im) = webcam.read()
        gr = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)

        #Detect faces in frame
        facess = fc.detectMultiScale (gr, 1.3, 5)
        for (x, y, w, h) in facess:
            cv2.rectangle(im, (x, y), (x+w, y+h), (0,0,255), 2)

            #Cropping + Resizing image
            face = gr[y:y+h, x:x+w]
            resize = cv2.resize(face, (width, height))

            #Using model
            pred = model.predict(resize)
            cv2.rectangle(im, (x, y), (x+w, y+h), (0,255,0), 2)
            if pred[1] < 500:
                cv2.putText(im, '%s-%.0f' %
                (names[pred[0]], pred[1])(x-10, y-10), 
                cv2.FONT_HERSHEY_DUPLEX, 1, (255,0,0))
            else: 
                cv2.putText(im, 'Unrecognized person', 
                (x-10, y-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,0,0))

        cv2.imshow('OpenCv', im)
        key = cv2.waitKey(1)
        if key == 27: 
            break
finally: 
    webcam.release()
    cv2.destroyAllWindows()





        
