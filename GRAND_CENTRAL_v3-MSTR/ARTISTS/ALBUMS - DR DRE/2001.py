#TKinter 2001
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

window = Tk()

l0 = Label(window, text="",bg="green")
l0.pack()

album = ImageTk.PhotoImage(Image.open("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\albums\\2001.jpg"))

label = Label(window, image=album)
label.pack()

l1 = Label(window, text="",bg="green")
l1.pack()

l2 = Label(window, text="Dr. Dre - 2001", font='Helvetica 18 bold',bg="green")
l2.pack()

l1 = Label(window, text="",bg="green")
l1.pack()

l1 = Label(window, text="""2001 is the second studio album by American rapper and producer Dr. Dre.
It was released on November 16, 1999, by Interscope Records
as the follow-up to his 1992 debut album The Chronic.
""",bg="green")
l1.pack()

def donothing():
    pass

def close_window (root): 
    root.destroy()

#CREATING VARIOUS BUTTONS FOR THE SONGS WITHIN THE ALBUM

def option():

    option1()

b1 = Button(window, text="PLAY ALL", command=option)
b1.pack()

l3 = Label(window, text="",bg="GREEN")
l3.pack()

def option1():
    #1
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Dr Dre\\2001\\Dr. Dre - Lolo (Intro) (feat. Xzibit & Tray Dee).mp3')
    song.play()
    time.sleep(45)
    option2()
    pyglet.app.run()
    

b1 = Button(window, text="                     Lolo(Intro)(Feat. Xzibit & Tray Dee)                 ", command=option1)
b1.pack()

def option2():
    #2
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Dr Dre\\2001\\Dr. Dre - The Watcher.mp3')
    song.play()
    time.sleep(206)
    option3()
    pyglet.app.run()
    
  
b1 = Button(window, text="                                       The Watcher                                     ", command=option2)
b1.pack()

def option3():
    #3
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Dr Dre\\2001\\Dr. Dre - Fuck You (feat. Devin The Dude & Snoop Dogg).mp3')
    song.play()
    time.sleep(207)
    option4()
    pyglet.app.run()
    

b1 = Button(window, text="         Fuck You (Feat. Devin The Dude & Snoop Dogg)     ", command=option3)
b1.pack()

def option4():
    #4
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Dr Dre\\2001\\Dr. Dre - Still D.R.E. (feat. Snoop Dogg).mp3')
    song.play()
    time.sleep(270)
    option5()
    pyglet.app.run()
    

b1 = Button(window, text="                         Still D.R.E (Feat. Snoop Dogg)                      ", command=option4)
b1.pack()

def option5():
    #5
    song = pyglet.media.load('''C:\\Users\\natda\\OneDrive\\Music\\Dr Dre\\2001\\Dr. Dre - Big Ego's (feat. Hittman).mp3''')
    song.play()
    time.sleep(238)
    option6()
    pyglet.app.run()
  
b1 = Button(window, text="                            Big Ego's (Feat. Hittman)                           ", command=option5)
b1.pack()

def option6():
    #6
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Dr Dre\\2001\\Dr. Dre - Xxplosive (feat. Hittman, Six-Two, Nate Dogg & Kurupt).mp3')
    song.play()
    time.sleep(215)
    option7()
    pyglet.app.run()

b1 = Button(window, text="Xxplosive (Feat. Hittman, Six-Two, Nate Dogg & Kurupt)", command=option6)
b1.pack()

def option7():
    #7
    song = pyglet.media.load('''C:\\Users\\natda\\OneDrive\\Music\\Dr Dre\\2001\\Dr. Dre - What's The Difference (feat. Eminem & Xzibit).mp3''')
    song.play()
    time.sleep()
    option8(240)
    pyglet.app.run()

b1 = Button(window, text="        What's The Differnce (Feat. Eminem & Xzibit)           ", command=option7)
b1.pack()

def option8():
    #8
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Dr Dre\\2001\\Dr. Dre - Bar One (feat. Traci Nelson, Ms. Roq & Eddie Griffin).mp3')
    song.play()
    time.sleep(50)
    option9()
    pyglet.app.run()

b1 = Button(window, text="    Bar One (Feat. Traci Nelson, Ms Roq & Eddie Griffin)   ", command=option8)
b1.pack()

def option9():
    #9
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Dr Dre\\2001\\Dr. Dre - Light Speed (feat. Hittman).mp3')
    song.play()
    time.sleep(161)
    option10()
    pyglet.app.run()

b1 = Button(window, text="                          Light Speed (Feat. Hittman)                        ", command=option9)
b1.pack()

def option10():
    #10
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Dr Dre\\2001\\Dr. Dre - Forgot About Dre (feat. Eminem).mp3')
    song.play()
    time.sleep(222)
    option11()
    pyglet.app.run()

b1 = Button(window, text="                   Forgot About Dre (Feat. Eminem)                     ", command=option10)
b1.pack()

def option11():
    #11
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Dr Dre\\2001\\Dr. Dre - The Message_ Outro (feat. Mary J. Blige & Rell).mp3')
    song.play()
    time.sleep(161)
    option12()
    pyglet.app.run()

b1 = Button(window, text="                The Next Episode (Feat. Snoop Dogg)                 ", command=option11)
b1.pack()

def option12():
    #12
    song = pyglet.media.load('''C:\\Users\\natda\\OneDrive\\Music\\Dr Dre\\2001\\Dr. Dre - Let's Get High (feat. Hittman, Ms. Roq & Kurupt).mp3''')
    song.play()
    time.sleep(147)
    option13()
    pyglet.app.run()

b1 = Button(window, text="      Let's Get High (Feat. Hittman, Ms Roq & Kurupt)       ", command=option12)
b1.pack()

def option13():
    #13
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Dr Dre\\2001\\Dr. Dre - Bitch Niggaz (feat. Hittman, Six-Two & Snoop Dogg).mp3')
    song.play()
    time.sleep(253)
    option14()
    pyglet.app.run()

b1 = Button(window, text="  Bitch Niggaz (Feat. Hittman, Six-Two & Snoop Dogg)   ", command=option13)
b1.pack()

def option14():
    #14
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Dr Dre\\2001\\Dr. Dre - The Car Bomb (feat. Mel-Man & Charis Henry).mp3')
    song.play()
    time.sleep(60)
    option15()
    pyglet.app.run()

b1 = Button(window, text="        The Car Bomb (Feat. Mel-Man & Charis Henry)        ", command=option14)
b1.pack()

def option15():
    #15
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Dr Dre\\2001\\Dr. Dre - Murder Ink (feat. Hittman & Ms. Roq).mp3')
    song.play()
    time.sleep(148)
    option16()
    pyglet.app.run()

b1 = Button(window, text="                Murder Ink (Feat. Hittman & Ms Roq)                 ", command=option15)
b1.pack()

def option16():
    #16
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Dr Dre\\2001\\Dr. Dre - Ed-Ucation (feat. Hittman, Ms. Roq & Eddie Griffin).mp3')
    song.play()
    time.sleep(92)
    option17()
    pyglet.app.run()

b1 = Button(window, text="    Ed-Ucation (Feat. Hittman, Ms Roq & Eddie Griffin)     ", command=option16)
b1.pack()
 
def option17():
    #17
    song = pyglet.media.load('''C:\\Users\\natda\\OneDrive\\Music\\Dr Dre\\2001\\Dr. Dre - Some L.A. Niggaz (feat. Hittman, Ms. Roq, Knoc-Turn'al, Time Bomb, Koka Kambon, Defari, MC Ren & Xzibit).mp3''')
    song.play()
    time.sleep(266)
    option18()
    pyglet.app.run()

b1 = Button(window, text="                                    Some L.A. Niggaz                               ", command=option17)
b1.pack()

def option18():
    #18
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Dr Dre\\2001\\Dr. Dre - Pause 4 Porno (feat. Jake Steed).mp3')
    song.play()
    time.sleep(92)
    option19()
    pyglet.app.run()

b1 = Button(window, text="                      Pause 4 Porno (Feat. Jake Steed)                    ", command=option18)
b1.pack()

def option19():
    #19
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Dr Dre\\2001\\Dr. Dre - Housewife (feat. Hittman & Kurupt).mp3')
    song.play()
    time.sleep(241)
    option20()
    pyglet.app.run()

b1 = Button(window, text="                  Housewife (Feat. Hittman & Kurupt)                ", command=option19)
b1.pack()

def option20():
    #20
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Dr Dre\\2001\\Dr. Dre - Ackrite (feat. Hittman).mp3')
    song.play()
    time.sleep(219)
    option21()
    pyglet.app.run()

b1 = Button(window, text="                             Ackrite (Feat. Hittman)                            ", command=option20)
b1.pack()

def option21():
    #21
    song = pyglet.media.load('''C:\\Users\\natda\\OneDrive\\Music\\Dr Dre\\2001\\Dr. Dre - Bang Bang (feat. Hittman & Knoc-Turn'al).mp3''')
    song.play()
    time.sleep(222)
    option21()                         
    pyglet.app.run()

b1 = Button(window, text="            Bang Bang (Feat. Hittman & Knoc-Turn'al)          ", command=option21)
b1.pack()

def option22():
    #22
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Dr Dre\\2001\\Dr. Dre - The Message_ Outro (feat. Mary J. Blige & Rell).mp3')
    song.play()
    time.sleep(330)
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\ARTISTS\\ALBUMS - DR DRE\\2001.py")
    window.destroy()
    pyglet.app.run()

b1 = Button(window, text="        The Message/ Outro (Feat. Mary J. Blige & Rell)       ", command=option21)
b1.pack() 

l2 = Label(window, text="",bg="green")
l2.pack()

def option14():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\ARTISTS\\DrDre.py")
    window.destroy()

#def optionP():

 #   player.pause()

b15 = Button(window, text="BACK",command=option14)
b15.pack()

window.resizable(0,0)
window.resizable(width=FALSE, height=FALSE)
window.title("2001 - MSTR")
#menubar = Menu(window)
#menubar.add_cascade(label="Pause", command=optionP)
#window.config(menu=menubar)
window.geometry("500x1000")
window.configure(background='green')


mainloop()
