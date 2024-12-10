from tkinter import *
from gtts import gTTS
import os


root = Tk()
root.title("Text to Speech Converter")
root.geometry("500x500")


fr = Frame(root, bg="red", height=200)
fr2 = Frame(root, bg="Green", height=300)

fr.pack(fill=X)
fr2.pack(fill=X)


data = Entry(fr2)
data.place(x=130, y=52)

lbl=Label(fr, text="Text to Speech", font="Calibri", fg="Black")
lbl.place(x=130, y=70)


def conv(): #Function for converting text to speech
    language="en" #English
    x= gTTS(text=data.get(), lang=language, slow=False) #Slow is for speaking speed- Doesn't havr to be super slow
    x.save("Convert.wav") #File Name and Format is saved
    os.system("Convert.wav") #Saves to System

Submit = Button(fr2, text="Submit", command=conv)
Submit.place(x=130, y=130)






root.mainloop()