#TKinter GC Email Send
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
import string          #ALLOWS FOR DATA/ENTRIES TO BE RECORED AS STRINGS AND NOT INDIVIDUAL CHARACTERS 
import getpass         #WHEN CHECKING THE PASSWORD/USERNAME ALLOWS FOR A FUNCTION TO DO NOTHING AND PASS IT ON
import statistics      #ALLOWS ACCESS TO THE STATISTICS LIBARY FOR THE DATA COLLECTION AND PROCESSING
import itertools       #ALLOWS ACCESS TO ACCESS TO THE ITERATORS LIBARY FOR EFFICENT LOOPING 
import datetime        #THIS ALLOWS FOR THE CURRENT TIME TO BE IMPORTED AND DISPLAYED FOR THE USER TO SEE 
import smtplib         #THIS IS A MODULE THAT ALLOWS PYTHON TO ACCESS THE 'Simple Mail Transfer Protocol' THAT ALLOWS FOR THE TRANSMISSION OF EMAILS  
import multiprocessing #THS ALLOWS FOR MULTIPLE PROCESSES TO BE CARRIED OUT AT THE SAME TIME - IN THIS CASE RECIEVING MULTIPLE EMAILS/SCROLLING
import pyglet          #THIS IS THE MODULE THAT ALLOWS FOR THE SOUNDS/MUSIC/SONGS TO BE PLAYED

def EMAILs():

    WindowSEND = Tk()                                      #DEFINING WHAT THE WINDOW WILL BE DEFINED AS

    HEADER = Label(WindowSEND,text="GRAND CENTRAL EMAIL SERVICES OUTBOX", font='Helvetica 16 bold',background="white") #CREATING A HEADER FOR THE WINDOW 
    
    WindowSEND.resizable (0,0)                             #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
    WindowSEND.resizable (width=FALSE, height=FALSE)       #THE USER CANNOT CHANGE THE SIZE OF THE MENU
    WindowSEND.title ("GRAND CENTRAL EMAIL SEND")          #GIVING THE LOGIN WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
    WindowSEND.geometry("1000x600")                        #CONFIGURING THE FIXED SIZE OF THE WINDOW WHICH WILL ALWAYS BE THIS SIZE            
    WindowSEND.configure(background='white')               #CONFIGURING THE BACKGROUND OF THE WINDOW TO BE WHITE

    def SEND():

        SENTmail = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\EMAILsent.mp3') #THE PATH FOR THE EMAIL SENT SOUND      
        
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #ALLOWS GRAND CENTRAL TO GATHER THE CURRENT IP ADDRESS
        s.connect(("8.8.8.8", 80))                           #CONNECTS TO THE IP ADDRESS AND ESTABLISHES THE CONNECTION
         
        emailUSER = 'GRANDCENTRALPYTHON@gmail.com'           #EMAIL ADDRESS OF THE USER 
        emailPASSWORD = 'Python301'                          #PASSWORD OF THE USER'S EMAIL ADDRESS
        user = 'GRANDCENTRALPYTHON'                          #USERNAME OF THE USER'S EMAIL ADDRESS

        emailSEND = str(emailADDR.get())                     #GATHERING THE EMAIL ADDRESS OF THE PERSON THEY ARE SENDING THE EMAIL TO FROM THE ENTRY BOX  
        subject = (str(emailSUB.get()))                      #GATHERING THE EMAIL SUBJECT OF THE EMAIL FROM THE SUBJECT ENTRY BOX

        msg = MIMEMultipart()                                #DEFINING A SHORTER NAME FOR THE FUNCTION THAT WILL CREATE THE EMAIL 
        msg['From'] = emailUSER                              #TAKING THE EMAIL USER'S ADDRESS FOR THE 'From' SECTION OF THE EMAIL
        msg['To'] = emailSEND                                #TAKING THE EMAIL ADDRESS OF THE PERSON IS GOING TO FOR THE 'To' SECTION OF THE EMAIL 
        msg['Subject'] = subject                             #TAKING THE EMIAL SUBJECT FOR THE THE 'Subject' SECTION OF THE EMAIL

        body = str(emailMSG.get("1.0",'end-1c'))             #TAKING THE MESSAGE THAT HAS BEEN INPUTTED INTO THE TEXT BOX AND ASSIGNING IT TO THE BODY OF THE EMAIL

        msg.attach(MIMEText(body,'plain'))                   #TAKING ALL OF THE PARTS THAT MAKE UP THE EMIAL AND COMBING THEM TOGETHER TO FORM THE ACTUAL EMAIL
        text = msg.as_string()                               #CREATING A VARIABLE FOR THE ACTUAL TEXT PARTS OF THE MESSAGE INTO ONE VARIABLE THAT CAN BE CALLED REPEATEDLY
        server = smtplib.SMTP('smtp.gmail.com',587)          #CREATING A VARIABLE SO THAT THE PROGRAM CAN ACCESS THE SMTP AND DEFINING THE PORT THAT THE EMAILS WILL TRANSMIT FROM
        server.starttls()                                    #STARTING THE 'Transport Layer Security (Protocol)' WHICH ALLOWS FOR SECURITY WHEN TRANSMITTING THE EMAIL
        server.login(emailUSER,emailPASSWORD)                #LOGGING INTO THE EMAIL SERVER WITH THE USERS EMAIL USERNAME AND PASSWORD 

        s.close()                                            #CLOSING THE CONNECTION BETWEEN THE IP ADDRESS AND THE PROGRAM AS IT NO LONGER REQUIRES IT 
        SENTmail.play()                                      #PLAYING THE EMAIL SENT SOUND 
        WindowSEND.destroy()                                 #CLOSING THE EMAIL SEND WINDOW AS THE EMAIL SENT SOUND IS PLAYED 
        server.sendmail(emailUSER,emailSEND,text)            #SENDING THE THE EMAIL TO THE EMAIL ACCOUNT OF THE PERSON THEY SPECIFIED ALONG WITH THE EMAIL ITSELF   
        server.quit() and EMAILs()                           #CLOSING THE CONNECTION BETWEEN THE SERVER AND IN THE PROCESS OPENING A NEW EMAIL SEND WINDOW 
         
    SPACE = Label(WindowSEND, text=" ", background="white")                                #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE
        
    EMAILaddr = Label (WindowSEND, text="Enter Their Email Address:", background="white")  #CREATING A LABEL THAT WILL ACT AS A HEADER FOR THE ENTRY BOX OF THE EMAIL ADDRESS 
    emailADDR = Entry (WindowSEND, width=40, background="light grey")                      #CREATING THE ACTUAL ENTRY BOX WHERE THE USER WILL INPUT THE EMAIL ADDRESS 

    EMAILsub = Label (WindowSEND, text="Enter The Email Subject:", background="white")     #CREATING A LABEL THAT WILL ACT AS A HEADER FOR THE ENTRY BOX OF THE EMAIL SUBJECT 
    emailSUB = Entry (WindowSEND, width=40, background="light grey")                       #CREATING THE ACTUAL ENTRY BOX WHERE THE USER WILL INPUT THE SUBJECT OF THE EMAIL     

    EMAILmsg = Label (WindowSEND, text="Enter Your Message:", background="white")          #CREATING A LABEL THAT WILL ACT AS A HEADER FOR THE ENTRY BOX OF THE MAIN EMAIL BODY
    emailMSG = Text (WindowSEND,  height=23, width=90, background="light grey")            #CREATING THE ACTUAL ENTRY BOX WHERE THE USER WILL INPUT THEIR EMAIL MESSAGE     
    
    SEND = Button (WindowSEND, text="      SEND      ", fg="green", command=SEND)          #CREATING A BUTTON TO START THE SEND SEQUENCE AND CREATE THE EMAIL AND THEN SEND IT   
    space = Label(WindowSEND, text=" ", background="white")                                #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE  

    HEADER.pack()
    SPACE.pack()      #DISPLAYING A SPACE THE TOP
    EMAILaddr.pack()  #DISPLAYING THE ACTUAL HEADER LABEL
    emailADDR.pack()  #DISPLAYING THE ACTUAL ENTRY BOX
    EMAILsub.pack()   #DISPLAYING THE ACTUAL HEADER LABEL
    emailSUB.pack()   #DISPLAYING THE ACTUAL ENTRY BOX
    space.pack()      #DISPLAYING THE SPACE INBETWEEN
    EMAILmsg.pack()   #DISPLAYING THE ACTUAL HEADER LABEL
    emailMSG.pack()   #DISPLAYING THE ACTUAL ENTRY BOX
    SEND.pack()       #DISPLAYING THE BUTTON TO SEND THE EMAIL

    WindowSEND.mainloop()     

EMAILs()

