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

#global variables - GREETINGS



window = Tk()

l2 = Label(window, text="",bg="light cyan")
l2.pack()

l0 = Label(window, text="MUSIC MAIN MENU",font='Helvetica 16 bold' ,bg="light cyan")
l0.pack()


l5 = Label(window, text="",bg="light cyan")
l5.pack()

def donothing():
    pass

def close_window (root): 
    root.destroy()

#CREATING VARIOUS BUTTONS FOR THE VARIOUS PROGRAMS THAT ARE WITHIN GRAND CENTRAL - WILL VARY DEPENDING ON THE USER 

def option1():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-COMPsci\\ALBUMmenu-CS.py")
    window.destroy()

b1 = Button(window, text="ALBUMS ", command=option1)
b1.pack()

l0 = Label(window, text="",bg="light cyan")
l0.pack()

def option14():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-COMPsci\\TK_COMPsci_v3.py")
    window.destroy()

b15 = Button(window, text="MAIN MENU",command=option14)
b15.pack()

window.resizable(0,0)
window.resizable(width=FALSE, height=FALSE)
window.title("MUSIC MAIN MENU - COMPsci")
window.geometry("400x500")
window.configure(background='light cyan')




mainloop()

