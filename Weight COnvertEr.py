from tkinter import *
root=Tk()


#Creating Labels
label=Label(root, text="Enter your weight(in kg)")
label.pack()

label2= Label(root, text="Grams")
label3= Label(root, text="Ounces")
label4= Label(root, text="Pounds")

button=Button(root, text="Convert?")
label.grid(row=0,column=0)
button.grid(row=0,column=2)
label2.grid(row=1,column=0)
label3.grid(row=1,column=1)
label4.grid(row=1,column=2)

root.mainloop()