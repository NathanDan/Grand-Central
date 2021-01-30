#TKinter Whatever People Say I Am, That's What I'm Not
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

l0 = Label(window, text="",bg="slategray3")
l0.pack()

#LOCATING THE ALBUM'S COVER/ARTWORK FOR THE PROGRAM TO THEN DISPLAY 
album = ImageTk.PhotoImage(Image.open("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\albums\\AMWPS.jpg"))

#THIS LABEL IS DISPLAYING THE ALBUM'S COVER/ARTWORK FOR THE USER TO SEE
label = Label(window, image=album)
label.pack()

l2 = Label(window, text="",bg="slategray3")
l2.pack()

#DISPLAYING THE ARTIST AND ALBUM NAME THAT HAS BEEN SELECTED
l2 = Label(window, text="Arctic Monkeys - Whatever People Say I Am, That's What I'm Not", font='Helvetica 12 bold',bg="slategray3")
l2.pack()

l1 = Label(window, text="",bg="slategray3")
l1.pack()

#THIS LABEL GIVES A SMALL/BREIF SUMMARY OF THE ALBUM THAT HAS BEEN LOADED 
l1 = Label(window, text="""Whatever People Say I Am, That's What I'm Not is the
debut studio album by English rock band Arctic Monkeys, released on 23 January 2006
by Domino Recording Company. The album surpassed Elastica's self-titled album to
become the fastest selling debut album in British music history
""",bg="slategray3")
l1.pack()

def donothing():
    pass

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option1():
    #1
    song = pyglet.media.load("C:\\Users\\natda\\OneDrive\\Music\\Artic Monkeys\\Whatever People Say I Am, That's What I'm Not\\Arctic Monkeys - The View from the Afternoon.mp3") #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(218) #LENGTH OF THE SONG IN SECONDS
    option2()       #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()
    

b1 = Button(window, text="                                             The View from the Afternoon                                       ", command=option1) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack() 

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option2():
    #2
    song = pyglet.media.load("C:\\Users\\natda\\OneDrive\\Music\\Artic Monkeys\\Whatever People Say I Am, That's What I'm Not\\Arctic Monkeys - I Bet You Look Good On the Dancefloor.mp3") #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(173) #LENGTH OF THE SONG IN SECONDS
    option3()       #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()
    

b1 = Button(window, text="                                     I Bet You Look Good On the Dancefloor                             ", command=option2) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option3():
    #3
    song = pyglet.media.load("C:\\Users\\natda\\OneDrive\\Music\\Artic Monkeys\\Whatever People Say I Am, That's What I'm Not\\Arctic Monkeys - Fake Tales of San Francisco.mp3") #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(177) #LENGTH OF THE SONG IN SECONDS
    option4()       #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()
    

b1 = Button(window, text="                                              Fake Tales of San Francisco                                          ", command=option3) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option4():
    #4
    song = pyglet.media.load("C:\\Users\\natda\\OneDrive\\Music\\Artic Monkeys\\Whatever People Say I Am, That's What I'm Not\\Arctic Monkeys - Dancing Shoes.mp3") #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(141) #LENGTH OF THE SONG IN SECONDS
    option5()       #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()
    

b1 = Button(window, text="                                                       Dancing Shoes                                                       ", command=option4) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option5():
    #5
    song = pyglet.media.load("C:\\Users\\natda\\OneDrive\\Music\\Artic Monkeys\\Whatever People Say I Am, That's What I'm Not\\Arctic Monkeys - You Probably Couldn't See for the Lights But You Were Staring Straight At Me.mp3") #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(130) #LENGTH OF THE SONG IN SECONDS
    option6()       #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()
  
b1 = Button(window, text="You Probably Couldn't See for the Lights But You Were Staring Straight At Me", command=option5) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option6():
    #6
    song = pyglet.media.load("C:\\Users\\natda\\OneDrive\\Music\\Artic Monkeys\\Whatever People Say I Am, That's What I'm Not\\Arctic Monkeys - Still Take You Home.mp3") #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(173) #LENGTH OF THE SONG IN SECONDS
    option7()       #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()

b1 = Button(window, text="                                                 Still Take You Home                                                   ", command=option6) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option7():
    #7
    song = pyglet.media.load("C:\\Users\\natda\\OneDrive\\Music\\Artic Monkeys\\Whatever People Say I Am, That's What I'm Not\\Arctic Monkeys - Riot Van.mp3") #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(134) #LENGTH OF THE SONG IN SECONDS
    option8()       #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()

b1 = Button(window, text="                                                          Riot Van                                                               ", command=option7) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option8():
    #8
    song = pyglet.media.load("C:\\Users\\natda\\OneDrive\\Music\\Artic Monkeys\\Whatever People Say I Am, That's What I'm Not\\Arctic Monkeys - Red Light Indicates Doors Are Secured.mp3") #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(143) #LENGTH OF THE SONG IN SECONDS
    option9()       #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()

b1 = Button(window, text="                                   Red Light Indicates Doors Are Secured                                  ", command=option8) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option9():
    #9
    song = pyglet.media.load("C:\\Users\\natda\\OneDrive\\Music\\Artic Monkeys\\Whatever People Say I Am, That's What I'm Not\\Arctic Monkeys - Mardy Bum.mp3")#DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(175) #LENGTH OF THE SONG IN SECONDS
    option10()      #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()

b1 = Button(window, text="                                                       Mardy Bum                                                            ", command=option9) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TOV
def option10():
    #10
    song = pyglet.media.load("C:\\Users\\natda\\OneDrive\\Music\\Artic Monkeys\\Whatever People Say I Am, That's What I'm Not\\Arctic Monkeys - Perhaps Vampires Is a Bit Strong But….mp3") #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(268) #LENGTH OF THE SONG IN SECONDS
    option12()      #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()

b1 = Button(window, text="                                  Perhaps Vampires Is a Bit Strong But…                                   ", command=option10) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option11():
    #11
    song = pyglet.media.load("C:\\Users\\natda\\OneDrive\\Music\\Artic Monkeys\\Whatever People Say I Am, That's What I'm Not\\Arctic Monkeys - When the Sun Goes Down.mp3") #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(200) #LENGTH OF THE SONG IN SECONDS
    option13()      #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()

b1 = Button(window, text="                                           When the Sun Goes Down                                               ", command=option11) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option12():
    #12
    song = pyglet.media.load("C:\\Users\\natda\\OneDrive\\Music\\Artic Monkeys\\Whatever People Say I Am, That's What I'm Not\\Arctic Monkeys - From the Ritz to the Rubble.mp3") #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(193) #LENGTH OF THE SONG IN SECONDS
    option14()      #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()

b1 = Button(window, text="                                             From the Ritz to the Rubble                                           ", command=option12) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option13():
    #13
    song = pyglet.media.load("C:\\Users\\natda\\OneDrive\\Music\\Artic Monkeys\\Whatever People Say I Am, That's What I'm Not\\Arctic Monkeys - A Certain Romance.mp3") #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(331) #LENGTH OF THE SONG IN SECONDS
    option14()      #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()

b1 = Button(window, text="                                                   A Certain Romance                                                   ", command=option13) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

l2 = Label(window, text="",bg="slategray3")
l2.pack()

#CREATING A BACK BUTTON SO THAT THE CLIENT/USER CAN RETURN BACK TO THE ALBUM PAGE 
def option14():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\ALBUMmenu.py")
    window.destroy() #CLOSES THE CURRENT WINDOW THAT IS OPEN

b15 = Button(window, text="BACK",command=option14) #CREATING THE BACK BUTTON
b15.pack() #DISPLAYING THE BACK BUTTON

#DEFINING THE PROPERTIES AND CHARACTERISTICS OF THE WINDOW
window.resizable(0,0)
window.resizable(width=FALSE, height=FALSE) #MEANS THAT THE WINDOW SIZE CAN NOT BE CHANGED BY THE USER (NO FULL SCREEN)
window.title("Whatever People Say I Am, That's What I'm Not - MSTR") #GIVING A TITLE TO THE WINDOW 
window.geometry("500x780") #DEFING THE SIZE OF THE WINDOW - ALL ALBUM WINDOWS HAVE AN X-AXIS OF 500
window.configure(background="slategray3") #DEFINING THE BACKGROUND COLOUR OF THE WINDOW 

mainloop()
