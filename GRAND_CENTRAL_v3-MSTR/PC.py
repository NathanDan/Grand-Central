#Nathan Jones
#GRAND CENTRAL PC 
#2019

from tkinter import messagebox, Label, Button, FALSE, Tk, Entry    #ALLOWING FOR TKINTER TO BE ACCESSED/UTILISED FOR THE PROGRAM TO USE ALL OF ITS FUNCTIONS AND GIVING THE PROGRAM A GUI
from tkinter import *                                              #ALLOWING FOR ALL OF TKINTER'S MODULES TO BE IMPORTED 
from datetime import datetime                                      #ALLOWING THE DATE AND TIME TO BE DISPLAYED 

import time        #THIS ALLOWS FOR THE PROGRAM TO USE THE SLEEP FUNCTION WITHIN THE PROGRAM
import sys         #ALLOWS ACCESS TO THE SYSTEM FROM WITHIN PYTHON 
import os.path     #ALLOWS THE PROGRAM TO OPEN OTHER SPECIFIC APPLICATIONS, IN THIS CASE THE GC PROGRAMS 
import os          #ALLOWS FOR CONTROL OF THE MACHINE AND ITS OS INCLUDING THE LIKES OF SAVING, OPENING/CLOSING FILES, ETC. 
import string      #ALLOWS FOR DATA/ENTRIES TO BE RECOREDAS STRINGS AND NOT INDIVIDUAL CHARACTERS 
import getpass     #WHEN CHECKING THE PASSWORD/USERNAME ALLOWS FOR A FUNCTION TO DO NOTHING AND PASS IT ON
import random      #THIS IMPORT ALLOWS FOR WORDS TO BE RANDOMLY SELECTED 
import statistics  #ALLOWS ACCESS TO THE STATISTICS LIBARY FOR THE DATA COLLECTION AND PROCESSING
import itertools   #ALLOWS ACCESS TO ACCESS TO THE ITERATORS LIBARY FOR EFFICENT LOOPING 
import datetime    #THIS ALLOWS FOR THE CURRENT TIME TO BE IMPORTED AND DISPLAYED FOR THE USER TO SEE 
 
window = Tk()      #DEFINING WHAT THE FIRST TKINTER WINDOW WILL BE DEFINED AS

window.resizable (0,0)                            #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
window.resizable (width=FALSE, height=FALSE)      #THE USER CANNOT CHANGE THE SIZE OF THE MENU
window.title ("Grand Central PIN")                #GIVING THE LOGIN WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
window.geometry("300x180")                        #CONFIGURING THE FIXED SIZE OF THE WINDOW WHICH WILL ALWAYS BE THIS SIZE            
window.configure(background='lightgrey')          #CONFIGURING THE BACKGROUND OF THE WINDOW TO BE LIGHT GREY 

def PIN4():
    Window4 = Tk()                                      #DEFINING WHAT THE PIN CARCK WINDOW WILL BE DEFINED AS

    scrollbarY = Scrollbar(Window4)                     #DEFING THE SCROLLBAR THAT WILL ASSIGNED TO THE WINDOW 
    scrollbarY.pack(side=RIGHT, fill=Y)                 #TELLING THE PROGRAM WHERE TO PLACE THE SCROLLBAR

    Window4.resizable (0,0)                             #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
    Window4.resizable (width=FALSE, height=FALSE)       #THE USER CANNOT CHANGE THE SIZE OF THE MENU
    Window4.title ("4 DIGIT CODE CRACK")                #GIVING THE LOGIN WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
    Window4.geometry("300x300")                         #CONFIGURING THE FIXED SIZE OF THE WINDOW WHICH WILL ALWAYS BE THIS SIZE            
    Window4.configure(background='white')               #CONFIGURING THE BACKGROUND OF THE WINDOW TO BE WHITE

    def CRACK4():

        n = list(DIGITS4.get())                                                                        #GATHERING THE 4 NUMBERS THAT THE USER HAS INPUTTED AND IS THEN CREATING A VARIABLE 
        a = [''.join(i) for i in itertools.permutations(n, 4)]                                         #TAKES THE PREVIOUS VARIABLE AND RE-ARRANGES THE NUMBERS IN ALL POSSIBLE COMINATIONS 
        L = Label(Window4, text="HERE ARE THE POSSIBLE COMBINATIONS:", fg="red", background="white")   #CREATING A LABEL THAT WILL ACT AS A HEADER FOR THE COMBINATIONS
        l = Text (Window4, height=10, width=20, background="light grey", wrap=WORD, yscrollcommand=scrollbarY.set) #CREATING A BOX THAT WILL DISPLAY ALL POSSIBLE COMBINATIONS 
        l.insert(END, list(a))                                                                         #INSERTING THE VALUES INTO THE BOX THAT WILL SHOW ALL THE POSSIBLE COMBINATIONS
        scrollbarY.config(command=l.yview)                                                             #TELLING THE SCROLLBAR WHAT IT WILL DO                                                             
        L.pack()                                                                                       #DISPLAYING THE LABEL THAT WILL SHOW THE HEADER
        l.pack()                                                                                       #DISPLAYING THE BOX THAT WILL SHOW ALL THE POSSIBLE COMBINATIONS 
        
    digits4 = Label (Window4, text="ENTER THE 4 DIGITS:", background="white")       #CREATING A LABEL THAT WILL ACT AS A HEADER FOR THE ENTRY BOX OF THE DIGITS 
    DIGITS4 = Entry (Window4, background="light grey")                              #CREATING THE ACTUAL ENTRY BOX WHERE THE USER WILL INPUT THEIR DIGITS     

    CRACK4 = Button (Window4, text="      CRACK      ", fg="red", command=CRACK4)   #CREATING A BUTTON FOR THE ENTRY BOX SO THAT THE DIGITS WILL BE SENT OFF AND PUT INTO THE PROGRAM      
    label4 = Label(Window4, text=" ", background="white")                           #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE BEFORE THE COMBINATIONS ARE DISPLAYED 

    digits4.pack()  #DISPLAYING THE ACTUAL HEADER LABEL
    DIGITS4.pack()  #DISPLAYING THE ACTUAL ENTRY BOX
    CRACK4.pack()   #DISPLAYING THE ACTUAL BUTTON FOR THE CRACK TO BEGIN 
    label4.pack()   #DISPLAYING THE ONE LINE SPACE 
    
    
def PIN5():

    Window5 = Tk()                                      #DEFINING WHAT THE PIN CARCK WINDOW WILL BE DEFINED AS

    scrollbarY = Scrollbar(Window5)                     #DEFING THE SCROLLBAR THAT WILL ASSIGNED TO THE WINDOW 
    scrollbarY.pack(side=RIGHT, fill=Y)                 #TELLING THE PROGRAM WHERE TO PLACE THE SCROLLBAR
    
    Window5.resizable (0,0)                             #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
    Window5.resizable (width=FALSE, height=FALSE)       #THE USER CANNOT CHANGE THE SIZE OF THE MENU
    Window5.title ("5 DIGIT CODE CRACK")                #GIVING THE LOGIN WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
    Window5.geometry("300x300")                         #CONFIGURING THE FIXED SIZE OF THE WINDOW WHICH WILL ALWAYS BE THIS SIZE            
    Window5.configure(background='white')               #CONFIGURING THE BACKGROUND OF THE WINDOW TO BE WHITE

    def CRACK5():

        n = list(DIGITS5.get())                                                                        #GATHERING THE 5 NUMBERS THAT THE USER HAS INPUTTED AND IS THEN CREATING A VARIABLE                                       
        a = [''.join(i) for i in itertools.permutations(n, 5)]                                         #TAKES THE PREVIOUS VARIABLE AND RE-ARRANGES THE NUMBERS IN ALL POSSIBLE COMINATIONS
        L = Label(Window5, text="HERE ARE THE POSSIBLE COMBINATIONS:", fg="red", background="white")   #CREATING A LABEL THAT WILL ACT AS A HEADER FOR THE COMBINATIONS 
        l = Text (Window5, height=10, width=20, background="light grey", wrap=WORD, yscrollcommand=scrollbarY.set) #CREATING A BOX THAT WILL DISPLAY ALL POSSIBLE COMBINATIONS 
        l.insert(END, list(a))                                                                         #INSERTING THE VALUES INTO THE BOX THAT WILL SHOW ALL THE POSSIBLE COMBINATIONS
        scrollbarY.config(command=l.yview)                                                             #TELLING THE SCROLLBAR WHAT IT WILL DO                                                          
        L.pack()                                                                                       #DISPLAYING THE LABEL THAT WILL SHOW THE HEADER
        l.pack()                                                                                       #DISPLAYING THE BOX THAT WILL SHOW ALL THE POSSIBLE COMBINATIONS 
        
    digits5 = Label (Window5, text="ENTER THE 5 DIGITS:", background="white")       #CREATING A LABEL THAT WILL ACT AS A HEADER FOR THE ENTRY BOX OF THE DIGITS   
    DIGITS5 = Entry (Window5, background="light grey")                              #CREATING THE ACTUAL ENTRY BOX WHERE THE USER WILL INPUT THEIR DIGITS    

    CRACK5 = Button (Window5, text="      CRACK      ", fg="red", command=CRACK5)   #CREATING A BUTTON FOR THE ENTRY BOX SO THAT THE DIGITS WILL BE SENT OFF AND PUT INTO THE PROGRAM   
    label5 = Label(Window5, text=" ", background="white")                           #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE BEFORE THE COMBINATIONS ARE DISPLAYED

    digits5.pack()  #DISPLAYING THE ACTUAL HEADER LABEL
    DIGITS5.pack()  #DISPLAYING THE ACTUAL ENTRY BOX
    CRACK5.pack()   #DISPLAYING THE ACTUAL BUTTON FOR THE CRACK TO BEGIN
    label5.pack()   #DISPLAYING THE ONE LINE SPACE
    
    
def PIN6():

    Window6 = Tk()                                      #DEFINING WHAT THE PIN CARCK WINDOW WILL BE DEFINED AS

    scrollbarY = Scrollbar(Window6)                     #DEFING THE SCROLLBAR THAT WILL ASSIGNED TO THE WINDOW 
    scrollbarY.pack(side=RIGHT, fill=Y)                 #TELLING THE PROGRAM WHERE TO PLACE THE SCROLLBAR

    Window6.resizable (0,0)                             #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
    Window6.resizable (width=FALSE, height=FALSE)       #THE USER CANNOT CHANGE THE SIZE OF THE MENU
    Window6.title ("6 DIGIT CODE CRACK")                #GIVING THE LOGIN WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
    Window6.geometry("300x300")                         #CONFIGURING THE FIXED SIZE OF THE WINDOW WHICH WILL ALWAYS BE THIS SIZE            
    Window6.configure(background='white')               #CONFIGURING THE BACKGROUND OF THE WINDOW TO BE WHITE

    def CRACK6():

        n = list(DIGITS6.get())                                                                        #GATHERING THE 6 NUMBERS THAT THE USER HAS INPUTTED AND IS THEN CREATING A VARIABLE
        a = [''.join(i) for i in itertools.permutations(n, 6)]                                         #TAKES THE PREVIOUS VARIABLE AND RE-ARRANGES THE NUMBERS IN ALL POSSIBLE COMINATIONS
        L = Label(Window6, text="HERE ARE THE POSSIBLE COMBINATIONS:", fg="red", background="white")   #CREATING A LABEL THAT WILL ACT AS A HEADER FOR THE COMBINATIONS
        l = Text (Window6, height=10, width=20, background="light grey", wrap=WORD, yscrollcommand=scrollbarY.set) #CREATING A BOX THAT WILL DISPLAY ALL POSSIBLE COMBINATIONS 
        l.insert(END, list(a))                                                                         #INSERTING THE VALUES INTO THE BOX THAT WILL SHOW ALL THE POSSIBLE COMBINATIONS
        scrollbarY.config(command=l.yview)                                                             #TELLING THE SCROLLBAR WHAT IT WILL DO  
        L.pack()                                                                                       #DISPLAYING THE LABEL THAT WILL SHOW THE HEADER
        l.pack()                                                                                       #DISPLAYING THE BOX THAT WILL SHOW ALL THE POSSIBLE COMBINATIONS 
        
    digits6 = Label (Window6, text="ENTER THE 6 DIGITS:", background="white")       #CREATING A LABEL THAT WILL ACT AS A HEADER FOR THE ENTRY BOX OF THE DIGITS
    DIGITS6 = Entry (Window6, background="light grey")                              #CREATING THE ACTUAL ENTRY BOX WHERE THE USER WILL INPUT THEIR DIGITS

    CRACK6 = Button (Window6, text="      CRACK      ", fg="red", command=CRACK6)   #CREATING A BUTTON FOR THE ENTRY BOX SO THAT THE DIGITS WILL BE SENT OFF AND PUT INTO THE PROGRAM 
    label6 = Label(Window6, text=" ", background="white")                           #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE BEFORE THE COMBINATIONS ARE DISPLAYED

    digits6.pack()  #DISPLAYING THE ACTUAL HEADER LABEL
    DIGITS6.pack()  #DISPLAYING THE ACTUAL ENTRY BOX
    CRACK6.pack()   #DISPLAYING THE ACTUAL BUTTON FOR THE CRACK TO BEGIN
    label6.pack()   #DISPLAYING THE ONE LINE SPACE

def PIN7():

    Window7 = Tk()                                      #DEFINING WHAT THE PIN CARCK WINDOW WILL BE DEFINED AS

    scrollbarY = Scrollbar(Window7)                     #DEFING THE SCROLLBAR THAT WILL ASSIGNED TO THE WINDOW 
    scrollbarY.pack(side=RIGHT, fill=Y)                 #TELLING THE PROGRAM WHERE TO PLACE THE SCROLLBAR

    Window7.resizable (0,0)                             #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
    Window7.resizable (width=FALSE, height=FALSE)       #THE USER CANNOT CHANGE THE SIZE OF THE MENU
    Window7.title ("7 DIGIT CODE CRACK")                #GIVING THE LOGIN WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
    Window7.geometry("300x300")                         #CONFIGURING THE FIXED SIZE OF THE WINDOW WHICH WILL ALWAYS BE THIS SIZE            
    Window7.configure(background='white')               #CONFIGURING THE BACKGROUND OF THE WINDOW TO BE WHITE

    def CRACK7():

        n = list(DIGITS7.get())                                                                        #GATHERING THE 7 NUMBERS THAT THE USER HAS INPUTTED AND IS THEN CREATING A VARIABLE
        a = [''.join(i) for i in itertools.permutations(n, 7)]                                         #TAKES THE PREVIOUS VARIABLE AND RE-ARRANGES THE NUMBERS IN ALL POSSIBLE COMINATIONS
        L = Label(Window7, text="HERE ARE THE POSSIBLE COMBINATIONS:", fg="red", background="white")   #CREATING A LABEL THAT WILL ACT AS A HEADER FOR THE COMBINATIONS
        l = Text (Window7, height=10, width=20, background="light grey", wrap=WORD, yscrollcommand=scrollbarY.set) #CREATING A BOX THAT WILL DISPLAY ALL POSSIBLE COMBINATIONS 
        l.insert(END, list(a))                                                                         #INSERTING THE VALUES INTO THE BOX THAT WILL SHOW ALL THE POSSIBLE COMBINATIONS
        scrollbarY.config(command=l.yview)                                                             #TELLING THE SCROLLBAR WHAT IT WILL DO  
        L.pack()                                                                                       #DISPLAYING THE LABEL THAT WILL SHOW THE HEADER
        l.pack()                                                                                       #DISPLAYING THE BOX THAT WILL SHOW ALL THE POSSIBLE COMBINATIONS
        
    digits7 = Label (Window7, text="ENTER THE 7 DIGITS:", background="white")       #CREATING A LABEL THAT WILL ACT AS A HEADER FOR THE ENTRY BOX OF THE DIGITS 
    DIGITS7 = Entry (Window7, background="light grey")                              #CREATING THE ACTUAL ENTRY BOX WHERE THE USER WILL INPUT THEIR DIGITS    

    CRACK7 = Button (Window7, text="      CRACK      ", fg="red", command=CRACK7)   #CREATING A BUTTON FOR THE ENTRY BOX SO THAT THE DIGITS WILL BE SENT OFF AND PUT INTO THE PROGRAM    
    label7 = Label(Window7, text=" ", background="white")                           #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE BEFORE THE COMBINATIONS ARE DISPLAYED

    digits7.pack()  #DISPLAYING THE ACTUAL HEADER LABEL
    DIGITS7.pack()  #DISPLAYING THE ACTUAL ENTRY BOX
    CRACK7.pack()   #DISPLAYING THE ACTUAL BUTTON FOR THE CRACK TO BEGIN
    label7.pack()   #DISPLAYING THE ONE LINE SPACE
    
    
def PIN8():

    Window8 = Tk()                                      #DEFINING WHAT THE PIN CARCK WINDOW WILL BE DEFINED AS

    scrollbarY = Scrollbar(Window8)                     #DEFING THE SCROLLBAR THAT WILL ASSIGNED TO THE WINDOW 
    scrollbarY.pack(side=RIGHT, fill=Y)                 #TELLING THE PROGRAM WHERE TO PLACE THE SCROLLBAR

    Window8.resizable (0,0)                             #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
    Window8.resizable (width=FALSE, height=FALSE)       #THE USER CANNOT CHANGE THE SIZE OF THE MENU
    Window8.title ("8 DIGIT CODE CRACK")                #GIVING THE LOGIN WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
    Window8.geometry("300x300")                         #CONFIGURING THE FIXED SIZE OF THE WINDOW WHICH WILL ALWAYS BE THIS SIZE            
    Window8.configure(background='white')               #CONFIGURING THE BACKGROUND OF THE WINDOW TO BE WHITE

    def CRACK8():

        n = list(DIGITS8.get())                                                                        #GATHERING THE 8 NUMBERS THAT THE USER HAS INPUTTED AND IS THEN CREATING A VARIABLE
        a = [''.join(i) for i in itertools.permutations(n, 8)]                                         #TAKES THE PREVIOUS VARIABLE AND RE-ARRANGES THE NUMBERS IN ALL POSSIBLE COMINATIONS
        L = Label(Window8, text="HERE ARE THE POSSIBLE COMBINATIONS:", fg="red", background="white")   #CREATING A LABEL THAT WILL ACT AS A HEADER FOR THE COMBINATIONS
        l = Text (Window8, height=10, width=20, background="light grey", wrap=WORD, yscrollcommand=scrollbarY.set) #CREATING A BOX THAT WILL DISPLAY ALL POSSIBLE COMBINATIONS 
        l.insert(END, list(a))                                                                         #INSERTING THE VALUES INTO THE BOX THAT WILL SHOW ALL THE POSSIBLE COMBINATIONS
        scrollbarY.config(command=l.yview)                                                             #TELLING THE SCROLLBAR WHAT IT WILL DO  
        L.pack()                                                                                       #DISPLAYING THE LABEL THAT WILL SHOW THE HEADER
        l.pack()                                                                                       #DISPLAYING THE BOX THAT WILL SHOW ALL THE POSSIBLE COMBINATIONS
        
    digits8 = Label (Window8, text="ENTER THE 8 DIGITS:", background="white")       #CREATING A LABEL THAT WILL ACT AS A HEADER FOR THE ENTRY BOX OF THE DIGITS 
    DIGITS8 = Entry (Window8, background="light grey")                              #CREATING THE ACTUAL ENTRY BOX WHERE THE USER WILL INPUT THEIR DIGITS 

    CRACK8 = Button (Window8, text="      CRACK      ", fg="red", command=CRACK8)   #CREATING A BUTTON FOR THE ENTRY BOX SO THAT THE DIGITS WILL BE SENT OFF AND PUT INTO THE PROGRAM    
    label8 = Label(Window8, text=" ", background="white")                           #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE BEFORE THE COMBINATIONS ARE DISPLAYED

    digits8.pack()  #DISPLAYING THE ACTUAL HEADER LABEL
    DIGITS8.pack()  #DISPLAYING THE ACTUAL ENTRY BOX 
    CRACK8.pack()   #DISPLAYING THE ACTUAL BUTTON FOR THE CRACK TO BEGIN
    label8.pack()   #DISPLAYING THE ONE LINE SPACE


L = Label (window, text=" ", background="lightgrey")                     #CREATING A LABEL THAT WILL ACT LIKE A ONE LINE SPACE ABOVE THE BUTTONS                           
PIN4 = Button (text="      4 DIGIT PIN      ", fg="blue", command=PIN4)  #CREATING THE BUTTON FOR THE 4 DIGIT PIN CRACK
PIN5 = Button (text="      5 DIGIT PIN      ", fg="blue", command=PIN5)  #CREATING THE BUTTON FOR THE 5 DIGIT PIN CRACK
PIN6 = Button (text="      6 DIGIT PIN      ", fg="blue", command=PIN6)  #CREATING THE BUTTON FOR THE 6 DIGIT PIN CRACK
PIN7 = Button (text="      7 DIGIT PIN      ", fg="blue", command=PIN7)  #CREATING THE BUTTON FOR THE 7 DIGIT PIN CRACK
PIN8 = Button (text="      8 DIGIT PIN      ", fg="blue", command=PIN8)  #CREATING THE BUTTON FOR THE 8 DIGIT PIN CRACK

L.pack()     #DISPLAYING THE ONE LINE SPACE  
PIN4.pack()  #DISPLAYING THE ACTUAL 4 DIGIT BUTTON
PIN5.pack()  #DISPLAYING THE ACTUAL 5 DIGIT BUTTON
PIN6.pack()  #DISPLAYING THE ACTUAL 6 DIGIT BUTTON
PIN7.pack()  #DISPLAYING THE ACTUAL 7 DIGIT BUTTON
PIN8.pack()  #DISPLAYING THE ACTUAL 8 DIGIT BUTTON

window.mainloop()
