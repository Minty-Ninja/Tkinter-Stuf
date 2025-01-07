from tkinter import *
from tkinter import messagebox
import time
import random

root = Tk()
root.title("Ping Pong")

#Canvas for the game
canvas = Canvas(root, width=1200, height=800, highlightthickness=5)
canvas.config(bg = "Dark Green")
canvas.pack()

txt = canvas.create_text(600, 20, font=("Calibri", 30, "bold"), text=" : ", fill="Blue")

#Dividing point between screen
canvas.create_line(600,0,600,1200, fill="Blue")
middle_circle= canvas.create_oval(10, 10, 150, 150, outline="white")
canvas.move(middle_circle, 525,350)
root.update()


#Score


root.mainloop()