import cv2
import numpy as np

x = cv2.imread("Heheheheheheh.png", 1)
y = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)

img = cv2.blur(y, (3,3))

#Detect cirles
h = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 10, param1 = 54, param2 = 40, minRadius = 2, maxRadius = 20) #(Blurred image, method for detection, ratio, min distance between center, Edge detection, Circle center, Wht circle shud be detected of smallest radius, Max)

#Draw the circle that is detected
if h is not None: 
    h = np.uint16(np.around(h))
    for i in h[0, :]:
        a,b,r = i[0], i[1], i[2]
        cv2.circle(x, (a, b), r, (0, 0, 0), 5)
        cv2.circle(x, (a, b), 1, (0, 0, 0), 5)
        cv2.imshow("Blax", x)
        cv2.waitKey(0)


      
