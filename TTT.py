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
    
