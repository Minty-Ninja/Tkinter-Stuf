from tkinter import *
import tkinter as tk
import random
from tkinter import messagebox


root=Tk()
root.title('Product Game')

def make(): 
    num1= random.randint(1,10)
    num2 = random.randint(1,10)
    return num1, num2, num1*num2
    
num1,num2,result= make()

#Generating UI
label = Label(root, text='Guess the product of {} and ?'.format(num1))
label.pack()


En= Entry(root)
En.pack()

b1= Button(root, text='Check?')
b1.pack()


def NewGame():
    global num1, num2, result
    num1, num2, result= make()
    label.config(text="Guess the prodcut of {} and ?".format(num1))
    messagebox.showinfo("A random number is {}".format(num1))
    En.delete(0,tk.END)

new_game=Button(root, text='New Game', command=NewGame)
new_game.pack()
NewGame()

root.mainloop()
