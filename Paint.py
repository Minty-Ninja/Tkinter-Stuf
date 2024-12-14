from tkinter import *
from tkinter.colorchooser import askcolor

root = Tk()
pen = Button(root, text="pen")
brush= Button(root, text="brush")
color = Button(root, text="color")
eraser = Button(root, text="eraser")
slider = Scale(root, from_=1, to=10, orient= HORIZONTAL) #MAkes a SLIDERRRR
canvas = Canvas(root, bg="white", width=600, height=600)

pen.grid(row=0, column=0)
brush.grid(row=0, column=1)
color.grid(row=0, column=2)
eraser.grid(row=0, column=3)
slider.grid(row=0, column=4)
canvas.grid(row=1, columnspan=5)






root.mainloop()