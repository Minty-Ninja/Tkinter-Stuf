from tkinter import *
import speech_recognition as sr
import os
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import *


root = Tk()
root.title("Speech to Text!")


def click(): 
    x= sr.Recognizer() #Initialize the speech recognizer
    with sr.Microphone() as source: #Sets the source for the microphone
        print("Epack")
        audio = x.listen(source) #Listens from source
        try: 
            text = x.recognize_google(audio) #Converting the audio to text using recognize google
        except: 
            text = 'Sorry, Could not recognize'
        
        Enter.delete(1.0, END) #Making sure that everything from the start to the end is deleted
        Enter.insert(END, text)



def save(): 
    y = asksaveasfile(defaultextension=".txt") #Opens the save as file pop up- Saves file as text because default
    if y:
        print(Enter.get(1.0, END), file=y) #Get everything from beginning to end
    else: 
        messagebox.showerror("Error", "Text not saved")


Lb = Label(root, text= "Voice Notepad", font="Arial, 32")
Rcd = Button(root, text="Start Recording", command=click)
Enter = Text(root, height = 3, width=40)
Save= Button(root, text="Save the Text", command=save)

Lb.grid(row = 0, column = 1)
Rcd.grid(row = 1, column=0)
Enter.grid(row = 1, column=1)
Save.grid(row = 1, column=2)



root.mainloop()
