#TKinter Whatever People Say I Am, That's What I'm Not
#2018
#Nathan Jones

from tkinter import messagebox, Label, Button, FALSE, Tk, Entry    #ALLOWING FOR TKINTER TO BE ACCESSED/UTILISED FOR THE PROGRAM TO USE ALL OF ITS FUNCTIONS AND GIVING THE PROGRAM A GUI                                           
from tkinter import *                                              #ALLOWING FOR ALL OF TKINTER'S MODULES TO BE IMPORTED 
from PIL import Image, ImageTk                                     #ALLOWING FOR IMAGES TO ADDED IN THE GUI FOR THE LIKES OF THE BACKGROUNDS AND OTHER IMAGES
from datetime import datetime                                      #ALLOWING THE DATE AND TIME TO BE DISPLAYED 
from uuid import getnode as get_mac                                #ALLOWS FOR TO ACCESS THE MODULES THAT ALLOW DIRECT ACCESS TO THE MAC ADDRESS OF THE MACHINE

import time        #THIS ALLOWS FOR THE PROGRAM TO USE THE SLEEP FUNCTION WITHIN THE PROGRAM
import socket      #ALLOWS FOR THE PROGRAM TO GATHER IP AND MAC ADDRESSES
import sys         #ALLOWS ACCESS TO THE SYSTEM FROM WITHIN PYTHON 
import os.path     #ALLOWS THE PROGRAM TO OPEN OTHER SPECIFIC APPLICATIONS, IN THIS CASE THE GC PROGRAMS 
import os          #ALLOWS FOR CONTROL OF THE MACHINE AND IS OS INCLUDING THE LIKES OF SAVING, OPENING/CLOSING FILES, ETC. 
import string      #ALLOWS FOR DATA/ENTRIES TO BE RECOREDAS STRINGS AND NOT INDIVIDUAL CHARACTERS 
import statistics  #ALLOWS ACCESS TO THE STATISTICS LIBARY FOR THE DATA COLLECTION AND PROCESSING
import itertools   #ALLOWS ACCESS TO ACCESS TO THE ITERATORS LIBARY FOR EFFICENT LOOPING 
import datetime    #THIS ALLOWS FOR THE CURRENT TIME TO BE IMPORTED AND DISPLAYED FOR THE USER TO SEE 
import pyglet      #THIS IS THE MODULE THAT ALLOWS FOR THE SOUNDS/MUSIC/SONGS TO BE PLAYED 

window = Tk()      #DEFING THE NAME OF THE WINDOW 

l0 = Label(window, text="",bg="slategray3") #CREATING A ONE LINE SPACE
l0.pack()                                   #DISPLAYING THE LABEL

#LOCATING THE ALBUM'S COVER/ARTWORK FOR THE PROGRAM TO THEN DISPLAY 
album = ImageTk.PhotoImage(Image.open("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\albums\\AMWPS.jpg"))

#THIS LABEL IS DISPLAYING THE ALBUM'S COVER/ARTWORK FOR THE USER TO SEE
label = Label(window, image=album)          #CREATING A LABEL THAT WILL HOLD THE ALBUM ARTWORK 
label.pack()                                #DISPLAYING THE LABEL THAT CONTAINS THE ARTWORK

l2 = Label(window, text="",bg="slategray3") #CREATING A ONE LINE SPACE
l2.pack()                                   #DISPLAYING THE LABEL

#DISPLAYING THE ARTIST AND ALBUM NAME THAT HAS BEEN SELECTED
l2 = Label(window, text="Arctic Monkeys - Whatever People Say I Am, That's What I'm Not", font='Helvetica 12 bold',bg="slategray3") #CREATING A LABEL THAT WILL DISPLAY THE ALBUM NAME 
l2.pack()                                                                                                                           #DISPLAYING THE LABEL 

l1 = Label(window, text="",bg="slategray3") #CREATING A ONE LINE SPACE
l1.pack()                                   #DISPLAYING THE LABEL

#THIS LABEL GIVES A SMALL/BREIF SUMMARY OF THE ALBUM THAT HAS BEEN SELECTED 
l1 = Label(window, text="""Whatever People Say I Am, That's What I'm Not is the
debut studio album by English rock band Arctic Monkeys, released on 23 January 2006
by Domino Recording Company. The album surpassed Elastica's self-titled album to
become the fastest selling debut album in British music history
""",bg="slategray3")  #CREATING A LABEL THAT WILL TELL THE USER ABOUT THE ALBUM
l1.pack()             #DISPLAYING THE LABEL

#CREATING THE 'PLAY ALL' BUTTON THAT WILL PLAY EACH TRACK STRATING FROM THE FIRST SONG IN THE ALBUM 
def option():

    option1()

b1 = Button(window, text="PLAY ALL", command=option) #CREATING A BUTTON THAT WILL PLAY EVERY SONG ONE AFTER ANOTHER 
b1.pack()                                            #DISPLAYING THE BUTTON 

l2 = Label(window, text="",bg="slategray3")          #CREATING A ONE LINE SPACE
l2.pack()                                            #DISPLAYING THE LABEL 

#CREATING A BUTTON FOR EACH SONG AS THE USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option1():
    #1
    song = pyglet.media.load("C:\\Users\\natda\\OneDrive\\Music\\Artic Monkeys\\Whatever People Say I Am, That's What I'm Not\\Arctic Monkeys - The View from the Afternoon.mp3") #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(218) #LENGTH OF THE SONG IN SECONDS
    option2()       #TAKES IT ONTO THE NEXT TRACK/FUNCTION    

b1 = Button(window, text="                                             The View from the Afternoon                                       ", command=option1) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()           #DISPLAYING THE BUTTON 

#CREATING A BUTTON FOR EACH SONG AS THE USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option2():
    #2
    song = pyglet.media.load("C:\\Users\\natda\\OneDrive\\Music\\Artic Monkeys\\Whatever People Say I Am, That's What I'm Not\\Arctic Monkeys - I Bet You Look Good On the Dancefloor.mp3") #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(173) #LENGTH OF THE SONG IN SECONDS
    option3()       #TAKES IT ONTO THE NEXT TRACK/FUNCTION

b1 = Button(window, text="                                     I Bet You Look Good On the Dancefloor                             ", command=option2) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()           #DISPLAYING THE BUTTON

#CREATING A BUTTON FOR EACH SONG AS THE USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option3():
    #3
    song = pyglet.media.load("C:\\Users\\natda\\OneDrive\\Music\\Artic Monkeys\\Whatever People Say I Am, That's What I'm Not\\Arctic Monkeys - Fake Tales of San Francisco.mp3") #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(177) #LENGTH OF THE SONG IN SECONDS
    option4()       #TAKES IT ONTO THE NEXT TRACK/FUNCTION

b1 = Button(window, text="                                              Fake Tales of San Francisco                                          ", command=option3) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()           #DISPLAYING THE BUTTON

#CREATING A BUTTON FOR EACH SONG AS THE USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option4():
    #4
    song = pyglet.media.load("C:\\Users\\natda\\OneDrive\\Music\\Artic Monkeys\\Whatever People Say I Am, That's What I'm Not\\Arctic Monkeys - Dancing Shoes.mp3") #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(141) #LENGTH OF THE SONG IN SECONDS
    option5()       #TAKES IT ONTO THE NEXT TRACK/FUNCTION

b1 = Button(window, text="                                                       Dancing Shoes                                                       ", command=option4) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()           #DISPLAYING THE BUTTON

#CREATING A BUTTON FOR EACH SONG AS THE USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option5():
    #5
    song = pyglet.media.load("C:\\Users\\natda\\OneDrive\\Music\\Artic Monkeys\\Whatever People Say I Am, That's What I'm Not\\Arctic Monkeys - You Probably Couldn't See for the Lights But You Were Staring Straight At Me.mp3")             #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(130) #LENGTH OF THE SONG IN SECONDS
    option6()       #TAKES IT ONTO THE NEXT TRACK/FUNCTION

b1 = Button(window, text="You Probably Couldn't See for the Lights But You Were Staring Straight At Me", command=option5) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()           #DISPLAYING THE BUTTON

#CREATING A BUTTON FOR EACH SONG AS THE USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option6():
    #6
    song = pyglet.media.load("C:\\Users\\natda\\OneDrive\\Music\\Artic Monkeys\\Whatever People Say I Am, That's What I'm Not\\Arctic Monkeys - Still Take You Home.mp3") #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(173) #LENGTH OF THE SONG IN SECONDS
    option7()       #TAKES IT ONTO THE NEXT TRACK/FUNCTION

b1 = Button(window, text="                                                 Still Take You Home                                                   ", command=option6) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()           #DISPLAYING THE BUTTON

#CREATING A BUTTON FOR EACH SONG AS THE USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option7():
    #7
    song = pyglet.media.load("C:\\Users\\natda\\OneDrive\\Music\\Artic Monkeys\\Whatever People Say I Am, That's What I'm Not\\Arctic Monkeys - Riot Van.mp3") #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(134) #LENGTH OF THE SONG IN SECONDS
    option8()       #TAKES IT ONTO THE NEXT TRACK/FUNCTION

b1 = Button(window, text="                                                          Riot Van                                                               ", command=option7) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()           #DISPLAYING THE BUTTON

#CREATING A BUTTON FOR EACH SONG AS THE USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option8():
    #8
    song = pyglet.media.load("C:\\Users\\natda\\OneDrive\\Music\\Artic Monkeys\\Whatever People Say I Am, That's What I'm Not\\Arctic Monkeys - Red Light Indicates Doors Are Secured.mp3") #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(143) #LENGTH OF THE SONG IN SECONDS
    option9()       #TAKES IT ONTO THE NEXT TRACK/FUNCTION

b1 = Button(window, text="                                   Red Light Indicates Doors Are Secured                                  ", command=option8) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()           #DISPLAYING THE BUTTON

#CREATING A BUTTON FOR EACH SONG AS THE USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option9():
    #9
    song = pyglet.media.load("C:\\Users\\natda\\OneDrive\\Music\\Artic Monkeys\\Whatever People Say I Am, That's What I'm Not\\Arctic Monkeys - Mardy Bum.mp3")#DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(175) #LENGTH OF THE SONG IN SECONDS
    option10()      #TAKES IT ONTO THE NEXT TRACK/FUNCTION

b1 = Button(window, text="                                                       Mardy Bum                                                            ", command=option9) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()           #DISPLAYING THE BUTTON

#CREATING A BUTTON FOR EACH SONG AS THE USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TOV
def option10():
    #10
    song = pyglet.media.load("C:\\Users\\natda\\OneDrive\\Music\\Artic Monkeys\\Whatever People Say I Am, That's What I'm Not\\Arctic Monkeys - Perhaps Vampires Is a Bit Strong But….mp3") #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(268) #LENGTH OF THE SONG IN SECONDS
    option12()      #TAKES IT ONTO THE NEXT TRACK/FUNCTION
 
b1 = Button(window, text="                                  Perhaps Vampires Is a Bit Strong But…                                   ", command=option10) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()                                   #DISPLAYING THE BUTTON

#CREATING A BUTTON FOR EACH SONG AS THE USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option11():
    #11
    song = pyglet.media.load("C:\\Users\\natda\\OneDrive\\Music\\Artic Monkeys\\Whatever People Say I Am, That's What I'm Not\\Arctic Monkeys - When the Sun Goes Down.mp3") #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(200) #LENGTH OF THE SONG IN SECONDS
    option13()      #TAKES IT ONTO THE NEXT TRACK/FUNCTION

b1 = Button(window, text="                                           When the Sun Goes Down                                               ", command=option11) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()           #DISPLAYING THE BUTTON

#CREATING A BUTTON FOR EACH SONG AS THE USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option12():
    #12
    song = pyglet.media.load("C:\\Users\\natda\\OneDrive\\Music\\Artic Monkeys\\Whatever People Say I Am, That's What I'm Not\\Arctic Monkeys - From the Ritz to the Rubble.mp3") #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(193) #LENGTH OF THE SONG IN SECONDS
    option14()      #TAKES IT ONTO THE NEXT TRACK/FUNCTION

b1 = Button(window, text="                                             From the Ritz to the Rubble                                           ", command=option12) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()           #DISPLAYING THE BUTTON

#CREATING A BUTTON FOR EACH SONG AS THE USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option13():
    #13
    song = pyglet.media.load("C:\\Users\\natda\\OneDrive\\Music\\Artic Monkeys\\Whatever People Say I Am, That's What I'm Not\\Arctic Monkeys - A Certain Romance.mp3") #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()      #PLAYING THE ACTUAL SONG 
    time.sleep(331)  #LENGTH OF THE SONG IN SECONDS
    option14()       #TAKES IT ONTO THE NEXT TRACK/FUNCTION

b1 = Button(window, text="                                                   A Certain Romance                                                   ", command=option13) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()           #DISPLAYING THE BUTTON

l2 = Label(window, text="",bg="slategray3") #CREATING A ONE LINE SPACE 
l2.pack()                                   #DISPLAYING THE SPACE 

#CREATING A BACK BUTTON SO THAT THE USER CAN RETURN BACK TO THE ALBUM PAGE 
def option14():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\ARTISTS\\AM.py") #THE PATH FOR THE ACRTIC MONKEYS MENU  
    window.destroy()                                                                                                                       #CLOSES THE CURRENT WINDOW THAT IS OPEN

b15 = Button(window, text="BACK",command=option14) #CREATING THE BACK BUTTON
b15.pack()                                         #DISPLAYING THE BACK BUTTON

#DEFINING THE PROPERTIES AND CHARACTERISTICS OF THE WINDOW
window.resizable(0,0)                                                #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
window.resizable(width=FALSE, height=FALSE)                          #MEANS THAT THE WINDOW SIZE CAN NOT BE CHANGED BY THE USER (NO FULL SCREEN)
window.title("Whatever People Say I Am, That's What I'm Not - MSTR") #GIVING A TITLE TO THE WINDOW 
window.geometry("500x780")                                           #DEFING THE SIZE OF THE WINDOW - ALL ALBUM WINDOWS HAVE AN X-AXIS OF 500
window.configure(background="slategray3")                            #DEFINING THE BACKGROUND COLOUR OF THE WINDOW 

mainloop()
