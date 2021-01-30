#TKinter Death Certificate
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

l0 = Label(window, text="",bg="AntiqueWhite2")
l0.pack()

album = ImageTk.PhotoImage(Image.open("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\albums\\DC.jpg"))

label = Label(window, image=album)
label.pack()

l2 = Label(window, text="",bg="AntiqueWhite2")
l2.pack()


l2 = Label(window, text="Ice Cube - Death Certificate",font='Helvetica 18 bold',bg="AntiqueWhite2")
l2.pack()

l1 = Label(window, text="",bg="AntiqueWhite2")
l1.pack()

l1 = Label(window, text="""Death Certificate is the second studio album by American rapper Ice Cube,
released on October 29, 1991 by Priority Records and EMI.
The album was re-released for the 25th anniversary edition
on June 9, 2017 by Interscope Records after Cube announced
signing to the label in late May 2017.
""",bg="AntiqueWhite2")
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


l2 = Label(window, text="",bg="AntiqueWhite2")
l2.pack()

def option1():
    #1
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Ice Cube\\Death Certificate\\Ice Cube - The Funeral.mp3')
    song.play()
    time.sleep(97)
    option2()
    pyglet.app.run()
    

b1 = Button(window, text="                       The Funeral                        ", command=option1)
b1.pack()

def option2():
    #2
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Ice Cube\\Death Certificate\\Ice Cube - The Wrong Nigga To Fuck Wit.mp3')
    song.play()
    time.sleep(168)
    option3()
    pyglet.app.run()
    

b1 = Button(window, text="       The Wrong Nigga To Fuck Wit       ", command=option2)
b1.pack()

def option3():
    #3
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Ice Cube\\Death Certificate\\Ice Cube - My Summer Vacation.mp3')
    song.play()
    time.sleep(236)
    option4()
    pyglet.app.run()
    

b1 = Button(window, text="              My Summer Vacation               ", command=option3)
b1.pack()

def option4():
    #4
    song = pyglet.media.load('''C:\\Users\\natda\\OneDrive\\Music\\Ice Cube\\Death Certificate\\Ice Cube - Steady Mobbin'.mp3''')
    song.play()
    time.sleep(250)
    option5()
    pyglet.app.run()
    

b1 = Button(window, text="                    Steady Mobbin'                   ", command=option4)
b1.pack()

def option5():
    #5
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Ice Cube\\Death Certificate\\Ice Cube - Robin Lench.mp3')
    song.play()
    time.sleep(73)
    option6()
    pyglet.app.run()
  
b1 = Button(window, text="                      Robin Lench                      ", command=option5)
b1.pack()

def option6():
    #6
    song = pyglet.media.load('''C:\\Users\\natda\\OneDrive\\Music\\Ice Cube\\Death Certificate\\Ice Cube - Givin' Up The Nappy Dug Out.mp3''')
    song.play()
    time.sleep(255)
    option7()
    pyglet.app.run()

b1 = Button(window, text="        Givin' Up The Nappy Dug Out     ", command=option6)
b1.pack()

def option7():
    #7
    song = pyglet.media.load('''C:\\Users\\natda\\OneDrive\\Music\\Ice Cube\\Death Certificate\\Ice Cube - Look Who's Burnin'.mp3''')
    song.play()
    time.sleep(233)
    option8()
    pyglet.app.run()

b1 = Button(window, text="              Look Who's Burnin'                 ", command=option7)
b1.pack()

def option8():
    #8
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Ice Cube\\Death Certificate\\Ice Cube - A Bird In The Hand.mp3')
    song.play()
    time.sleep(137)
    option9()
    pyglet.app.run()

b1 = Button(window, text="                 A Bird In The Hand               ", command=option8)
b1.pack()

def option9():
    #9
    song = pyglet.media.load('''C:\\Users\\natda\\OneDrive\\Music\\Ice Cube\\Death Certificate\\Ice Cube - Man's Best Friend.mp3''')
    song.play()
    time.sleep(126)
    option10()
    pyglet.app.run()

b1 = Button(window, text="                  Man's Best Friend                ", command=option9)
b1.pack()

def option10():
    #10
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Ice Cube\\Death Certificate\\Ice Cube - Alive On Arrival.mp3')
    song.play()
    time.sleep(191)
    option11()
    pyglet.app.run()

b1 = Button(window, text="                   Alive On Arrival                  ", command=option10)
b1.pack()

def option11():
    #11
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Ice Cube\\Death Certificate\\Ice Cube - Death.mp3')
    song.play()
    time.sleep(63)
    option12()
    pyglet.app.run()

b1 = Button(window, text="                          Death                            ", command=option11)
b1.pack()

def option12():
    #12
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Ice Cube\\Death Certificate\\Ice Cube - The Birth.mp3')
    song.play()
    time.sleep(81)
    option13()
    pyglet.app.run()

b1 = Button(window, text="                         The Birth                       ", command=option12)
b1.pack()

def option13():
    #13
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Ice Cube\\Death Certificate\\Ice Cube - I Wanna Kill Sam.mp3')
    song.play()
    time.sleep(202)
    option14()
    pyglet.app.run()

b1 = Button(window, text="                   I Wanna Kill Sam                ", command=option13)
b1.pack()

def option14():
    #14
    song = pyglet.media.load('''C:\\Users\\natda\\OneDrive\\Music\\Ice Cube\\Death Certificate\\Ice Cube - Horny Lil' Devil.mp3''')
    song.play()
    time.sleep(222)
    option15()
    pyglet.app.run()

b1 = Button(window, text="                  Horny Lil' Devil                    ", command=option14)
b1.pack()

def option15():
    #15
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Ice Cube\\Death Certificate\\Ice Cube - Black Korea.mp3')
    song.play()
    time.sleep(46)
    option16()
    pyglet.app.run()

b1 = Button(window, text="                      Black Korea                      ", command=option15)
b1.pack()

def option16():
    #16
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Ice Cube\\Death Certificate\\Ice Cube - True To The Game.mp3')
    song.play()
    time.sleep(250)
    option17()
    pyglet.app.run()

b1 = Button(window, text="               True To The Game                 ", command=option16)
b1.pack()
 
def option17():
    #17
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Ice Cube\\Death Certificate\\Ice Cube - Color Blind.mp3')
    song.play()
    time.sleep(269)
    option18()
    pyglet.app.run()

b1 = Button(window, text="                    Color Blind                        ", command=option17)
b1.pack()

def option18():
    #18
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Ice Cube\\Death Certificate\\Ice Cube - Doing Dumb Shit.mp3')
    song.play()
    time.sleep(225)
    option19()
    pyglet.app.run()

b1 = Button(window, text="                   Doing Dumb Shit              ", command=option18)
b1.pack()

def option19():
    #19
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Ice Cube\\Death Certificate\\Ice Cube - Us.mp3')
    song.play()
    time.sleep(223)
    option20()
    pyglet.app.run()

b1 = Button(window, text="                            Us                               ", command=option19)
b1.pack()

def option20():
    #20
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Ice Cube\\Death Certificate\\Ice Cube - No Vaseline.mp3')
    song.play()
    time.sleep(312)
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\albums\\DC.py")
    window.destroy()
    pyglet.app.run()

b1 = Button(window, text="                     No Vaseline                      ", command=option20)
b1.pack() 

l2 = Label(window, text="",bg="AntiqueWhite2")
l2.pack()

def option14():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\ALBUMmenu.py")
    window.destroy()

b15 = Button(window, text="BACK",command=option14)
b15.pack()

window.resizable(0,0)
window.resizable(width=FALSE, height=FALSE)
window.title("Death Certificate - MSTR")
window.geometry("500x970")
window.configure(background='AntiqueWhite2')




mainloop()
