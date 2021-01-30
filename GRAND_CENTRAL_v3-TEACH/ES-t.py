#Nathan Jones
#GRAND CENTRAL v3 - ES TEACH EDITION
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


def EMAILs():

    mac = get_mac()
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    
    email_user = 'GRANDCENTRALPYTHON@gmail.com'
    email_password = 'Python301'
    user = 'GRANDCENTRALPYTHON'

    print("CURRENT EMAIL USER: "+str(user))
    print(" ")
    
    email_send = input("ENTER THEIR EMAIL ADDRESS: ")
    subject = ("GRAND CENTRAL EMAIL SERVICES ")

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = input("""ENTER YOUR MESSAGE:
""")


    msg.attach(MIMEText(body,'plain'))
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)

    s.close()
    server.sendmail(email_user,email_send,text)
    server.quit()

    Q=input("Would you like to return back to the main menu? Y/N ")

    if Q == "Y" or "y":
        os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-TEACH\\TK_TEACH_v3.py")
        sys.exit()

    elif Q == "N" or "n":
        EMAILs()

    else:
        EMAILs()  


EMAILs()
