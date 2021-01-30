#TKinter One More Light
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
"pythonw 1ML.py"

window = Tk()

l0 = Label(window, text="",bg="peach puff")
l0.pack()

album = ImageTk.PhotoImage(Image.open("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\GENRES\\albums - AR\\1ML.jpg"))

label = Label(window, image=album)
label.pack()

l2 = Label(window, text="",bg="peach puff")
l2.pack()


l2 = Label(window, text="Linkin Park - One More Light", font='Helvetica 18 bold',bg="peach puff")
l2.pack()

l1 = Label(window, text="",bg="peach puff")
l1.pack()

l1 = Label(window, text="""One More Light is the seventh studio album by American rock band Linkin Park.
It was released on May 19, 2017 through Warner Bros. and Machine Shop.
It is the last Linkin Park record produced before lead vocalist
Chester Bennington's death on July 20, 2017
""",bg="peach puff")
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

l2 = Label(window, text="",bg="peach puff")
l2.pack()

def option1():
    #1
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Linkin Park\\One More Light\\Linkin Park - Nobody Can Save Me.mp3')
    song.play()
    time.sleep(225)
    option2()
    pyglet.app.run()
    

b1 = Button(window, text="                   Nobody Can Save Me                     ", command=option1)
b1.pack()

def option2():
    #2
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Linkin Park\\One More Light\\Linkin Park - Good Goodbye (feat. Pusha T and Stormzy).mp3')
    song.play()
    time.sleep(211)
    option3()
    pyglet.app.run()
    

b1 = Button(window, text=" Good Goodbye (feat. Pusha T and Stormzy) ", command=option2)
b1.pack()

def option3():
    #3
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Linkin Park\\One More Light\\Linkin Park - Talking to Myself.mp3')
    song.play()
    time.sleep(231)
    option4()
    pyglet.app.run()
    

b1 = Button(window, text="                        Talking to Myself                       ", command=option3)
b1.pack()

def option4():
    #4
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Linkin Park\\One More Light\\Linkin Park - Battle Symphony.mp3')
    song.play()
    time.sleep(216)
    option5()
    pyglet.app.run()
    

b1 = Button(window, text="                       Battle Symphony                        ", command=option4)
b1.pack()

def option5():
    #5
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Linkin Park\\One More Light\\Linkin Park - Invisible.mp3')
    song.play()
    time.sleep(214)
    option6()
    pyglet.app.run()
  
b1 = Button(window, text="                             Invisible                                  ", command=option5)
b1.pack()

def option6():
    #6
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Linkin Park\\One More Light\\Linkin Park - Heavy (feat. Kiiara).mp3')
    song.play()
    time.sleep(169)
    option7()
    pyglet.app.run()

b1 = Button(window, text="                      Heavy (feat. Kiiara)                      ", command=option6)
b1.pack()

def option7():
    #7
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Linkin Park\\One More Light\\Linkin Park - Sorry for Now.mp3')
    song.play()
    time.sleep(203)
    option8()
    pyglet.app.run()

b1 = Button(window, text="                         Sorry for Now                            ", command=option7)
b1.pack()

def option8():
    #8
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Linkin Park\\One More Light\\Linkin Park - Halfway Right.mp3')
    song.play()
    time.sleep(217)
    option9()
    pyglet.app.run()

b1 = Button(window, text="                         Halfway Right                           ", command=option8)
b1.pack()

def option9():
    #9
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Linkin Park\\One More Light\\Linkin Park - One More Light.mp3')
    song.play()
    time.sleep(255)
    option10()
    pyglet.app.run()

b1 = Button(window, text="                        One More Light                         ", command=option9)
b1.pack()


def option10():
    #10
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Linkin Park\\One More Light\\Linkin Park - Sharp Edges.mp3')
    song.play()
    time.sleep(178)
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\GENRES\\albums - AR\\1ML.py")
    window.destroy()
    pyglet.app.run()

b1 = Button(window, text="                              Sharp Edges                         ", command=option10)
b1.pack() 

l2 = Label(window, text="",bg="peach puff")
l2.pack()

def option14():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\GENRES\\ALTERNATIVErockMENU.py")
    window.destroy()

b15 = Button(window, text="BACK",command=option14)
b15.pack()

window.resizable(0,0)
window.resizable(width=FALSE, height=FALSE)
window.title("California - MSTR")
window.geometry("500x700")
window.configure(background='peach puff')




mainloop()
