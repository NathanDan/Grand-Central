#TKinter California
#2018
#Nathan Jones

from tkinter import messagebox, Label, Button, FALSE, Tk, Entry
from tkinter import *
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
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
import pyglet

#global variables - GREETINGS



window = Tk()

l2 = Label(window, text="",bg="lightblue")
l2.pack()


l2 = Label(window, text="Blink 182 - California", font='Helvetica 18 bold',bg="lightblue")
l2.pack()

l1 = Label(window, text="",bg="lightblue")
l1.pack()

l1 = Label(window, text="""California is the seventh studio album by American rock band Blink-182,
released on July 1, 2016 through BMG. Produced by John Feldmann,
it is the first album by the band to feature vocalist/guitarist Matt Skiba,
who replaced former member Tom DeLonge.
""",bg="lightblue")
l1.pack()

def donothing():
    pass

def close_window (root): 
    root.destroy()

#CREATING VARIOUS BUTTONS FOR THE VARIOUS PROGRAMS THAT ARE WITHIN GRAND CENTRAL - WILL VARY DEPENDING ON THE USER 

def option():

    option1()

b1 = Button(window, text="PLAY ALL", command=option)
b1.pack()

l2 = Label(window, text="",bg="lightblue")
l2.pack()

def option1():
    #1
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\California\\blink-182 - Cynical.mp3')
    song.play()
    time.sleep(115)
    option2()
    pyglet.app.run()
    

b1 = Button(window, text="                          Cynical                           ", command=option1)
b1.pack()

def option2():
    #2
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\California\\blink-182 - Bored to Death.mp3')
    song.play()
    time.sleep(235)
    option3()
    pyglet.app.run()
    

b1 = Button(window, text="                   Bored To Death                    ", command=option2)
b1.pack()

def option3():
    #3
    song = pyglet.media.load('''C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\California\\blink-182 - She's out of Her Mind.mp3''')
    song.play()
    time.sleep(162)
    option4()
    pyglet.app.run()
    

b1 = Button(window, text="             She's Out Of Her Mind              ", command=option3)
b1.pack()

def option4():
    #4
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\California\\blink-182 - Los Angeles.mp3')
    song.play()
    time.sleep(183)
    option5()
    pyglet.app.run()
    

b1 = Button(window, text="                       Los Angles                         ", command=option4)
b1.pack()

def option5():
    #5
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\California\\blink-182 - Sober.mp3')
    song.play()
    time.sleep(179)
    option6()
    pyglet.app.run()
  
b1 = Button(window, text="                          Sober                               ", command=option5)
b1.pack()

def option6():
    #6
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\California\\blink-182 - Built This Pool.mp3')
    song.play()
    time.sleep(16)
    option7()
    pyglet.app.run()

b1 = Button(window, text="                     Built This Pool                     ", command=option6)
b1.pack()

def option7():
    #7
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\California\\blink-182 - No Future.mp3')
    song.play()
    time.sleep(225)
    option8()
    pyglet.app.run()

b1 = Button(window, text="                        No Future                          ", command=option7)
b1.pack()

def option8():
    #8
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\California\\blink-182 - Home Is Such a Lonely Place.mp3')
    song.play()
    time.sleep(201)
    option9()
    pyglet.app.run()

b1 = Button(window, text="        Home Is Such A Lonely Place         ", command=option8)
b1.pack()

def option9():
    #9
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\California\\blink-182 - Kings of the Weekend.mp3')
    song.play()
    time.sleep(176)
    option10()
    pyglet.app.run()

b1 = Button(window, text="                Kings Of The Weekend            ", command=option1)
b1.pack()

def option10():
    #10
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\California\\blink-182 - Teenage Satellites.mp3')
    song.play()
    time.sleep(191)
    option11()
    pyglet.app.run()

b1 = Button(window, text="                     Teenage Satellites                ", command=option10)
b1.pack()

def option11():
    #11
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\California\\blink-182 - Left Alone.mp3')
    song.play()
    time.sleep(189)
    option12()
    pyglet.app.run()

b1 = Button(window, text="                         Left Alone                          ", command=option11)
b1.pack()

def option12():
    #12
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\California\\blink-182 - Rabbit Hole.mp3')
    song.play()
    time.sleep(155)
    option13()
    pyglet.app.run()

b1 = Button(window, text="                         Rabbit Hole                       ", command=option12)
b1.pack()

def option13():
    #13
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\California\\blink-182 - San Diego.mp3')
    song.play()
    time.sleep(192)
    option14()
    pyglet.app.run()

b1 = Button(window, text="                           San Diego                        ", command=option13)
b1.pack()

def option14():
    #14
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\California\\blink-182 - The Only Thing That Matters.mp3')
    song.play()
    time.sleep(117)
    option15()
    pyglet.app.run()

b1 = Button(window, text="         The Only Thing That Matters         ", command=option14)
b1.pack()

def option15():
    #15
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\California\\blink-182 - California.mp3')
    song.play()
    time.sleep(190)
    option16()
    pyglet.app.run()

b1 = Button(window, text="                          California                         ", command=option15)
b1.pack()

def option16():
    #16
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\California\\blink-182 - Brohemian Rhapsody.mp3')
    song.play()
    time.sleep(30)
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\albums\\California.py")
    window.destroy()
    pyglet.app.run()

b1 = Button(window, text="                Brohemian Rhapsody               ", command=option16)
b1.pack() 

l2 = Label(window, text="",bg="lightblue")
l2.pack()

def option14():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-COMPsci\\ALBUMmenu-CS.py")
    window.destroy()

b15 = Button(window, text="BACK",command=option14)
b15.pack()

window.resizable(0,0)
window.resizable(width=FALSE, height=FALSE)
window.title("California - COMPsci")
window.geometry("500x800")
window.configure(background='lightblue')




mainloop()
