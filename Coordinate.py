import cv2

#Function for clicking on the image
def coord(event, x, y, flag, params):
    #If left key is clicked
    if event==cv2.EVENT_LBUTTONDOWN: 
        print(x, y)
        #Choosing a font
        font1 = cv2.FONT_HERSHEY_COMPLEX_SMALL
        cv2.putText(a, str(x) + ","+str(y), (x, y), font1, 1, (0, 0, 255), 2)
        #SHowing updated img w text
        cv2.imshow("Cartton", a)

    if event==cv2.EVENT_RBUTTONDOWN: 
        font2 = cv2.FONT_HERSHEY_DUPLEX


        #Getting the BGR code
        bl = a[y, x, 0]
        gr = a[y, x, 1]
        re = a[y, x, 2]

        cv2.putText(a, str(bl) + ","+ str(gr) + "," + str(re), (x,y), font2, 1, (255, 255, 0) , 2)
        cv2.imshow("Cartton", a)







if __name__ == "__main__":
    a = cv2.imread("Cartton.jpeg", 1)
    cv2.imshow("Cartton", a)
    cv2.setMouseCallback("Cartton", coord)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

