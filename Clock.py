from tkinter import *
from tkinter.ttk import *
from time import strftime


root=Tk()
root.title('Clock')
label= Label(root, font=('Pacifico', 40, 'bold'), background = 'orange', foreground='green')
label.pack(anchor='center')

def time():
    string=strftime('%H:%M:%S %p') 
    label.config(text=string) #This string text comes in the label
    label.after(1000,time) #.after is used for scheduling function call

time()

root.mainloop()
