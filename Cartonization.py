import cv2

#Class for cartonization
class carton:
    def __init__(self):
        pass
    def render(self, path):
        x = cv2.imread(path)
        #If img doesn't exist
        if x is None:
            print("No image")
            return None

        #Resizing the image
        x = cv2.resize(x, (500, 300)) 

        #No of times image is shrunk
        y = 2
        smooth = 50
        temp = x
        for _ in range(smooth):
            temp = cv2.bilateralFilter(temp, 9, 9, 7)


        #Enlarging image back to original size 
        for _ in range(y): 
            temp = cv2.pyrUp(temp)

        #Converting image to greyscale
        gr = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)

        #Blurring effect
        blur= cv2.medianBlur(gr, 3)
        edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
        edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

        #Resizing the edges of the image
        edges = cv2.resize(edges, (temp.shape[1], temp.shape[0]))

        #Using Bitwise AND operator
        cartonized = cv2.bitwise_and(temp, edges)
        return cartonized
    
#Object Creation     
obj1 = carton()
file = "Place.jpeg"
rend = obj1.render(file)

if rend is not None: 
    cv2.imshow("Cartoon", rend)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("Cartton.jpeg", rend)