from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title("Tables")
lb = Label(root, text = "Mathematical Table")
lb2 = Label(root, text="Number and Range")
lb.grid(row=0,column=1, columnspan=3,pady=30)
lb2.grid(row=2,column=0, padx=10)

endVal = IntVar() #Whtever user selects is converted to integer
R1= Radiobutton(root, text="10", variable=endVal, value=10) 
R2= Radiobutton(root, text="20", variable=endVal, value=20) 
R3= Radiobutton(root, text="30", variable=endVal, value=30) 
endVal.set(10)


R1.grid(row=2, column=3, padx= 30)
R2.grid(row=3, column=3, padx= 30)
R3.grid(row=4, column=3, padx= 30)

#Drop down listtt (Combo Box)
num= IntVar()
numb=Combobox(root, textvariable=num, width=10)
numb["values"]=tuple(range(100))
numb.grid(row=2, column=2)

table=Label(root, anchor="center")


def maths(): 
    e=''
    for i in range(endVal.get()+1):
        e+=str(num.get())+'  x  '+str(i)+'  =  '+str(num.get()*i) + '\n'
    table.configure(text=e)


button=Button(root, text= "Generate?", command=maths)
button.grid(row = 4, column=2)

table.grid(row=6, column=2, pady=30)

root.mainloop()