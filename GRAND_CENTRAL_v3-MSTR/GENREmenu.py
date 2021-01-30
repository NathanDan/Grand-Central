#TKinter GC GENRES - MSTR
#2019
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
import getpass     #WHEN CHECKING THE PASSWORD/USERNAME ALLOWS FOR A FUNCTION TO DO NOTHING AND PASS IT ON
import random      #THIS IMPORT ALLOWS FOR WORDS TO BE RANDOMLY SELECTED 
import statistics  #ALLOWS ACCESS TO THE STATISTICS LIBARY FOR THE DATA COLLECTION AND PROCESSING
import itertools   #ALLOWS ACCESS TO ACCESS TO THE ITERATORS LIBARY FOR EFFICENT LOOPING 
import datetime    #THIS ALLOWS FOR THE CURRENT TIME TO BE IMPORTED AND DISPLAYED FOR THE USER TO SEE 

window = Tk()                                                                 #DEFINING WHAT THE FIRST TKINTER WINDOW WILL BE DEFINED AS

l2 = Label(window, text=" ",bg="gray84")                                      #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE
l2.pack()                                                                     #DISPLAY THE LABEL WITHIN THE MENU WINDOW 

l0 = Label(window, text="GENRE MENU",font='Helvetica 16 bold' ,bg="gray84") #GIVING THE WINDOW A TITLE SO THE USER/CLIENT KNOWS WHAT MENU THEY ARE ON 
l0.pack()                                                                     #DISPLAYING THE TITLE FOR THE USER/CLIENT TO SEE

l5 = Label(window, text=" ",bg="gray84")                                      #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE
l5.pack()                                                                     #DISPLAY THE LABEL WITHIN THE MENU WINDOW   
 
#CREATING THE BUTTONS FOR EACH ARTIST, ONCE A BUTTON IS PRESSED IT WILL TAKE THEM TO ANOTHER GUI WHICH WILL DISPLAY ALL THE ALBUMS OF THAT ARTIST
def option1():

    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\GENRES\\ALTERNATIVErockMENU.py") #TAKING THE USER/CLIENT TO THEIR ALBUM THEY HAVE SELECTED
    window.destroy()                                                                                                                       #CLOSING THE WINDOW AUTOMATICALLY AS THEY LEAVE THE MENU

b1 = Button(window, text="  ALTERNATIVE ROCK ", command=option1)         #CREATING THE BUTTON AND ADDING THE ARTIST AND ALBUM NAME
b1.pack()                                                                                 #DISPLAYING THE BUTTON ON THE MENU 


def option2():

    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\GENRES\\INDIEmenu.py") #TAKING THE USER/CLIENT TO THEIR ALBUM THEY HAVE SELECTED
    window.destroy()                                                                                                                             #CLOSING THE WINDOW AUTOMATICALLY AS THEY LEAVE THE MENU

b1 = Button(window, text="               INDIE              ", command=option2)     #CREATING THE BUTTON AND ADDING THE ARTIST AND ALBUM NAME
b1.pack()                                                                                 #DISPLAYING THE BUTTON ON THE MENU       

def option3():

    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\GENRES\\RAPmenu.py") #TAKING THE USER TO THEIR ARTIST THEY HAVE SELECTED
    window.destroy()                                                                                                                             #CLOSING THE WINDOW AUTOMATICALLY AS THEY LEAVE THE MENU

b1 = Button(window, text="            HIP HOP           ", command=option3)   #CREATING THE BUTTON AND ADDING THE ARTIST AND ALBUM NAME
b1.pack()                                                                                #DISPLAYING THE BUTTON ON THE MENU 

def option4():

    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\GENRES\\REGGAEmenu.py") #TAKING THE USER TO THEIR ARTIST THEY HAVE SELECTED
    window.destroy()                                                                                                                              #CLOSING THE WINDOW AUTOMATICALLY AS THEY LEAVE THE MENU

b1 = Button(window, text="           REGGAE             ", command=option4)                  #CREATING THE BUTTON AND ADDING THE ARTIST AND ALBUM NAME
b1.pack()                                                                                #DISPLAYING THE BUTTON ON THE MENU

def option5():

    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\GENRES\\PUNKmenu.py") #TAKING THE USER/CLIENT TO THEIR ALBUM THEY HAVE SELECTED
    window.destroy()                                                                                                                       #CLOSING THE WINDOW AUTOMATICALLY AS THEY LEAVE THE MENU

b1 = Button(window, text="        PUNK ROCK        ", command=option5)           #CREATING THE BUTTON AND ADDING THE ARTIST AND ALBUM NAME
b1.pack()                                                                                #DISPLAYING THE BUTTON ON THE MENU


l5 = Label(window, text=" ",bg="gray84")                                                 #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE
l5.pack()                                                                                #DISPLAY THE LABEL WITHIN THE MENU WINDOW

def option14():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\MUSICmenu.py") #TAKING THE USER BACK TO THE MUSIC MENU
    window.destroy()                                                                                                                     #CLOSING THE WINDOW AUTOMATICALLY AS THEY LEAVE THE MENU  

b15 = Button(window, text="BACK",command=option14) #CREATING THE BUTTON THAT WILL BE DISPLAYED
b15.pack()                                         #DISPLAYING THE BUTTON ON THE MENU 

window.resizable(0,0)
window.resizable(width=FALSE, height=FALSE)        #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW 
window.title("GENRE MAIN MENU - MSTR")           #GIVING THE WINDOW A TITLE THAT WILL BE AT THE VERY TOP ALONGSIDE THE '- O X' BUTTONS 
window.geometry("400x350")                         #GENERATING THE SIZE OF THE WINDOW 
window.configure(background='gray84')              #GIVING THE WINDOW A SPECIFIC BACKGROUND COLOUR 

mainloop()
