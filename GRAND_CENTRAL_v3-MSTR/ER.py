#TKinter GC Email Recieve
#2019
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

import time            #THIS ALLOWS FOR THE PROGRAM TO USE THE SLEEP FUNCTION WITHIN THE PROGRAM
import socket          #ALLOWS FOR THE PROGRAM TO GATHER IP AND MAC ADDRESSES
import sys             #ALLOWS ACCESS TO THE SYSTEM FROM WITHIN PYTHON 
import os.path         #ALLOWS THE PROGRAM TO OPEN OTHER SPECIFIC APPLICATIONS, IN THIS CASE THE GC PROGRAMS 
import os              #ALLOWS FOR CONTROL OF THE MACHINE AND IS OS INCLUDING THE LIKES OF SAVING, OPENING/CLOSING FILES, ETC. 
import string          #ALLOWS FOR DATA/ENTRIES TO BE RECOREDAS STRINGS AND NOT INDIVIDUAL CHARACTERS 
import getpass         #WHEN CHECKING THE PASSWORD/USERNAME ALLOWS FOR A FUNCTION TO DO NOTHING AND PASS IT ON
import random          #THIS IMPORT ALLOWS FOR WORDS TO BE RANDOMLY SELECTED 
import statistics      #ALLOWS ACCESS TO THE STATISTICS LIBARY FOR THE DATA COLLECTION AND PROCESSING
import itertools       #ALLOWS ACCESS TO ACCESS TO THE ITERATORS LIBARY FOR EFFICENT LOOPING 
import datetime        #THIS ALLOWS FOR THE CURRENT TIME TO BE IMPORTED AND DISPLAYED FOR THE USER TO SEE 
import easyimap        #THIS IS A MODULE THAT ALLOWS PYTHON TO ACCESS THE 'Internet Message Access Protocol' THAT ALLOWS ACCESSING EMAILS 
import multiprocessing #THS ALLOWS FOR MULTIPLE PROCESSES TO BE CARRIED OUT AT THE SAME TIME - IN THIS CASE RECIEVING MULTIPLE EMAILS/SCROLLING
import pyglet          #THIS IS THE MODULE THAT ALLOWS FOR THE SOUNDS/MUSIC/SONGS TO BE PLAYED 

WindowRECV = Tk()                     #DEFINING WHAT THE WINDOW WILL BE DEFINED AS
 
scrollbarY = Scrollbar(WindowRECV)    #DEFING THE SCROLLBAR THAT WILL ASSIGNED TO THE WINDOW 
scrollbarY.pack(side=RIGHT, fill=Y)   #TELLING THE PROGRAM WHERE TO PLACE THE SCROLLBAR

HEADER = Label(WindowRECV,text="GRAND CENTRAL EMAIL SERVICES INBOX", font='Helvetica 16 bold',background="white") #CREATING A HEADER FOR THE WINDOW 

WindowRECV.resizable (0,0)                              #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
WindowRECV.resizable (width=FALSE, height=FALSE)        #THE USER CANNOT CHANGE THE SIZE OF THE MENU
WindowRECV.title ("GRAND CENTRAL EMAIL SERVICES INBOX") #GIVING THE WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
WindowRECV.geometry("1200x800")                         #CONFIGURING THE FIXED SIZE OF THE WINDOW WHICH WILL ALWAYS BE THIS SIZE            
WindowRECV.configure(background='white')                #CONFIGURING THE BACKGROUND OF THE WINDOW TO BE WHITE
    
def RECIEVE():

    login = 'grandcentralpython@gmail.com'              #USERNAME OF THE USER'S EMAIL ADDRESS
    password = 'Python301'                              #PASSWORD OF THE USER'S EMAIL ADDRESS

    imapper = easyimap.connect('imap.gmail.com', login, password) #TAKING THE USENAME AND PASSWORD FROM ABOVE AND IS USING THIS TO CONNECT TO THE GMAIL SERVERS
    for mail_id in imapper.listids(limit=5):                      #LIMITING THE PROGRAM TO ONLY DISPLAYING THE 5 MOST RECENT EMAILS 
        mail = imapper.mail(mail_id)                              #DEFINING A SHORTER NAME FOR EMAIL COLLECTOR AS IT WILL BE REPEATED A FEW TIMES - MAKES IT MORE EFFICIENT 
                                                        
        emailSENDER = Text(WindowRECV, height=1, width=800, background="light grey", wrap=WORD, yscrollcommand=scrollbarY.set) #CREATING A TEXT BOX THAT WILL HOLD THE SENDER'S ADDRESS            
        emailTITLE = Text(WindowRECV, height=1, width=800, background="light grey", wrap=WORD, yscrollcommand=scrollbarY.set)  #CREATING A TEXT BOX THAT WILL HOLD THE SUBJECT OF THE EMAIL 
        emailMSG = Text(WindowRECV, height=7, width=800, background="white", wrap=WORD, yscrollcommand=scrollbarY.set)         #CREATING A TEXT BOX THAT WILL HOLD THE BODY OF THE EMAIL

        NEWmail = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\EMAILnew.mp3') #THE PATH THAT HOLDS THE NEW EMAIL SOUND
         
        emailSENDER.insert(END, str(mail.from_addr)) #INSERTING THE SENDER'S ADDRESS INTO IT'S TEXT BOX
        emailTITLE.insert(END, str(mail.title))      #INSERTING THE SUBJECT OF THE EMAIL INTO IT'S TEXT BOX
        emailMSG.insert(END, str(mail.body))         #INSERTING THE MAIN BODY OF THE EMAIL INTO IT'S TEXT BOX
        HEADER.pack()                                #DISPLAYING THE HEADER AT THE TOP OF THE WINDOW 
        emailSENDER.pack()                           #DISPLAYING THE SENDER'S ADDRESS TEXT BOX 
        emailTITLE.pack()                            #DISPLAYING THE SUBJECT OF THE EMAIL TEXT BOX
        emailMSG.pack()                              #DISPLAYING THE MAIN BODY OF THE EMAIL TEXT BOX
        scrollbarY.config(command=emailSENDER.yview) #ASSIGING THE SCROLLBAR TO WORK WITH THE SENDER'S ADDRESS TEXT BOX IF ALL OF THE TEXT DOES NOT FIT IN THE BOX AS IS 
        scrollbarY.config(command=emailTITLE.yview)  #ASSIGING THE SCROLLBAR TO WORK WITH THE EMAIL SUBJECT TEXT BOX IF ALL OF THE TEXT DOES NOT FIT IN THE BOX AS IS 
        scrollbarY.config(command=emailMSG.yview)    #ASSIGING THE SCROLLBAR TO WORK WITH THE MAIN BODY OF THE EMAIL TEXT BOX IF ALL OF THE TEXT DOES NOT FIT IN THE BOX AS IS 
    NEWmail.play()                                   #PLAYING THE NEW EMAIL SOUND AFTER ALL 5 EMAILS HAVE BEEN LOADED 
RECIEVE()        
WindowRECV.mainloop()

