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

---------------------------------------------------------------------------------------------------------------------------------------------------------------------
from tkinter import *
root=Tk()

#Function for converting the stuff
def Conv():
    grm= float(var.get())*1000
    pnd= float(var.get())*2.20462
    onc= float(var.get())*35.274
    T1.delete("1.0", END)     #1.0 refers to the position within the text widget
    T1.insert(END, grm)       #End refers to the end of the text    
    T2.delete("1.0", END)
    T2.insert(END,pnd)
    T3.delete("1.0", END)         #Delete will delete all the text from the beginning to the end of the widget
    T3.insert(END,onc)



#Creating Labels
label=Label(root, text="Enter your weight(in kg)")
label.pack()

label2= Label(root, text="Grams")
label3= Label(root, text="Ounces")
label4= Label(root, text="Pounds")
var= StringVar()


entryBox= Entry(root, textvariable=var)
T1= Text(root, height=1, width=20)
T2= Text(root, height=1, width=20)
T3= Text(root, height=1, width=20)



button=Button(root, text="Convert?", command=Conv)
label.grid(row=0,column=0)
button.grid(row=0,column=2)
label2.grid(row=1,column=0)
label3.grid(row=1,column=1)
label4.grid(row=1,column=2)
entryBox.grid(row=0, column=1)
T1.grid(row=2,column=0)
T3.grid(row=2,column=2)
T2.grid(row=2,column=1)
button.grid(row=0,column=2)


root.mainloop()
