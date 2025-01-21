#Image manipulation
import cv2

#Grayscaling
x = cv2.imread("Crazy Cat.jpeg")

cv2.imshow("Original", x)
cv2.waitKey(0)
cv2.destroyAllWindows()

y= cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", y)

cv2.waitKey(0)
cv2.destroyAllWindows()


#Average Pixel to Grayscale w/o library

import cv2

#Grayscaling
x = cv2.imread("Crazy Cat.jpeg")

cv2.imshow("Original", x)
cv2.waitKey(0)
cv2.destroyAllWindows()

(row, col) = x.shape[0:2] #Converting image to grayscale
for i in range(row): 
    for j in range(col): 
        x[i, j] = sum(x[i, j]*0.33) #0.33- Calculates approx grayscale val

cv2.imshow("grayscale", x)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Rotating AN Image

x = cv2.imread("Crazy Cat.jpeg")

cv2.imshow("Original", x)
cv2.waitKey(0)
cv2.destroyAllWindows()

(row, col) = x.shape[0:2]
s = cv2.getRotationMatrix2D((col/2, row/2), 45, 1)
res = cv2.warpAffine(x, s, (col, row))

cv2.imwrite("Rotated.jpeg", res)

#----------------------------------------------------------------------------------------------

y = cv2.imread("Crazy Monkey.jpeg")

cv2.imshow("Original", y)
cv2.waitKey(0)
cv2.destroyAllWindows()

(rows, cols) = y.shape[0:2]
temp = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
rest = cv2.warpAffine(y, temp, (cols, rows))


cv2.imwrite("Rotate.jpeg", rest)

#Converting image from RGB to HSV (Hue, Saturation and Value)

im = cv2.imread("Crazy Cat.jpeg")
cv2.imshow("Original", im)
x = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV",x)

cv2.waitKey(0)
cv2.destroyAllWindows()