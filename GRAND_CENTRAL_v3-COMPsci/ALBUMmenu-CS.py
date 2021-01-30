#TKinter GC Main Menu - MSTR
#July 2018
#Nathan Jones

from tkinter import messagebox, Label, Button, FALSE, Tk, Entry
from tkinter import *
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from uuid import getnode as get_mac

import time
import socket
import sys
import os.path
import os
import string 
import getpass
import random
import statistics
import itertools
import datetime



window = Tk()

l2 = Label(window, text="",bg="light cyan")
l2.pack()

l0 = Label(window, text="ALBUMS MENU",font='Helvetica 16 bold' ,bg="light cyan")
l0.pack()

l5 = Label(window, text="",bg="light cyan")
l5.pack()

def donothing():
    pass

def close_window (root): 
    root.destroy()

#CREATING VARIOUS BUTTONS FOR THE VARIOUS PROGRAMS THAT ARE WITHIN GRAND CENTRAL - WILL VARY DEPENDING ON THE USER 

def option1():

    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-COMPsci\\albums-COMPsci\\R.E.D-CS.py")
    window.destroy()

b1 = Button(window, text="The Game - The R.E.D Album ", command=option1)
b1.pack()

def option2():

    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-COMPsci\\albums-COMPsci\\2001-CS.py")
    window.destroy()

b1 = Button(window, text="             Dr. Dre - 2001                ", command=option1)
b1.pack()

def option3():

    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-COMPsci\\albums-COMPsci\\California-CS.py")
    window.destroy()

b1 = Button(window, text="          Blink 182 - California      ", command=option3)
b1.pack()

def option4():

    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-COMPsci\\albums-COMPsci\\1ML-CS.py")
    window.destroy()

b1 = Button(window, text=" Linkin Park - One More Light ", command=option4)
b1.pack()



l5 = Label(window, text="",bg="light cyan")
l5.pack()

def option14():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-COMPsci\\MUSICmenu-CS.py")
    window.destroy()

b15 = Button(window, text="BACK",command=option14)
b15.pack()

window.resizable(0,0)
window.resizable(width=FALSE, height=FALSE)
window.title("ALBUMS MAIN MENU - COMPsci")
window.geometry("400x650")
window.configure(background='light cyan')




mainloop()
