import cv2
import numpy as np
import time
print(cv2.__version__)

--------------------------------------------------------------------------------------------------
import cv2
import numpy as np
import time


print(cv2.__version__)


rv = cv2.VideoCapture("video.mp4")
time.sleep(1)



counter = 0
bg = 0

#Capturing the bg- Used for masking
---------------------------------------------------------------------------------------------------------------------------------------
import cv2
import numpy as np
import time


print(cv2.__version__)


rv = cv2.VideoCapture("video.mp4")
time.sleep(1)



counter = 0
bg = 0

#Capturing the bg- Used for masking
for i in range(60):
    return_val, bg= rv.read()
    if return_val == False:
        continue 

bg = np.flip(bg, axis=1)

#Reading each frame from the video
while (rv.isOpened()):
    return_val, img= rv.read()
    if not return_val:
        break
    counter+=1
    img = np.flip(img, axis=1)

    #Converting to HSV color
    Col = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #Finding Red colour
    small = np.array([100,40,40])
    big = np.array([100,255,255])
    mask1 = cv2.inRange(Col, small, big)

    #Finding another shade
    small = np.array([155,40,40])
    big = np.array([180,255,255])
    mask2 = cv2.inRange(Col, small, big)
    mask1=mask1+mask2 

    #Making mask smoother
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations=2)
    mask1= cv2.dilate(mask1,np.ones((3,3), np.uint8), iterations=1)

    #Inverse mask
    mask2 = cv2.bitwise_not(mask1)

    #Combining backgrounds and current frame
    result1 = cv2.bitwise_and(bg, bg, mask=mask1)
    result2 = cv2.bitwise_and(img, img, mask=mask2)

    #Final Output
    x = cv2.addWeighted(result1, 1, result2, 1, 0)

    #Displaying final video
    cv2.imshow("Final", x)
    c= cv2.waitKey(10)
    if c==27:
        break
    



    




