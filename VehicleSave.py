import cv2

#Opening the video file to read frames
vid = cv2.VideoCapture("cars.mp4")
file = cv2.CascadeClassifier("cars.xml")

while True:
    ret, frames = vid.read()
    #If no frames are captured in the video
    if not ret: 
        break
    x = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    #Detecting cars in the greyscale img
    cars = file.detectMultiScale(x, 1.1, 1)
    
    #Looping through all detected cars and drawing red rect
    for (x, y, w, h) in cars: 
        cv2.rectangle(frames, (x,y), (x+w, y+h), (0, 0, 255), 3)
        
        
    cv2.imshow("Title", frames)
    if cv2.waitKey(20) == 27:
        break

cv2.destroyAllWindows()
        