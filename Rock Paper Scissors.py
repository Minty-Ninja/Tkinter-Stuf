import random
from tkinter import *
import tkinter.font as font

pScore=0
cScore=0
root=Tk()

list= [('rock',0), ('paper',1), ('scissors',2)]
root.title("Game")
Tfont=font.Font(size=12)
label1= Label(root, text='Rock, Paper, Scissors', font=font.Font(size=30),fg='Grey')
label1.pack()
Wfr= Label(root, text='', font=font.Font(size=15),fg='Red')
Wfr.pack()
frame=Frame(root)
frame.pack()


root.mainloop()

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
import random
from tkinter import *
import tkinter.font as font


pScore = 0
cScore = 0

root = Tk()
root.title("Rock Paper Scissors Game")

# Define font styles
title_font = font.Font(size=30)
font1 = font.Font(size=15)
font2 = font.Font(size=12)


title_label = Label(root, text='Rock Paper Scissors', font=title_font, fg='Grey')
title_label.pack()


status_label = Label(root, text='', font=font1, fg='Green')
status_label.pack()

frame = Frame(root)
frame.pack()


def play(player_choice):
    global pScore, cScore

    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        result = "Player Won!!!"
        pScore += 1
    else:
        result = "Computer Won!!!"
        cScore += 1


    status_label.config(text=result, fg="Green" if "Player" in result else "Red")
    Scorefr.config(text=f"Your Selected: {player_choice.capitalize()}      Player Score: {pScore}\n"
                            f"Computer Selected: {computer_choice.capitalize()}      Computer Score: {cScore}")


option= Label(root, text='Your Options:', font=font2, fg='Grey')
option.pack()

# Create the Rock button
rock= Button(frame, text='Rock', width=10, bd=1,bg='lightcoral',
command=lambda: play('rock'))
rock.grid(row=0, column=0)

# Create the Paper button
paper= Button(frame, text='Paper', width=10, bd=1, bg='lightgrey',
command=lambda: play('paper'))
paper.grid(row=0, column=1)

# Create the Scissors button
scissors = Button(frame, text='Scissors', width=10, bd=1,  bg='lightblue',
command=lambda: play('scissors'))
scissors.grid(row=0, column=2)

# Score label
Scorefr = Label(root, text=f"Your Selected: None      Player Score: 0\n"
"Computer Selected: None      Computer Score: 0",
font=font2, fg='Black')
Scorefr.pack()

# Start the main event loop
root.mainloop()
