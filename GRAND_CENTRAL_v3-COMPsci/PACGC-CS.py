#CHATBOT VERSION 1 - Personal Android Chatbot (PAC) IN GC
#Nathan Jones
#August 2018

import urllib.request
import json as m_json
from uuid import getnode as get_mac


import time
import socket
import sys
import os.path
import os
import string 
import getpass
import random
import statistics
import itertools
import datetime

#Welcome/Inital Message
GREETINGS=["How's it going ","Whats Up ","What's new ","What's going on ","How's everything ","How are things ","How's life ","How's your day ","How's your day going "]

STORY=["""They are lost, but also not lost but somewhere in the world.
Most of them are small, though two are larger, one a coat and one a dog.
Of the small things, one is a certain ring, one a certain button.
They are lost from me and where I am, but they are also not gone.
They are somewhere else, and they are there to someone else, it may be.
But if not there to someone else, the ring is, still, not lost to itself, but there, only not where I am, and the button, too, there, still, only not where I am""",
""" """,]

NAME1=("Nathan ") #Test Purposes ONLY


def SCROLL():

    Scroll="\n"*70
    print(Scroll)

def SCROLL2():

    Scroll2="\n"*5
    print(Scroll2)

def SCROLL3():

    Scroll3="\n"*28
    print(Scroll3)      


def StartUP():

    mac = get_mac()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))

    print("SYSTEMS LOADING...")
    time.sleep(2)
    print("SYSTEMS ONLINE.")
    time.sleep(2)
    print(("SYSTEM IP ADDRESS: ")+str(s.getsockname()[0]))
    print(("SYSTEM MAC ADDRESS: ")+str(mac))
    time.sleep(2)
    print("Personal Android Chatbot - ACTIVATED")
    time.sleep(2)
    print("""

     ╔═╗╔═╗╔═╗
     ╠═╝╠═╣║  
     ╩  ╩ ╩╚═╝ 


""")
    MOOD()

def MOOD():
    
    MOOD=input(GREETINGS[random.randint(0,8)]+NAME1)
    if MOOD == "Good" or "good" or "Alright" or "alright" or "alot" or "Alot":
        print("Excellent To Hear Sir! ")
        STAGE1()
        
    elif MOOD == "Bad" or "bad" or "Not alot" or "not alot" :
        print("That's No Good Sir! ")
        STAGE1()

    if MOOD == "Nothing":
        ml=input("Is That A Bad Thing Sir? ")
        if ml == "No" or "NO" or "Nope" or "nope" or "Nah" or "nah":
            print("Phew, I Was Worried For A Second Sir!" or "Well I Am Glad Sir!")
            STAGE1()

        elif ml == "Yes" or "YES" or "Yeah" or "yeah" or "Unfortunatley" or "unfortunatley":
            print("I Am Sorry To Hear Sir, But You Know I Am No Good With Emotions Sir!")
            STAGE1()

    else:
        print("I Am Sorry Sir That Response Is NOT In My Directory! I Will Ask Another Question")
        MOOD()                 

def STAGE1():
    
    S1=input(["What Can I Do For You Today? ","Can I Do Anything For You Today? "][random.randint(0,1)])
    
    if S1 == "Google Something" or "google something" or "Google" or "google":
        print("Certainly Sir, Please WAIT Just A Moment Before Entering Your Search Term... ")

    if S1 == "Tell Me A Story" or "tell me a story" or "Story" or "story" or "Story Time" or "Story time" or "story time" or "Storytime" or "storytime":
        print(" ")
        print("I Thought You Would Never Ask, Sir!")
        STORYTIME()
    
    if S1 == "Info" or "info" or "INFO":
        mac = get_mac()
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))

        print(" ")
        print(("SYSTEM TIME: ")+str(datetime.datetime.now()))
        print(" ")
        print(("SYSTEM IP ADDRESS: ")+str(s.getsockname()[0]))
        print(" ")
        print(("SYSTEM MAC ADDRESS: ")+str(mac))
        print(" ")

    else:
        print("I Am Sorry Sir That Response Is NOT In My Directory! I Will Ask Another Question")
        STAGE1()

def STAGE2():

    S2=input(["What Else Can I Do For You Today? ","Can I Do Anything Else For You Today? "][random.randint(0,1)])
    
    if S2 == "Google Something" or "google something" or "Google" or "google":
        print("Certainly Sir, Please WAIT Just A Moment Before Entering Your Search Term... ")

    if S2 == "Tell Me A Story" or "tell me a story" or "Story" or "story" or "Story Time" or "Story time" or "story time" or "Storytime" or "storytime":
        print(" ")
        print("I Thought You Would Never Ask, Sir!")
        STORYTIME()

    elif S2 == "Nope" or "nope" or "Nah" or "nah" or "No" or "no":
        print("No Problem Sir I Will Leave You For Now!")
        sys.exit()

    else:
        print("I Am Sorry Sir That Response Is NOT In My Directory! I Will Ask Another Question")
        STAGE2()

def STORYTIME():
    
    print(" ")
    print(STORY[random.randint(0,1)])
    print(" ")

    N1=input("Is There Anything Else I Can Do For You, Sir? ")

    if N1 == "Yeah" or "yeah" or "Yes" or "yes" or "Sure" or "sure":
        print(" ")
        print(["Hold On A Second Please, Sir...", "One Moment Please, Sir...", "Just A Second, Sir..."][random.randint(0,2)])
        print(" ")
        time.sleep(2)
        STAGE2()

    elif N1 == "Nope" or "nope" or "Nah" or "nah" or "No" or "no":
        print("No Problem Sir I Will Leave You For Now!")
        sys.exit()
  
StartUP()

