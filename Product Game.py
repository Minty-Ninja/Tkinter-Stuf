from tkinter import *
import random
from tkinter import messagebox

root=Tk()
root.title('Product Game')

#Generating UI
label = Label(root, text='Guess the product of {} and ?'.format(num1))
label.pack()

b1= Button(root, text='Check?')
b1.pack()

new_game=Button(root, text='New Game')
new_game.pack()

En= Entry(root)



root.mainloop()