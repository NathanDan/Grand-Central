#TKinter GC Utilities Main Menu
#2018
#Nathan Jones

from tkinter import messagebox, Label, Button, FALSE, Tk, Entry    #ALLOWING FOR TKINTER TO BE ACCESSED/UTILISED FOR THE PROGRAM TO USE ALL OF ITS FUNCTIONS AND GIVING THE PROGRAM A GUI                                           
from tkinter import *                                              #ALLOWING FOR ALL OF TKINTER'S MODULES TO BE IMPORTED 
from PIL import Image, ImageTk                                     #ALLOWING FOR IMAGES TO ADDED IN THE GUI FOR THE LIKES OF THE BACKGROUNDS AND OTHER IMAGES 

import time        #THIS ALLOWS FOR THE PROGRAM TO USE THE SLEEP FUNCTION WITHIN THE PROGRAM
import sys         #ALLOWS ACCESS TO THE SYSTEM FROM WITHIN PYTHON 
import os.path     #ALLOWS THE PROGRAM TO OPEN OTHER SPECIFIC APPLICATIONS, IN THIS CASE THE GC PROGRAMS 
import os          #ALLOWS FOR CONTROL OF THE MACHINE AND IS OS INCLUDING THE LIKES OF SAVING, OPENING/CLOSING FILES, ETC. 
import string      #ALLOWS FOR DATA/ENTRIES TO BE RECOREDAS STRINGS AND NOT INDIVIDUAL CHARACTERS 
import statistics  #ALLOWS ACCESS TO THE STATISTICS LIBARY FOR THE DATA COLLECTION AND PROCESSING
import itertools   #ALLOWS ACCESS TO ACCESS TO THE ITERATORS LIBARY FOR EFFICENT LOOPING 

window = Tk()      #DEFINING THE NAME OF THE WINDOW

l2 = Label(window, text="",bg="white") #CREATING A ONE LINE SPACE
l2.pack()                               #DISPLAYING THE LABEL

l0 = Label(window, text="UTILITIES",font='Helvetica 16 bold' ,bg="white") #GIVING THE WINDOW A TITLE SO THE USER KNOWS WHAT MENU THEY ARE ON 
l0.pack()                                                                        #DISPLAYING THE TITLE FOR THE USER TO SEE

l5 = Label(window, text="",bg="white") #CREATING A ONE LINE SPACE
l5.pack()                               #DISPLAYING THE LABEL

#CREATING VARIOUS BUTTONS FOR THE VARIOUS PROGRAMS THAT ARE WITHIN GRAND CENTRAL - WILL VARY DEPENDING ON THE USER 
def option1():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\ALBUMmenu.py")   #TAKING THE USER TO THE ALBUM MENU
    window.destroy()                                                                     #CLOSING THE WINDOW AUTOMATICALLY AS THEY LEAVE THE MENU

b1 = Button(window, text="                CALCULATOR                 ", command=option1) #CREATING THE BUTTON THAT WILL DISPLAY THE ALBUMS AND WILL TAKE THE USER THERE
b1.pack()                                                                                #DISPLAYING THE BUTTON IN THE WINDOW

def option2():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\RESOURCE MANAGEMENT.py") #TAKING THE USER TO THE ARTISTS MENU
    window.destroy()                                                      #CLOSING THE WINDOW AUTOMATICALLY AS THEY LEAVE THE MENU

b2 = Button(window, text="    GRAND CENTRAL MONITOR   ", command=option2) #CREATING THE BUTTON THAT WILL DISPLAY THE ARTISTS AND WILL TAKE THE USER THERE
b2.pack()                                                                 #DISPLAYING THE BUTTON IN THE WINDOW

l0 = Label(window, text="",bg="white")                                    #CREATING A ONE LINE SPACE
l0.pack()                                                                 #DISPLAYING THE LABEL

def option14():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\TK_MSTR_v3.py")  #TAKING THE USER BACK TO THE MAIN MENU
    window.destroy()                                          #CLOSING THE WINDOW AUTOMATICALLY AS THEY LEAVE THE MENU

b15 = Button(window, text="MAIN MENU",command=option14)       #CREATING THE BUTTON THAT WILL TAKE THE USER BACK TO THE MAIN MENU
b15.pack()                                                    #DISPLAYING THE MAIN MENU BUTTON 

window.resizable(0,0)                        #THE WINDOW WILL NOT ENTER FULLSCREEN MODE 
window.resizable(width=FALSE, height=FALSE)  #THE USER CANNOT CHANGE THE SIZE OF THE MENU
window.title("UTILITIES - MSTR")       #GIVING THE MENU WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
window.geometry("350x250")                   #CONFIGURING THE FIXED SIZE OF THE MENU WINDOW WHICH WILL ALWAYS BE THIS SIZE
window.configure(background='white')        #CONFIGURING THE BACKGROUND OF THE MENU WINDOW TO BE GREYISH COLOUR 

mainloop()
