from tkinter import *
from tkinter import messagebox
import time 

root=Tk()
root.title("StopWatch")

#Variables for time
hour= StringVar()
minute=StringVar()
second=StringVar()

#Setting all Variable values to 0
hour.set("00")
minute.set("00")
second.set("00")



Bt= Button(root, title="Set Timer")
Hour= Entry(root, width=3, font=("Calibri", 18, ""), fg=("Blue"), textvariable=hour)
Minute= Entry(root, width=3, font=("Calibri", 18, ""), fg=("Red"), textvariable=minute)
Second= Entry(root, width=3, font=("Calibri", 18, ""), fg=("Green"), textvariable=second)

