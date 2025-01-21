import cv2

x = cv2.imread("Whiteboard.jpg")

#Drawing a line
sp = (0,0)
ep = (500,500)

col = (0, 0, 0)

thc = 5

Acte = cv2.line(x, sp, ep, col, thc)
cv2.imshow("NewLine", Acte)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Drawing a Rectangle on the Image

x = cv2.imread("Whiteboard.jpg")

sp = (250,250)
ep = (500,300)

col = (0, 0, 0)

thc = 5
y = cv2.rectangle(x, sp, ep, col, thc)

cv2.imshow("Rectangle", y)

cv2.waitKey(0)
cv2.destroyAllWindows()

sp = (250,250)
ep = (500,300)

col = (0, 0, 0)

thc = -1 #Colour fill
y = cv2.rectangle(x, sp, ep, col, thc)

cv2.imshow("Rectangle", y)

cv2.waitKey(0)
cv2.destroyAllWindows()

