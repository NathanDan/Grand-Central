#TKinter GC SQG
#2019
#Nathan Jones

from tkinter import messagebox, Label, Button, FALSE, Tk, Entry    #ALLOWING FOR TKINTER TO BE ACCESSED/UTILISED FOR THE PROGRAM TO USE ALL OF ITS FUNCTIONS AND GIVING THE PROGRAM A GUI
from tkinter import *                                              #ALLOWING FOR ALL OF TKINTER'S MODULES TO BE IMPORTED 

import time            #THIS ALLOWS FOR THE PROGRAM TO USE THE SLEEP FUNCTION WITHIN THE PROGRAM
import sys             #ALLOWS ACCESS TO THE SYSTEM FROM WITHIN PYTHON 
import os.path         #ALLOWS THE PROGRAM TO OPEN OTHER SPECIFIC APPLICATIONS, IN THIS CASE THE GC PROGRAMS 
import os              #ALLOWS FOR CONTROL OF THE MACHINE AND IS OS INCLUDING THE LIKES OF SAVING, OPENING/CLOSING FILES, ETC. 
import string          #ALLOWS FOR DATA/ENTRIES TO BE RECOREDAS STRINGS AND NOT INDIVIDUAL CHARACTERS 
import random          #THIS IMPORT ALLOWS FOR WORDS TO BE RANDOMLY SELECTED 
import itertools       #ALLOWS ACCESS TO ACCESS TO THE ITERATORS LIBARY FOR EFFICENT LOOPING 
import datetime        #THIS ALLOWS FOR THE CURRENT TIME TO BE IMPORTED AND DISPLAYED FOR THE USER TO SEE 

window = Tk()          #DEFINING THE MAIN MENU WINDOW'S NAME 

window.resizable (0,0)                                    #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
window.resizable (width=FALSE, height=FALSE)              #THE USER CANNOT CHANGE THE SIZE OF THE MENU
window.title ("GRAND CENTRAL MATH QUESTION GENERATOR") #GIVING THE WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
window.geometry("500x300")                                #CONFIGURING THE FIXED SIZE OF THE WINDOW WHICH WILL ALWAYS BE THIS SIZE            
window.configure(background='white')                      #CONFIGURING THE BACKGROUND OF THE WINDOW TO BE WHITE

l2 = Label(window, text=" ",bg="white")                                                    #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE
l2.pack()                                                                                  #DISPLAY THE LABEL WITHIN THE MENU WINDOW 

l0 = Label(window, text="MATH QUESTION GENERATOR",font='Helvetica 16 bold' ,bg="white") #GIVING THE WINDOW A TITLE SO THE USER/CLIENT KNOWS WHAT MENU THEY ARE ON 
l0.pack()                                                                                  #DISPLAYING THE TITLE FOR THE USER/CLIENT TO SEE

l5 = Label(window, text=" ",bg="white")                                                    #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE
l5.pack()                                                                                  #DISPLAY THE LABEL WITHIN THE MENU WINDOW   

def HELP():

    windowHELP = Tk()                                                    #DEFINING THE HELP WINDOW'S NAME

    windowHELP.resizable (0,0)                                           #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
    windowHELP.resizable (width=FALSE, height=FALSE)                     #THE USER CANNOT CHANGE THE SIZE OF THE MENU  
    windowHELP.title("GRAND CENTRAL MATH QUESTION GENERATOR - HELP")  #GIVING THE WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
    windowHELP.geometry("500x400")                                       #CONFIGURING THE FIXED SIZE OF THE WINDOW WHICH WILL ALWAYS BE THIS SIZE            
    windowHELP.configure(background='white')                             #CONFIGURING THE BACKGROUND OF THE WINDOW TO BE WHITE

    time = datetime.datetime.now()                                       #ALLOWS THE PROGRAM TO GATHER THE CURRENT TIME
        
    TIME=Label(windowHELP, text="SYSTEM TIME: "+str(time.strftime("%Y-%m-%d %H:%M")),bg="white") #CREATING A LABEL THAT WILL DISPLAY THE CURRENT TIME
    l=Label(windowHELP, text=" ",bg="white")                                                     #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE
    HELP=Label(windowHELP,text=""" HELP! 

The program is designed to randomly select a maths question for the
give topic and Key Stage you have asked for.

It does this by YOU the user selecting which Key Stage and Topic you
would like and then the question is randomly selected from the question
database which is pre-loaded with exisitng questions for each Key Stage
and Topic.

If YOU end up in the wrong Key Stage YOU can simply 'BACK' to return
back to the previous menu.

Once a question has been given the program will then ask you if you would
like another question or not, if 'NO' is selected then you will return back
to the Key Stage menu, but if you select 'YES' then another randomly selected
question will be given. - This process will continue until you select 'NO'.
""")                                                   #CREATING A LABEL THAT WILL ACT AS THE HELP AND TELLS THE USER HOW TO USE THE APPLICATION 

    l1=Label(windowHELP, text=" ",bg="white")          #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE

    def HELPback():
        windowHELP.destroy()                           #CLOSING THE WINDOW WITH THE USE OF THE '.destroy()' FUNCTION WITHIN TKINTER
    
    b=Button(windowHELP, text="BACK",command=HELPback) #CREATING THE BUTTON THAT WILL BE ACT AS THE BACK BUTTON 
    
    TIME.pack()               #DISPLAYING THE CURRET TIME LABEL
    l.pack()                  #DISPLAYING THE LABEL WITHIN THE MENU WINDOW 
    HELP.pack()               #DISPLAYING THE HELP LABEL
    l1.pack()                 #DISPLAYING THE LABEL WITHIN THE MENU WINDOW 
    b.pack()                  #DISPLAYING THE BACK BUTTON 

    windowHELP.mainloop()     

def KS1():

   KS1=["""5 + 1 = ___

2 + 7 = ___

37 + 5 = ___

10 + 20 = ___""","""18 - 8 = ___

88 - 4 = ___

3 x 10 = ___""","""3 + 30 + 3 = ___

37 + 5 = ___

5 + 1 = ___

88 - 4 = ___""","""6 x 10 = ___

100 − 10 = ___

4 + 81 = ___

7 x 2 = ___""","""63 - 4 =  ___

54 - 20 = ___

99 + 10 = ___

67 + 33 = ___""","""98 - ___ = 28

120 ÷ 10 = ___

74 - 47 = ___

17 + 48 = ___"""] #CREATING THE ARRAY THAT WILL STORE ALL OF THE KS1 QUESTIONS AND 1 WILL BE RANDOMLY SELECTED 


   windowKS1 = Tk()                                                    #DEFINING THE KS1 WINDOW 

   windowKS1.resizable (0,0)                                           #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
   windowKS1.resizable (width=FALSE, height=FALSE)                     #THE USER CANNOT CHANGE THE SIZE OF THE MENU  
   windowKS1.title("GRAND CENTRAL MATH QUESTION GENERATOR - KS1")   #GIVING THE WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
   windowKS1.geometry("300x350")                                       #CONFIGURING THE FIXED SIZE OF THE WINDOW WHICH WILL ALWAYS BE THIS SIZE            
   windowKS1.configure(background='white')                             #CONFIGURING THE BACKGROUND OF THE WINDOW TO BE WHITE

   time = datetime.datetime.now()                                      #ALLOWS THE PROGRAM TO GATHER THE CURRENT TIME
       
   TIME=Label(windowKS1, text="SYSTEM TIME: "+str(time.strftime("%Y-%m-%d %H:%M")),bg="white") #CREATING A LABEL THAT WILL DISPLAY THE CURRENT TIME IN THE FORMAT Y-M-D AND H:M
   
   l=Label(windowKS1, text=" ",bg="white")                                  #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE
   Q=Label(windowKS1,text=str(random.choice(KS1)))                          #CREATING A LABEL THAT WILL SELECTED ONE OF THE QUESTIONS RANDOMLY AND THEN DISPLAY IT 

   l1=Label(windowKS1, text=" ",bg="white")                                 #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE

   l2=Label(windowKS1, text="Do YOU want another question? ",bg="white")    #CREATING A LABEL THAT WILL ASK THE USER IF THEY WOULD LIKE ANOTHER QUESTION 

   l3=Label(windowKS1, text=" ",bg="white")                                 #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE

   def KS1button():
       windowKS1.destroy()     #CLOSING THE WINDOW WITH THE USE OF THE '.destroy()' FUNCTION WITHIN TKINTER

   def KS1Button():
       windowKS1.destroy()     #CLOSING THE WINDOW WITH THE USE OF THE '.destroy()' FUNCTION WITHIN TKINTER
       option2()               #REPEATING THE FUNCTION SO THAT IT WILL GENERATE ANOTHER QUESTION 
    
   b1=Button(windowKS1, text="   YES   ", fg="green", command=KS1Button) #CREATING A BUTTON THAT WILL RUN THE FUNCTION AGAIN ALLOWING FOR THE USER TO GET ANOTHER QUESTION
   b2=Button(windowKS1, text="   NO    ", fg="red", command=KS1button)   #CREATING A BUTTON THAT WILL TAKE THE USER BACK TO THE MAIN MENU
    
   TIME.pack()            #DISPLAYING THE CURRET TIME LABEL
   l.pack()               #DISPLAYING THE LABEL WITHIN THE MENU WINDOW 
   Q.pack()               #DISPLAYING THE RANDOMLY SELECTED QUESTION  
   l1.pack()              #DISPLAYING THE LABEL WITHIN THE MENU WINDOW 
   l2.pack()              #DISPLAYING THE 'Do YOU want another question?' LABEL
   l3.pack()              #DISPLAYING THE LABEL WITHIN THE MENU WINDOW 
   b1.pack()              #DISPLAYING THE 'Yes' BUTTON 
   b2.pack()              #DISPLAYING THE 'No' BUTTON

   windowKS1.mainloop()

def KS2():

   KS2=["""39 + 673 = ___

2 × 45 = ___

5 × 4 × 10 = ___

838 ÷ 1 = ___""","""99 ÷ 11 = ___

5 × 4 × 10 = ___

7,064 − 502 = ___

56.38 + 24.7 = ___""","""___ − 10 = 298

270 ÷ 3 = ___

5,400 ÷ 9 = ___

60 ÷ 15 = ___""",""" ___= 5,776 − 855

3,050,020 = 3,000,000 + _____ + 20

10 − 5.4 = ___

0.1 ÷ 100 = ___""","""20% of 1,200 = ___

0.5 × 28 = ___

6 − 5.738 = ___

3.9 × 30 = ___""","""99% of 200 =___

28% of 650 = ___

5 × 4 × 10 = ___

270 ÷ 3 = ___"""] #CREATING THE ARRAY THAT WILL STORE ALL OF THE KS2 QUESTIONS AND 1 WILL BE RANDOMLY SELECTED 

   windowKS2 = Tk()                                                    #DEFINING THE KS2 WINDOW 

   windowKS2.resizable (0,0)                                           #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
   windowKS2.resizable (width=FALSE, height=FALSE)                     #THE USER CANNOT CHANGE THE SIZE OF THE MENU  
   windowKS2.title("GRAND CENTRAL MATH QUESTION GENERATOR - KS2")   #GIVING THE WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
   windowKS2.geometry("300x350")                                       #CONFIGURING THE FIXED SIZE OF THE WINDOW WHICH WILL ALWAYS BE THIS SIZE            
   windowKS2.configure(background='white')                             #CONFIGURING THE BACKGROUND OF THE WINDOW TO BE WHITE

   time = datetime.datetime.now()                                      #ALLOWS THE PROGRAM TO GATHER THE CURRENT TIME
       
   TIME=Label(windowKS2, text="SYSTEM TIME: "+str(time.strftime("%Y-%m-%d %H:%M")),bg="white") #CREATING A LABEL THAT WILL DISPLAY THE CURRENT TIME IN THE FORMAT Y-M-D AND H:M

   l=Label(windowKS2, text=" ",bg="white")                                  #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE
   Q=Label(windowKS2,text=str(random.choice(KS2)))                          #CREATING A LABEL THAT WILL SELECTED ONE OF THE QUESTIONS RANDOMLY AND THEN DISPLAY IT 

   l1=Label(windowKS2, text=" ",bg="white")                                 #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE

   l2=Label(windowKS2, text="Do YOU want another question? ",bg="white")    #CREATING A LABEL THAT WILL ASK THE USER IF THEY WOULD LIKE ANOTHER QUESTION 

   l3=Label(windowKS2, text=" ",bg="white")                                 #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE

   def KS2button():
       windowKS2.destroy()      #CLOSING THE WINDOW WITH THE USE OF THE '.destroy()' FUNCTION WITHIN TKINTER

   def KS2Button():
       windowKS2.destroy()      #CLOSING THE WINDOW WITH THE USE OF THE '.destroy()' FUNCTION WITHIN TKINTER
       option3()                #REPEATING THE FUNCTION SO THAT IT WILL GENERATE ANOTHER QUESTION
    
   b1=Button(windowKS2, text="   YES   ", fg="green", command=KS2Button) #CREATING A BUTTON THAT WILL RUN THE FUNCTION AGAIN ALLOWING FOR THE USER TO GET ANOTHER QUESTION
   b2=Button(windowKS2, text="   NO    ", fg="red", command=KS2button)   #CREATING A BUTTON THAT WILL TAKE THE USER BACK TO THE MAIN MENU
    
   TIME.pack()            #DISPLAYING THE CURRET TIME LABEL
   l.pack()               #DISPLAYING THE LABEL WITHIN THE MENU WINDOW 
   Q.pack()               #DISPLAYING THE RANDOMLY SELECTED QUESTION  
   l1.pack()              #DISPLAYING THE LABEL WITHIN THE MENU WINDOW 
   l2.pack()              #DISPLAYING THE 'Do YOU want another question?' LABEL
   l3.pack()              #DISPLAYING THE LABEL WITHIN THE MENU WINDOW 
   b1.pack()              #DISPLAYING THE 'Yes' BUTTON 
   b2.pack()              #DISPLAYING THE 'No' BUTTON

   windowKS2.mainloop()

def KS3():

   KS3=["""Here is a number grid.

41  42  43  44  45  46  47  48  49  50

51  52 |53| 54  55  56  57  58  59  60

61  62  63  64  65  66  67  68  69  70

71  72  73  74  75  76  77  78 |79| 80

81  82  83  84  85  86  87  88  89  90

Two numbers are in | |.

(a) What is the total of the numbers in the two | |?

(b) Shade two different squares that have the same total as the answer to part (a).

(c) What is the total of the numbers in all four shaded squares? ""","""
A café sells small, medium and large drinks.

The table shows the number of drinks the café sold on one day.

        Coffee Tea Chocolate
Small    110   14   24
Medium   121   103  42
Large     90   64   58

(a) Altogether, how many chocolate drinks were sold?

(b) A small tea costs 50p.

    Altogether, how much was spent on small teas?

    £____""","""Look at the number sentences below.

Tick (/) ones that are correct and cross (X) ones that are incorrect.

5 + 8 = 8 + 5     
5 – 8 = 8 – 5     
5 × 8 = 8 × 5     
5 ÷ 8 = 8 ÷ 5 
""","""Which one of these is most likely to hold about 5 litres when it is full?

Select your answer.

A spoon
A bottle of cough mixture
A watering can
A garden pond
""","""Write in the missing numbers.

79 + 85 = ___

36 + ___ = 90""","""
In this question you need to know:
    Jo’s birthday is June 5th.

(a) Sanjay’s birthday is exactly three weeks after Jo’s birthday.
    On what date is Sanjay’s birthday?

(b) Tina’s birthday is 5 months after Jo’s birthday.
    In which month is Tina’s birthday?""","""
Lily finished 2nd out of 8 runners in a race.
How many runners finished the race after Lily?
                                    _________

Max was in a different race.
7 runners finished the race before Max.
3 runners finished the race after Max.

Altogether, how many runners finished the race?
                                    __________    ""","""In a school, lessons are 55 minutes long.

(a) A maths lesson starts at 9:15am
    At what time does the lesson end?
    
                              ___:___ am

(b) A history lesson ends at 3:30pm
    At what time does the lesson start?
    
                              ___:___ pm

(c) Lunch break is 1.25 hours long.
    Lunch break ends at 1:30pm
    At what time does it start?

                            ___:___ pm ""","""
(a) Look at this information about recycling:
    25 large plastic bottles can be recycled to make 1 fleece jacket.

Write the missing number in this sentence.

200 large plastic bottles can be recycled to make _______ fleece jackets.

(b) In a survey, 9 out of 10 people said they would like to recycle more.
    What percentage of people said they would like to recycle more?

                                                               ____% ""","""
A teacher said:
    Choose values for a and b
    Use the letters to make expressions for the numbers 1 to 8

(a) One group of pupils chose a = 2 and b = 3
    Complete their table.

            a = 2 b = 3

            b – a = 1
                a = 2
                b = 3
            2 × a = 4
              ___ = 5
            a × b = 6
            2 × a + b = 7
              ___ = 8
            
(b) Here is part of the table from a different group of pupils.

    2 × a = 6
    a + b = 7

    What values did they choose?

    a = ___ b = ___ ""","""
The table below helps to change centimetres into inches.

    Number of centimetres              2 4 6 8 10 12
    Number of inches (approximately)   0.8 1.6 2.4 3.1 3.9 4.7

    About how many inches are there in 14 centimetres?
 
                                        _____ inches"""] #CREATING THE ARRAY THAT WILL STORE ALL OF THE KS3 QUESTIONS AND 1 WILL BE RANDOMLY SELECTED

   windowKS3 = Tk()                                                    #DEFINING THE KS3 WINDOW 

   windowKS3.resizable (0,0)                                           #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
   windowKS3.resizable (width=FALSE, height=FALSE)                     #THE USER CANNOT CHANGE THE SIZE OF THE MENU  
   windowKS3.title("GRAND CENTRAL MATH QUESTION GENERATOR - KS3")   #GIVING THE WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
   windowKS3.geometry("500x500")                                       #CONFIGURING THE FIXED SIZE OF THE WINDOW WHICH WILL ALWAYS BE THIS SIZE            
   windowKS3.configure(background='white')                             #CONFIGURING THE BACKGROUND OF THE WINDOW TO BE WHITE

   time = datetime.datetime.now()                                      #ALLOWS THE PROGRAM TO GATHER THE CURRENT TIME
       
   TIME=Label(windowKS3, text="SYSTEM TIME: "+str(time.strftime("%Y-%m-%d %H:%M")),bg="white") #CREATING A LABEL THAT WILL DISPLAY THE CURRENT TIME IN THE FORMAT Y-M-D AND H:M 
   
   l=Label(windowKS3, text=" ",bg="white")                                  #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE
   Q=Label(windowKS3,text=str(random.choice(KS3)))                          #CREATING A LABEL THAT WILL SELECTED ONE OF THE QUESTIONS RANDOMLY AND THEN DISPLAY IT 

   l1=Label(windowKS3, text=" ",bg="white")                                 #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE

   l2=Label(windowKS3, text="Do YOU want another question? ",bg="white")    #CREATING A LABEL THAT WILL ASK THE USER IF THEY WOULD LIKE ANOTHER QUESTION

   l3=Label(windowKS3, text=" ",bg="white")                                 #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE

   def KS3button():
       windowKS3.destroy()      #CLOSING THE WINDOW WITH THE USE OF THE '.destroy()' FUNCTION WITHIN TKINTER

   def KS3Button():
       windowKS3.destroy()      #CLOSING THE WINDOW WITH THE USE OF THE '.destroy()' FUNCTION WITHIN TKINTER
       option4()                #REPEATING THE FUNCTION SO THAT IT WILL GENERATE ANOTHER QUESTION
    
   b1=Button(windowKS3, text="   YES   ", fg="green", command=KS3Button) #CREATING A BUTTON THAT WILL RUN THE FUNCTION AGAIN ALLOWING FOR THE USER TO GET ANOTHER QUESTION 
   b2=Button(windowKS3, text="   NO    ", fg="red", command=KS3button)   #CREATING A BUTTON THAT WILL TAKE THE USER BACK TO THE MAIN MENU
    
   TIME.pack()            #DISPLAYING THE CURRET TIME LABEL
   l.pack()               #DISPLAYING THE LABEL WITHIN THE MENU WINDOW 
   Q.pack()               #DISPLAYING THE RANDOMLY SELECTED QUESTION  
   l1.pack()              #DISPLAYING THE LABEL WITHIN THE MENU WINDOW 
   l2.pack()              #DISPLAYING THE 'Do YOU want another question?' LABEL
   l3.pack()              #DISPLAYING THE LABEL WITHIN THE MENU WINDOW 
   b1.pack()              #DISPLAYING THE 'Yes' BUTTON 
   b2.pack()              #DISPLAYING THE 'No' BUTTON

   windowKS3.mainloop()

def KS4():

    windowKS4 = Tk()                                                    #DEFINING THE KS4 MENU WINDOW 

    windowKS4.resizable (0,0)                                           #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
    windowKS4.resizable (width=FALSE, height=FALSE)                     #THE USER CANNOT CHANGE THE SIZE OF THE MENU
    windowKS4.title ("GRAND CENTRAL MATH QUESTION GENERATOR - KS4")  #GIVING THE WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
    windowKS4.geometry("500x250")                                       #CONFIGURING THE FIXED SIZE OF THE WINDOW WHICH WILL ALWAYS BE THIS SIZE            
    windowKS4.configure(background='white')                             #CONFIGURING THE BACKGROUND OF THE WINDOW TO BE WHITE


    l2 = Label(windowKS4, text=" ",bg="white")                          #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE
    l2.pack()                                                           #DISPLAYING THE LABEL WITHIN THE MENU WINDOW 

    l0 = Label(windowKS4, text="MATH QUESTION GENERATOR - KS4",font='Helvetica 14 bold' ,bg="white") #GIVING THE WINDOW A TITLE SO THE USER KNOWS WHAT MENU THEY ARE ON 
    l0.pack()                                                                                           #DISPLAYING THE TITLE FOR THE USER TO SEE

    l5 = Label(windowKS4, text=" ",bg="white")                          #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE
    l5.pack()                                                           #DISPLAYING THE LABEL WITHIN THE MENU WINDOW                                  

    def KS4b():
        KS4bio()                                                                                         #THE FUNCTION THAT HOLDS THE KS4 BIOLOGY QUESTIONS   

    b1 = Button(windowKS4, text="                 Key Stage 4 - Core                 ", command=KS4b) #CREATING THE BUTTON THAT TAKES THEM TO KS4 BIOLOGY
    b1.pack()                                                                                            #DISPLAYING THE BUTTON ON THE MENU       

    def KS4c():
        KS4chem()                                                                                        #THE FUNCTION THAT HOLDS THE KS4 CHEMISTRY QUESTIONS   
    
    b1 = Button(windowKS4, text="               Key Stage 4 - Statistics              ", command=KS4c)    #CREATING THE BUTTON THAT TAKES THEM TO KS4 CHEMISTRY
    b1.pack()                                                                                            #DISPLAYING THE BUTTON ON THE MENU 

    def KS4p():
        KS4phy()                                                                                         #THE FUNCTION THAT HOLDS THE KS4 PHYSICS QUESTIONS    

    b1 = Button(windowKS4, text="                  Key Stage 4 - Further                ", command=KS4p) #CREATING THE BUTTON THAT TAKES THEM TO KS4 PHYSICS
    b1.pack()                                                                                            #DISPLAYING THE BUTTON ON THE MENU

    l3 = Label(windowKS4, text=" ",bg="white")                          #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE
    l3.pack()                                                           #DISPLAY THE LABEL WITHIN THE MENU WINDOW 

    def KS4button():
       windowKS4.destroy()                                              #CLOSING THE WINDOW WITH THE USE OF THE '.destroy()' FUNCTION WITHIN TKINTER

    b = Button(windowKS4, text="BACK",command=KS4button)                #CREATING THE BACK BUTTON THAT WILL TAKE THE USER BACK TO THE MAIN SQG MENU
    b.pack()                                                            #DISPLAYING THE BUTTON ON THE KS4 MENU 

    windowKS4.mainloop()

def KS4CORE():

   CORE4=[""" """] #CREATING THE ARRAY THAT WILL STORE ALL OF THE KS4 BIOLOGY QUESTIONS AND 1 WILL BE RANDOMLY SELECTED

   windowKS4bio = Tk()                                                            #DEFINING THE KS4 BIOLOGY WINDOW 

   windowKS4bio.resizable (0,0)                                                   #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
   windowKS4bio.resizable (width=FALSE, height=FALSE)                             #THE USER CANNOT CHANGE THE SIZE OF THE MENU  
   windowKS4bio.title("GRAND CENTRAL SCIENCE QUESTION GENERATOR - KS4 Biology")   #GIVING THE WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
   windowKS4bio.geometry("500x600")                                               #CONFIGURING THE FIXED SIZE OF THE WINDOW WHICH WILL ALWAYS BE THIS SIZE            
   windowKS4bio.configure(background='white')                                     #CONFIGURING THE BACKGROUND OF THE WINDOW TO BE WHITE

   time = datetime.datetime.now()                                                 #ALLOWS THE PROGRAM TO GATHER THE CURRENT TIME
       
   TIME=Label(windowKS4bio, text="SYSTEM TIME: "+str(time.strftime("%Y-%m-%d %H:%M")),bg="white") #CREATING A LABEL THAT WILL DISPLAY THE CURRENT TIME IN THE FORMAT Y-M-D AND H:M
   
   l=Label(windowKS4bio, text=" ",bg="white")                                  #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE
   Q=Label(windowKS4bio,text=str(random.choice(BIO4)))                         #CREATING A LABEL THAT WILL SELECTED ONE OF THE QUESTIONS RANDOMLY AND THEN DISPLAY IT

   l1=Label(windowKS4bio, text=" ",bg="white")                                 #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE

   l2=Label(windowKS4bio, text="Do YOU want another question? ",bg="white")    #CREATING A LABEL THAT WILL ASK THE USER IF THEY WOULD LIKE ANOTHER QUESTION

   l3=Label(windowKS4bio, text=" ",bg="white")                                 #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE

   def KS4button():
       windowKS4bio.destroy()  #CLOSING THE WINDOW WITH THE USE OF THE '.destroy()' FUNCTION WITHIN TKINTER

   def KS4Button():
       windowKS4bio.destroy()  #CLOSING THE WINDOW WITH THE USE OF THE '.destroy()' FUNCTION WITHIN TKINTER
       KS4bio()                #REPEATING THE FUNCTION SO THAT IT WILL GENERATE ANOTHER QUESTION
    
   b1=Button(windowKS4bio, text="   YES   ", fg="green", command=KS4Button) #CREATING A BUTTON THAT WILL RUN THE FUNCTION AGAIN ALLOWING FOR THE USER TO GET ANOTHER QUESTION  
   b2=Button(windowKS4bio, text="   NO    ", fg="red", command=KS4button)   #CREATING A BUTTON THAT WILL TAKE THE USER BACK TO THE MAIN MENU
    
   TIME.pack()            #DISPLAYING THE CURRET TIME LABEL
   l.pack()               #DISPLAYING THE LABEL WITHIN THE MENU WINDOW 
   Q.pack()               #DISPLAYING THE RANDOMLY SELECTED QUESTION  
   l1.pack()              #DISPLAYING THE LABEL WITHIN THE MENU WINDOW 
   l2.pack()              #DISPLAYING THE 'Do YOU want another question?' LABEL
   l3.pack()              #DISPLAYING THE LABEL WITHIN THE MENU WINDOW 
   b1.pack()              #DISPLAYING THE 'Yes' BUTTON 
   b2.pack()              #DISPLAYING THE 'No' BUTTON

   windowKS4bio.mainloop()

def KS4STATS():

   STATS4=[] #CREATING THE ARRAY THAT WILL STORE ALL OF THE KS4 CHEMISTRY QUESTIONS AND 1 WILL BE RANDOMLY SELECTED

   windowKS4chem = Tk()                                                              #DEFINING THE KS4 CHEMISTRY WINDOW 

   windowKS4chem.resizable (0,0)                                                     #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
   windowKS4chem.resizable (width=FALSE, height=FALSE)                               #THE USER CANNOT CHANGE THE SIZE OF THE MENU  
   windowKS4chem.title("GRAND CENTRAL SCIENCE QUESTION GENERATOR - KS4 Chemistry")   #GIVING THE WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
   windowKS4chem.geometry("500x600")                                                 #CONFIGURING THE FIXED SIZE OF THE WINDOW WHICH WILL ALWAYS BE THIS SIZE            
   windowKS4chem.configure(background='white')                                       #CONFIGURING THE BACKGROUND OF THE WINDOW TO BE WHITE

   time = datetime.datetime.now()                                                    #ALLOWS THE PROGRAM TO GATHER THE CURRENT TIME
       
   TIME=Label(windowKS4chem, text="SYSTEM TIME: "+str(time.strftime("%Y-%m-%d %H:%M")),bg="white") #CREATING A LABEL THAT WILL DISPLAY THE CURRENT TIME IN THE FORMAT Y-M-D AND H:M
   
   l=Label(windowKS4chem, text=" ",bg="white")                                  #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE
   Q=Label(windowKS4chem,text=str(random.choice(CHEM4)))                        #CREATING A LABEL THAT WILL SELECTED ONE OF THE QUESTIONS RANDOMLY AND THEN DISPLAY IT

   l1=Label(windowKS4chem, text=" ",bg="white")                                 #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE

   l2=Label(windowKS4chem, text="Do YOU want another question? ",bg="white")    #CREATING A LABEL THAT WILL ASK THE USER IF THEY WOULD LIKE ANOTHER QUESTION

   l3=Label(windowKS4chem, text=" ",bg="white")                                 #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE

   def KS4button():
       windowKS4chem.destroy()  #CLOSING THE WINDOW WITH THE USE OF THE '.destroy()' FUNCTION WITHIN TKINTER

   def KS4Button():
       windowKS4chem.destroy()  #CLOSING THE WINDOW WITH THE USE OF THE '.destroy()' FUNCTION WITHIN TKINTER
       KS4chem()                #REPEATING THE FUNCTION SO THAT IT WILL GENERATE ANOTHER QUESTION
    
   b1=Button(windowKS4chem, text="   YES   ", fg="green", command=KS4Button) #CREATING A BUTTON THAT WILL RUN THE FUNCTION AGAIN ALLOWING FOR THE USER TO GET ANOTHER QUESTION  
   b2=Button(windowKS4chem, text="   NO    ", fg="red", command=KS4button)   #CREATING A BUTTON THAT WILL TAKE THE USER BACK TO THE MAIN MENU
    
   TIME.pack()            #DISPLAYING THE CURRET TIME LABEL
   l.pack()               #DISPLAYING THE LABEL WITHIN THE MENU WINDOW 
   Q.pack()               #DISPLAYING THE RANDOMLY SELECTED QUESTION  
   l1.pack()              #DISPLAYING THE LABEL WITHIN THE MENU WINDOW 
   l2.pack()              #DISPLAYING THE 'Do YOU want another question?' LABEL
   l3.pack()              #DISPLAYING THE LABEL WITHIN THE MENU WINDOW 
   b1.pack()              #DISPLAYING THE 'Yes' BUTTON 
   b2.pack()              #DISPLAYING THE 'No' BUTTON

   windowKS4chem.mainloop()

def KS4FURTHER():

   RURTHER4=[] #CREATING THE ARRAY THAT WILL STORE ALL OF THE KS4 PHYSICS QUESTIONS AND 1 WILL BE RANDOMLY SELECTED
   
   windowKS4phy = Tk()                                                            #DEFINING THE KS4 PHYSICS WINDOW 

   windowKS4phy.resizable (0,0)                                                   #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
   windowKS4phy.resizable (width=FALSE, height=FALSE)                             #THE USER CANNOT CHANGE THE SIZE OF THE MENU  
   windowKS4phy.title("GRAND CENTRAL SCIENCE QUESTION GENERATOR - KS4 Physics")   #GIVING THE WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
   windowKS4phy.geometry("500x600")                                               #CONFIGURING THE FIXED SIZE OF THE WINDOW WHICH WILL ALWAYS BE THIS SIZE            
   windowKS4phy.configure(background='white')                                     #CONFIGURING THE BACKGROUND OF THE WINDOW TO BE WHITE

   time = datetime.datetime.now()                                                 #ALLOWS THE PROGRAM TO GATHER THE CURRENT TIME
       
   TIME=Label(windowKS4phy, text="SYSTEM TIME: "+str(time.strftime("%Y-%m-%d %H:%M")),bg="white") #CREATING A LABEL THAT WILL DISPLAY THE CURRENT TIME IN THE FORMAT Y-M-D AND H:M
   
   l=Label(windowKS4phy, text=" ",bg="white")                                  #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE
   Q=Label(windowKS4phy,text=str(random.choice(PHY4)))                         #CREATING A LABEL THAT WILL SELECTED ONE OF THE QUESTIONS RANDOMLY AND THEN DISPLAY IT

   l1=Label(windowKS4phy, text=" ",bg="white")                                 #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE

   l2=Label(windowKS4phy, text="Do YOU want another question? ",bg="white")    #CREATING A LABEL THAT WILL ASK THE USER IF THEY WOULD LIKE ANOTHER QUESTION

   l3=Label(windowKS4phy, text=" ",bg="white")                                 #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE

   def KS4button():
       windowKS4phy.destroy()  #CLOSING THE WINDOW WITH THE USE OF THE '.destroy()' FUNCTION WITHIN TKINTER

   def KS4Button():
       windowKS4phy.destroy()  #CLOSING THE WINDOW WITH THE USE OF THE '.destroy()' FUNCTION WITHIN TKINTER
       KS4phy()                #REPEATING THE FUNCTION SO THAT IT WILL GENERATE ANOTHER QUESTION
    
   b1=Button(windowKS4phy, text="   YES   ", fg="green", command=KS4Button) #CREATING A BUTTON THAT WILL RUN THE FUNCTION AGAIN ALLOWING FOR THE USER TO GET ANOTHER QUESTION  
   b2=Button(windowKS4phy, text="   NO    ", fg="red", command=KS4button)   #CREATING A BUTTON THAT WILL TAKE THE USER BACK TO THE MAIN MENU
    
   TIME.pack()            #DISPLAYING THE CURRET TIME LABEL
   l.pack()               #DISPLAYING THE LABEL WITHIN THE MENU WINDOW 
   Q.pack()               #DISPLAYING THE RANDOMLY SELECTED QUESTION  
   l1.pack()              #DISPLAYING THE LABEL WITHIN THE MENU WINDOW 
   l2.pack()              #DISPLAYING THE 'Do YOU want another question?' LABEL
   l3.pack()              #DISPLAYING THE LABEL WITHIN THE MENU WINDOW 
   b1.pack()              #DISPLAYING THE 'Yes' BUTTON 
   b2.pack()              #DISPLAYING THE 'No' BUTTON

   windowKS4phy.mainloop()
   
def option1():
    HELP()

b1 = Button(window, text="HELP", fg="purple", command=option1)        #CREATING THE HELP BUTTON WHICH WILL TAKE THE USER TO HELP MENU SO THEY KNOW WHAT TO DO 
b1.pack()                                                             #DISPLAYING THE BUTTON ON THE MAIN MENU 

l = Label(window, text=" ",bg="white")                                #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE
l.pack()                                                              #DISPLAYING THE LABEL WITHIN THE MAIN MENU WINDOW

def option2():
    KS1()    

b1 = Button(window, text="                Key Stage 1                ", command=option2)  #CREATING THE KEY STAGE 1 BUTTON WHICH WILL TAKE THEM TO THE KS1 QUESTIONS 
b1.pack()                                                                                 #DISPLAYING THE BUTTON ON THE MIAN MENU       

def option3():
    KS2()
    
b1 = Button(window, text="                Key Stage 2                ", command=option3)  #CREATING THE KEY STAGE 2 BUTTON WHICH WILL TAKE THEM TO THE KS2 QUESTIONS
b1.pack()                                                                                 #DISPLAYING THE BUTTON ON THE MIAN MENU 

def option4():
    KS3()

b1 = Button(window, text="                Key Stage 3                ", command=option4)  #CREATING THE KEY STAGE 3 BUTTON WHICH WILL TAKE THEM TO THE KS3 QUESTIONS
b1.pack()                                                                                 #DISPLAYING THE BUTTON ON THE MIAN MENU

def option5():
    KS4()

b1 = Button(window, text="                Key Stage 4                ", command=option5)  #CREATING THE KEY STAGE 4 BUTTON WHICH WILL TAKE THEM TO THE KS4 MENU
b1.pack()                                                                                 #DISPLAYING THE BUTTON ON THE MIAN MENU

l5 = Label(window, text=" ",bg="white")                                                   #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE
l5.pack()                                                                                 #DISPLAY THE LABEL WITHIN THE MAIN MENU WINDOW

def option14():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\TK_MSTR_v3.py") #FILE DIRECTORY FOR THE USERS GRAND CENTRAL 
    window.destroy()                                                                                                                      #CLOSING THE WINDOW WITH THE USE OF THE '.destroy()' FUNCTION WITHIN TKINTER 

b15 = Button(window, text="BACK",command=option14) #CREATING THE BACK BUTTON THAT WILL TAKE THE USER BACK TO THEIR GRAND CENTRAL MAIN MENU 
b15.pack()                                         #DISPLAYING THE BUTTON ON THE MIAN MENU 

mainloop()
