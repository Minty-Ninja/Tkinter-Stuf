from tkinter import *
from tkinter import messagebox
import time 

root=Tk()
root.title("StopWatch")

#Variables for time
hour= StringVar()
minute=StringVar()
second=StringVar()

#Setting all Variable values to 0
hour.set("00")
minute.set("00")
second.set("00")



Bt= Button(root, title="Set Timer")
Hour= Entry(root, width=3, font=("Calibri", 18, ""), fg=("Blue"), textvariable=hour)
Minute= Entry(root, width=3, font=("Calibri", 18, ""), fg=("Red"), textvariable=minute)
Second= Entry(root, width=3, font=("Calibri", 18, ""), fg=("Green"), textvariable=second)

-----------------------------------------------------------------------------

from tkinter import *
from tkinter import messagebox
import time 

root=Tk()
root.title("StopWatch")
root.geometry("400x400")

#Variables for time
hour= StringVar()
minute=StringVar()
second=StringVar()

#Setting all Variable values to 0
hour.set("00")
minute.set("00")
second.set("00")

def StopWatch(): 
    try:
        #Converting everythng into seconds and adding them up
        var= int(hour.get()) * 3600  + int(minute.get()) * 60 + int(second.get())
    except: 
        print ("Input right Valueee")
    while var>-1: 
        mins, secs= divmod(var, 60)
        hours= 00
        if mins>60: 
          hours, mins=divmod(mins,60)
        hour.set("{00:2d}".format(hours)) #Formatting the hour to 2 decimal places
        minute.set("{00:2d}".format(mins)) #Formatting the minute to 2 decimal places
        second.set("{00:2d}".format(secs)) #Formatting the second to 2 decimal places
        root.update()
        time.sleep(1) #Removes execution for one second and then updates- Makes project sleep for that many seconds
        if var==0: 
            messagebox.showinfo("Done", 'Time is Finished')
        
        var-=1

Bt= Button(root, text="Set Timer", command=StopWatch)
Hour= Entry(root, width=3, font=("Calibri", 18, ""), fg=("Blue"), textvariable=hour).place(x=100, y=100)
Minute= Entry(root, width=3, font=("Calibri", 18, ""), fg=("Red"), textvariable=minute).place(x=200, y=100)
Second= Entry(root, width=3, font=("Calibri", 18, ""), fg=("Green"), textvariable=second).place(x=300, y=100)

Bt.pack()





        



root.mainloop()
