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
