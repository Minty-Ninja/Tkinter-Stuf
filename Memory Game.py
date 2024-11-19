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
