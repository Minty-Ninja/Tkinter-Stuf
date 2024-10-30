from tkinter import *

root=Tk()
root.geometry("300x150")

label= Label(root, text="Crackers", font="40")
label.pack()
frame=Frame(root)
frame.pack()

#Creating frames
fr=Frame(root)
fr.pack(side=BOTTOM)
button=Button(frame, text="Rockets", fg="Green", bg="Red")
button.pack(side=LEFT)

button=Button(frame, text="Flowerpot", fg="Blue", bg="Red")
button.pack(side=LEFT)

button=Button(fr, text="sparkler", fg="Green", bg="Red")
button.pack(side=BOTTOM)

button=Button(fr, text="Sparks", fg="Blue", bg="Red")
button.pack(side=LEFT)

#Crrating scroll barr for the listbox
scbar=Scrollbar(root)
scbar.pack(side=RIGHT, fill=Y)

#Creating List Boxes
x=Listbox(root, yscrollcommand= scbar.set,height=40, width=15, bg="Red", font="40",fg="blue")
lb=Label(root,text="Anything", font="40")
x.insert(1,"abcd")
x.insert(2,"efgh")
x.insert(3,"ijkl")
x.insert(4,"mnop")
x.insert(5,"qrst")
lb.pack()
x.pack()
scbar.config(command=x.yview)





root.mainloop()
