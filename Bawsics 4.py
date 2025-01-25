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

-----------------------------------------------------------------------------------------------------------
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

#Drawing a circle on the image
x = cv2.imread("Whiteboard.jpg")

sp = (250,250)
col = (0,0,0)
thc=10
radius = 100

y = cv2.circle(x, sp, radius, col, thc)

cv2.imshow("Circle", y)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Draw text on screen
sp = (250, 250)
col = (0, 0, 0)
thc = 3
font1 = cv2.FONT_HERSHEY_TRIPLEX
fontScale = 2

x = cv2.imread("Whiteboard.jpg")

y = cv2.putText(x, "Helloooo", sp, font1, fontScale, col, thc)

cv2.imshow("Text", y)

cv2.waitKey(0)
cv2.destroyAllWindows()
