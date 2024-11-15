from tkinter import *
from tkinter.ttk import *
from time import strftime
import random

def Randomm():
    x= random.randint(0,255)
    y= random.randint(0,255)
    z= random.randint(0,255)
    return f"#{x:02x}{y:02x}{z:02x}"

root=Tk()
root.title('Clock')
label= Label(root, font=('Pacifico', 40, 'bold'), background = Randomm(), foreground=Randomm())
label.pack(anchor='center')





def time():
    string=strftime('%H:%M:%S %p') 
    label.config(text=string) #This string text comes in the label
    label.after(1000,time) #.after is used for scheduling function call

time()

root.mainloop()
