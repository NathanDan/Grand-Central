#TKinter GC Main Menu - MSTR
#2018/2019
#Nathan Jones

from tkinter import messagebox, Label, Button, FALSE, Tk, Entry    #ALLOWING FOR TKINTER TO BE ACCESSED/UTILISED FOR THE PROGRAM TO USE ALL OF ITS FUNCTIONS AND GIVING THE PROGRAM A GUI
from tkinter import *                                              #ALLOWING FOR ALL OF TKINTER'S MODULES TO BE IMPORTED
from PIL import Image, ImageTk                                     #ALLOWING FOR IMAGES TO ADDED IN THE GUI FOR THE LIKES OF THE BACKGROUNDS AND OTHER IMAGES
from datetime import datetime                                      #ALLOWING THE DATE AND TIME TO BE DISPLAYED
from email.mime.text import MIMEText                               #ALLOWS FOR GRAND CENTRAL TO GENERATE TEH TEXT TAHT WILL BE DISPLAYED IN THE BODY OF TEH EMAIL
from email.mime.multipart import MIMEMultipart                     #ALLOWS FOR GRAND CENTRAL TO ACCESS THE EMAIL SERVERS TO CREATE THE EMAILS FOR THE FAILED LOGINS
from email.mime.base import MIMEBase                               #ALLOWS FOR GRAND CENTRAL TO CREATE THE EMAILS MAIN BODY OF TEXT FOR THE FAILED LOGINS
from email import encoders                                         #ALLOWS FOR GRAND CENTRAL TO ENCODE THE EMAILS FOR THE FAILED LOGINS AND TEHN SEND THEM DIRECTLY
from uuid import getnode as get_mac                                #ALLOWS FOR TO ACCESS THE MODULES THAT ALLOW DIRECT ACCESS TO THE MAC ADDRESS OF THE MACHINE

import time        #THIS ALLOWS FOR THE PROGRAM TO USE THE SLEEP FUNCTION WITHIN THE PROGRAM
import time as t   #THIS ALLOWS FOR THE PROGRAM TO USE THE SLEEP FUNCTION WITHIN THE PROGRAM BUT WILL NOT CONFLICT WITH THE OTHER SLEEP FUNCTIONS
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
import pyglet      #THIS IS THE MODULE THAT ALLOWS FOR THE SOUNDS/MUSIC/SONGS TO BE PLAYED


#GLOBAL VARIABLES - GREETINGS
GREETINGS=["Hey ","Hi ","How's it going ","Whats Up ","What's new ","What's going on ","How's everything ","How are things ","How's life ","How's your day ","How's your day going ","Long time no see ","It's been a while "] #THESE ARE THE TEXT GREETINGS THAT WILL BE RANDOMLY SELECTED
NAME1=("Nathan")                #NAME OF THE USER AND WILL BE ALOCATED TO THE TEXT GREETING
Greet=[1,2,3,4,5,6,7,8,9,10,11] #THIS IS THE LIST THAT ALLOWS THE RANDOM FUNCTION TO RANDOMLY SELECT ONE OF THE NUMBERS WHICH WILL LINK WITH ONE OF THE GREETINGS
LogOut=[1,2]                    #THIS IS THE LIST THAT ALLOWS THE RANDOM FUNCTION TO RANDOMLY SELECT ONE OF THE NUMBERS WHICH WILL LINK WITH ONE OF THE GREETINGS

time = datetime.datetime.now()                       #ALLOWS GRAND CENTRAL TO GATHER THE CURRENT TIME
mac = get_mac()                                      #ALLOWS GRAND CENTRAL TO GATHER THE CURRENT MAC ADDRESS OF THE MACHINE
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #ALLOWS GRAND CENTRAL TO GATHER THE CURRENT IP ADDRESS
s.connect(("8.8.8.8", 80))                           #CONNECTS TO THE IP ADDRESS AND ESTABLISHES THE CONNECTION

SEL=Greet[random.randint(0,10)] #RANDOMLY SELECTING ONE OF THE 11 DIFFERNT WELCOME GREETINGS TAHT ARE UNIQUE TO EACH USER AND WILL PLAY JUST AFTER THE LOGIN SOUND

if SEL ==1:
    song1 = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\GCMSTR\\HowAreThings.mp3')      #THE PATH OF THE SELECTED GREETING
    song1.play()                                                                                                                                       #PLAYING THE MP3 FILE
if SEL ==2:
    song2 = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\GCMSTR\\Hey.mp3')               #THE PATH OF THE SELECTED GREETING
    song2.play()                                                                                                                                       #PLAYING THE MP3 FILE
if SEL ==3:
    song3 = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\GCMSTR\\HowIsYourDay.mp3')      #THE PATH OF THE SELECTED GREETING
    song3.play()                                                                                                                                       #PLAYING THE MP3 FILE
if SEL ==4:
    song4 = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\GCMSTR\\HowIsYourDayGoing.mp3') #THE PATH OF THE SELECTED GREETING
    song4.play()                                                                                                                                       #PLAYING THE MP3 FILE
if SEL ==5:
    song5 = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\GCMSTR\\HowsEverything.mp3')    #THE PATH OF THE SELECTED GREETING
    song5.play()                                                                                                                                       #PLAYING THE MP3 FILE
if SEL ==6:
    song6 = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\GCMSTR\\HowsItGoing.mp3')       #THE PATH OF THE SELECTED GREETING
    song6.play()                                                                                                                                       #PLAYING THE MP3 FILE
if SEL ==7:
    song7 = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\GCMSTR\\ItsBeenAWhile.mp3')     #THE PATH OF THE SELECTED GREETING
    song7.play()                                                                                                                                       #PLAYING THE MP3 FILE
if SEL ==8:
    song8 = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\GCMSTR\\LongTimeNoSee.mp3')     #THE PATH OF THE SELECTED GREETING
    song8.play()                                                                                                                                       #PLAYING THE MP3 FILE
if SEL ==9:
    song9 = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\GCMSTR\\WelcomeBack.mp3')       #THE PATH OF THE SELECTED GREETING
    song9.play()                                                                                                                                       #PLAYING THE MP3 FILE
if SEL ==10:
    song10 = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\GCMSTR\\WhatsGoingOn.mp3')     #THE PATH OF THE SELECTED GREETING
    song10.play()                                                                                                                                      #PLAYING THE MP3 FILE
if SEL ==11:
    song11 = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\GCMSTR\\WhatsNew.mp3')         #THE PATH OF THE SELECTED GREETING
    song11.play()                                                                                                                                      #PLAYING THE MP3 FILE

window = Tk()        #DEFINING WHAT THE FIRST TKINTER WINDOW WILL BE DEFINED AS
Window = Toplevel()  #DEFINING WHAT THE SECOND TKINTER WINDOW WILL BE DEFINED AS, BY USING TK'S TOPLEVEL FUNCTION IT ALLOWS FOR THE BACKGROUND TO DISPLAY AN IMAGE MAKING IT A DESKTOP

#DISPLAYING GENERAL INFORMATION ABOUT THE SYSTEM AS WELL AS THE TIME AND GREETINGS
l2 = Label(window, text="",bg="lightgrey")                                                    #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE
l2.pack()                                                                                     #DISPLAY THE LABEL WITHIN THE MENU WINDOW

l3 = Label(window, text="SYSTEM IP ADDRESS: "+str(s.getsockname()[0]),bg="lightgrey")         #CREATING A LABEL THAT WILL GATHER AND DISPLAY THE CURRENT IP ADDRESS
l3.pack()                                                                                     #DISPLAYING THE LABEL WITHIN THE MENU WINDOW

l4 = Label(window, text="SYSTEM TIME: "+str(time.strftime("%Y-%m-%d %H:%M")),bg="lightgrey")  #CREATING A LABEL THAT WILL GATHER AND DISPLAY THE CURRENT TIME IN THE FORMAT Y-M-D AND H:M
l4.pack()                                                                                     #DISPLAYING THE LABEL WITHIN THE MENU WINDOW

l5 = Label(window, text="SYSTEM MAC ADDRESS: "+str(mac),bg="lightgrey")                       #CREATING A LABEL THAT WILL GATHER AND DISPLAYB THE CURRENT MAC ADDRESS
l5.pack()                                                                                     #DISPLAYING THE LABEL WITHIN THE MENU WINDOW

l0 = Label(window, text="",bg="lightgrey")                                                    #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE
l0.pack()                                                                                     #DISPLAY THE LABEL WITHIN THE MENU WINDOW

l1 = Label(window, text=GREETINGS[random.randint(0,12)]+NAME1+str("!"),bg="lightgrey")        #CREATING A LABEL THAT WILL HAVE A PERSONALISED MESSAGE IN FOR THE USER, SELECTS OUT OF 13 PHRASES
l1.pack()                                                                                     #DISPLAY THE LABEL WITHIN THE MENU WINDOW

l5 = Label(window, text="",bg="lightgrey")                                                    #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE
l5.pack()                                                                                     #DISPLAY THE LABEL WITHIN THE MENU WINDOW

def donothing():
    pass

#CREATING VARIOUS BUTTONS FOR THE VARIOUS PROGRAMS THAT ARE WITHIN GRAND CENTRAL - WILL VARY DEPENDING ON THE USER (DUE TO MASTER EDITION IT WILL HAVE ALL PROGRAMS)

def option1():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\GFDM.py")      #THE PATH FOR THIS APPLICATION AND OPENS IT
    #window.destroy()                                                                                                                     #CLOSING THE MENU AFTER LAUNCHING THE SELECTED PROGRAM

b1 = Button(window, text="      Greenfly Data Model     ", command=option1)                                                              #THIS IS WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()                                                                                                                                #DISPLAYING THE BUTTON WITHIN THE MENU WINDOW

def option2():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\THG.py")       #THE PATH FOR THIS APPLICATION AND OPENS IT
    #window.destroy()                                                                                                                     #CLOSING THE MENU AFTER LAUNCHING THE SELECTED PROGRAM

b2 = Button(window, text="      Treasure Hunt Game     ", command=option2)                                                               #THIS IS WHAT WILL BE DISPLAYED IN THE BUTTON
b2.pack()                                                                                                                                #DISPLAY THE BUTTON WITHIN THE MENU WINDOW

def option4a():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\SQG.py")       #THE PATH FOR THIS APPLICATION AND OPENS IT
    #window.destroy()                                                                                                                     #CLOSING THE MENU AFTER LAUNCHING THE SELECTED PROGRAM

b4 = Button(window, text="        Science Questions       ", command=option4a)                                                           #THIS IS WHAT WILL BE DISPLAYED IN THE BUTTON
b4.pack()                                                                                                                                #DISPLAYING THE BUTTON WITHIN THE MENU WINDOW

def option4b():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\EQG.py")       #THE PATH FOR THIS APPLICATION AND OPENS IT
    #window.destroy()                                                                                                                     #CLOSING THE MENU AFTER LAUNCHING THE SELECTED PROGRAM

b4 = Button(window, text="        English Questions       ", command=option4b)                                                           #THIS IS WHAT WILL BE DISPLAYED IN THE BUTTON
b4.pack()                                                                                                                                #DISPLAYING THE BUTTON WITHIN THE MENU WINDOW

def option4c():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\MQG.py")       #THE PATH FOR THIS APPLICATION AND OPENS IT
    #window.destroy()                                                                                                                     #CLOSING THE MENU AFTER LAUNCHING THE SELECTED PROGRAM

b4 = Button(window, text="        Maths Questions         ", command=option4c)                                                            #THIS IS WHAT WILL BE DISPLAYED IN THE BUTTON
b4.pack()                                                                                                                                #DISPLAYING THE BUTTON WITHIN THE MENU WINDOW

def option5():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\TGG")          #THE PATH FOR THIS APPLICATION AND OPENS IT
    #window.destroy()                                                                                                                     #CLOSING THE MENU AFTER LAUNCHING THE SELECTED PROGRAM

b5 = Button(window, text="      Test Grade Generator    ", command=option5)                                                              #THIS IS WHAT WILL BE DISPLAYED IN THE BUTTON
b5.pack()                                                                                                                                #DISPLAYING THE BUTTON WITHIN THE MENU WINDOW

def option6():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\FM.py")        #THE PATH FOR THIS APPLICATION AND OPENS IT
    #window.destroy()                                                                                                                     #CLOSING THE MENU AFTER LAUNCHING THE SELECTED PROGRAM

b6 = Button(window, text="           Fruit Machine            ", command=option6)                                                        #THIS IS WHAT WILL BE DISPLAYED IN THE BUTTON
b6.pack()                                                                                                                                #DISPLAYING THE BUTTON WITHIN THE MENU WINDOW

def option7():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\CA.py")        #THE PATH FOR THIS APPLICATION AND OPENS IT
    #window.destroy()                                                                                                                     #CLOSING THE MENU AFTER LAUNCHING THE SELECTED PROGRAM

b7 = Button(window, text="        Card Authenticator     ", command=option7)                                                             #THIS IS WHAT WILL BE DISPLAYED IN THE BUTTON
b7.pack()                                                                                                                                #DISPLAYING THE BUTTON WITHIN THE MENU WINDOW

def option8():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\PC.py")        #THE PATH FOR THIS APPLICATION AND OPENS IT
    #window.destroy()                                                                                                                     #CLOSING THE MENU AFTER LAUNCHING THE SELECTED PROGRAM

b8 = Button(window, text="                PIN Crack             ", command=option8)                                                      #THIS IS WHAT WILL BE DISPLAYED IN THE BUTTON
b8.pack()                                                                                                                                #DISPLAYING THE BUTTON WITHIN THE MENU WINDOW

def option9():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\ES.py")        #THE PATH FOR THIS APPLICATION AND OPENS IT
    #window.destroy()                                                                                                                     #CLOSING THE MENU AFTER LAUNCHING THE SELECTED PROGRAM

b9 = Button(window, text="               Email Send            ", command=option9)                                                       #THIS IS WHAT WILL BE DISPLAYED IN THE BUTTON
b9.pack()                                                                                                                                #DISPLAYING THE BUTTON WITHIN THE MENU WINDOW

def option10():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\ER.py")        #THE PATH FOR THIS APPLICATION AND OPENS IT
    #window.destroy()                                                                                                                    #CLOSING THE MENU AFTER LAUNCHING THE SELECTED PROGRAM

b10 = Button(window, text="           Email Recieve           ", command=option10)                                                       #THIS IS WHAT WILL BE DISPLAYED IN THE BUTTON
b10.pack()                                                                                                                               #DISPLAYING THE BUTTON WITHIN THE MENU WINDOW


l6 = Label(window, text="",bg="lightgrey")                                                                                               #CREATING A LABEL THAT WILL DISPLAY NOTHING
l6.pack()                                                                                                                                #DISPLAYING THE LABEL WITHIN THE MENU WINDOW

def option11():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\CS.py")        #THE PATH FOR THIS APPLICATION AND OPENS IT

b11 = Button(window, text="   Chatroom Server Start  ", fg="red", command=option11)                                                      #THIS IS WHAT WILL BE DISPLAYED IN THE BUTTON
b11.pack()                                                                                                                               #DISPLAYING THE BUTTON WITHIN THE MENU WINDOW

def option12():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\CC.py")        #THE PATH FOR THIS APPLICATION AND OPENS IT

b12 = Button(window, text="Grand Central Messaging", fg="green", command=option12)                                                       #THIS IS WHAT WILL BE DISPLAYED IN THE BUTTON
b12.pack()                                                                                                                               #DISPLAYING THE BUTTON WITHIN THE MENU WINDOW


l7 = Label(window, text="",bg="lightgrey")                                                                                               #CREATING A LABEL THAT WILL DISPLAY NOTHING
l7.pack()                                                                                                                                #DISPLAYING THE LABEL WITHIN THE MENU WINDOW

def option16():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\MUSICmenu.py") #THE PATH FOR THIS APPLICATION AND OPENS IT

b15 = Button(window, text="                MUSIC               ", fg="red", command=option16)                                            #THIS IS WHAT WILL BE DISPLAYED IN THE BUTTON
b15.pack()                                                                                                                               #DISPLAYING THE BUTTON WITHIN THE MENU WINDOW

def optionU():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\Utilites.py") #THE PATH FOR THIS APPLICATION AND OPENS IT

b15 = Button(window, text="              UTILITIES             ",  command=optionU)                                                      #THIS IS WHAT WILL BE DISPLAYED IN THE BUTTON
b15.pack()                                                                                                                               #DISPLAYING THE BUTTON WITHIN THE MENU WINDOW


l8 = Label(window, text="",bg="lightgrey")                                                                                               #CREATING A LABEL THAT WILL DISPLAY NOTHING
l8.pack()                                                                                                                                #DISPLAYING THE LABEL WITHIN THE MENU WINDOW

def option15():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\PACGC.py")     #THE PATH FOR THIS APPLICATION AND OPENS IT

b15 = Button(window, text="                   PAC                 ", fg="purple", command=option15)                                      #THIS IS WHAT WILL BE DISPLAYED IN THE BUTTON
b15.pack()                                                                                                                               #DISPLAYING THE BUTTON WITHIN THE MENU WINDOW


l9 = Label(window, text="",bg="lightgrey")                                                                                               #CREATING A LABEL THAT WILL DISPLAY NOTHING
l9.pack()

def option16():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\HTML CODE\\Grand Central Online - MSTR.html")                #THE PATH FOR THIS APPLICATION AND OPENS IT

b16 = Button(window, text="GRAND CENTRAL ONLINE", command=option16)                                                                      #THIS IS WHAT WILL BE DISPLAYED IN THE BUTTON
b16.pack()                                                                                                                               #DISPLAYING THE BUTTON WITHIN THE MENU WINDOW


l7 = Label(window, text="",bg="lightgrey")                                                                                               #CREATING A LABEL THAT WILL DISPLAY NOTHING
l7.pack()                                                                                                                                #DISPLAYING THE LABEL WITHIN THE MENU WINDOW


def option13():

    SEL=LogOut[random.randint(0,1)]                                                                                                          #RANDOMLY SELECTING 1 OF THE 2 LEAVING GREETINGS

    if SEL ==1:
        song1 = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\GoodBye.mp3')     #PATH FOR A LEAVING GREETING
        song1.play()                                                                                                                         #PLAYS THE LEAVING GREETING MP3
    if SEL ==2:
        song2 = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\SeeYouLater.mp3') #PATH FOR A LEAVING GREETING
        song2.play()                                                                                                                         #PLAYS THE LEAVING GREETING MP3
    t.sleep(1)
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\LOGOUT.mp3')           #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\TK_LOGIN_v3.py")                         #THE PATH FOR THE LOGIN APPLICATION
    window.destroy()                                                                                                                         #CLOSING REMAINED WINDOWS
    t.sleep(4)
    Window.destroy()


b13 = Button(window, text="               LOG OUT             ", fg="blue" ,command=option13)                                                #THIS IS WHAT WILL BE DISPLAYED IN THE BUTTON
b13.pack()                                                                                                                                   #DISPLAYING THE BUTTON WITHIN THE MENU WINDOW

def close_window():

    SEL=LogOut[random.randint(0,1)]                                                                                                          #RANDOMLY SELECTS 1 OF THE EXIT GREETINGS

    if SEL ==1:
        song1 = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\GoodBye.mp3')     #PATH FOR A LEAVING GREETING
        song1.play()                                                                                                                         #PLAYS THE LEAVING GREETING MP3
    if SEL ==2:
        song2 = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\SeeYouLater.mp3') #PATH FOR A LEAVING GREETING
        song2.play()                                                                                                                         #PLAYS THE LEAVING GREETING MP3
    t.sleep(1)                                                                                                                               #WAITS 1 SECOND - WHILST MP3 PLAYS
    window.destroy()                                                                                                                         #CLOSES THE MENU WINDOW
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\GC_SHUT_DOWN.mp3')     #PATH FOR THE SHUT DOWN SOUND
    song.play()                                                                                                                              #PLAYS THE SHUT DOWN MP3
    t.sleep(2)                                                                                                                               #WAITS 2 SECONDS - WHILLST MP3 PLAYS
    Window.destroy()                                                                                                                         #CLOSES THE SECOND WINDOW

b14 = Button(window, text="           SHUT DOWN          ", fg="red" , command=close_window)                                                 #THIS IS WHAT WILL BE DISPLAYED IN THE BUTTON
b14.pack()                                                                                                                                   #DISPLAYING THE BUTTON IN THE MENU WINDOW


l8 = Label(window, text="",bg="lightgrey")                                                                                                   #CREATING A LABEL THAT WILL DISPLAY NOTHING
l8.pack()                                                                                                                                    #DISPLAYING THE LABEL WITHIN THE MENU WINDOW

def option14():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\TK_MSTR_v3.py")    #THE PATH FOR GC-MSTR AS IT IS A REFRESH
    window.destroy()                                                                                                                         #CLOSES THE MAIN MENU WINDOW
    t.sleep(4)                                                                                                                               #WAITS FOR 4 SECONDS
    Window.destroy()                                                                                                                         #CLOSES THE SECOND WINDOW


b14 = Button(window, text="              REFRESH              ", fg="green" ,command=option14)                                               #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b14.pack()                                                                                                                                   #DISPLAYS THE BUTTON IN THE MENU WINDOW

l9 = Label(window, text="",bg="lightgrey")                                                                                                   #CREATING A LABEL THAT WILL DISPLAY NOTHING
l9.pack()                                                                                                                                    #DISPLAYING THE LABEL WITHIN THE MENU WINDOW


b15 = Button(Window, text="MAIN MENU", bg="White", relief=FLAT ,command=option14)                                                            #THIS IS WHAT WILL BE DISPLAYED IN THE BUTTON
b15.pack()                                                                                                                                   #DISPLAYING THE BUTTON IN THE MENU

window.resizable(0,0)                                                                                                                        #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
window.protocol('WM_DELETE_WINDOW',donothing)                                                                                                #THE 'X' IN THE TOP BAR DOES NOTHING
window.resizable(width=FALSE, height=FALSE)                                                                                                  #THE USER CANNOT CHANGE THE SIZE OF THE MENU
window.title("GRAND CENTRAL MAIN MENU - MSTR")                                                                                               #GIVING THE MENU WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
window.geometry("400x790")                                                                                                                   #CONFIGURING THE FIXED SIZE OF THE MENU WINDOW WHICH WILL ALWAYS BE THIS SIZE
window.configure(background='lightgrey')                                                                                                     #CONFIGURING THE BACKGROUND OF THE MENU WINDOW TO BE LIGHT GREY

Window.overrideredirect(True)                                                                                                                #ALLOWING FOR THE PRGRAM TO ENTER FULLSCREEN MODE
Window.resizable(width=FALSE, height=FALSE)                                                                                                  #THIS MEANS THAT THE PROGRAM WILL NOT HAVE A FIXED SIZE
Window.geometry("{0}x{1}+0+0".format(Window.winfo_screenwidth(), Window.winfo_screenheight()))                                               #MAKING THE SIZE OF THE SECOND WINDOW FIT AUTOMATICALLY TO THE SIZE OF THE USERS SCREEN
Window.configure(background='White')                                                                                                         #CONFIGURING THE BACKGROUND OF THE SECOND WINDOW TO BE WHITE

label = Label(Window)                                                                                                                                   #CREATING THE LABEL FOR THE SECOND WINDOW
label.img = PhotoImage(file="C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\MSTRDESKTOP.png") #THIS IS THE PATH FOR THE BACKGROUND
label.configure(image=label.img)                                                                                                                        #CONFIGURING THE LABEL TO HOLD THE IMAGE FOR THE BACKGROUND
label.pack()                                                                                                                                            #DISPLAYING THE LABEL ON THE SECOND WINDOW

Window.mainloop()                                                                                                                                       #CALLING THE 'Window' AS THE MAIN LOOP AND TO EXECUTE
window.mainloop()                                                                                                                                       #CALLING THE 'window' AS THE MAIN LOOP AND TO EXECUTE
