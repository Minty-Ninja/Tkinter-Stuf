#Importing EVERYTHING FROM Tkinter moduleeeeeeeeeeeeeeee
from tkinter import *

#Creating Tkinter Windowwwwwwwwwwwwwwwwww
root = Tk()

#Window Sizzzzweeee
root.geometry('3600x800')


#Button variable = Button(Window Name, text, border, button colour, What happens when u click on button)
x = Button(root, text = "Bye Bye", bd = "8", background="Black", command=root.destroy) 

#Positionnnnnnnnn
x.pack(side="top")


root.mainloop()
