#TKinter Post Traumatic 
#2018
#Nathan Jones

from tkinter import messagebox, Label, Button, FALSE, Tk, Entry
from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime
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

l0 = Label(window, text="",bg="lemonchiffon3")
l0.pack()

album = ImageTk.PhotoImage(Image.open("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\GENRES\\albums - I\\PT.jpg"))

label = Label(window, image=album)
label.pack()

l2 = Label(window, text="",bg="lemonchiffon3")
l2.pack()


l2 = Label(window, text="Mike Shinoda - Post Traumatic", font='Helvetica 18 bold',bg="lemonchiffon3")
l2.pack()

l1 = Label(window, text="",bg="lemonchiffon3")
l1.pack()

l1 = Label(window, text="""Post Traumatic is the debut solo studio album by Linkin Park vocalist Mike Shinoda.
It was released on June 15, 2018. The album was announced on March 29, 2018,
along with the release of two new songs to promote the album,
"Crossing a Line" and "Nothing Makes Sense Anymore".
""",bg="lemonchiffon3")
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

l2 = Label(window, text="",bg="lemonchiffon3")
l2.pack()

def option1():
    #1
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Mike Shinoda\\Post Traumatic\\Mike Shinoda - Place To Start.mp3')
    song.play()
    time.sleep(133)
    option2()
    pyglet.app.run()
    

b1 = Button(window, text="                                   Place To Start                                     ", command=option1)
b1.pack()

def option2():
    #2
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Mike Shinoda\\Post Traumatic\\Mike Shinoda - Over Again.mp3')
    song.play()
    time.sleep(231)
    option3()
    pyglet.app.run()
    

b1 = Button(window, text="                                      Over Again                                      ", command=option2)
b1.pack()

def option3():
    #3
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Mike Shinoda\\Post Traumatic\\Mike Shinoda - Watching As I Fall.mp3')
    song.play()
    time.sleep(211)
    option4()
    pyglet.app.run()
    

b1 = Button(window, text="                                Watching As I Fall                                ", command=option3)
b1.pack()

def option4():
    #4
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Mike Shinoda\\Post Traumatic\\Mike Shinoda - Nothing Makes Sense Anymore.mp3')
    song.play()
    time.sleep(215)
    option5()
    pyglet.app.run()
    

b1 = Button(window, text="                   Nothing Makes Sense Anymore                     ", command=option4)
b1.pack()

def option5():
    #5
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Mike Shinoda\\Post Traumatic\\Mike Shinoda - About You (feat. blackbear).mp3')
    song.play()
    time.sleep(206)
    option6()
    pyglet.app.run()
  
b1 = Button(window, text="                     About You (Feat. Blackbear)                         ", command=option5)
b1.pack()

def option6():
    #6
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Mike Shinoda\\Post Traumatic\\Mike Shinoda - Brooding (Instrumental).mp3')
    song.play()
    time.sleep(152)
    option7()
    pyglet.app.run()

b1 = Button(window, text="                          Brooding (Instrumental)                           ", command=option6)
b1.pack()

def option7():
    #7
    song = pyglet.media.load('''C:\\Users\\natda\\OneDrive\\Music\\Mike Shinoda\\Post Traumatic\\Mike Shinoda - Promises I Can't Keep.mp3''')
    song.play()
    time.sleep(203)
    option8()
    pyglet.app.run()

b1 = Button(window, text="                              Promises I Can't Keep                           ", command=option7)
b1.pack()

def option8():
    #8
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Mike Shinoda\\Post Traumatic\\Mike Shinoda - Crossing A Line.mp3')
    song.play()
    time.sleep(243)
    option9()
    pyglet.app.run()

b1 = Button(window, text="                                 Crossing A Line                                   ", command=option8)
b1.pack()

def option9():
    #9
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Mike Shinoda\\Post Traumatic\\Mike Shinoda - Hold It Together.mp3')
    song.play()
    time.sleep(205)
    option10()
    pyglet.app.run()

b1 = Button(window, text="                                   Hold It Together                               ", command=option9)
b1.pack()

def option10():
    #10
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Mike Shinoda\\Post Traumatic\\Mike Shinoda - Ghosts.mp3')
    song.play()
    time.sleep(175)
    option11()
    pyglet.app.run()
 
b1 = Button(window, text="                                          Ghosts                                         ", command=option10)
b1.pack()

def option11():
    #11
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Mike Shinoda\\Post Traumatic\\Mike Shinoda - Make It Up As I Go (feat. K.Flay).mp3')
    song.play()
    time.sleep(210)
    option12()
    pyglet.app.run()

b1 = Button(window, text="                    Make It Up As I Go (Feat. K.Flay)                   ", command=option11)
b1.pack()

def option12():
    #12
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Mike Shinoda\\Post Traumatic\\Mike Shinoda - Lift Off (feat. Chino Moreno and Machine Gun Kelly).mp3')
    song.play()
    time.sleep(240)
    option13()
    pyglet.app.run()

b1 = Button(window, text="   Lift Off (Feat. Chino Moreno & Machine Gun Kelly)  ", command=option12)
b1.pack()

def option13():
    #13
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Mike Shinoda\\Post Traumatic\\Mike Shinoda - I.O.U..mp3')
    song.play()
    time.sleep(163)
    option14()
    pyglet.app.run()

b1 = Button(window, text="                                           I.O.U.                                          ", command=option13)
b1.pack()

def option14():
    #14
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Mike Shinoda\\Post Traumatic\\Mike Shinoda - Running From My Shadow (feat. grandson).mp3')
    song.play()
    time.sleep(205)
    option15()
    pyglet.app.run()

b1 = Button(window, text="         Running From My Shadow (Feat. Grandson)        ", command=option14)
b1.pack()

def option15():
    #15
    song = pyglet.media.load('''C:\\Users\\natda\\OneDrive\\Music\\Mike Shinoda\\Post Traumatic\\Mike Shinoda - World's On Fire.mp3''')
    song.play()
    time.sleep(196)
    option16()
    pyglet.app.run()

b1 = Button(window, text="                                  World's On Fire                                 ", command=option15)
b1.pack()

def option16():
    #16
    song = pyglet.media.load('''C:\\Users\\natda\\OneDrive\\Music\\Mike Shinoda\\Post Traumatic\\Mike Shinoda - Can't Hear You Now.mp3''')
    song.play()
    time.sleep(208)
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\GENRES\\albums - I\\PT.py")
    window.destroy()
    pyglet.app.run()

b1 = Button(window, text="                             Can't Hear You Now                             ", command=option16)
b1.pack() 

l2 = Label(window, text="",bg="lemonchiffon3")
l2.pack()

def option14():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\GENRES\\INDIEmenu.py")
    window.destroy()

b15 = Button(window, text="BACK",command=option14)
b15.pack()

window.resizable(0,0)
window.resizable(width=FALSE, height=FALSE)
window.title("Post Traumatic - MSTR")
window.geometry("500x850")
window.configure(background='lemonchiffon3')




mainloop()
