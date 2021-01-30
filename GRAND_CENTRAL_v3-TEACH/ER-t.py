#Nathan Jones
#GRAND CENTRAL v3 - ER TEACH EDITION
#2018

from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from uuid import getnode as get_mac

import easyimap
import socket
import smtplib
import multiprocessing
import time
import sys
import os.path
import os
import string 
import getpass
import random
import statistics
import itertools
import datetime

def SCROLL():

    Scroll="\n"*70
    print(Scroll)

def SCROLL2():

    Scroll2="\n"*10
    print(Scroll2)

def SCROLL3():

    Scroll3="\n"*28
    print(Scroll3)      



def EMAILr():
    login = 'grandcentralpython@gmail.com'
    password = 'Python301'

    imapper = easyimap.connect('imap.gmail.com', login, password)
    for mail_id in imapper.listids(limit=3):
        mail = imapper.mail(mail_id)
        print(mail.from_addr)
        print(" ")
        print(" ")
        print(mail.title)
        print(" ")
        print(mail.body)
        print(" ")
        

    time.sleep(10)
    SCROLL2()
    
    Q=input("Would you like to return back to the main menu? Y/N ")

    if Q == "Y" or "y":
         os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-TEACH\\TK_TEACH_v3.py")
         sys.exit()

    elif Q == "N" or "n":
        EMAILr()

    else:
        EMAILr()

EMAILr()
