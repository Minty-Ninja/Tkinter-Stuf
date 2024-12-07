from tkinter import *
import random
from tkinter import messagebox
from functools import partial #Pass additional args to functions
from copy import deepcopy #Create copies of game board

root = Tk()
root.title("Tic-Tac-Toe")
turn = 0 #Whose turn it is
global board
board = [["" for x in range(3)] for y in range(3)]
def gb(gameboard, P1, P2):
    global button
    button = []
    
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

from tkinter import *
import random
from tkinter import messagebox
from functools import partial #Pass additional args to functions
from copy import deepcopy #Create copies of game board

root = Tk()
root.title("Tic-Tac-Toe")
turn = 0 #Whose turn it is
global board
board = [["" for x in range(3)] for y in range(3)]

def get_text(i,g,gbs,P1,P2): #Configure's text on buttons when multiplaying
    global turn
    if board[i][g] == "": 
        if turn%2 == 0:
            P1.config(state= DISABLED)
            P2.config(state=ACTIVE)
            board[i][g] = "X"
        else: 
            P1.config(state = ACTIVE)
            P2.config(state = DISABLED)
            board[i][g] = "O"
        turn+=1
         




def gb(game_board, P1, P2): #Making Gameboard
    global button, button2
    button = []
    button2 = []
    for i in range(3):
        a= 3+i #Adding 3 cause we need 3 buttons. Determines position
        button.append(i)
        for g in range(3): 
            button2.append(g)
            b=g
            button[i].append(g)
            get_t = partial(get_text, i, g, game_board, P1, P2,)
            button[i][g] = Button(game_board, bd=5, command = get_text, height = 4, width = 8)
            button[i][g].grid(row= a, column= b)
    game_board.mainloop()


def comp(game_board, P1, P2): #Computer Opponent
    global button, button2
    button = []
    button2 = []
    for i in range(3):
        a= 3+i #Adding 3 cause we need 3 buttons. Determines position
        button.append(i)
        for g in range(3): 
            button2.append(g)
            b=g
            button[i].append(g)
            get_t = partial(get_text_comp, i, g, game_board, P1, P2,)
            button[i][g] = Button(game_board, bd=5, command = get_text, height = 4, width = 8)
            button[i][g].grid(row= a, column= b)
    game_board.mainloop()


def play():
    S= Tk()
    S.geometry("250x250") 
    S.title("Main Menu")
    Head = Button(S, text= "Welcome to Tic-Tac-Toe", activeforeground= "Green", activebackground= "Black", bg="Pink", width=400, font="Pacifico", bd=5)
    Sp = Button(S, text= "Single Player", activeforeground= "Green", activebackground= "Black", bg="Pink", width=400, font="Pacifico", bd=5)
    Mp = Button(S, text= "MultiPlayer", activeforeground= "Green", activebackground= "Black", bg="Pink", width=400, font="Pacifico", bd=5)
    Exit = Button(S, text= "Exit", activeforeground= "Green", activebackground= "Black", bg="Pink", width=400, font="Pacifico", bd=5)
    Head.pack()
    Sp.pack()
    Mp.pack()
    Exit.pack()

    S.mainloop()


if __name__=='__main__': 
    play()

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from tkinter import *
import random
from tkinter import messagebox
from functools import partial #Pass additional args to functions
from copy import deepcopy #Create copies of game board

root = Tk()
root.title("Tic-Tac-Toe")
turn = 0 #Whose turn it is
global board
board = [["" for x in range(3)] for y in range(3)]

def Winner(b,l):  
    return((b[0][0]== l and b[0][1]==l and b[0][2]==l) or
     (b[1][0]== l and b[1][1]==l and b[1][2]==l) or
     (b[2][0]== l and b[2][1]==l and b[2][2]==l) or
     (b[0][0]== l and b[1][0]==l and b[2][0]==l) or
     (b[0][1]== l and b[1][1]==l and b[2][1]==l) or
     (b[0][2]== l and b[1][2]==l and b[2][2]==l) or
     (b[0][0]== l and b[1][1]==l and b[2][2]==l) or
     (b[0][2]== l and b[1][1]==l and b[2][0]==l))

    
def isfull(): 
    x= True
    for i in board: 
        if (i.count('')>0):
            x = False
    return x


    

def get_text(i,g,gbs,P1,P2): #Configures text on buttons when multiplaying
    global turn
    if board[i][g] == "": 
        if turn%2 == 0:
            P1.config(state= DISABLED)
            P2.config(state=ACTIVE)
            board[i][g] = "X"
        else: 
            P1.config(state = ACTIVE)
            P2.config(state = DISABLED)
            board[i][g] = "O"
        turn+=1
        button[i][g].config(text=board[i][g])
    if Winner(board, "X"): 
        gbs.destroy()
        mg = messagebox.showinfo("Finished","P1 Wins")
    elif Winner(board, "O"):
        gbs.destroy()
        mg = messagebox.showinfo("Finished", "P2 wins")
    elif (isfull()): 
        gbs.destroy()
        mg=messagebox.showinfo("Finished", "It's a tie") 

       
def Mlt(gboard):
    gboard.destroy()
    gboard= Tk()
    gboard.title("Multiplayer")
    l1 = Button(gboard, text="P1 = X", width=10)
    l1.grid(row=1, column=1)
    l2 = Button(gboard, text= "P2 = O")
    l2.grid(row = 2, column = 1)
    gb(gboard, l1, l2)

    




def gb(game_board, P1, P2): #Making Gameboard
    global button, button2
    button = []
    button2 = []
    for i in range(3):
        a= 3+i #Adding 3 cause we need 3 buttons. Determines position
        button.append(i)
        button[i] = []
        for g in range(3): 
            b=g
            button[i].append(g)
            get_t = partial(get_text, i, g, game_board, P1, P2,)
            button[i][g] = Button(game_board, bd=5, command = get_text, height = 4, width = 8)
            button[i][g].grid(row= a, column= b)
    game_board.mainloop()


def comp(game_board, P1, P2): #Computer Opponent
    global button, button2
    button = []
    button2 = []
    for i in range(3):
        a= 3+i #Adding 3 cause we need 3 buttons. Determines position
        button.append(i)
        for g in range(3): 
            button2.append(g)
            b=g
            button[i].append(g)
            get_t = partial(get_text_comp, i, g, game_board, P1, P2,)
            button[i][g] = Button(game_board, bd=5, command = get_text, height = 4, width = 8)
            button[i][g].grid(row= a, column= b)
    game_board.mainloop()


def play():
    S= Tk()
    S.geometry("250x250") 
    S.title("Main Menu")
    wpl= partial(Mlt, S)
    Head = Button(S, text= "Welcome to Tic-Tac-Toe", activeforeground= "Green", activebackground= "Black", bg="Pink", width=400, font="Pacifico", bd=5)
    Sp = Button(S, text= "Single Player", activeforeground= "Green", activebackground= "Black", bg="Pink", width=400, font="Pacifico", bd=5)
    Mp = Button(S, text= "MultiPlayer", activeforeground= "Green", activebackground= "Black", bg="Pink", width=400, font="Pacifico", bd=5, command=wpl)
    Exit = Button(S, text= "Exit", activeforeground= "Green", activebackground= "Black", bg="Pink", width=400, font="Pacifico", bd=5, command=S.quit)
    Head.pack()
    Sp.pack()
    Mp.pack()
    Exit.pack()


    S.mainloop()


if __name__=='__main__': 
    play()

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from tkinter import *
import random
from tkinter import messagebox
from functools import partial #Pass additional args to functions
from copy import deepcopy #Create copies of game board

root = Tk()
root.title("Tic-Tac-Toe")
turn = 0 #Whose turn it is
global board
board = [["" for x in range(3)] for y in range(3)]

def Winner(b,l):  
    return((b[0][0]== l and b[0][1]==l and b[0][2]==l) or
     (b[1][0]== l and b[1][1]==l and b[1][2]==l) or
     (b[2][0]== l and b[2][1]==l and b[2][2]==l) or
     (b[0][0]== l and b[1][0]==l and b[2][0]==l) or
     (b[0][1]== l and b[1][1]==l and b[2][1]==l) or
     (b[0][2]== l and b[1][2]==l and b[2][2]==l) or
     (b[0][0]== l and b[1][1]==l and b[2][2]==l) or
     (b[0][2]== l and b[1][1]==l and b[2][0]==l))

    
def isfull(): 
    x= True
    for i in board: 
        if (i.count('')>0):
            x = False
    return x


    

def get_text(i,g,gbs,P1,P2): #Configures text on buttons when multiplaying
    global turn
    if board[i][g] == "": 
        if turn%2 == 0:
            P1.config(state= DISABLED)
            P2.config(state=ACTIVE)
            board[i][g] = "X"
        else: 
            P1.config(state = ACTIVE)
            P2.config(state = DISABLED)
            board[i][g] = "O"
        turn+=1
        button[i][g].config(text=board[i][g])
    if Winner(board, "X"): 
        gbs.destroy()
        mg = messagebox.showinfo("Finished","P1 Wins")
    elif Winner(board, "O"):
        gbs.destroy()
        mg = messagebox.showinfo("Finished", "P2 wins")
    elif (isfull()): 
        gbs.destroy()
        mg=messagebox.showinfo("Finished", "It's a tie") 

def PC(): 
    #Defining Next Move of Computer
    el = []
    for i in range(len(board)): #First For Loop Goes through board
        for g in range(len(board[i])): #Second For Loop Goes through every Column
            if board[i][g] == "": 
                el.append([i,g])
    move = []
    if el == []:
        return #Passes Control Back to Main Program
    else: 
        for a in ['O', 'X']: 
            for b in el: 
                bcopy = deepcopy(board)
                bcopy[b[0]][b[1]] = a
                if Winner(bcopy, a): 
                    return b #Whatever is the possible move for computer is returned
        corner = []
        for i in el: 
            if i in [[0,0], [0,2], [2,0], [2,2]]:
                corner.append(i)
        if len(corner) > 0: 
            move= random.randint(0,len(corner)-1)
            return corner[move]
        edge = []
        for i in el: 
            if i in [[0,1], [1,0], [1,2], [2,1]]:
                edge.append(i)
        if len(edge) > 0: 
            move= random.randint(0,len(edge)-1)
            return edge[move]
        








def get_text_comp(i,g,gbs,P1,P2): #Configures text on buttons when multiplaying
    global turn
    if board[i][g] == "": 
        if turn%2 == 0:
            P1.config(state= DISABLED)
            P2.config(state=ACTIVE)
            board[i][g] = "X"
        else: 
            P1.config(state = ACTIVE)
            P2.config(state = DISABLED)
            board[i][g] = "O"
        turn+=1
        button[i][g].config(text=board[i][g])
    
    run = True

    if Winner(board, "X"): 
        gbs.destroy()
        run = False
        mg = messagebox.showinfo("Finished","P1 Wins")
    elif Winner(board, "O"):
        gbs.destroy()
        run=False
        mg = messagebox.showinfo("Finished", "Computer wins")
    elif (isfull()): 
        gbs.destroy()
        run = False
        mg=messagebox.showinfo("Finished", "It's a tie") 
    
    if run: 
        if turn%2 != 0:
            move = PC()
            button[move[0]][move[1]].config(state=DISABLED)
            get_text_comp(move[0], move[1], gbs, P1, P2) #Putting Position for Computer
    

def Mlt(gboard):
    gboard.destroy()
    gboard= Tk()
    gboard.title("Multiplayer")
    l1 = Button(gboard, text="P1 = X", width=10)
    l1.grid(row=1, column=1)
    l2 = Button(gboard, text= "P2 = O")
    l2.grid(row = 2, column = 1)
    gb(gboard, l1, l2)

    
def compu(gboard):
    gboard.destroy()
    gboard= Tk()
    gboard.title("Single Player")
    l1 = Button(gboard, text="P1 = X", width=10)
    l1.grid(row=1, column=1)
    l2 = Button(gboard, text= "Computer = O", width=10, state=DISABLED)
    l2.grid(row = 2, column = 1)
    comp(gboard, l1, l2)



def gb(game_board, P1, P2): #Making Gameboard
    global button, button2
    button = []
    button2 = []
    for i in range(3):
        a= 3+i #Adding 3 cause we need 3 buttons. Determines position
        button.append(i)
        button[i] = []
        for g in range(3): 
            b=g
            button[i].append(g)
            get_t = partial(get_text, i, g, game_board, P1, P2,)
            button[i][g] = Button(game_board, bd=5, command = get_t, height = 4, width = 8)
            button[i][g].grid(row= a, column= b)
    game_board.mainloop()


def comp(game_board, P1, P2): #Computer Opponent
    global button, button2
    button = []
    for i in range(3):
        a= 3+i #Adding 3 cause we need 3 buttons. Determines position
        button.append(i)
        button[i] = []
        for g in range(3): 
            b=g
            button[i].append(g)
            get_t = partial(get_text_comp, i, g, game_board, P1, P2,)
            button[i][g] = Button(game_board, bd=5, command = get_t, height = 4, width = 8)
            button[i][g].grid(row= a, column= b)
    game_board.mainloop()


def play():
    S= Tk()
    S.geometry("250x250") 
    S.title("Main Menu")
    wpl= partial(Mlt, S) #Versus Playes
    wpc= partial(compu, S) #Versus Computer
    Head = Button(S, text= "Welcome to Tic-Tac-Toe", activeforeground= "Green", activebackground= "Black", bg="Pink", width=400, font="Pacifico", bd=5)
    Sp = Button(S, text= "Single Player", activeforeground= "Green", activebackground= "Black", bg="Pink", width=400, font="Pacifico", bd=5, command=wpc)
    Mp = Button(S, text= "MultiPlayer", activeforeground= "Green", activebackground= "Black", bg="Pink", width=400, font="Pacifico", bd=5, command=wpl)
    Exit = Button(S, text= "Exit", activeforeground= "Green", activebackground= "Black", bg="Pink", width=400, font="Pacifico", bd=5, command=S.quit)
    Head.pack()
    Sp.pack()
    Mp.pack()
    Exit.pack()


    S.mainloop()


if __name__=='__main__': 
    play()





