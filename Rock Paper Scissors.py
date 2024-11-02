import random
from tkinter import *
import tkinter.font as font

pScore=0
cScore=0
root=Tk()

list= [('rock',0), ('paper',1), ('scissors',2)]
root.title("Game")
Tfont=font.Font(size=12)
label1= Label(root, text='Rock, Paper, Scissors', font=font.Font(size=30),fg='Grey')
label1.pack()
Wfr= Label(root, text='', font=font.Font(size=15),fg='Red')
Wfr.pack()
frame=Frame(root)
frame.pack()


root.mainloop()