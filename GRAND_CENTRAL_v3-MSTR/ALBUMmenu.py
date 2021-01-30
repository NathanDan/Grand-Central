#TKinter GC - ALBUM MENU
#2018
#Nathan Jones

from tkinter import messagebox, Label, Button, FALSE, Tk, Entry    #ALLOWING FOR TKINTER TO BE ACCESSED/UTILISED FOR THE PROGRAM TO USE ALL OF ITS FUNCTIONS AND GIVING THE PROGRAM A GUI                                           
from tkinter import *                                              #ALLOWING FOR ALL OF TKINTER'S MODULES TO BE IMPORTED 
from PIL import Image, ImageTk                                     #ALLOWING FOR IMAGES TO ADDED IN THE GUI FOR THE LIKES OF THE BACKGROUNDS AND OTHER IMAGES 

import time        #THIS ALLOWS FOR THE PROGRAM TO USE THE SLEEP FUNCTION WITHIN THE PROGRAM
import socket      #ALLOWS FOR THE PROGRAM TO GATHER IP AND MAC ADDRESSES
import sys         #ALLOWS ACCESS TO THE SYSTEM FROM WITHIN PYTHON 
import os.path     #ALLOWS THE PROGRAM TO OPEN OTHER SPECIFIC APPLICATIONS, IN THIS CASE THE GC PROGRAMS 
import os          #ALLOWS FOR CONTROL OF THE MACHINE AND IS OS INCLUDING THE LIKES OF SAVING, OPENING/CLOSING FILES, ETC. 
import string      #ALLOWS FOR DATA/ENTRIES TO BE RECOREDAS STRINGS AND NOT INDIVIDUAL CHARACTERS 
import statistics  #ALLOWS ACCESS TO THE STATISTICS LIBARY FOR THE DATA COLLECTION AND PROCESSING
import itertools   #ALLOWS ACCESS TO ACCESS TO THE ITERATORS LIBARY FOR EFFICENT LOOPING 
import datetime    #THIS ALLOWS FOR THE CURRENT TIME TO BE IMPORTED AND DISPLAYED FOR THE USER TO SEE 
import pyglet      #THIS IS THE MODULE THAT ALLOWS FOR THE SOUNDS/MUSIC/SONGS TO BE PLAYED 

window = Tk()      #DEFINING THE NAME OF THE WINDOW 

l2 = Label(window, text="",bg="gray84") #CREATING A ONE LINE SPACE
l2.pack()                               #DISPLAYING THE LABEL

l0 = Label(window, text="ALBUMS MENU",font='Helvetica 16 bold' ,bg="gray84") #GIVING THE WINDOW A TITLE SO THE USER KNOWS WHAT MENU THEY ARE ON 
l0.pack()                                                                    #DISPLAYING THE TITLE FOR THE USER TO SEE

l5 = Label(window, text="",bg="gray84") #CREATING A ONE LINE SPACE
l5.pack()                               #DISPLAYING THE LABEL

#CREATING THE BUTTONS FOR EACH ALBUM, ONCE A BUTTON IS PRESSED IT WILL TAKE THEM TO ANOTHER GUI WHICH WILL DISPLAY THE ALBUM AND ALL OF THE SONGS IN THE ALBUM  
def option1():

    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\albums\\R.E.D.py") #TAKING THE USER TO THEIR ALBUM THEY HAVE SELECTED
    window.destroy() #CLOSING THE WINDOW AUTOMATICALLY AS THEY LEAVE THE MENU

b1 = Button(window, text="          The Game - The R.E.D Album       ", command=option1) #CREATING THE BUTTON AND ADDING THE ARTIST AND ALBUM NAME
b1.pack() #DISPLAYING THE BUTTON FOR THE USER TO ACTUALLY SEE AND BE ABLE TO CLICK 

def option2():

    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\albums\\2001.py") #TAKING THE USER TO THEIR ALBUM THEY HAVE SELECTED
    window.destroy() #CLOSING THE WINDOW AUTOMATICALLY AS THEY LEAVE THE MENU

b1 = Button(window, text="                      Dr. Dre - 2001                       ", command=option2) #CREATING THE BUTTON AND ADDING THE ARTIST AND ALBUM NAME
b1.pack() #DISPLAYING THE BUTTON FOR THE USER TO ACTUALLY SEE AND BE ABLE TO CLICK

def option3():

    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\albums\\California.py") #TAKING THE USER TO THEIR ALBUM THEY HAVE SELECTED
    window.destroy() #CLOSING THE WINDOW AUTOMATICALLY AS THEY LEAVE THE MENU

b1 = Button(window, text="                Blink 182 - California                 ", command=option3) #CREATING THE BUTTON AND ADDING THE ARTIST AND ALBUM NAME
b1.pack() #DISPLAYING THE BUTTON FOR THE USER TO ACTUALLY SEE AND BE ABLE TO CLICK

def option4():

    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\albums\\GH.py") #TAKING THE USER TO THEIR ALBUM THEY HAVE SELECTED
    window.destroy() #CLOSING THE WINDOW AUTOMATICALLY AS THEY LEAVE THE MENU

b1 = Button(window, text="             Blink 182 - Greatest Hits               ", command=option4) #CREATING THE BUTTON AND ADDING THE ARTIST AND ALBUM NAME
b1.pack() #DISPLAYING THE BUTTON FOR THE USER TO ACTUALLY SEE AND BE ABLE TO CLICK

def option5():

    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\albums\\1ML.py") #TAKING THE USER TO THEIR ALBUM THEY HAVE SELECTED
    window.destroy() #CLOSING THE WINDOW AUTOMATICALLY AS THEY LEAVE THE MENU

b1 = Button(window, text="         Linkin Park - One More Light          ", command=option5) #CREATING THE BUTTON AND ADDING THE ARTIST AND ALBUM NAME
b1.pack() #DISPLAYING THE BUTTON FOR THE USER TO ACTUALLY SEE AND BE ABLE TO CLICK

def option6():

    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\albums\\PT.py") #TAKING THE USER TO THEIR ALBUM THEY HAVE SELECTED
    window.destroy() #CLOSING THE WINDOW AUTOMATICALLY AS THEY LEAVE THE MENU

b1 = Button(window, text="        Mike Shinoda - Post Traumatic       ", command=option6) #CREATING THE BUTTON AND ADDING THE ARTIST AND ALBUM NAME
b1.pack() #DISPLAYING THE BUTTON FOR THE USER TO ACTUALLY SEE AND BE ABLE TO CLICK

def option7():

    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\albums\\DC.py") #TAKING THE USER TO THEIR ALBUM THEY HAVE SELECTED
    window.destroy() #CLOSING THE WINDOW AUTOMATICALLY AS THEY LEAVE THE MENU

b1 = Button(window, text="            Ice Cube - Death Certificate         ", command=option7) #CREATING THE BUTTON AND ADDING THE ARTIST AND ALBUM NAME
b1.pack() #DISPLAYING THE BUTTON FOR THE USER TO ACTUALLY SEE AND BE ABLE TO CLICK

def option8():

    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\albums\\1l.py") #TAKING THE USER TO THEIR ALBUM THEY HAVE SELECTED
    window.destroy() #CLOSING THE WINDOW AUTOMATICALLY AS THEY LEAVE THE MENU

b1 = Button(window, text="  Bob Marley & The Wailers - One Love  ", command=option8) #CREATING THE BUTTON AND ADDING THE ARTIST AND ALBUM NAME
b1.pack() #DISPLAYING THE BUTTON FOR THE USER TO ACTUALLY SEE AND BE ABLE TO CLICK

def option9():

    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\albums\\AMWPS.py") #TAKING THE USER TO THEIR ALBUM THEY HAVE SELECTED
    window.destroy() #CLOSING THE WINDOW AUTOMATICALLY AS THEY LEAVE THE MENU

b1 = Button(window, text="Arctic Monkeys - Whatever People Say I Am, That's What I'm Not", command=option9) #CREATING THE BUTTON AND ADDING THE ARTIST AND ALBUM NAME
b1.pack() #DISPLAYING THE BUTTON FOR THE USER TO ACTUALLY SEE AND BE ABLE TO CLICK

def option10():

    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\albums\\BFS.py") #TAKING THE USER TO THEIR ALBUM THEY HAVE SELECTED
    window.destroy() #CLOSING THE WINDOW AUTOMATICALLY AS THEY LEAVE THE MENU

b1 = Button(window, text="            Bowling For Soup - The Songs People Actualy Liked            ", command=option10) #CREATING THE BUTTON AND ADDING THE ARTIST AND ALBUM NAME
b1.pack() #DISPLAYING THE BUTTON FOR THE USER TO ACTUALLY SEE AND BE ABLE TO CLICK

def option11():

    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\albums\\BE.py") #TAKING THE USER TO THEIR ALBUM THEY HAVE SELECTED
    window.destroy() #CLOSING THE WINDOW AUTOMATICALLY AS THEY LEAVE THE MENU

b1 = Button(window, text="                     Beady Eye - BE                       ", command=option11) #CREATING THE BUTTON AND ADDING THE ARTIST AND ALBUM NAME
b1.pack() #DISPLAYING THE BUTTON FOR THE USER TO ACTUALLY SEE AND BE ABLE TO CLICK


l5 = Label(window, text="",bg="gray84") #CREATING A ONE LINE SPACE
l5.pack()                               #DISPLAYING THE LABEL

def option14():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\MUSICmenu.py") #TAKING TEH USER BACK TO THE PREVIOUS MENU
    window.destroy()                               #CLOSING THE WINDOW AUTOMATICALLY AS THEY LEAVE THE MENU  

b15 = Button(window, text="BACK",command=option14) #CREATING THE BUTTON THAT WILL BE DISPLAYED
b15.pack()                                         #DISPLAYING THE BUTTON ON THE MENU 

window.resizable(0,0)                      #WINDOW WILL NOT GO INTO FULL SCREEN MODE 
window.resizable(width=FALSE, height=FALSE)#STOPPING THE USER/CLIENT FROM RESIZING THE CURRENT WINDOW 
window.title("ALBUMS MAIN MENU - MSTR")    #GIVING THE WINDOW A TITLE THAT WILL BE AT THE VERY TOP ALONGSIDE THE '- O X' BUTTONS 
window.geometry("400x650")                 #GENERATING THE SIZE OF THE WINDOW 
window.configure(background='gray84')      #GIVING THE WINDOW A SPECIFIC BACKGROUND COLOUR 

mainloop()
