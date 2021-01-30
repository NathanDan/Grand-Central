#TKinter GC Main Menu - MSTR
#July 2018
#Nathan Jones

from tkinter import messagebox, Label, Button, FALSE, Tk, Entry
from tkinter import *
from datetime import datetime

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

l2 = Label(window, text="",bg="gray84")
l2.pack()

l0 = Label(window, text="ARTISTS - BLINK 182",font='Helvetica 16 bold' ,bg="gray84") #GIVING THE WINDOW A TITLE SO THE USER KNOWS WHAT MENU THEY ARE ON 
l0.pack() #DISPLAYING THE TITLE FOR THE USER/CLIENT TO SEE

l5 = Label(window, text="",bg="gray84")
l5.pack()

#THIS LABEL GIVES A SMALL/BREIF SUMMARY OF THE ALBUM THAT HAS BEEN SELECTED 
l1 = Label(window, text="""Blink-182 is an American rock band formed in Poway, California in 1992.
Since 2015, the lineup of the band has consisted of bassist and vocalist
Mark Hoppus, drummer Travis Barker, and guitarist and vocalist
Matt Skiba.
""",bg="gray84")  #CREATING A LABEL THAT WILL TELL THE USER ABOUT THE ALBUM
l1.pack()         #DISPLAYING THE LABEL

l6 = Label(window, text="",bg="gray84")
l6.pack()

#CREATING THE BUTTONS FOR EACH ALBUM, ONCE A BUTTON IS PRESSED IT WILL TAKE THEM TO ANOTHER GUI WHICH WILL DISPLAY THE ALBUM AND ALL OF THE SONGS IN THE ALBUM  
def option1():

    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\ARTISTS\\ALBUMS - BLINK 182\\California.py") #TAKING THE USER/CLIENT TO THEIR ALBUM THEY HAVE SELECTED
    window.destroy() #CLOSING THE WINDOW AUTOMATICALLY AS THEY LEAVE THE MENU

b1 = Button(window, text="                Blink 182 - California                 ", command=option1) #CREATING THE BUTTON AND ADDING THE ARTIST AND ALBUM NAME
b1.pack() #DISPLAYING THE BUTTONS FOR THE USER/CLIENT TO ACTUALLY SEE AND BE ABLE TO CLICK

def option2():

    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\ARTISTS\\ALBUMS - BLINK 182\\GH.py") #TAKING THE USER/CLIENT TO THEIR ALBUM THEY HAVE SELECTED
    window.destroy() #CLOSING THE WINDOW AUTOMATICALLY AS THEY LEAVE THE MENU

b1 = Button(window, text="             Blink 182 - Greatest Hits               ", command=option2) #CREATING THE BUTTON AND ADDING THE ARTIST AND ALBUM NAME
b1.pack() #DISPLAYING THE BUTTONS FOR THE USER/CLIENT TO ACTUALLY SEE AND BE ABLE TO CLICK

l5 = Label(window, text="",bg="gray84")
l5.pack()

def option14():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\ARTISTSmenu.py") #TAKING TEH USER/CLENT BACK TO THE PREVIOUS MENU
    window.destroy()                               #CLOSING THE WINDOW AUTOMATICALLY AS THEY LEAVE THE MENU  

b15 = Button(window, text="BACK",command=option14) #CREATING THE BUTTON THAT WILL BE DISPLAYED
b15.pack()                                         #DISPLAYING THE BUTTON ON THE MENU 

window.resizable(0,0)
window.resizable(width=FALSE, height=FALSE)#STOPPING THE USER/CLIENT FROM RESIZING THE CURRENT WINDOW 
window.title("ALBUMS MAIN MENU - MSTR")    #GIVING THE WINDOW A TITLE THAT WILL BE AT THE VERY TOP ALONGSIDE THE '- O X' BUTTONS 
window.geometry("400x500")                 #GENERATING THE SIZE OF THE WINDOW 
window.configure(background='gray84')      #GIVING THE WINDOW A SPECIFIC BACKGROUND COLOUR 

mainloop()

