#Nathan Jones
#GRAND CENTRAL - LOG IN                                                                                   

from tkinter import messagebox, Label, Button, FALSE, Tk, Entry    #ALLOWING FOR TKINTER TO BE ACCESSED/UTILISED FOR THE PROGRAM TO USE ALL OF ITS FUNCTIONS AND GIVING THE PROGRAM A GUI
from tkinter import *                                              #ALLOWING FOR ALL OF TKINTER'S MODULES TO BE IMPORTED 
from cv2 import *                                                  #ALLOWS PYTHON TO DIRECTLY ACCESS THE WEBCAM FOR USE IN THE FAILED LOG IN ATTEMPTS 
from PIL import Image, ImageTk                                     #ALLOWING FOR IMAGES TO ADDED IN THE GUI FOR THE LIKES OF THE BACKGROUNDS AND OTHER IMAGES
from datetime import datetime                                      #ALLOWING THE DATE AND TIME TO BE DISPLAYED 
from email.mime.text import MIMEText                               #ALLOWS FOR GRAND CENTRAL TO GENERATE THE TEXT THAT WILL BE DISPLAYED IN THE BODY OF TEH EMAIL  
from email.mime.multipart import MIMEMultipart                     #ALLOWS FOR GRAND CENTRAL TO ACCESS THE EMAIL SERVERS TO CREATE THE EMAILS FOR THE FAILED LOGINS
from email.mime.base import MIMEBase                               #ALLOWS FOR GRAND CENTRAL TO CREATE THE EMAILS MAIN BODY OF TEXT FOR THE FAILED LOGINS
from email import encoders                                         #ALLOWS FOR GRAND CENTRAL TO ENCODE THE EMAILS FOR THE FAILED LOGINS AND TEHN SEND THEM DIRECTLY
from uuid import getnode as get_mac                                #ALLOWS FOR TO ACCESS THE MODULES THAT ALLOW DIRECT ACCESS TO THE MAC ADDRESS OF THE MACHINE

import smtplib     #ALLOWS DIRECT ACCESS TO THE SMTP LIBARIES SO THAT THE EMAILS CAN BE SENT FOR THE FAILED LOG IN ATTEMPTS
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
import pyglet      #THIS IS THE MODULE THAT ALLOWS FOR THE SOUNDS/MUSIC/SONGS TO BE PLAYED 

#GLOBAL VARIABLES - LOGIN ATTEMPTS

TRYS=0                       #KEEPING COUNT OF HOW MANY TRYS THE USER HAS HAD WHEN LOGGING IN
trys=2                       #USED TO CREATE A COUNT DOWN OF HOW MANY MORE ATTEMPTS THE USER HAS FOR THE LOG IN 

#VALIDATION KEYS - MAC ADDRESSES

MAC1=["128531078084978"]    #VERIFIED MAC ADDRESS FOR GRAND CENTRAL
MAC2=[""]                   #VERIFIED MAC ADDRESS FOR GRAND CENTRAL
MAC3=[""]                   #VERIFIED MAC ADDRESS FOR GRAND CENTRAL
MAC4=[""]                   #VERIFIED MAC ADDRESS FOR GRAND CENTRAL
MAC5=[""]                   #VERIFIED MAC ADDRESS FOR GRAND CENTRAL
MAC6=[""]                   #VERIFIED MAC ADDRESS FOR GRAND CENTRAL

#USERNAMES AND PASSWORDS

username1 = ("Admin")       #USER'S NAME TO ACCESS THE MASTER ACCOUNT
password1 = ("Develop01")   #USER'S PASSWORD TO ACCES THE MASTER ACCOUNT

username2 = ("Teacher")     #USER'S NAME TO ACCESS THE TEACHER ACCOUNT
password2 = ("TEACH2018")   #USER'S PASSWORD TO ACCESS THE TEACHER ACCOUNT
 
username3 = ("CompSci")     #USER'S NAME TO ACCESS THE COMPSCI ACCOUNT
password3 = ("PYTHON3")     #USER'S PASSWORD TO ACCESS THE COMPSCI ACCOUNT

username4 = ("Adrian")      #USER'S NAME TO ACCESS THEIR USER ACCOUNT
password4 = ("120770")      #USER'S PASSWORD TO ACCESS THEIR USER ACCOUNT
 
username5 = ("Tracey")      #USER'S NAME TO ACCESS THEIR USER ACCOUNT
password5 = ("010871")      #USER'S PASSWORD TO ACCESS THEIR USER ACCOUNT

username6 = ("Jess")        #USER'S NAME TO ACCESS THEIR USER ACCOUNT
password6 = ("291004")      #USER'S PASSWORD TO ACCESS THEIR USER ACCOUNT

username666 = ("SHUT_DOWN") #DEBUG USERNAME TO MANUALLY SHUT DOWN GRAND CENTRAL
password666 = ("666")       #DEBUG USERNAME'S PASSWORD TO MANUALLY SHUT DOWN GRAND CENTRAL

def donothing():            #CREATING THE FUNCTION THAT WILL LITERALLY DO NOTHING BY THE USE OF THE 'pass' FUNCTION WITHIN PYTHON
    pass                    #CALLING THE 'pass' FUNCTION TO DO NOTHING

def login():

    mac = get_mac()  #IMPORTING THE 'get_mac()' FUNCTION AS 'mac' SO IT IS EASIER TO CALL

    global TRYS      #IMPORTING THE 'TRYS' ARRAY TO KEEP TRACK OF HOW MANY ATTEMPTS THEY HAVE HAD AT LOGGING IN
    global trys      #IMPORTING THE 'trys' ARRAY TO CREATE A COUNT DOWN OF HOW MANY MORE ATTEMPTS THEY HAVE AT LOGGING IN
    global MAC1      #IMPORTING THE MAC ADDRESSES FOR THE VALIDATION PURPOSES 
    global MAC2      #IMPORTING THE MAC ADDRESSES FOR THE VALIDATION PURPOSES
    global MAC3      #IMPORTING THE MAC ADDRESSES FOR THE VALIDATION PURPOSES
    global MAC4      #IMPORTING THE MAC ADDRESSES FOR THE VALIDATION PURPOSES
    global MAC5      #IMPORTING THE MAC ADDRESSES FOR THE VALIDATION PURPOSES
    global MAC6      #IMPORTING THE MAC ADDRESSES FOR THE VALIDATION PURPOSES
    
    if username.get() == username1 and password.get() == password1:       #CHECKING THE USERNAME AND PASSWORD THAT WAS ENTERED AGAINST THE 1ST USERNAME/PASSWORD SET
        if mac == MAC1 or MAC2 or MAC3 or MAC4 or MAC5 or MAC6:           #CHECKING THE MAC ADDRESS AGAINST THE VALIDATION KEYS (VALIDATED MAC ADDRESS)
            window.destroy()                                                                                                                         #CLOSING THE LOG IN WINDOW 
            song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\LOGIN.mp3')            #PATH FOR THE LOG IN SOUND   
            song.play()                                                                                                                              #PLAYING THE LOG IN MP3
            time.sleep(1)                                                                                                                            #WAITING FOR 1 SECOND 
            os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\TK_MSTR_v3.py")   #LAUNCHING MASTER EDITION OF GRAND CENTRAL
            time.sleep(4)                                                                                                                            #WAITING FOR 4 SECONDS
            Window.destroy()                                                                                                                         #CLOSING THE SECOND WINDOW
        else: 
            window.destroy()                                                                                                                         #CLOSING THE LOG IN WINDOW                                 
            song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\ERROR.mp3')            #PATH FOR THE GRAND CENTRAL ERROR SOUND
            song.play()                                                                                                                              #PLAYING THE ERROR MP3
            time.sleep(1)                                                                                                                            #WAITING FOR 1 SECOND
            messagebox.showinfo("   ERROR!   ", "  NOT A VALID MACHINE!" , icon="error")                                                             #DISPLAYING THE ERROR MESSAGE BOX
            time.sleep(3)                                                                                                                            #WAITING FOR 3 SECONDS
            song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\GC_SHUT_DOWN.mp3')     #PATH FOR THE SHUT DOWN SOUND
            song.play()                                                                                                                              #PLAYING THE SHUT DOWN MP3
            time.sleep(3)                                                                                                                            #WAITING FOR 3 SECONDS
            Window.destroy()                                                                                                                         #CLOSING THE SECOND WINDOW 
             
            

    elif username.get() == username2 and password.get() == password2:     #CHECKING THE USERNAME AND PASSWORD THAT WAS ENTERED AGAINST THE 2ND USERNAME/PASSWORD SET
        if mac == MAC1 or MAC2 or MAC3 or MAC4 or MAC5 or MAC6:           #CHECKING THE MAC ADDRESS AGAINST THE VALIDATION KEYS (VALIDATED MAC ADDRESS)
            window.destroy()                                                                                                                         #CLOSING THE LOG IN WINDOW 
            song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\LOGIN.mp3')            #PATH FOR THE LOG IN SOUND 
            song.play()                                                                                                                              #PLAYING THE LOG IN MP3
            time.sleep(1)                                                                                                                            #WAITING FOR 1 SECOND
            os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-TEACH\\TK_TEACH_v3.py") #LAUNCHING THE TEACHER EDITION OF GRAND CENTRAL
            time.sleep(4)                                                                                                                            #WAITING FOR 4 SECONDS
            Window.destroy()                                                                                                                         #CLOSING THE SECOND WINDOW
        else:
            window.destroy()                                                                                                                         #CLOSING THE LOG IN WINDOW 
            song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\ERROR.mp3')            #PATH FOR THE GRAND CENTRAL ERROR SOUND
            song.play()                                                                                                                              #PLAYING THE ERROR MP3
            time.sleep(1)                                                                                                                            #WAITING FOR 1 SECOND
            messagebox.showinfo("   ERROR!   ", "  NOT A VALID MACHINE!" , icon="error")                                                             #DISPLAYING THE ERROR MESSAGE BOX
            time.sleep(3)                                                                                                                            #WAITING FOR 3 SECONDS
            song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\GC_SHUT_DOWN.mp3')     #PATH FOR THE SHUT DOWN SOUND
            song.play()                                                                                                                              #PLAYING THE SHUT DOWN MP3
            time.sleep(3)                                                                                                                            #WAITING FOR 3 SECONDS
            Window.destroy()                                                                                                                         #CLOSING THE SECOND WINDOW

    elif username.get() == username3 and password.get() == password3:     #CHECKING THE USERNAME AND PASSWORD THAT WAS ENTERED AGAINST THE 3RD USERNAME/PASSWORD SET
        if mac == MAC1 or MAC2 or MAC3 or MAC4 or MAC5 or MAC6:           #CHECKING THE MAC ADDRESS AGAINST THE VALIDATION KEYS (VALIDATED MAC ADDRESS)
            window.destroy()                                                                                                                         #CLOSING THE LOG IN WINDOW
            song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\LOGIN.mp3')            #PATH FOR THE LOG IN SOUND
            song.play()                                                                                                                              #PLAYING THE LOG IN MP3
            time.sleep(1)                                                                                                                            #WAITING FOR 1 SECOND 
            os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\COMPSCI.py")                             #LAUNCHING THE COMPUTER SCIENCE EDITION OF GRAND CENTRAL
            time.sleep(4)                                                                                                                            #WAITING FOR 4 SECONDS
            Window.destroy()                                                                                                                         #CLOSING THE SECOND WINDOW
        else:
            window.destroy()                                                                                                                         #CLOSING THE LOG IN WINDOW 
            song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\ERROR.mp3')            #PATH FOR THE GRAND CENTRAL ERROR SOUND
            song.play()                                                                                                                              #PLAYING THE ERROR MP3
            time.sleep(1)                                                                                                                            #WAITING FOR 1 SECOND
            messagebox.showinfo("   ERROR!   ", "  NOT A VALID MACHINE!" , icon="error")                                                             #DISPLAYING THE ERROR MESSAGE BOX
            time.sleep(3)                                                                                                                            #WAITING FOR 3 SECONDS
            song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\GC_SHUT_DOWN.mp3')     #PATH FOR THE SHUT DOWN SOUND
            song.play()                                                                                                                              #PLAYING THE SHUT DOWN MP3
            time.sleep(3)                                                                                                                            #WAITING FOR 3 SECONDS
            Window.destroy()                                                                                                                         #CLOSING THE SECOND WINDOW

    elif username.get() == username4 and password.get() == password4:     #CHECKING THE USERNAME AND PASSWORD THAT WAS ENTERED AGAINST THE 4TH USERNAME/PASSWORD SET
        if mac == MAC1 or MAC2 or MAC3 or MAC4 or MAC5 or MAC6:           #CHECKING THE MAC ADDRESS AGAINST THE VALIDATION KEYS (VALIDATED MAC ADDRESS)
            window.destroy()                                                                                                                         #CLOSING THE LOG IN WINDOW
            song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\LOGIN.mp3')            #PATH FOR THE LOG IN SOUND
            song.play()                                                                                                                              #PLAYING THE LOG IN MP3
            time.sleep(1)                                                                                                                            #WAITING FOR 1 SECOND 
            os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-USERS\\AJ\\TK_AJ.py")   #LAUNCHING A USER VERSION OF GRAND CENTRAL
            time.sleep(4)                                                                                                                            #WAITING FOR 4 SECONDS
            Window.destroy()                                                                                                                         #CLOSING THE SECOND WINDOW
        else:
            window.destroy()                                                                                                                         #CLOSING THE LOG IN WINDOW 
            song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\ERROR.mp3')            #PATH FOR THE GRAND CENTRAL ERROR SOUND
            song.play()                                                                                                                              #PLAYING THE ERROR MP3
            time.sleep(1)                                                                                                                            #WAITING FOR 1 SECOND
            messagebox.showinfo("   ERROR!   ", "  NOT A VALID MACHINE!" , icon="error")                                                             #DISPLAYING THE ERROR MESSAGE BOX
            time.sleep(3)                                                                                                                            #WAITING FOR 3 SECONDS
            song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\GC_SHUT_DOWN.mp3')     #PATH FOR THE SHUT DOWN SOUND
            song.play()                                                                                                                              #PLAYING THE SHUT DOWN MP3
            time.sleep(3)                                                                                                                            #WAITING FOR 3 SECONDS
            Window.destroy()                                                                                                                         #CLOSING THE SECOND WINDOW

    elif username.get() == username5 and password.get() == password5:     #CHECKING THE USERNAME AND PASSWORD THAT WAS ENTERED AGAINST THE 5TH USERNAME/PASSWORD SET
        if mac == MAC1 or MAC2 or MAC3 or MAC4 or MAC5 or MAC6:           #CHECKING THE MAC ADDRESS AGAINST THE VALIDATION KEYS (VALIDATED MAC ADDRESS)
            window.destroy()                                                                                                                         #CLOSING THE LOG IN WINDOW
            song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\LOGIN.mp3')            #PATH FOR THE LOG IN SOUND
            song.play()                                                                                                                              #PLAYING THE LOG IN MP3
            time.sleep(1)                                                                                                                            #WAITING FOR 1 SECOND 
            os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\TJ.py")                                  #LAUNCHING A USER VERSION OF GRAND CENTRAL
            time.sleep(4)                                                                                                                            #WAITING FOR 4 SECONDS
            Window.destroy()                                                                                                                         #CLOSING THE SECOND WINDOW
        else:
            window.destroy()                                                                                                                         #CLOSING THE LOG IN WINDOW 
            song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\ERROR.mp3')            #PATH FOR THE GRAND CENTRAL ERROR SOUND
            song.play()                                                                                                                              #PLAYING THE ERROR MP3
            time.sleep(1)                                                                                                                            #WAITING FOR 1 SECOND
            messagebox.showinfo("   ERROR!   ", "  NOT A VALID MACHINE!" , icon="error")                                                             #DISPLAYING THE ERROR MESSAGE BOX
            time.sleep(3)                                                                                                                            #WAITING FOR 3 SECONDS
            song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\GC_SHUT_DOWN.mp3')     #PATH FOR THE SHUT DOWN SOUND
            song.play()                                                                                                                              #PLAYING THE SHUT DOWN MP3
            time.sleep(3)                                                                                                                            #WAITING FOR 3 SECONDS
            Window.destroy()                                                                                                                         #CLOSING THE SECOND WINDOW

    elif username.get() == username6 and password.get() == password6:     #CHECKING THE USERNAME AND PASSWORD THAT WAS ENTERED AGAINST THE 6TH USERNAME/PASSWORD SET
        if mac == MAC1 or MAC2 or MAC3 or MAC4 or MAC5 or MAC6:           #CHECKING THE MAC ADDRESS AGAINST THE VALIDATION KEYS (VALIDATED MAC ADDRESS)
            window.destroy()                                                                                                                         #CLOSING THE LOG IN WINDOW
            song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\LOGIN.mp3')            #PATH FOR THE LOG IN SOUND
            song.play()                                                                                                                              #PLAYING THE LOG IN MP3
            time.sleep(1)                                                                                                                            #WAITING FOR 1 SECOND 
            os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\JJ.py")                                  #LAUNCHING A USER VERSION OF GRAND CENTRAL
            time.sleep(4)                                                                                                                            #WAITING FOR 4 SECONDS
            Window.destroy()                                                                                                                         #CLOSING THE SECOND WINDOW
        else:
            window.destroy()                                                                                                                         #CLOSING THE LOG IN WINDOW 
            song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\ERROR.mp3')            #PATH FOR THE GRAND CENTRAL ERROR SOUND
            song.play()                                                                                                                              #PLAYING THE ERROR MP3
            time.sleep(1)                                                                                                                            #WAITING FOR 1 SECOND
            messagebox.showinfo("   ERROR!   ", "  NOT A VALID MACHINE!" , icon="error")                                                             #DISPLAYING THE ERROR MESSAGE BOX
            time.sleep(3)                                                                                                                            #WAITING FOR 3 SECONDS
            song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\GC_SHUT_DOWN.mp3')     #PATH FOR THE SHUT DOWN SOUND
            song.play()                                                                                                                              #PLAYING THE SHUT DOWN MP3
            time.sleep(3)                                                                                                                            #WAITING FOR 3 SECONDS
            Window.destroy()                                                                                                                         #CLOSING THE SECOND WINDOW

    elif username.get() == username666 and password.get() == password666: #CHECKING THE USERNAME AND PASSWORD THAT WAS ENTERED AGAINST THE 7TH USERNAME/PASSWORD SET
        window.destroy()                                                                                                                         #CLOSING THE LOG IN WINDOW
        song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\GC_SHUT_DOWN.mp3')     #PATH FOR THE SHUT DOWN SOUND
        song.play()                                                                                                                              #PLAYING THE SHUT DOWN MP3
        time.sleep(3)                                                                                                                            #WAITING FOR 3 SECONDS
        Window.destroy()                                                                                                                         #CLOSING THE SECOND WINDOW
        sys.exit()                                                                                                                               #ENDING THE SESSION 
           
    else:                                                                 #IF THE USERNAME AND/OR PASSWORD DO NOT MATCH ANY OF THE USERNAME/PASSWORD SET
        song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\ERROR.mp3')            #PATH FOR THE GRAND CENTRAL ERROR SOUND
        song.play()                                                                                                                              #PLAYING THE ERROR MP3
        time.sleep(1)                                                                                                                            #WAITING 1 SECOND
        messagebox.showinfo("   ERROR!   ", """  Your username and/or password was incorrect!                                                        
                     You have """+str(trys)+str(" attempts left!") , icon="error")                                    #DISPLAYING THE ERROR MESSAGE BOX WITH ATTEMPTS LEFT
        TRYS = TRYS+1                                                                                                 #ADDS +1 TO THE 'TRYS' ARRAY TO KEEP COUNT
        trys = trys-1                                                                                                 #TAKES -1 AWAY FROM THE 'trys' ARRAY TO DISPLAY REMAINDER OF ATTMEPTS 


    if TRYS == 4 or trys == -1:                #IF THE THE 'TRYS' ARRAY IS EQUAL TO 4 OR THE 'trys' ARRAY IS EQUAL TO -1 THEN THE FOLLOWING WILL TAKE PLACE                
        if username.get == username1:          #IF THE USERNAME ENTERED IS THE SAME AS THE ONE STORED UNDER 'username1' THEN THE FOLLOWING WILL TAKE PLACE
            PHOTO_TIME()                       #REDIRECTS THE PROGRAM TO THE USER SPECIFIC PHOTO FUNCTION 
            window.destroy()                   #CLOSES THE LOGIN WINDOW
        elif username.get == username2:        #IF THE USERNAME ENTERED IS THE SAME AS THE ONE STORED UNDER 'username2' THEN THE FOLLOWING WILL TAKE PLACE
            PHOTO_TIME1()                      #REDIRECTS THE PROGRAM TO THE USER SPECIFIC PHOTO FUNCTION
            window.destroy()                   #CLOSES THE LOGIN WINDOW
        elif username.get == username3:        #IF THE USERNAME ENTERED IS THE SAME AS THE ONE STORED UNDER 'username3' THEN THE FOLLOWING WILL TAKE PLACE
            PHOTO_TIME2()                      #REDIRECTS THE PROGRAM TO THE USER SPECIFIC PHOTO FUNCTION
            window.destroy()                   #CLOSES THE LOGIN WINDOW
        elif username.get == username4:        #IF THE USERNAME ENTERED IS THE SAME AS THE ONE STORED UNDER 'username4' THEN THE FOLLOWING WILL TAKE PLACE
            PHOTO_TIME3()                      #REDIRECTS THE PROGRAM TO THE USER SPECIFIC PHOTO FUNCTION
            window.destroy()                   #CLOSES THE LOGIN WINDOW
        elif username.get == username5:        #IF THE USERNAME ENTERED IS THE SAME AS THE ONE STORED UNDER 'username5' THEN THE FOLLOWING WILL TAKE PLACE
            PHOTO_TIME4()                      #REDIRECTS THE PROGRAM TO THE USER SPECIFIC PHOTO FUNCTION
            window.destroy()                   #CLOSES THE LOGIN WINDOW
        else:                                  #IF THE USERNAME ENTERED IS NOT THE SAME AS ANY OF THE USERNAMES THEN THE FOLLOWING WILL TAKE PLACE
            PHOTO_TIME()                       #REDIRECTS THE PROGRAM TO THE USER SPECIFIC PHOTO FUNCTION
            window.destroy()                   #CLOSES THE LOGIN WINDOW
               
window = Tk() #DEFINING WHAT THE FIRST TKINTER WINDOW WILL BE DEFINED AS
Window = Tk() #DEFINING WHAT THE SECOND TKINTER WINDOW WILL BE DEFINED AS

window.resizable (0,0)                        #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
window.protocol ('DELETE_WINDOW', donothing)  #THE 'X' IN THE TOP BAR DOES NOTHING 
window.resizable (width=FALSE, height=FALSE)  #THE USER CANNOT CHANGE THE SIZE OF THE MENU
window.title ("GRAND CENTRAL LOG IN")         #GIVING THE LOGIN WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
window.geometry("400x600")                    #CONFIGURING THE FIXED SIZE OF THE LOGIN WINDOW WHICH WILL ALWAYS BE THIS SIZE            
window.configure(background='white')          #CONFIGURING THE BACKGROUND OF THE LOGIN WINDOW TO BE WHITE

album = PhotoImage(file="C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\GCimg.png") #THIS IS THE PATH FOR THE IMAGE DISPLAYED WITHIN THE LOGIN WINDOW

label = Label (window, image=album)                                      #CREATING THE LABEL THAT WILL DISPLAY THE GRAND CENTRAL LOGO AT THE TOP OF THE LOGIN WINDOW
Username = Label (window, text="Username:", background="white")          #CREATING THE LABEL THAT WILL SAY 'Username' ABOVE THE ENTRY BOX
username = Entry (window, background="light grey")                       #CREATING AN ENTRY BOX WHERE THE USER WILL INPUT THEIR USERNAME, IT WILL HAVE A LIGHT GREY BACKGROUND WITHIN THE BOX 
Password = Label (window, text="Password:", background="white")          #CREATING THE LABEL TAHT WILL SAY 'Password' ABOVE THE ENTRY BOX
password = Entry (window, background="light grey", show="*")             #CREATING AN ENTRY BOX WHERE THE USER WILL INPUT THEIR PASSOWRD, IT WILL HAVE A LIGHT GREY BACKGROUND WITHIN THE BOX 

login = Button (text="      LOGIN      ", fg="blue", command=login)      #CREATING THE ACTUAL LOGIN BUTTON 

label.pack()                        #DISPLAYING THE LABEL THAT HOLDS THE GRAND CENTRAL LOGO
Username.pack()                     #DISPLAYING THE USERNAME LABEL THAT WILL SIT ABOVE THE ENTRY BOX
username.pack()                     #DISPLAYING THE ENTRY BOX FOR THE USER TO INPUT THEIR USERNAME
Password.pack()                     #DISPLAYING THE PASSWORD LABEL THAT WILL SIT ABOVE THE ENTRY BOX
password.pack()                     #DISPLAYING THE ENTRY BOX FOR THE USER TO INPUT THEIR PASSWORD
login.pack()                        #DISPLAYING THE LOGIN BUTTON 
 
l1 = Label (text=" ", bg ="white")  #CREATING A LABEL THAT WILL BE WHITE AND WILL ACT AS A SPACE BETWEEN THELOGIN AND SHUT DOWN BUTTONS
l1.pack()                           #DISPLAYING THE WHITE LABEL 

def close_window():
 
    window.destroy()                                                                                                                      #CLOSING THE LOG IN WINDOW
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\GC_SHUT_DOWN.mp3')  #PATH FOR THE SHUT DOWN SOUND
    song.play()                                                                                                                           #PLAYING THE SHUT DOWN MP3 
    time.sleep(2)                                                                                                                         #WAITING FOR 2 SECONDS 
    Window.destroy()                                                                                                                      #CLOSING THE SECOND WINDOW 

b1 = Button (window, text="SHUT DOWN", fg ="red", command=close_window)                         #CREATING THE SHUT DOWN BUTTON TO COMPLETLEY SHUT DOWN GRAND CENTRAL
b1.pack()                                                                                       #DISPLAYING THE SHUT DOWN BUTTON

l2 = Label (window, text="""

""", bg ="white")                                                                               #CREATING AN EMPTY LABEL THAT WILL ACT AS A SPACE IN THE LOGIN WINDOW 
l2.pack()                                                                                       #DISPLAYING THE LABEL ON THE LOGIN WINDOW 

l3 = Label (window, text="*DISCLAIMER*", font='Helvetica 10 bold', fg ="red", bg ="white")      #CREATING A LABEL TAHT WILL BE DISPLAYED IN BOLD AND RED 
l3.pack()                                                                                       #DISPLAYING THE LABEL ON THE LOGIN WINDOW

l4 = Label (window, text="""IF YOU ENTER YOUR PASSOWRD/USERNAME WRONG 3 TIMES 
A PHOTO WILL BE TAKEN AND EMAILED TO THE USER OF THE ACCOUNT
YOU ARE TRYING TO ACCESS""", font='Helvetica 8 ', fg ="red", bg ="white")                       #CREATING THE LABEL THAT WILL HOLD THE DISCLAIMER ABOUT TAKING THE PHOTO AFTER 3 WRONG ATTEMPTS 
l4.pack()                                                                                       #DISPLAYING THE LABEL ON THE LOGIN WINDOW 

Window.overrideredirect(True)                                                                   #ALLOWING FOR THE PRGRAM TO ENTER FULLSCREEN MODE
Window.resizable(width=FALSE, height=FALSE)                                                     #GIVING THE WINDOW NO FIXED VALUES AS THE WINDOW WILL AUTOMATICALLY FIT THE SCREEN  
Window.geometry("{0}x{1}+0+0".format(Window.winfo_screenwidth(), Window.winfo_screenheight()))  #THIS ALLOWS FOR THE BACKGROUND TO AUTOMATICALLY FIT THE SCREEN
Window.configure(background='grey')                                                             #CREATING THE BACKGROUND OF THE LOGIN PROGRAM 

faceCascade = cv2.CascadeClassifier('C:\\Users\\natda\\AppData\\Local\\Programs\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml') #PATH FOR THE TEMPLATE THAT WILL MAP A BOX TO THE PERSONS FACE


def PHOTO_TIME():

    global username1                                        #GETTING THE USERNAME OF THE FAILED LOGIN

    window.destroy()                                        #CLOSING THE LOGIN WINDOW 

    cam = cv2.VideoCapture (0)                              #DEFINING WHAT THE WEBCAM WILL BE DIFINED AS  
    s, image = cam.read()                                   #ACTIVATING THE WEBCAM OF THE MACHINE IF AVALIABLE 
    image = cv2.flip(image, 1)                              #DEFINING WHAT THE IMAGE FROM THE WEBCAM WILL BE KNOW AS
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)          #DEFINING HOW THE WEBCAM WILL SEE THE FACE - IF THERE IS ONE
    faces = faceCascade.detectMultiScale(                   #DEFINING WHAT THE FACE TEMPLATE WILL BE KNOWN AS SO IT CAN MAP A BOX TO A PERSONS FACE
        gray,                                               
        scaleFactor=1.2,                                    #PARAMETERS FOR THE FACE TEMPLATE THAT WILL LOOK FOR A PERSONS FACE
        minNeighbors=5,                                     #PARAMETERS FOR THE FACE TEMPLATE THAT WILL LOOK FOR A PERSONS FACE
        minSize=(20, 20)                                    #PARAMETERS FOR THE FACE TEMPLATE THAT WILL LOOK FOR A PERSONS FACE
    )
    for (x,y,w,h) in faces:                                 
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)    #ONCE A FACE HAS BEEN FOUND WITHIN THE IMAGE IT WILL MAP A BOX AROUND THEIR FACE
        roi_gray = gray[y:y+h, x:x+w]                       #ONCE A FACE HAS BEEN FOUND WITHIN THE IMAGE IT WILL MAP A BOX AROUND THEIR FACE
        roi_color = image[y:y+h, x:x+w]                     #ONCE A FACE HAS BEEN FOUND WITHIN THE IMAGE IT WILL MAP A BOX AROUND THEIR FACE

    if s: 
        
        imwrite ("FAILED LOGIN GCv3.jpg", image)            #SAVING THE IMAGE AS 'FAILED LOGIN GCv3.jpg' SO THAT IT CAN BE EMAILED OFF TO THE USER

    mac = get_mac()                                         #DEFINING A SHORTER NAME FOR THE 'get_mac()' AS IT WILL BE REPEATED SO THE SHORTER NAME HELPS WITH THIS
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    #CONNECTING TO THE SERVERS FOR THE EMAIL TO BE SENT
    s.connect(("8.8.8.8", 80))                              #CONNECTING TO THE SERVERS FOR THE EMAIL TO BE SENT
    
    EmailUser = 'GRANDCENTRALPYTHON@gmail.com'              #EMAIL ADDRESS OF GRAND CENTRAL - DEFINING IT AS A VARIABLE
    EmailPassword = 'Python301'                             #EMAIL ADDRESS'S PASSWORD TO LOGIN - DEFINING IT AS A VARIABLE
    EmailSend = 'natdanjones@btinternet.com'                #EMAIL ADDRESS OF THE USER'S ACCOUNT THAT THE FAILED LOGIN TOOK PLACE ON - DEFINING IT AS A VARIABLE

    subject = 'FAILED LOG IN ATTEMPT'                       #DEFINING THE SUBJECT OF THE EMAIL AS A VARIABLE AS IT WILL BE CALLED LATER ON 

    msg = MIMEMultipart()                                   #DEFINING A SHORTER NAME FOR THE PART OF CODE THAT ALLOWS EMAILS TO BE WRITTEN - SO IT CAN BE REPEATED 
    msg['From'] = EmailUser                                 #ASIGNING THE VARIABLE OF GRAND CENTRAL'S EMAIL ADDRESS TO FORM THE 'From' PART OF THE EMAIL SO IT KNOWS WHO IT IS GOING FROM
    msg['To'] = EmailSend                                   #ASIGNING THE VARIABLE OF USER'S EMAIL ADDRESS TO FORM THE 'To' PART OF THE EMAIL SO IT KNOWS WHO IT IS GOING TO
    msg['Subject'] = subject                                #ASIGNING THE VARIABLE OF THE SUBJECT OF THE EMAIL TO FORM THE 'Subject' PART OF THE EMAIL SO THE RECIEVER KNOWS WHAT THE EMAIL IS ABOUT



  
    body = (('''
IMPORTANT INFORMATION REGARDING YOUR ACCOUNT OF ''')+str(username1)+str('''

THE FILE ATTACHED IS THE PERSON WHO JUST TRIED TO GAIN ACCESS TO GRAND CENTRAL!

TIME OF FAILED LOGIN: ''')+str(datetime.datetime.now())+str('''

IP ADDRESS OF FAILED LOGIN: '''+str(s.getsockname()[0]))+str('''

MAC ADDRESS OF FAILED LOGIN: ''')+str(mac)+str('''

_________________________________________________________________________________________________
   THIS MESSAGE IS AUTOMATICALLY GENERATED WHEN SOMEONE TRIES TO GAIN ACCESS TO GRAND CENTRAL!
PLEASE DO NOT RESPOND TO THIS MESSAGE AS IT IS AUTOMATICALLY GENERATED AND WILL NOT RESPOND BACK!
                                All Rights Reserved 2018
                                    

© GRAND CENRTRAL 2018
NATHAN JONES
                                    
 
'''))                                                                               #THE SECTION ABOVE IS THE TEMPLATE FOR THE EMAIL THAT THE USER WILL RECIEVE IF THEIR ACCOUNT HAS A FAILED LOGIN ATTEMPT,
                                                                                    #WITHIN THE EMAIL IT WILL HAVE THE USER'S NAME, TIME OF ATTEMPT, IP ADDRESS, MAC ADDRESS AND A PHOTO OF THE PERSON
    msg.attach (MIMEText(body,'plain'))                                             #THIS ALLOWS THE PROGRAM TO ATTACH THE TEMPLATE OF THE EMAIL TO THE ACTUAL EMAIL WITH ALL INFORMATION FILLED OUT

    filename='FAILED LOGIN GCv3.jpg'                                                #DEFINING THE IMAGE PATH TO BE A VARIABLE SO THAT IT CAN BE CALLED LATER ON
    attachment=open(filename,'rb')                                                  #DEFINING THE 'filename' VARIABLE TO BE OPENED AND THEN ASSIGNED AS ANOTHER VARIABLE 'attachment' SO IT CAN BE ADDED TO THE EMAIL

    part = MIMEBase('application','octet-stream')                                   #DEFININNG THE 'MIME' WHICH IS TO DO WITH THE CONTENT-TRANSFER AND THIS SECTION IS CREATINNG THE FRAME FOR THE ATTACHMENTS 
    part.set_payload((attachment).read())                                           #THIS IS DEFINING THE PAYLOAD OF THE EMAIL SO IN THIS CASE IT WILL BE THE IMAGE FROM TEH VARIABLE 'attachment'
    encoders.encode_base64(part)                                                    #HERE IT IS ENCODING THE PAYLOAD AS A BASE64 AND ALLOWS FOR THE DATA TRANSFER OF TEH IMAGE
    part.add_header('Content-Disposition',"attachment; filename= "+filename)        #ADDING TO THE HEADER OF THE EMAIL THE ACTUAL IMAGE THAT WILL BE SENT TO THE USER 

    msg.attach(part)                                                                #ATTACHING THE ATTACHMENTS FRAME THAT IS ABOVE TO THE ACTUAL EMAIL THAT WILL BE SENT
    text = msg.as_string()                                                          #CONVERTING THE MESSAGE INTO A STRING FORMAT  
    server = smtplib.SMTP('smtp.gmail.com',587)                                     #DEFING THE SERVER THAT WILL BE USED WHEN SENDING THE EMAIL - IN THIS CASE GRAND CENTRAL WILL USE THE GMAIL SERVERS
    server.starttls()                                                               #ADDING ADDITIONAL SECURITY TO THE EMAIL BY USING THE 'Transport Layer Security' WHICH WILL BASICALLY ENCRYPT THE DATA TRANSFER
    server.login(EmailUser,EmailPassword)                                           #LOGGING IN TO THE EMAIL SERVER AND ACCOUNT OF GRAND CENTRAL SO THE EMAILS CAN BE SENT

    s.close()                                                                       #CLOSING A PART OF THE SERVER 
    server.sendmail(EmailUser,EmailSend,text)                                       #SENDING THE EMAIL ALONG WITH ALL OF THE APPROPRIATE INFORMATION 
    server.quit()                                                                   #DISCONNECTING FROM THES ERVER AFTER THE EMAIL HAS BEEN SENT
    Window.destroy()                                                                #CLOSING THE GREY BACKGROUND AS THE PROGRAM HAS NOW FINISHED
    sys.exit()                                                                      #CLOSING ANY PYTHON WINDOWS THAT ARE STILL OPEN 



def PHOTO_TIME1():


    global username2                                        #GETTING THE USERNAME OF THE FAILED LOGIN

    window.destroy()                                        #CLOSING THE LOGIN WINDOW 

    cam = cv2.VideoCapture (0)                              #DEFINING WHAT THE WEBCAM WILL BE DIFINED AS    
    s, image = cam.read()                                   #ACTIVATING THE WEBCAM OF THE MACHINE IF AVALIABLE 
    image = cv2.flip(image, 1)                              #DEFINING WHAT THE IMAGE FROM THE WEBCAM WILL BE KNOW AS
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)          #DEFINING HOW THE WEBCAM WILL SEE THE FACE - IF THERE IS ONE
    faces = faceCascade.detectMultiScale(                   #DEFINING WHAT THE FACE TEMPLATE WILL BE KNOWN AS SO IT CAN MAP A BOX TO A PERSONS FACE
        gray,     
        scaleFactor=1.2,                                    #PARAMETERS FOR THE FACE TEMPLATE THAT WILL LOOK FOR A PERSONS FACE
        minNeighbors=5,                                     #PARAMETERS FOR THE FACE TEMPLATE THAT WILL LOOK FOR A PERSONS FACE    
        minSize=(20, 20)                                    #PARAMETERS FOR THE FACE TEMPLATE THAT WILL LOOK FOR A PERSONS FACE
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)    #ONCE A FACE HAS BEEN FOUND WITHIN THE IMAGE IT WILL MAP A BOX AROUND THEIR FACE
        roi_gray = gray[y:y+h, x:x+w]                       #ONCE A FACE HAS BEEN FOUND WITHIN THE IMAGE IT WILL MAP A BOX AROUND THEIR FACE
        roi_color = image[y:y+h, x:x+w]                     #ONCE A FACE HAS BEEN FOUND WITHIN THE IMAGE IT WILL MAP A BOX AROUND THEIR FACE 

    if s: 
        
        imwrite ("FAILED LOGIN GCv3.jpg", image)            #SAVING THE IMAGE AS 'FAILED LOGIN GCv3.jpg' SO THAT IT CAN BE EMAILED OFF TO THE USER

    mac = get_mac()
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    #DEFINING A SHORTER NAME FOR THE 'get_mac()' AS IT WILL BE REPEATED SO THE SHORTER NAME HELPS WITH THIS
    s.connect(("8.8.8.8", 80))
    
    EmailUser = 'GRANDCENTRALPYTHON@gmail.com'              #EMAIL ADDRESS OF GRAND CENTRAL - DEFINING IT AS A VARIABLE
    EmailPassword = 'Python301'                             #EMAIL ADDRESS'S PASSWORD TO LOGIN - DEFINING IT AS A VARIABLE
    EmailSend = 'natdanjones@btinternet.com'                #EMAIL ADDRESS OF THE USER'S ACCOUNT THAT THE FAILED LOGIN TOOK PLACE ON - DEFINING IT AS A VARIABLE

    subject = 'FAILED LOG IN ATTEMPT'                       #DEFINING THE SUBJECT OF THE EMAIL AS A VARIABLE AS IT WILL BE CALLED LATER ON 

    msg = MIMEMultipart()                                   #DEFINING A SHORTER NAME FOR THE PART OF CODE THAT ALLOWS EMAILS TO BE WRITTEN - SO IT CAN BE REPEATED 
    msg['From'] = EmailUser                                 #ASIGNING THE VARIABLE OF GRAND CENTRAL'S EMAIL ADDRESS TO FORM THE 'From' PART OF THE EMAIL SO IT KNOWS WHO IT IS GOING FROM
    msg['To'] = EmailSend                                   #ASIGNING THE VARIABLE OF USER'S EMAIL ADDRESS TO FORM THE 'To' PART OF THE EMAIL SO IT KNOWS WHO IT IS GOING TO
    msg['Subject'] = subject                                #ASIGNING THE VARIABLE OF THE SUBJECT OF THE EMAIL TO FORM THE 'Subject' PART OF THE EMAIL SO THE RECIEVER KNOWS WHAT THE EMAIL IS ABOUT



  
    body = (('''
IMPORTANT INFORMATION REGARDING YOUR ACCOUNT OF ''')+str(username2)+str('''

THE FILE ATTACHED IS THE PERSON WHO JUST TRIED TO GAIN ACCESS TO GRAND CENTRAL!

TIME OF FAILED LOGIN: ''')+str(datetime.datetime.now())+str('''

IP ADDRESS OF FAILED LOGIN: '''+str(s.getsockname()[0]))+str('''

MAC ADDRESS OF FAILED LOGIN: ''')+str(mac)+str('''

_________________________________________________________________________________________________
   THIS MESSAGE IS AUTOMATICALLY GENERATED WHEN SOMEONE TRIES TO GAIN ACCESS TO GRAND CENTRAL!
PLEASE DO NOT RESPOND TO THIS MESSAGE AS IT IS AUTOMATICALLY GENERATED AND WILL NOT RESPOND BACK!
                                All Rights Reserved 2018
                                    

© GRAND CENRTRAL 2018
NATHAN JONES
                                    
 
'''))                                                                               #THE SECTION ABOVE IS THE TEMPLATE FOR THE EMAIL THAT THE USER WILL RECIEVE IF THEIR ACCOUNT HAS A FAILED LOGIN ATTEMPT,
                                                                                    #WITHIN THE EMAIL IT WILL HAVE THE USER'S NAME, TIME OF ATTEMPT, IP ADDRESS, MAC ADDRESS AND A PHOTO OF THE PERSON
    msg.attach (MIMEText(body,'plain'))                                             #THIS ALLOWS THE PROGRAM TO ATTACH THE TEMPLATE OF THE EMAIL TO THE ACTUAL EMAIL WITH ALL INFORMATION FILLED OUT

    filename='FAILED LOGIN GCv3.jpg'                                                #DEFINING THE IMAGE PATH TO BE A VARIABLE SO THAT IT CAN BE CALLED LATER ON
    attachment=open(filename,'rb')                                                  #DEFINING THE 'filename' VARIABLE TO BE OPENED AND THEN ASSIGNED AS ANOTHER VARIABLE 'attachment' SO IT CAN BE ADDED TO THE EMAIL

    part = MIMEBase('application','octet-stream')                                   #DEFININNG THE 'MIME' WHICH IS TO DO WITH THE CONTENT-TRANSFER AND THIS SECTION IS CREATINNG THE FRAME FOR THE ATTACHMENTS 
    part.set_payload((attachment).read())                                           #THIS IS DEFINING THE PAYLOAD OF THE EMAIL SO IN THIS CASE IT WILL BE THE IMAGE FROM TEH VARIABLE 'attachment'
    encoders.encode_base64(part)                                                    #HERE IT IS ENCODING THE PAYLOAD AS A BASE64 AND ALLOWS FOR THE DATA TRANSFER OF TEH IMAGE
    part.add_header('Content-Disposition',"attachment; filename= "+filename)        #ADDING TO THE HEADER OF THE EMAIL THE ACTUAL IMAGE THAT WILL BE SENT TO THE USER 

    msg.attach(part)                                                                #ATTACHING THE ATTACHMENTS FRAME THAT IS ABOVE TO THE ACTUAL EMAIL THAT WILL BE SENT
    text = msg.as_string()                                                          #CONVERTING THE MESSAGE INTO A STRING FORMAT  
    server = smtplib.SMTP('smtp.gmail.com',587)                                     #DEFING THE SERVER THAT WILL BE USED WHEN SENDING THE EMAIL - IN THIS CASE GRAND CENTRAL WILL USE THE GMAIL SERVERS
    server.starttls()                                                               #ADDING ADDITIONAL SECURITY TO THE EMAIL BY USING THE 'Transport Layer Security' WHICH WILL BASICALLY ENCRYPT THE DATA TRANSFER
    server.login(EmailUser,EmailPassword)                                           #LOGGING IN TO THE EMAIL SERVER AND ACCOUNT OF GRAND CENTRAL SO THE EMAILS CAN BE SENT

    s.close()                                                                       #CLOSING A PART OF THE SERVER 
    server.sendmail(EmailUser,EmailSend,text)                                       #SENDING THE EMAIL ALONG WITH ALL OF THE APPROPRIATE INFORMATION 
    server.quit()                                                                   #DISCONNECTING FROM THES ERVER AFTER THE EMAIL HAS BEEN SENT
    Window.destroy()                                                                #CLOSING THE GREY BACKGROUND AS THE PROGRAM HAS NOW FINISHED
    sys.exit()                                                                      #CLOSING ANY PYTHON WINDOWS THAT ARE STILL OPEN 




def PHOTO_TIME2():

    global username3                                        #GETTING THE USERNAME OF THE FAILED LOGIN

    window.destroy()                                        #CLOSING THE LOGIN WINDOW 

    cam = cv2.VideoCapture (0)                              #DEFINING WHAT THE WEBCAM WILL BE DIFINED AS  
    s, image = cam.read()                                   #ACTIVATING THE WEBCAM OF THE MACHINE IF AVALIABLE 
    image = cv2.flip(image, 1)                              #DEFINING WHAT THE IMAGE FROM THE WEBCAM WILL BE KNOW AS
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)          #DEFINING HOW THE WEBCAM WILL SEE THE FACE - IF THERE IS ONE
    faces = faceCascade.detectMultiScale(                   #DEFINING WHAT THE FACE TEMPLATE WILL BE KNOWN AS SO IT CAN MAP A BOX TO A PERSONS FACE
        gray,                                               
        scaleFactor=1.2,                                    #PARAMETERS FOR THE FACE TEMPLATE THAT WILL LOOK FOR A PERSONS FACE
        minNeighbors=5,                                     #PARAMETERS FOR THE FACE TEMPLATE THAT WILL LOOK FOR A PERSONS FACE
        minSize=(20, 20)                                    #PARAMETERS FOR THE FACE TEMPLATE THAT WILL LOOK FOR A PERSONS FACE
    )
    for (x,y,w,h) in faces:                                 
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)    #ONCE A FACE HAS BEEN FOUND WITHIN THE IMAGE IT WILL MAP A BOX AROUND THEIR FACE
        roi_gray = gray[y:y+h, x:x+w]                       #ONCE A FACE HAS BEEN FOUND WITHIN THE IMAGE IT WILL MAP A BOX AROUND THEIR FACE
        roi_color = image[y:y+h, x:x+w]                     #ONCE A FACE HAS BEEN FOUND WITHIN THE IMAGE IT WILL MAP A BOX AROUND THEIR FACE

    if s: 
        
        imwrite ("FAILED LOGIN GCv3.jpg", image)            #SAVING THE IMAGE AS 'FAILED LOGIN GCv3.jpg' SO THAT IT CAN BE EMAILED OFF TO THE USER

    mac = get_mac()                                         #DEFINING A SHORTER NAME FOR THE 'get_mac()' AS IT WILL BE REPEATED SO THE SHORTER NAME HELPS WITH THIS
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    #CONNECTING TO THE SERVERS FOR THE EMAIL TO BE SENT
    s.connect(("8.8.8.8", 80))                              #CONNECTING TO THE SERVERS FOR THE EMAIL TO BE SENT
    
    EmailUser = 'GRANDCENTRALPYTHON@gmail.com'              #EMAIL ADDRESS OF GRAND CENTRAL - DEFINING IT AS A VARIABLE
    EmailPassword = 'Python301'                             #EMAIL ADDRESS'S PASSWORD TO LOGIN - DEFINING IT AS A VARIABLE
    EmailSend = 'natdanjones@btinternet.com'                #EMAIL ADDRESS OF THE USER'S ACCOUNT THAT THE FAILED LOGIN TOOK PLACE ON - DEFINING IT AS A VARIABLE

    subject = 'FAILED LOG IN ATTEMPT'                       #DEFINING THE SUBJECT OF THE EMAIL AS A VARIABLE AS IT WILL BE CALLED LATER ON 

    msg = MIMEMultipart()                                   #DEFINING A SHORTER NAME FOR THE PART OF CODE THAT ALLOWS EMAILS TO BE WRITTEN - SO IT CAN BE REPEATED 
    msg['From'] = EmailUser                                 #ASIGNING THE VARIABLE OF GRAND CENTRAL'S EMAIL ADDRESS TO FORM THE 'From' PART OF THE EMAIL SO IT KNOWS WHO IT IS GOING FROM
    msg['To'] = EmailSend                                   #ASIGNING THE VARIABLE OF USER'S EMAIL ADDRESS TO FORM THE 'To' PART OF THE EMAIL SO IT KNOWS WHO IT IS GOING TO
    msg['Subject'] = subject                                #ASIGNING THE VARIABLE OF THE SUBJECT OF THE EMAIL TO FORM THE 'Subject' PART OF THE EMAIL SO THE RECIEVER KNOWS WHAT THE EMAIL IS ABOUT



  
    body = (('''
IMPORTANT INFORMATION REGARDING YOUR ACCOUNT OF ''')+str(username3)+str('''

THE FILE ATTACHED IS THE PERSON WHO JUST TRIED TO GAIN ACCESS TO GRAND CENTRAL!

TIME OF FAILED LOGIN: ''')+str(datetime.datetime.now())+str('''

IP ADDRESS OF FAILED LOGIN: '''+str(s.getsockname()[0]))+str('''

MAC ADDRESS OF FAILED LOGIN: ''')+str(mac)+str('''

_________________________________________________________________________________________________
   THIS MESSAGE IS AUTOMATICALLY GENERATED WHEN SOMEONE TRIES TO GAIN ACCESS TO GRAND CENTRAL!
PLEASE DO NOT RESPOND TO THIS MESSAGE AS IT IS AUTOMATICALLY GENERATED AND WILL NOT RESPOND BACK!
                                All Rights Reserved 2018
                                    

© GRAND CENRTRAL 2018
NATHAN JONES
                                    
 
'''))                                                                               #THE SECTION ABOVE IS THE TEMPLATE FOR THE EMAIL THAT THE USER WILL RECIEVE IF THEIR ACCOUNT HAS A FAILED LOGIN ATTEMPT,
                                                                                    #WITHIN THE EMAIL IT WILL HAVE THE USER'S NAME, TIME OF ATTEMPT, IP ADDRESS, MAC ADDRESS AND A PHOTO OF THE PERSON
    msg.attach (MIMEText(body,'plain'))                                             #THIS ALLOWS THE PROGRAM TO ATTACH THE TEMPLATE OF THE EMAIL TO THE ACTUAL EMAIL WITH ALL INFORMATION FILLED OUT

    filename='FAILED LOGIN GCv3.jpg'                                                #DEFINING THE IMAGE PATH TO BE A VARIABLE SO THAT IT CAN BE CALLED LATER ON
    attachment=open(filename,'rb')                                                  #DEFINING THE 'filename' VARIABLE TO BE OPENED AND THEN ASSIGNED AS ANOTHER VARIABLE 'attachment' SO IT CAN BE ADDED TO THE EMAIL

    part = MIMEBase('application','octet-stream')                                   #DEFININNG THE 'MIME' WHICH IS TO DO WITH THE CONTENT-TRANSFER AND THIS SECTION IS CREATINNG THE FRAME FOR THE ATTACHMENTS 
    part.set_payload((attachment).read())                                           #THIS IS DEFINING THE PAYLOAD OF THE EMAIL SO IN THIS CASE IT WILL BE THE IMAGE FROM TEH VARIABLE 'attachment'
    encoders.encode_base64(part)                                                    #HERE IT IS ENCODING THE PAYLOAD AS A BASE64 AND ALLOWS FOR THE DATA TRANSFER OF TEH IMAGE
    part.add_header('Content-Disposition',"attachment; filename= "+filename)        #ADDING TO THE HEADER OF THE EMAIL THE ACTUAL IMAGE THAT WILL BE SENT TO THE USER 

    msg.attach(part)                                                                #ATTACHING THE ATTACHMENTS FRAME THAT IS ABOVE TO THE ACTUAL EMAIL THAT WILL BE SENT
    text = msg.as_string()                                                          #CONVERTING THE MESSAGE INTO A STRING FORMAT  
    server = smtplib.SMTP('smtp.gmail.com',587)                                     #DEFING THE SERVER THAT WILL BE USED WHEN SENDING THE EMAIL - IN THIS CASE GRAND CENTRAL WILL USE THE GMAIL SERVERS
    server.starttls()                                                               #ADDING ADDITIONAL SECURITY TO THE EMAIL BY USING THE 'Transport Layer Security' WHICH WILL BASICALLY ENCRYPT THE DATA TRANSFER
    server.login(EmailUser,EmailPassword)                                           #LOGGING IN TO THE EMAIL SERVER AND ACCOUNT OF GRAND CENTRAL SO THE EMAILS CAN BE SENT

    s.close()                                                                       #CLOSING A PART OF THE SERVER 
    server.sendmail(EmailUser,EmailSend,text)                                       #SENDING THE EMAIL ALONG WITH ALL OF THE APPROPRIATE INFORMATION 
    server.quit()                                                                   #DISCONNECTING FROM THES ERVER AFTER THE EMAIL HAS BEEN SENT
    Window.destroy()                                                                #CLOSING THE GREY BACKGROUND AS THE PROGRAM HAS NOW FINISHED
    sys.exit()                                                                      #CLOSING ANY PYTHON WINDOWS THAT ARE STILL OPEN 




def PHOTO_TIME3():

    global username4                                        #GETTING THE USERNAME OF THE FAILED LOGIN

    window.destroy()                                        #CLOSING THE LOGIN WINDOW 

    cam = cv2.VideoCapture (0)                              #DEFINING WHAT THE WEBCAM WILL BE DIFINED AS  
    s, image = cam.read()                                   #ACTIVATING THE WEBCAM OF THE MACHINE IF AVALIABLE 
    image = cv2.flip(image, 1)                              #DEFINING WHAT THE IMAGE FROM THE WEBCAM WILL BE KNOW AS
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)          #DEFINING HOW THE WEBCAM WILL SEE THE FACE - IF THERE IS ONE
    faces = faceCascade.detectMultiScale(                   #DEFINING WHAT THE FACE TEMPLATE WILL BE KNOWN AS SO IT CAN MAP A BOX TO A PERSONS FACE
        gray,                                               
        scaleFactor=1.2,                                    #PARAMETERS FOR THE FACE TEMPLATE THAT WILL LOOK FOR A PERSONS FACE
        minNeighbors=5,                                     #PARAMETERS FOR THE FACE TEMPLATE THAT WILL LOOK FOR A PERSONS FACE
        minSize=(20, 20)                                    #PARAMETERS FOR THE FACE TEMPLATE THAT WILL LOOK FOR A PERSONS FACE
    )
    for (x,y,w,h) in faces:                                 
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)    #ONCE A FACE HAS BEEN FOUND WITHIN THE IMAGE IT WILL MAP A BOX AROUND THEIR FACE
        roi_gray = gray[y:y+h, x:x+w]                       #ONCE A FACE HAS BEEN FOUND WITHIN THE IMAGE IT WILL MAP A BOX AROUND THEIR FACE
        roi_color = image[y:y+h, x:x+w]                     #ONCE A FACE HAS BEEN FOUND WITHIN THE IMAGE IT WILL MAP A BOX AROUND THEIR FACE

    if s: 
        
        imwrite ("FAILED LOGIN GCv3.jpg", image)            #SAVING THE IMAGE AS 'FAILED LOGIN GCv3.jpg' SO THAT IT CAN BE EMAILED OFF TO THE USER

    mac = get_mac()                                         #DEFINING A SHORTER NAME FOR THE 'get_mac()' AS IT WILL BE REPEATED SO THE SHORTER NAME HELPS WITH THIS
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    #CONNECTING TO THE SERVERS FOR THE EMAIL TO BE SENT
    s.connect(("8.8.8.8", 80))                              #CONNECTING TO THE SERVERS FOR THE EMAIL TO BE SENT
    
    EmailUser = 'GRANDCENTRALPYTHON@gmail.com'              #EMAIL ADDRESS OF GRAND CENTRAL - DEFINING IT AS A VARIABLE
    EmailPassword = 'Python301'                             #EMAIL ADDRESS'S PASSWORD TO LOGIN - DEFINING IT AS A VARIABLE
    EmailSend = 'natdanjones@btinternet.com'                #EMAIL ADDRESS OF THE USER'S ACCOUNT THAT THE FAILED LOGIN TOOK PLACE ON - DEFINING IT AS A VARIABLE

    subject = 'FAILED LOG IN ATTEMPT'                       #DEFINING THE SUBJECT OF THE EMAIL AS A VARIABLE AS IT WILL BE CALLED LATER ON 

    msg = MIMEMultipart()                                   #DEFINING A SHORTER NAME FOR THE PART OF CODE THAT ALLOWS EMAILS TO BE WRITTEN - SO IT CAN BE REPEATED 
    msg['From'] = EmailUser                                 #ASIGNING THE VARIABLE OF GRAND CENTRAL'S EMAIL ADDRESS TO FORM THE 'From' PART OF THE EMAIL SO IT KNOWS WHO IT IS GOING FROM
    msg['To'] = EmailSend                                   #ASIGNING THE VARIABLE OF USER'S EMAIL ADDRESS TO FORM THE 'To' PART OF THE EMAIL SO IT KNOWS WHO IT IS GOING TO
    msg['Subject'] = subject                                #ASIGNING THE VARIABLE OF THE SUBJECT OF THE EMAIL TO FORM THE 'Subject' PART OF THE EMAIL SO THE RECIEVER KNOWS WHAT THE EMAIL IS ABOUT



  
    body = (('''
IMPORTANT INFORMATION REGARDING YOUR ACCOUNT OF ''')+str(username4)+str('''

THE FILE ATTACHED IS THE PERSON WHO JUST TRIED TO GAIN ACCESS TO GRAND CENTRAL!

TIME OF FAILED LOGIN: ''')+str(datetime.datetime.now())+str('''

IP ADDRESS OF FAILED LOGIN: '''+str(s.getsockname()[0]))+str('''

MAC ADDRESS OF FAILED LOGIN: ''')+str(mac)+str('''

_________________________________________________________________________________________________
   THIS MESSAGE IS AUTOMATICALLY GENERATED WHEN SOMEONE TRIES TO GAIN ACCESS TO GRAND CENTRAL!
PLEASE DO NOT RESPOND TO THIS MESSAGE AS IT IS AUTOMATICALLY GENERATED AND WILL NOT RESPOND BACK!
                                All Rights Reserved 2018
                                    

© GRAND CENRTRAL 2018
NATHAN JONES
                                    
 
'''))                                                                               #THE SECTION ABOVE IS THE TEMPLATE FOR THE EMAIL THAT THE USER WILL RECIEVE IF THEIR ACCOUNT HAS A FAILED LOGIN ATTEMPT,
                                                                                    #WITHIN THE EMAIL IT WILL HAVE THE USER'S NAME, TIME OF ATTEMPT, IP ADDRESS, MAC ADDRESS AND A PHOTO OF THE PERSON
    msg.attach (MIMEText(body,'plain'))                                             #THIS ALLOWS THE PROGRAM TO ATTACH THE TEMPLATE OF THE EMAIL TO THE ACTUAL EMAIL WITH ALL INFORMATION FILLED OUT

    filename='FAILED LOGIN GCv3.jpg'                                                #DEFINING THE IMAGE PATH TO BE A VARIABLE SO THAT IT CAN BE CALLED LATER ON
    attachment=open(filename,'rb')                                                  #DEFINING THE 'filename' VARIABLE TO BE OPENED AND THEN ASSIGNED AS ANOTHER VARIABLE 'attachment' SO IT CAN BE ADDED TO THE EMAIL

    part = MIMEBase('application','octet-stream')                                   #DEFININNG THE 'MIME' WHICH IS TO DO WITH THE CONTENT-TRANSFER AND THIS SECTION IS CREATINNG THE FRAME FOR THE ATTACHMENTS 
    part.set_payload((attachment).read())                                           #THIS IS DEFINING THE PAYLOAD OF THE EMAIL SO IN THIS CASE IT WILL BE THE IMAGE FROM TEH VARIABLE 'attachment'
    encoders.encode_base64(part)                                                    #HERE IT IS ENCODING THE PAYLOAD AS A BASE64 AND ALLOWS FOR THE DATA TRANSFER OF TEH IMAGE
    part.add_header('Content-Disposition',"attachment; filename= "+filename)        #ADDING TO THE HEADER OF THE EMAIL THE ACTUAL IMAGE THAT WILL BE SENT TO THE USER 

    msg.attach(part)                                                                #ATTACHING THE ATTACHMENTS FRAME THAT IS ABOVE TO THE ACTUAL EMAIL THAT WILL BE SENT
    text = msg.as_string()                                                          #CONVERTING THE MESSAGE INTO A STRING FORMAT  
    server = smtplib.SMTP('smtp.gmail.com',587)                                     #DEFING THE SERVER THAT WILL BE USED WHEN SENDING THE EMAIL - IN THIS CASE GRAND CENTRAL WILL USE THE GMAIL SERVERS
    server.starttls()                                                               #ADDING ADDITIONAL SECURITY TO THE EMAIL BY USING THE 'Transport Layer Security' WHICH WILL BASICALLY ENCRYPT THE DATA TRANSFER
    server.login(EmailUser,EmailPassword)                                           #LOGGING IN TO THE EMAIL SERVER AND ACCOUNT OF GRAND CENTRAL SO THE EMAILS CAN BE SENT

    s.close()                                                                       #CLOSING A PART OF THE SERVER 
    server.sendmail(EmailUser,EmailSend,text)                                       #SENDING THE EMAIL ALONG WITH ALL OF THE APPROPRIATE INFORMATION 
    server.quit()                                                                   #DISCONNECTING FROM THES ERVER AFTER THE EMAIL HAS BEEN SENT
    Window.destroy()                                                                #CLOSING THE GREY BACKGROUND AS THE PROGRAM HAS NOW FINISHED
    sys.exit()                                                                      #CLOSING ANY PYTHON WINDOWS THAT ARE STILL OPEN 





def PHOTO_TIME4():

    global username5                                        #GETTING THE USERNAME OF THE FAILED LOGIN

    window.destroy()                                        #CLOSING THE LOGIN WINDOW 

    cam = cv2.VideoCapture (0)                              #DEFINING WHAT THE WEBCAM WILL BE DIFINED AS  
    s, image = cam.read()                                   #ACTIVATING THE WEBCAM OF THE MACHINE IF AVALIABLE 
    image = cv2.flip(image, 1)                              #DEFINING WHAT THE IMAGE FROM THE WEBCAM WILL BE KNOW AS
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)          #DEFINING HOW THE WEBCAM WILL SEE THE FACE - IF THERE IS ONE
    faces = faceCascade.detectMultiScale(                   #DEFINING WHAT THE FACE TEMPLATE WILL BE KNOWN AS SO IT CAN MAP A BOX TO A PERSONS FACE
        gray,                                               
        scaleFactor=1.2,                                    #PARAMETERS FOR THE FACE TEMPLATE THAT WILL LOOK FOR A PERSONS FACE
        minNeighbors=5,                                     #PARAMETERS FOR THE FACE TEMPLATE THAT WILL LOOK FOR A PERSONS FACE
        minSize=(20, 20)                                    #PARAMETERS FOR THE FACE TEMPLATE THAT WILL LOOK FOR A PERSONS FACE
    )
    for (x,y,w,h) in faces:                                 
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)    #ONCE A FACE HAS BEEN FOUND WITHIN THE IMAGE IT WILL MAP A BOX AROUND THEIR FACE
        roi_gray = gray[y:y+h, x:x+w]                       #ONCE A FACE HAS BEEN FOUND WITHIN THE IMAGE IT WILL MAP A BOX AROUND THEIR FACE
        roi_color = image[y:y+h, x:x+w]                     #ONCE A FACE HAS BEEN FOUND WITHIN THE IMAGE IT WILL MAP A BOX AROUND THEIR FACE

    if s: 
        
        imwrite ("FAILED LOGIN GCv3.jpg", image)            #SAVING THE IMAGE AS 'FAILED LOGIN GCv3.jpg' SO THAT IT CAN BE EMAILED OFF TO THE USER

    mac = get_mac()                                         #DEFINING A SHORTER NAME FOR THE 'get_mac()' AS IT WILL BE REPEATED SO THE SHORTER NAME HELPS WITH THIS
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    #CONNECTING TO THE SERVERS FOR THE EMAIL TO BE SENT
    s.connect(("8.8.8.8", 80))                              #CONNECTING TO THE SERVERS FOR THE EMAIL TO BE SENT
    
    EmailUser = 'GRANDCENTRALPYTHON@gmail.com'              #EMAIL ADDRESS OF GRAND CENTRAL - DEFINING IT AS A VARIABLE
    EmailPassword = 'Python301'                             #EMAIL ADDRESS'S PASSWORD TO LOGIN - DEFINING IT AS A VARIABLE
    EmailSend = 'natdanjones@btinternet.com'                #EMAIL ADDRESS OF THE USER'S ACCOUNT THAT THE FAILED LOGIN TOOK PLACE ON - DEFINING IT AS A VARIABLE

    subject = 'FAILED LOG IN ATTEMPT'                       #DEFINING THE SUBJECT OF THE EMAIL AS A VARIABLE AS IT WILL BE CALLED LATER ON 

    msg = MIMEMultipart()                                   #DEFINING A SHORTER NAME FOR THE PART OF CODE THAT ALLOWS EMAILS TO BE WRITTEN - SO IT CAN BE REPEATED 
    msg['From'] = EmailUser                                 #ASIGNING THE VARIABLE OF GRAND CENTRAL'S EMAIL ADDRESS TO FORM THE 'From' PART OF THE EMAIL SO IT KNOWS WHO IT IS GOING FROM
    msg['To'] = EmailSend                                   #ASIGNING THE VARIABLE OF USER'S EMAIL ADDRESS TO FORM THE 'To' PART OF THE EMAIL SO IT KNOWS WHO IT IS GOING TO
    msg['Subject'] = subject                                #ASIGNING THE VARIABLE OF THE SUBJECT OF THE EMAIL TO FORM THE 'Subject' PART OF THE EMAIL SO THE RECIEVER KNOWS WHAT THE EMAIL IS ABOUT



  
    body = (('''
IMPORTANT INFORMATION REGARDING YOUR ACCOUNT OF ''')+str(username5)+str('''

THE FILE ATTACHED IS THE PERSON WHO JUST TRIED TO GAIN ACCESS TO GRAND CENTRAL!

TIME OF FAILED LOGIN: ''')+str(datetime.datetime.now())+str('''

IP ADDRESS OF FAILED LOGIN: '''+str(s.getsockname()[0]))+str('''

MAC ADDRESS OF FAILED LOGIN: ''')+str(mac)+str('''

_________________________________________________________________________________________________
   THIS MESSAGE IS AUTOMATICALLY GENERATED WHEN SOMEONE TRIES TO GAIN ACCESS TO GRAND CENTRAL!
PLEASE DO NOT RESPOND TO THIS MESSAGE AS IT IS AUTOMATICALLY GENERATED AND WILL NOT RESPOND BACK!
                                All Rights Reserved 2018
                                    

© GRAND CENRTRAL 2018
NATHAN JONES
                                    
 
'''))                                                                               #THE SECTION ABOVE IS THE TEMPLATE FOR THE EMAIL THAT THE USER WILL RECIEVE IF THEIR ACCOUNT HAS A FAILED LOGIN ATTEMPT,
                                                                                    #WITHIN THE EMAIL IT WILL HAVE THE USER'S NAME, TIME OF ATTEMPT, IP ADDRESS, MAC ADDRESS AND A PHOTO OF THE PERSON
    msg.attach (MIMEText(body,'plain'))                                             #THIS ALLOWS THE PROGRAM TO ATTACH THE TEMPLATE OF THE EMAIL TO THE ACTUAL EMAIL WITH ALL INFORMATION FILLED OUT

    filename='FAILED LOGIN GCv3.jpg'                                                #DEFINING THE IMAGE PATH TO BE A VARIABLE SO THAT IT CAN BE CALLED LATER ON
    attachment=open(filename,'rb')                                                  #DEFINING THE 'filename' VARIABLE TO BE OPENED AND THEN ASSIGNED AS ANOTHER VARIABLE 'attachment' SO IT CAN BE ADDED TO THE EMAIL

    part = MIMEBase('application','octet-stream')                                   #DEFININNG THE 'MIME' WHICH IS TO DO WITH THE CONTENT-TRANSFER AND THIS SECTION IS CREATINNG THE FRAME FOR THE ATTACHMENTS 
    part.set_payload((attachment).read())                                           #THIS IS DEFINING THE PAYLOAD OF THE EMAIL SO IN THIS CASE IT WILL BE THE IMAGE FROM TEH VARIABLE 'attachment'
    encoders.encode_base64(part)                                                    #HERE IT IS ENCODING THE PAYLOAD AS A BASE64 AND ALLOWS FOR THE DATA TRANSFER OF TEH IMAGE
    part.add_header('Content-Disposition',"attachment; filename= "+filename)        #ADDING TO THE HEADER OF THE EMAIL THE ACTUAL IMAGE THAT WILL BE SENT TO THE USER 

    msg.attach(part)                                                                #ATTACHING THE ATTACHMENTS FRAME THAT IS ABOVE TO THE ACTUAL EMAIL THAT WILL BE SENT
    text = msg.as_string()                                                          #CONVERTING THE MESSAGE INTO A STRING FORMAT  
    server = smtplib.SMTP('smtp.gmail.com',587)                                     #DEFING THE SERVER THAT WILL BE USED WHEN SENDING THE EMAIL - IN THIS CASE GRAND CENTRAL WILL USE THE GMAIL SERVERS
    server.starttls()                                                               #ADDING ADDITIONAL SECURITY TO THE EMAIL BY USING THE 'Transport Layer Security' WHICH WILL BASICALLY ENCRYPT THE DATA TRANSFER
    server.login(EmailUser,EmailPassword)                                           #LOGGING IN TO THE EMAIL SERVER AND ACCOUNT OF GRAND CENTRAL SO THE EMAILS CAN BE SENT

    s.close()                                                                       #CLOSING A PART OF THE SERVER 
    server.sendmail(EmailUser,EmailSend,text)                                       #SENDING THE EMAIL ALONG WITH ALL OF THE APPROPRIATE INFORMATION 
    server.quit()                                                                   #DISCONNECTING FROM THES ERVER AFTER THE EMAIL HAS BEEN SENT
    Window.destroy()                                                                #CLOSING THE GREY BACKGROUND AS THE PROGRAM HAS NOW FINISHED
    sys.exit()                                                                      #CLOSING ANY PYTHON WINDOWS THAT ARE STILL OPEN 





def PHOTO_TIME6():

    global username7                                        #GETTING THE USERNAME OF THE FAILED LOGIN

    window.destroy()                                        #CLOSING THE LOGIN WINDOW 

    cam = cv2.VideoCapture (0)                              #DEFINING WHAT THE WEBCAM WILL BE DIFINED AS  
    s, image = cam.read()                                   #ACTIVATING THE WEBCAM OF THE MACHINE IF AVALIABLE 
    image = cv2.flip(image, 1)                              #DEFINING WHAT THE IMAGE FROM THE WEBCAM WILL BE KNOW AS
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)          #DEFINING HOW THE WEBCAM WILL SEE THE FACE - IF THERE IS ONE
    faces = faceCascade.detectMultiScale(                   #DEFINING WHAT THE FACE TEMPLATE WILL BE KNOWN AS SO IT CAN MAP A BOX TO A PERSONS FACE
        gray,                                               
        scaleFactor=1.2,                                    #PARAMETERS FOR THE FACE TEMPLATE THAT WILL LOOK FOR A PERSONS FACE
        minNeighbors=5,                                     #PARAMETERS FOR THE FACE TEMPLATE THAT WILL LOOK FOR A PERSONS FACE
        minSize=(20, 20)                                    #PARAMETERS FOR THE FACE TEMPLATE THAT WILL LOOK FOR A PERSONS FACE
    )
    for (x,y,w,h) in faces:                                 
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)    #ONCE A FACE HAS BEEN FOUND WITHIN THE IMAGE IT WILL MAP A BOX AROUND THEIR FACE
        roi_gray = gray[y:y+h, x:x+w]                       #ONCE A FACE HAS BEEN FOUND WITHIN THE IMAGE IT WILL MAP A BOX AROUND THEIR FACE
        roi_color = image[y:y+h, x:x+w]                     #ONCE A FACE HAS BEEN FOUND WITHIN THE IMAGE IT WILL MAP A BOX AROUND THEIR FACE

    if s: 
        
        imwrite ("FAILED LOGIN GCv3.jpg", image)            #SAVING THE IMAGE AS 'FAILED LOGIN GCv3.jpg' SO THAT IT CAN BE EMAILED OFF TO THE USER

    mac = get_mac()                                         #DEFINING A SHORTER NAME FOR THE 'get_mac()' AS IT WILL BE REPEATED SO THE SHORTER NAME HELPS WITH THIS
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    #CONNECTING TO THE SERVERS FOR THE EMAIL TO BE SENT
    s.connect(("8.8.8.8", 80))                              #CONNECTING TO THE SERVERS FOR THE EMAIL TO BE SENT
    
    EmailUser = 'GRANDCENTRALPYTHON@gmail.com'              #EMAIL ADDRESS OF GRAND CENTRAL - DEFINING IT AS A VARIABLE
    EmailPassword = 'Python301'                             #EMAIL ADDRESS'S PASSWORD TO LOGIN - DEFINING IT AS A VARIABLE
    EmailSend = 'natdanjones@btinternet.com'                #EMAIL ADDRESS OF THE USER'S ACCOUNT THAT THE FAILED LOGIN TOOK PLACE ON - DEFINING IT AS A VARIABLE

    subject = 'FAILED LOG IN ATTEMPT'                       #DEFINING THE SUBJECT OF THE EMAIL AS A VARIABLE AS IT WILL BE CALLED LATER ON 

    msg = MIMEMultipart()                                   #DEFINING A SHORTER NAME FOR THE PART OF CODE THAT ALLOWS EMAILS TO BE WRITTEN - SO IT CAN BE REPEATED 
    msg['From'] = EmailUser                                 #ASIGNING THE VARIABLE OF GRAND CENTRAL'S EMAIL ADDRESS TO FORM THE 'From' PART OF THE EMAIL SO IT KNOWS WHO IT IS GOING FROM
    msg['To'] = EmailSend                                   #ASIGNING THE VARIABLE OF USER'S EMAIL ADDRESS TO FORM THE 'To' PART OF THE EMAIL SO IT KNOWS WHO IT IS GOING TO
    msg['Subject'] = subject                                #ASIGNING THE VARIABLE OF THE SUBJECT OF THE EMAIL TO FORM THE 'Subject' PART OF THE EMAIL SO THE RECIEVER KNOWS WHAT THE EMAIL IS ABOUT



  
    body = (('''
IMPORTANT INFORMATION REGARDING YOUR ACCOUNT OF ''')+str(username7)+str('''

THE FILE ATTACHED IS THE PERSON WHO JUST TRIED TO GAIN ACCESS TO GRAND CENTRAL!

TIME OF FAILED LOGIN: ''')+str(datetime.datetime.now())+str('''

IP ADDRESS OF FAILED LOGIN: '''+str(s.getsockname()[0]))+str('''

MAC ADDRESS OF FAILED LOGIN: ''')+str(mac)+str('''

_________________________________________________________________________________________________
   THIS MESSAGE IS AUTOMATICALLY GENERATED WHEN SOMEONE TRIES TO GAIN ACCESS TO GRAND CENTRAL!
PLEASE DO NOT RESPOND TO THIS MESSAGE AS IT IS AUTOMATICALLY GENERATED AND WILL NOT RESPOND BACK!
                                All Rights Reserved 2018
                                    

© GRAND CENRTRAL 2018
NATHAN JONES
                                    
 
'''))                                                                               #THE SECTION ABOVE IS THE TEMPLATE FOR THE EMAIL THAT THE USER WILL RECIEVE IF THEIR ACCOUNT HAS A FAILED LOGIN ATTEMPT,
                                                                                    #WITHIN THE EMAIL IT WILL HAVE THE USER'S NAME, TIME OF ATTEMPT, IP ADDRESS, MAC ADDRESS AND A PHOTO OF THE PERSON
    msg.attach (MIMEText(body,'plain'))                                             #THIS ALLOWS THE PROGRAM TO ATTACH THE TEMPLATE OF THE EMAIL TO THE ACTUAL EMAIL WITH ALL INFORMATION FILLED OUT

    filename='FAILED LOGIN GCv3.jpg'                                                #DEFINING THE IMAGE PATH TO BE A VARIABLE SO THAT IT CAN BE CALLED LATER ON
    attachment=open(filename,'rb')                                                  #DEFINING THE 'filename' VARIABLE TO BE OPENED AND THEN ASSIGNED AS ANOTHER VARIABLE 'attachment' SO IT CAN BE ADDED TO THE EMAIL

    part = MIMEBase('application','octet-stream')                                   #DEFININNG THE 'MIME' WHICH IS TO DO WITH THE CONTENT-TRANSFER AND THIS SECTION IS CREATINNG THE FRAME FOR THE ATTACHMENTS 
    part.set_payload((attachment).read())                                           #THIS IS DEFINING THE PAYLOAD OF THE EMAIL SO IN THIS CASE IT WILL BE THE IMAGE FROM TEH VARIABLE 'attachment'
    encoders.encode_base64(part)                                                    #HERE IT IS ENCODING THE PAYLOAD AS A BASE64 AND ALLOWS FOR THE DATA TRANSFER OF TEH IMAGE
    part.add_header('Content-Disposition',"attachment; filename= "+filename)        #ADDING TO THE HEADER OF THE EMAIL THE ACTUAL IMAGE THAT WILL BE SENT TO THE USER 

    msg.attach(part)                                                                #ATTACHING THE ATTACHMENTS FRAME THAT IS ABOVE TO THE ACTUAL EMAIL THAT WILL BE SENT
    text = msg.as_string()                                                          #CONVERTING THE MESSAGE INTO A STRING FORMAT  
    server = smtplib.SMTP('smtp.gmail.com',587)                                     #DEFING THE SERVER THAT WILL BE USED WHEN SENDING THE EMAIL - IN THIS CASE GRAND CENTRAL WILL USE THE GMAIL SERVERS
    server.starttls()                                                               #ADDING ADDITIONAL SECURITY TO THE EMAIL BY USING THE 'Transport Layer Security' WHICH WILL BASICALLY ENCRYPT THE DATA TRANSFER
    server.login(EmailUser,EmailPassword)                                           #LOGGING IN TO THE EMAIL SERVER AND ACCOUNT OF GRAND CENTRAL SO THE EMAILS CAN BE SENT

    s.close()                                                                       #CLOSING A PART OF THE SERVER 
    server.sendmail(EmailUser,EmailSend,text)                                       #SENDING THE EMAIL ALONG WITH ALL OF THE APPROPRIATE INFORMATION 
    server.quit()                                                                   #DISCONNECTING FROM THES ERVER AFTER THE EMAIL HAS BEEN SENT
    Window.destroy()                                                                #CLOSING THE GREY BACKGROUND AS THE PROGRAM HAS NOW FINISHED
    sys.exit()                                                                      #CLOSING ANY PYTHON WINDOWS THAT ARE STILL OPEN 



def PHOTO_TIME5():


    global username6                                        #GETTING THE USERNAME OF THE FAILED LOGIN

    window.destroy()                                        #CLOSING THE LOGIN WINDOW 

    cam = cv2.VideoCapture (0)                              #DEFINING WHAT THE WEBCAM WILL BE DIFINED AS  
    s, image = cam.read()                                   #ACTIVATING THE WEBCAM OF THE MACHINE IF AVALIABLE 
    image = cv2.flip(image, 1)                              #DEFINING WHAT THE IMAGE FROM THE WEBCAM WILL BE KNOW AS
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)          #DEFINING HOW THE WEBCAM WILL SEE THE FACE - IF THERE IS ONE
    faces = faceCascade.detectMultiScale(                   #DEFINING WHAT THE FACE TEMPLATE WILL BE KNOWN AS SO IT CAN MAP A BOX TO A PERSONS FACE
        gray,                                               
        scaleFactor=1.2,                                    #PARAMETERS FOR THE FACE TEMPLATE THAT WILL LOOK FOR A PERSONS FACE
        minNeighbors=5,                                     #PARAMETERS FOR THE FACE TEMPLATE THAT WILL LOOK FOR A PERSONS FACE
        minSize=(20, 20)                                    #PARAMETERS FOR THE FACE TEMPLATE THAT WILL LOOK FOR A PERSONS FACE
    )
    for (x,y,w,h) in faces:                                 
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)    #ONCE A FACE HAS BEEN FOUND WITHIN THE IMAGE IT WILL MAP A BOX AROUND THEIR FACE
        roi_gray = gray[y:y+h, x:x+w]                       #ONCE A FACE HAS BEEN FOUND WITHIN THE IMAGE IT WILL MAP A BOX AROUND THEIR FACE
        roi_color = image[y:y+h, x:x+w]                     #ONCE A FACE HAS BEEN FOUND WITHIN THE IMAGE IT WILL MAP A BOX AROUND THEIR FACE

    if s: 
        
        imwrite ("FAILED LOGIN GCv3.jpg", image)            #SAVING THE IMAGE AS 'FAILED LOGIN GCv3.jpg' SO THAT IT CAN BE EMAILED OFF TO THE USER

    mac = get_mac()                                         #DEFINING A SHORTER NAME FOR THE 'get_mac()' AS IT WILL BE REPEATED SO THE SHORTER NAME HELPS WITH THIS
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    #CONNECTING TO THE SERVERS FOR THE EMAIL TO BE SENT
    s.connect(("8.8.8.8", 80))                              #CONNECTING TO THE SERVERS FOR THE EMAIL TO BE SENT
    
    EmailUser = 'GRANDCENTRALPYTHON@gmail.com'              #EMAIL ADDRESS OF GRAND CENTRAL - DEFINING IT AS A VARIABLE
    EmailPassword = 'Python301'                             #EMAIL ADDRESS'S PASSWORD TO LOGIN - DEFINING IT AS A VARIABLE
    EmailSend = 'natdanjones@btinternet.com'                #EMAIL ADDRESS OF THE USER'S ACCOUNT THAT THE FAILED LOGIN TOOK PLACE ON - DEFINING IT AS A VARIABLE

    subject = 'FAILED LOG IN ATTEMPT'                       #DEFINING THE SUBJECT OF THE EMAIL AS A VARIABLE AS IT WILL BE CALLED LATER ON 

    msg = MIMEMultipart()                                   #DEFINING A SHORTER NAME FOR THE PART OF CODE THAT ALLOWS EMAILS TO BE WRITTEN - SO IT CAN BE REPEATED 
    msg['From'] = EmailUser                                 #ASIGNING THE VARIABLE OF GRAND CENTRAL'S EMAIL ADDRESS TO FORM THE 'From' PART OF THE EMAIL SO IT KNOWS WHO IT IS GOING FROM
    msg['To'] = EmailSend                                   #ASIGNING THE VARIABLE OF USER'S EMAIL ADDRESS TO FORM THE 'To' PART OF THE EMAIL SO IT KNOWS WHO IT IS GOING TO
    msg['Subject'] = subject                                #ASIGNING THE VARIABLE OF THE SUBJECT OF THE EMAIL TO FORM THE 'Subject' PART OF THE EMAIL SO THE RECIEVER KNOWS WHAT THE EMAIL IS ABOUT



  
    body = (('''
IMPORTANT INFORMATION REGARDING YOUR ACCOUNT OF ''')+str(username6)+str('''

THE FILE ATTACHED IS THE PERSON WHO JUST TRIED TO GAIN ACCESS TO GRAND CENTRAL!

TIME OF FAILED LOGIN: ''')+str(datetime.datetime.now())+str('''

IP ADDRESS OF FAILED LOGIN: '''+str(s.getsockname()[0]))+str('''

MAC ADDRESS OF FAILED LOGIN: ''')+str(mac)+str('''

_________________________________________________________________________________________________
   THIS MESSAGE IS AUTOMATICALLY GENERATED WHEN SOMEONE TRIES TO GAIN ACCESS TO GRAND CENTRAL!
PLEASE DO NOT RESPOND TO THIS MESSAGE AS IT IS AUTOMATICALLY GENERATED AND WILL NOT RESPOND BACK!
                                All Rights Reserved 2018
                                    

© GRAND CENRTRAL 2018
NATHAN JONES
                                    
 
'''))                                                                               #THE SECTION ABOVE IS THE TEMPLATE FOR THE EMAIL THAT THE USER WILL RECIEVE IF THEIR ACCOUNT HAS A FAILED LOGIN ATTEMPT,
                                                                                    #WITHIN THE EMAIL IT WILL HAVE THE USER'S NAME, TIME OF ATTEMPT, IP ADDRESS, MAC ADDRESS AND A PHOTO OF THE PERSON
    msg.attach (MIMEText(body,'plain'))                                             #THIS ALLOWS THE PROGRAM TO ATTACH THE TEMPLATE OF THE EMAIL TO THE ACTUAL EMAIL WITH ALL INFORMATION FILLED OUT

    filename='FAILED LOGIN GCv3.jpg'                                                #DEFINING THE IMAGE PATH TO BE A VARIABLE SO THAT IT CAN BE CALLED LATER ON
    attachment=open(filename,'rb')                                                  #DEFINING THE 'filename' VARIABLE TO BE OPENED AND THEN ASSIGNED AS ANOTHER VARIABLE 'attachment' SO IT CAN BE ADDED TO THE EMAIL

    part = MIMEBase('application','octet-stream')                                   #DEFININNG THE 'MIME' WHICH IS TO DO WITH THE CONTENT-TRANSFER AND THIS SECTION IS CREATINNG THE FRAME FOR THE ATTACHMENTS 
    part.set_payload((attachment).read())                                           #THIS IS DEFINING THE PAYLOAD OF THE EMAIL SO IN THIS CASE IT WILL BE THE IMAGE FROM TEH VARIABLE 'attachment'
    encoders.encode_base64(part)                                                    #HERE IT IS ENCODING THE PAYLOAD AS A BASE64 AND ALLOWS FOR THE DATA TRANSFER OF TEH IMAGE
    part.add_header('Content-Disposition',"attachment; filename= "+filename)        #ADDING TO THE HEADER OF THE EMAIL THE ACTUAL IMAGE THAT WILL BE SENT TO THE USER 

    msg.attach(part)                                                                #ATTACHING THE ATTACHMENTS FRAME THAT IS ABOVE TO THE ACTUAL EMAIL THAT WILL BE SENT
    text = msg.as_string()                                                          #CONVERTING THE MESSAGE INTO A STRING FORMAT  
    server = smtplib.SMTP('smtp.gmail.com',587)                                     #DEFING THE SERVER THAT WILL BE USED WHEN SENDING THE EMAIL - IN THIS CASE GRAND CENTRAL WILL USE THE GMAIL SERVERS
    server.starttls()                                                               #ADDING ADDITIONAL SECURITY TO THE EMAIL BY USING THE 'Transport Layer Security' WHICH WILL BASICALLY ENCRYPT THE DATA TRANSFER
    server.login(EmailUser,EmailPassword)                                           #LOGGING IN TO THE EMAIL SERVER AND ACCOUNT OF GRAND CENTRAL SO THE EMAILS CAN BE SENT

    s.close()                                                                       #CLOSING A PART OF THE SERVER 
    server.sendmail(EmailUser,EmailSend,text)                                       #SENDING THE EMAIL ALONG WITH ALL OF THE APPROPRIATE INFORMATION 
    server.quit()                                                                   #DISCONNECTING FROM THES ERVER AFTER THE EMAIL HAS BEEN SENT
    Window.destroy()                                                                #CLOSING THE GREY BACKGROUND AS THE PROGRAM HAS NOW FINISHED
    sys.exit()                                                                      #CLOSING ANY PYTHON WINDOWS THAT ARE STILL OPEN 

    
window.mainloop()                                                                   #CREATING A LOOP THAT WILL KEEP THE PROGRAM RUNNING UNTIL STATED OTHERWISE
