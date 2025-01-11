from tkinter import *
from tkinter import messagebox
import time
import random

root = Tk()
root.title("Ping Pong")

#Canvas for the game
canvas = Canvas(root, width=1200, height=800, highlightthickness=5)
canvas.config(bg = "Dark Green")
canvas.pack()

txt = canvas.create_text(600, 20, font=("Calibri", 30, "bold"), text=" : ", fill="Blue")

#Dividing point between screen
canvas.create_line(600,0,600,1200, fill="Blue")
middle_circle= canvas.create_oval(10, 10, 150, 150, outline="white")
canvas.move(middle_circle, 525,350)
root.update()


#Score


root.mainloop()

-------------------------------------------------------------------------------

from tkinter import *
from tkinter import messagebox
import time
import random

root = Tk()
root.title("Ping Pong")

#Canvas for the game
canvas = Canvas(root, width=1200, height=800, highlightthickness=5)
canvas.config(bg = "Dark Green")
canvas.pack()

txt = canvas.create_text(600, 20, font=("Calibri", 30, "bold"), text=" : ", fill="Blue")

#Dividing point between screen
canvas.create_line(600,0,600,1200, fill="Blue")
middle_circle= canvas.create_oval(10, 10, 150, 150, outline="white")
canvas.move(middle_circle, 520,350)
root.update()



#Padel 1 class
class Padel1(): 
    def __init__(self, canvas, col):
        self.canvas = canvas
        self.id= canvas.create_rectangle(10,180,25,280,fill=col)
        self.y = 0 #Initializing vertical movement
        self.canvas_height = self.canvas.winfo_height()
        self.canvas.bind_all("a", self.turn_left)
        self.canvas.bind_all("d", self.turn_right)
    def draw(self): 
        self.canvas.move(self.id, 0, self.y) #Intialising
        pos = self.canvas.coords(self.id) #GEtting padel position
        if pos[1]<=0: 
            self.y = 0
        if pos[3]>= 800: 
            self.y = 0
    def turn_left(self,event):
        self.y = -4
    def turn_right(self, event): 
        self.y = +4


#Padel 2 class
class Padel2(): 
    def __init__(self, canvas, col):
        self.canvas = canvas
        self.id= canvas.create_rectangle(1185,180,1200,280,fill=col)
        self.y = 0 #Initializing vertical movement
        self.canvas_height = self.canvas.winfo_height()
        self.canvas.bind_all("<KeyPress-Up>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Down>", self.turn_right)
    def draw(self): 
        self.canvas.move(self.id, 0, self.y) #Intialising
        pos = self.canvas.coords(self.id) #GEtting padel position
        if pos[1]<=0: 
            self.y = 0
        if pos[3]>= 800: 
            self.y = 0
    def turn_left(self,event):
        self.y = -4
    def turn_right(self, event): 
        self.y = +4

#Ball class
class ball():
    #Updating the score
    def update(self):
        canvas.configure(text = str(self.score1) + ':' + str(self.score2))
    def __init__(self, canvas, Paddle1, Paddle2, col): 
        self.Paddle1 = Paddle1
        self.Paddle2 = Paddle2
        self.canvas = canvas 
        self.id = canvas.create_oval(10,10,30,30,fill=col)
        self.canvas.move(self.id, 600, 400)
        ispeed = [1,2,3,4,5,6]
        random.shuffle(ispeed)
        self.x=ispeed[1]
        self.y=ispeed[2]
        self.canvasheight= self.canvas.winfo_height()
        self.canvasheight= self.canvas.winfo_width()
        self.score1 = 0
        self.score2 = 0
    def draw(self):
        #Moving the ball
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id) 
        #Checking collision with edge
        if pos[1] <= 0: 
            self.y = 3
        if pos[3]>= 800: 
            self.y = -3
        if pos[0] <=0: 
            self.score1 += 1
            self.x = 3
            canvas.itemconfigure(canvas, text = str(self.score1) + ':' + str(self.score2))
        if pos[2] >= 1200:
            self.score2 += 1 
            self.x = -3
            canvas.itemconfigure(canvas, text = str(self.score1) + ':' + str(self.score2))
        if self.hitpaddle1(pos): 
            self.x = 4
        if self.hitpaddle2(pos): 
            self.x= -4
    def hitpaddle1(self, pos):
        paddlepos = self.canvas.coords(self.Paddle1.id)
        if pos[1] >= paddlepos[1] and pos[1] <= paddlepos[3] : 
            if pos[0] >= paddlepos[0] and pos[0] <= paddlepos[2] : 
                return True
        return False 

    def hitpaddle2(self, pos):
        paddlepos = self.canvas.coords(self.Paddle2.id)
        if pos[1] >= paddlepos[1] and pos[1] <= paddlepos[3] : 
            if pos[2] >= paddlepos[0] and pos[2] <= paddlepos[2] : 
                return True
        return False 



Paddle1 = Padel1(canvas, "blue")
Paddle2 = Padel2(canvas, "orange")
Ball = ball(canvas, Paddle1, Paddle2, "white")
while True:
    Paddle1.draw()
    Paddle2.draw()
    Ball.draw()
    root.update()
    




root.mainloop()
