import cv2

x = cv2.imread("Whiteboard.jpeg")

#Drawing a line
sp = (0,0)
ep = (25,25)

col = (0, 0, 0)

thc = 5

Acte = cv2.line(x, sp, ep, col, thc)
cv2.imshow("NewLine", Acte)
cv2.waitKey(0)
cv2.destroyAllWindows()
