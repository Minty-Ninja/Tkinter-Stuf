import cv2
import os
from PIL import Image

print(os.getcwd())

#Folder for all the images
os.chdir(r"C:\Users\DELL\Desktop\Coding Stuff\Python Stuff Fr\OpenCVVV\Images")
x = r"C:\Users\DELL\Desktop\Coding Stuff\Python Stuff Fr\OpenCVVV\Images"

mean_h = 0
mean_w = 0
#No. of images
y = len(os.listdir("."))
print(y)

for i in os.listdir("."): 
    img = Image.open(os.path.join(x, i))
    width, height = img.size
    mean_w += width
    mean_h += height

mean_w = int(mean_w/y)
mean_h = int(mean_h/y)
print(mean_w, mean_h)

for i in os.listdir("."): 
    if i.endswith("jpg") or i.endswith("jpeg") or i.endswith("png"): 
        ig = Image.open(os.path.join(x, i))
        width, height = ig.size
        print(width, height)

        #resizing
        img_resize = ig.resize((mean_w), (mean_h), Image.LANCZOS)
        img_resize.save(i, "JPEG", quality = 95)

        print(ig.filename.split('\\')[-1], "is resized")

--------------------------------------------------------------------------------------------------------------------
import cv2
import os
from PIL import Image

print(os.getcwd())

#Folder for all the images
os.chdir(r"C:\Users\DELL\Desktop\Coding Stuff\Python Stuff Fr\OpenCVVV\Images")
x = r"C:\Users\DELL\Desktop\Coding Stuff\Python Stuff Fr\OpenCVVV\Images"

mean_h = 0
mean_w = 0
#No. of images
y = len(os.listdir("."))
print(y)

for i in os.listdir("."): 
    img = Image.open(os.path.join(x, i))
    width, height = img.size
    mean_w += width
    mean_h += height

mean_w = int(mean_w/y)
mean_h = int(mean_h/y)
print(mean_w, mean_h)

for i in os.listdir("."): 
    if i.endswith("jpg") or i.endswith("jpeg") or i.endswith("png"): 
        ig = Image.open(os.path.join(x, i))
        width, height = ig.size
        print(width, height)

        #resizing
        img_resize = ig.resize((mean_w, mean_h), Image.LANCZOS)
        img_resize.save(i, "JPEG", quality = 95)

        print(ig.filename.split('\\')[-1], "is resized")


#Generating Video
def gen(): 
    imgf= "."
    fn = "Generated video.avi"
    os.chdir(r"C:\Users\DELL\Desktop\Coding Stuff\Python Stuff Fr\OpenCVVV\Images")
    imgs = [img for img in os.listdir(imgf)
            if img.endswith(".jpeg") or img.endswith(".png") or img.endswith(".jpg")]
    print (imgs)
    frame = cv2.imread(os.path.join(imgf, imgs[0]))
    height, width, layers = frame.shape
    vid = cv2.VideoWriter(fn, 0, 1, (width, height))
    for i in imgs: 
        vid.write(cv2.imread(os.path.join(imgf, i)))
    cv2.destroyAllWindows()
    vid.release()

gen()
