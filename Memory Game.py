from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.title("Memory")

OPen= Button(root, text="Open")
Save=Button(root, text="Save")
Add=Button(root, text="Add")
Delete= Button(root, text="Delete")
Search=Entry(root, width=40)

OPen.pack(side=LEFT, padx=10, pady=10)
Delete.pack(side=RIGHT, padx=10, pady=10)
Save.pack(padx=10, pady=10)
Search.pack()
Add.pack(padx=10, pady=10)

Fr= Frame(root)
ScB=Scrollbar(Fr, orient= "vertical")
ScB.pack(side=RIGHT, fill=Y)

lb=Listbox(root, width=60, yscrollcommand=ScB.set, bg="Turquoise")
for i in range(100):
    lb.insert(END, "November "+str(i))


lb.pack(side=LEFT, padx=5)
ScB.config(command=lb.yview)
Fr.pack(side=RIGHT)

root.mainloop()


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from tkinter import *
from tkinter.filedialog import *

#File Handling
#pgzrun- Single player 2D games





root = Tk()
root.title("Memory")


# Defining Functions
def Delete(): 
    x= lb.curselection()  #Current selected item in the listbox
    if x:
        lb.delete(x)

def Adds(): 
    lb.insert(END, Search.get()) #Gets value of entry box
    Search.delete(0,END) #Deletes everything from Start to end in Entry Box

def Opens(): 
    y= askopenfile(title="Opening file") #Used to open a file dialog box 
    if y is not None: #Checking if Y exists, if any file is selected
        lb.delete(0, END) #Whatever previous content was there in list box is deleted
        r= y.readlines() #Function to read the text file lines
        for i in r: #Loop statement- Iterating through the lines
            lb.insert(END, i.strip()) #END is end, i.strip()= Removes any white spaces from the file

def Savess(): 
    s= asksaveasfile(defaultextension=".txt") #Open a dialogue box for saving the file
    if s is not None:  #Checking if anything has been selected
        for i in lb.get(0, END): #Iterates through listbox items
            print(i.strip(), file=s) #Write on ur file as new file
        lb.delete(0, END) #Deletes everything from listbox


OPen= Button(root, text="Open", command=Opens)
Save=Button(root, text="Save", command=Savess)
Add=Button(root, text="Add", command=Adds)
Delete= Button(root, text="Delete", command=Delete)
Search=Entry(root, width=40)

OPen.pack(side=LEFT, padx=10, pady=10)
Delete.pack(side=RIGHT, padx=10, pady=10)
Save.pack(padx=10, pady=10)
Search.pack()
Add.pack(padx=10, pady=10)

Fr= Frame(root)
ScB=Scrollbar(Fr, orient= "vertical")
ScB.pack(side=RIGHT, fill=Y)

lb=Listbox(Fr, width=60, yscrollcommand=ScB.set, bg="Turquoise")
for i in range(100):
    lb.insert(END, "November "+str(i))


lb.pack(side=LEFT, padx=5)
ScB.config(command=lb.yview)
Fr.pack(side=RIGHT)

root.mainloop()
