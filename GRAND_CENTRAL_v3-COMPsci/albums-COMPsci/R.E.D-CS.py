#TKinter The R.E.D Album
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

l2 = Label(window, text="",bg="red")
l2.pack()


l2 = Label(window, text="The Game - The R.E.D Album",font='Helvetica 18 bold',bg="red")
l2.pack()

l1 = Label(window, text="",bg="red")
l1.pack()

l1 = Label(window, text="""The R.E.D. Album is the fourth studio album by American rapper Game.
It was released on August 23, 2011, by DGC Records,
which serves as Game's first release with DGC, a division label under Interscope Records.
""",bg="red")
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

l2 = Label(window, text="",bg="red")
l2.pack()

def option1():
    #1
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Dr. Dre - Dr. Dre Intro.mp3')
    song.play()
    time.sleep(25)
    option2()
    pyglet.app.run()
    

b1 = Button(window, text="                       Dr. Dre Intro                        ", command=option1)
b1.pack()

def option2():
    #2
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Game - The City (feat. Kendrick Lamar).mp3')
    song.play()
    time.sleep(342)
    option3()
    pyglet.app.run()
    

b1 = Button(window, text="                          The City                           ", command=option2)
b1.pack()

def option3():
    #3
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Game - Drug Test (feat. Dr. Dre, Snoop Dogg & Sly).mp3')
    song.play()
    time.sleep(167)
    option4()
    pyglet.app.run()
    

b1 = Button(window, text="                       Drug Test                           ", command=option3)
b1.pack()

def option4():
    #4
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Game - Martians Vs Goblins (feat. Lil Wayne & Tyler, The Creator).mp3')
    song.play()
    time.sleep(229)
    option5()
    pyglet.app.run()
    

b1 = Button(window, text="              Martians Vs Goblins                   ", command=option4)
b1.pack()

def option5():
    #5
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Game - Red Nation (feat. Lil Wayne).mp3')
    song.play()
    time.sleep(230)
    option6()
    pyglet.app.run()
  
b1 = Button(window, text="                        Red Nation                        ", command=option5)
b1.pack()

def option6():
    #6
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Dr. Dre - Dr. Dre 1.mp3')
    song.play()
    time.sleep(25)
    option7()
    pyglet.app.run()

b1 = Button(window, text="                          Dr. Dre 1                           ", command=option6)
b1.pack()

def option7():
    #7
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Game - Good Girls Go Bad (feat. Drake).mp3')
    song.play()
    time.sleep()
    option8(279)
    pyglet.app.run()

b1 = Button(window, text="               Good Girls Go Bad                     ", command=option7)
b1.pack()

def option8():
    #8
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Game - Ricky.mp3')
    song.play()
    time.sleep(248)
    option9()
    pyglet.app.run()

b1 = Button(window, text="                               Ricky                            ", command=option8)
b1.pack()

def option9():
    #9
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Game - The Good, The Bad, The Ugly.mp3')
    song.play()
    time.sleep(149)
    option10()
    pyglet.app.run()

b1 = Button(window, text="          The Good, The Bad, The Ugly       ", command=option1)
b1.pack()

def option10():
    #10
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Game - Heavy Artillery (feat. Rick Ross & Beanie Sigel).mp3')
    song.play()
    time.sleep(255)
    option11()
    pyglet.app.run()

b1 = Button(window, text="                        Heavy Artillery                   ", command=option10)
b1.pack()

def option11():
    #11
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Game - Paramedics (feat. Young Jeezy).mp3')
    song.play()
    time.sleep(297)
    option12()
    pyglet.app.run()

b1 = Button(window, text="                       Paramedics                         ", command=option11)
b1.pack()

def option12():
    #12
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Game - Speakers On Blast (feat. Big Boi & E-40).mp3')
    song.play()
    time.sleep(312)
    option13()
    pyglet.app.run()

b1 = Button(window, text="                    Speakers On Blast                 ", command=option12)
b1.pack()

def option13():
    #13
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Game - Hello (feat. Lloyd).mp3')
    song.play()
    time.sleep(230)
    option14()
    pyglet.app.run()

b1 = Button(window, text="                    Hello (feat. Lloyd)                 ", command=option13)
b1.pack()

def option14():
    #14
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Game - All The Way Gone (feat. Mario & Wale).mp3')
    song.play()
    time.sleep(248)
    option15()
    pyglet.app.run()

b1 = Button(window, text="All The Way Gone (feat. Mario & Wale)", command=option14)
b1.pack()

def option15():
    #15
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Game - Pot Of Gold (feat. Chris Brown).mp3')
    song.play()
    time.sleep(202)
    option16()
    pyglet.app.run()

b1 = Button(window, text="       Pot Of Gold (feat. Chris Brown)      ", command=option15)
b1.pack()

def option16():
    #16
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Dr. Dre - Dr. Dre 2.mp3')
    song.play()
    time.sleep(25)
    option17()
    pyglet.app.run()

b1 = Button(window, text="                          Dr. Dre 2                          ", command=option16)
b1.pack()
 
def option17():
    #17
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Game - All I Know.mp3')
    song.play()
    time.sleep(244)
    option18()
    pyglet.app.run()

b1 = Button(window, text="                         All I Know                        ", command=option17)
b1.pack()

def option18():
    #18
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Game - Born In The Trap.mp3')
    song.play()
    time.sleep(227)
    option19()
    pyglet.app.run()

b1 = Button(window, text="                    Born In The Trap                 ", command=option18)
b1.pack()

def option19():
    #19
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Game - Mama Knows (feat. Nelly Furtado).mp3')
    song.play()
    time.sleep(233)
    option20()
    pyglet.app.run()

b1 = Button(window, text="   Mama Knows (feat. Nelly Furtado)   ", command=option19)
b1.pack()

def option20():
    #20
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Game - California Dream.mp3')
    song.play()
    time.sleep(373)
    option21()
    pyglet.app.run()

b1 = Button(window, text="                  Califonia Dream                    ", command=option20)
b1.pack()

def option21():
    #21
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Dr. Dre - Dr. Dre Outro.mp3')
    song.play()
    time.sleep(31)
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\albums\\R.E.D.py")
    window.destroy()
    pyglet.app.run()

b1 = Button(window, text="                     Dr. Dre Outro                      ", command=option21)
b1.pack() 

l2 = Label(window, text="",bg="red")
l2.pack()

def option14():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-COMPsci\\ALBUMmenu-CS.py")
    window.destroy()

b15 = Button(window, text="BACK",command=option14)
b15.pack()

window.resizable(0,0)
window.resizable(width=FALSE, height=FALSE)
window.title("The R.E.D Album - COMPsci")
window.geometry("500x800")
window.configure(background='red')




mainloop()
