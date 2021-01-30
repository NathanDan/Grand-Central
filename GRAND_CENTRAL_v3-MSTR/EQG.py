#TKinter GC EQG
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
window.title ("GRAND CENTRAL ENGLISH QUESTION GENERATOR") #GIVING THE WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
window.geometry("500x300")                                #CONFIGURING THE FIXED SIZE OF THE WINDOW WHICH WILL ALWAYS BE THIS SIZE            
window.configure(background='white')                      #CONFIGURING THE BACKGROUND OF THE WINDOW TO BE WHITE

l2 = Label(window, text=" ",bg="white")                                                    #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE
l2.pack()                                                                                  #DISPLAY THE LABEL WITHIN THE MENU WINDOW 

l0 = Label(window, text="ENGLISH QUESTION GENERATOR",font='Helvetica 16 bold' ,bg="white") #GIVING THE WINDOW A TITLE SO THE USER/CLIENT KNOWS WHAT MENU THEY ARE ON 
l0.pack()                                                                                  #DISPLAYING THE TITLE FOR THE USER/CLIENT TO SEE

l5 = Label(window, text=" ",bg="white")                                                    #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE
l5.pack()                                                                                  #DISPLAY THE LABEL WITHIN THE MENU WINDOW   

def HELP():

    windowHELP = Tk()                                                    #DEFINING THE HELP WINDOW'S NAME

    windowHELP.resizable (0,0)                                           #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
    windowHELP.resizable (width=FALSE, height=FALSE)                     #THE USER CANNOT CHANGE THE SIZE OF THE MENU  
    windowHELP.title("GRAND CENTRAL ENGLISH QUESTION GENERATOR - HELP")  #GIVING THE WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
    windowHELP.geometry("500x400")                                       #CONFIGURING THE FIXED SIZE OF THE WINDOW WHICH WILL ALWAYS BE THIS SIZE            
    windowHELP.configure(background='white')                             #CONFIGURING THE BACKGROUND OF THE WINDOW TO BE WHITE

    time = datetime.datetime.now()                                       #ALLOWS THE PROGRAM TO GATHER THE CURRENT TIME
        
    TIME=Label(windowHELP, text="SYSTEM TIME: "+str(time.strftime("%Y-%m-%d %H:%M")),bg="white") #CREATING A LABEL THAT WILL DISPLAY THE CURRENT TIME
    l=Label(windowHELP, text=" ",bg="white")                                                     #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE
    HELP=Label(windowHELP,text=""" HELP! 

The program is designed to randomly select a english question for the
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

   KS1=["""Point out the the full stop below.

The classroom display is great. ""","""Tick the correct option to complete the sentence below.

___________ going to Jasvir’s party.

Tick one.

Were’ 
W’ere
Wer’e
We’re ""","""Tick the correct word to complete the sentence below.
It was raining heavily, _____________ Fatima went out to play.

Tick one.

but
if
or
that ""","""Point out the adjective in the sentence below.

The tree was taller than the house. ""","""What type of word is in CAPITAL in the sentence below?
We saw the BOAT move across the pond.
           
Tick one.

a verb
a noun
an adjective
an adverb ""","""Add two letters to the word happy to make a word that means
not happy.

We went to a football game. Our team lost and I
was very __happy. ""","""Point the adverb out in the sentence below.

We all sang loudly in assembly. ""","""Select the two nouns in the sentence below.

We played with our cat in the garden.
   ------          --- --     ------ ""","""Look at the parts of the words in CAPITALS.

cheerFUL     helpED     hopeLESS     kindNESS

What is the name for this part of the word?

Tick one.

an adverb
a noun phrase
a suffix
a verb ""","""Select one word in the sentence below that can be replaced with
the word if.

My friend and I ride our bikes to school when the
weather is good. ""","""Which punctuation mark is needed in the sentence below?

Charlie read a story a poem and a letter.

Tick one.

a comma
an apostrophe
a question mark
an exclamation mark ""","""Which option is punctuated correctly?

Tick one.

My sister loves netball she plays every Saturday
my sister loves netball She plays every Saturday.
My sister loves netball. She plays every Saturday.
my sister loves netball. she plays every Saturday ""","""The sentence below should all be in the past tense.

Select one word that needs to be changed.

The swimming pool was closed so Ted plays in the park. """] #CREATING THE ARRAY THAT WILL STORE ALL OF THE KS1 QUESTIONS AND 1 WILL BE RANDOMLY SELECTED 


   windowKS1 = Tk()                                                    #DEFINING THE KS1 WINDOW 

   windowKS1.resizable (0,0)                                           #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
   windowKS1.resizable (width=FALSE, height=FALSE)                     #THE USER CANNOT CHANGE THE SIZE OF THE MENU  
   windowKS1.title("GRAND CENTRAL ENGLISH QUESTION GENERATOR - KS1")   #GIVING THE WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
   windowKS1.geometry("500x350")                                       #CONFIGURING THE FIXED SIZE OF THE WINDOW WHICH WILL ALWAYS BE THIS SIZE            
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

   KS2=["""Insert a comma in the correct place in the sentence below.

Although he was the youngest Tom was one of the tallest. ""","""Which sentence must end with a question mark?

Tick one.

What happened that day might never be known
What really happened that day
Someone must know what really happened that day
I’d like to know what happened that day ""","""The prefix re- can be added to the root word play to make the
word replay.
 
Tick the meaning of the word replay.

Tick one.

to play together
to play later
to play again
to play badly ""","""Add two commas to the sentence below to make it clear that Ana
has four favourite things.

Ana’s favourite things are camping holidays cycling and swimming. ""","""Tick the adverb in the sentence below.

Tick one.
 
The lively crowd cheered loudly when the rally car race began.
    ------               ------ ----     -----            ""","""Insert a pair of commas in the correct place in the sentence below.

My father who works at the museum gave my class a guided tour. ""","""Which sentence is grammatically correct?

Tick one.

Tomorrow we went shopping at the sales.
In three weeks’ time, I will be on holiday.
Next weekend, we had gone to the river to fish.
Last summer, we swim at the beach and collect seashells. ""","""Which verb is a synonym of the verb produce?

Tick one.

make
buy
sell
trade""","""Which sentence is a command?

Tick one.

You should bring a coat.
You will need a coat in case it rains.
I am going to bring a coat.
Bring a coat in case it rains. ""","""Soon after a Frenchman ____________ the first land speed
record, it was broken.

Tick one.

has set
had set
set
was setting """] #CREATING THE ARRAY THAT WILL STORE ALL OF THE KS2 QUESTIONS AND 1 WILL BE RANDOMLY SELECTED 

   windowKS2 = Tk()                                                    #DEFINING THE KS2 WINDOW 

   windowKS2.resizable (0,0)                                           #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
   windowKS2.resizable (width=FALSE, height=FALSE)                     #THE USER CANNOT CHANGE THE SIZE OF THE MENU  
   windowKS2.title("GRAND CENTRAL ENGLISH QUESTION GENERATOR - KS2")   #GIVING THE WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
   windowKS2.geometry("500x350")                                       #CONFIGURING THE FIXED SIZE OF THE WINDOW WHICH WILL ALWAYS BE THIS SIZE            
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

   KS3=["""Longer writing task

Rescued

Imagine you are an explorer who travels to faraway places.

On your last trip, things went wrong and you lost contact with the outside world.
After two weeks you were found, and now a magazine wants you to write about
your experience.

Below is what the magazine asks for:

Start at the point when you knew things were going wrong.

Include details about:
+ the difficulties you faced before you were found;
+ how you felt at each stage;
+ how the whole experience has affected you.

We want our readers to share the full drama and
excitment of your experience."""] #CREATING THE ARRAY THAT WILL STORE ALL OF THE KS3 QUESTIONS AND 1 WILL BE RANDOMLY SELECTED

   windowKS3 = Tk()                                                    #DEFINING THE KS3 WINDOW 

   windowKS3.resizable (0,0)                                           #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
   windowKS3.resizable (width=FALSE, height=FALSE)                     #THE USER CANNOT CHANGE THE SIZE OF THE MENU  
   windowKS3.title("GRAND CENTRAL ENGLISH QUESTION GENERATOR - KS3")   #GIVING THE WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
   windowKS3.geometry("500x600")                                       #CONFIGURING THE FIXED SIZE OF THE WINDOW WHICH WILL ALWAYS BE THIS SIZE            
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
    windowKS4.title ("GRAND CENTRAL ENGLISH QUESTION GENERATOR - KS4")  #GIVING THE WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
    windowKS4.geometry("500x250")                                       #CONFIGURING THE FIXED SIZE OF THE WINDOW WHICH WILL ALWAYS BE THIS SIZE            
    windowKS4.configure(background='white')                             #CONFIGURING THE BACKGROUND OF THE WINDOW TO BE WHITE


    l2 = Label(windowKS4, text=" ",bg="white")                          #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE
    l2.pack()                                                           #DISPLAYING THE LABEL WITHIN THE MENU WINDOW 

    l0 = Label(windowKS4, text="ENGLISH QUESTION GENERATOR - KS4",font='Helvetica 14 bold' ,bg="white") #GIVING THE WINDOW A TITLE SO THE USER KNOWS WHAT MENU THEY ARE ON 
    l0.pack()                                                                                           #DISPLAYING THE TITLE FOR THE USER TO SEE

    l5 = Label(windowKS4, text=" ",bg="white")                          #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE
    l5.pack()                                                           #DISPLAYING THE LABEL WITHIN THE MENU WINDOW                                  

    def KS4Lit():
        KS4LIT()                                                                                         #THE FUNCTION THAT HOLDS THE KS4 BIOLOGY QUESTIONS   

    b1 = Button(windowKS4, text="              Key Stage 4 - Literature               ", command=KS4Lit) #CREATING THE BUTTON THAT TAKES THEM TO KS4 LITERATURE
    b1.pack()                                                                                            #DISPLAYING THE BUTTON ON THE MENU       

    def KS4Lan():
        KS4LAN()                                                                                        #THE FUNCTION THAT HOLDS THE KS4 CHEMISTRY QUESTIONS   
    
    b1 = Button(windowKS4, text="               Key Stage 4 - Language              ", command=KS4Lan)    #CREATING THE BUTTON THAT TAKES THEM TO KS4 LANGUAGE
    b1.pack()                                                                                            #DISPLAYING THE BUTTON ON THE MENU 

    l3 = Label(windowKS4, text=" ",bg="white")                          #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE
    l3.pack()                                                           #DISPLAY THE LABEL WITHIN THE MENU WINDOW 

    def KS4button():
       windowKS4.destroy()                                              #CLOSING THE WINDOW WITH THE USE OF THE '.destroy()' FUNCTION WITHIN TKINTER

    b = Button(windowKS4, text="BACK",command=KS4button)                #CREATING THE BACK BUTTON THAT WILL TAKE THE USER BACK TO THE MAIN EQG MENU
    b.pack()                                                            #DISPLAYING THE BUTTON ON THE KS4 MENU 

    windowKS4.mainloop()

def KS4LIT():

   LIT4=["""THE QUESTION

Starting with this extract, how does Lady Macbeth use language to manipulate her husband in the play?

Write about:

how she persuades him to her point of view in this extract
how she uses her powers of persuasion in the rest of the play
The extract

MACBETH
We will proceed no further in this business.
He hath honoured me of late, and I have bought
Golden opinions from all sorts of people,
Which would be worn now in their newest gloss,
Not cast aside so soon.

LADY MACBETH
Was the hope drunk
Wherein you dressed yourself? Hath it slept since?
And wakes it now to look so green and pale
At what it did so freely? From this time,
Such I account thy love. Art thou afeard
To be the same in thine own act and valour
As thou art in desire? Wouldst thou have that
Which thou esteem'st the ornament of life,
And live a coward in thine own esteem,
Letting I dare not wait upon I would,
Like the poor cat i'th'adage?
MACBETH
Prithee, peace.
I dare do all that may become a man;
Who dares do more is none.

LADY MACBETH
What beast was't then
That made you break this enterprise to me?
When you durst do it, then you were a man.
And to be more than what you were, you would
Be so much more the man. Nor time, nor place
Did then adhere, and yet you would make both.
They have made themselves and that their fitness now
Does unmake you. I have given suck and know
How tender 'tis to love the babe that milks me:
I would, while it was smiling in my face,
Have plucked my nipple from his boneless gums
And dashed the brains out, had I so sworn
As you have done to this.

MACBETH
If we should fail?
LADY MACBETH
We fail?
But screw your courage to the sticking-place,
And we'll not fail.

Act 1 Scene 7 ""","""THE QUESTION

Starting with this extract, analyse how Shakespeare presents Capulet's attitudes towards his daughter, Juliet. How does he portray their relationship?

Write about:

+ How Shakespeare presents Capulet's attitudes and their relationship in this extract
+ How Shakespeare presents Capulet's attitudes and their relationship in the play as a whole

The extract

In this extract Capulet is telling Juliet about her forthcoming marriage to Paris.

CAPULET
Fie, fie, what, are you mad?
JULIET
Good father, I beseech you on my knees,
Hear me with patience but to speak a word.
[She kneels down]

CAPULET
Hang thee, young baggage, disobedient wretch!
I tell thee what: get thee to church a' Thursday
Or never after look me in the face.
Speak not, reply not, do not answer me.
My fingers itch. Wife, we scarce thought us blessed
That God had lent us but this only child,
But now I see this one is too much,
And that we have a curse in having her.
Out on her, hilding!

Act 3 Scene 5 """, """THE QUESTION

How does Shakespeare present the character of Benedick?

Write about:

+ how Shakespeare presents Benedick in this extract
+ how Shakespeare presents Benedick at the start of the play

The extract

BENEDICK
They say the lady is fair; 'tis a
truth, I can bear them witness; and virtuous; 'tis
so, I cannot reprove it; and wise, but for loving
me; by my troth, it is no addition to her wit, nor
no great argument of her folly, for I will be
horribly in love with her. I may chance have some
odd quirks and remnants of wit broken on me,
because I have railed so long against marriage: but
doth not the appetite alter? a man loves the meat
in his youth that he cannot endure in his age.
Shall quips and sentences and these paper bullets of
the brain awe a man from the career of his humour?
No, the world must be peopled. When I said I would
die a bachelor, I did not think I should live till I
were married. Here comes Beatrice. By this day!
she's a fair lady: I do spy some marks of love in
her.

Act 2 Scene 3 ""","""THE QUESTION

How does Priestley present Mr Birling in An Inspector Calls?

Write about:

+ how Mr Birling is presented in this extract
+ how Priestley uses Mr Birling to get his ideas across in the rest of the play

The extract

GERALD (AMUSED)
Sounds a bit fishy to me.

BIRLING (TAKING IT IN THE SAME MANNER)
Yes, you don't know what some of these boys get up to nowadays. More money to spend and time to spare than I had when I was Eric’s age. They worked us hard in those days and kept us short of cash. Though even then – we broke out and had a bit of fun sometimes.

GERALD
I'll bet you did.

BIRLING (SOLEMNLY)
But this is the point. I don't want to lecture you two young fellows again. But what so many of you don't seem to understand now, when things are so much easier, is that a man has to make his own way - has to look after himself - and his family too, of course, when he has one - and so long as he does that he won't come to much harm. But the way some of these cranks talk and write now, you'd think everybody has to look after everybody else, as if we were all mixed up together like bees in a hive - community and all that nonsense. But take my word for it, you youngsters - and I’ve learnt in the good hard school of experience - that a man has to mind his own business and look after himself and his own - and -

WE HEAR THE SHARP RING OF A DOOR BELL. BIRLING STOPS TO LISTEN.

BIRLING
Edna'll answer it. Well, have another glass of port, Gerald - and then we'll join the ladies. That'll stop me giving you good advice.

ERIC
Yes, you've piled it on a bit tonight, Father.

BIRLING
Special occasion. And feeling contented, for once, I wanted you to have the benefit of my experience.

Act One ""","""THE QUESTION

How does Dickens present the redeemed character of Scrooge?

Write about:

+ how Dickens presents Scrooge in this extract
+ how Dickens presents Scrooge at the start of the novella

The extract

"I don't know what to do!" cried Scrooge, laughing and crying in the same breath; and making a perfect Laocoön of himself with his stockings. "I am as light as a feather, I am as happy as an angel, I am as merry as a schoolboy. I am as giddy as a drunken man. A merry Christmas to everybody! A happy New Year to all the world. Hallo here! Whoop! Hallo!"

He had frisked into the sitting-room, and was now standing there: perfectly winded.

"There's the saucepan that the gruel was in!" cried Scrooge, starting off again, and going round the fireplace.

"There's the door, by which the Ghost of Jacob Marley entered! There's the corner where the Ghost of Christmas Present, sat! There's the window where I saw the wandering Spirits! It's all right, it's all true, it all happened. Ha ha ha!"

Really, for a man who had been out of practice for so many years, it was a splendid laugh, a most illustrious laugh. The father of a long, long line of brilliant laughs!

From Stave V, A Christmas Carol ""","""THE QUESTION

Starting with this extract, how does Stevenson present Mr Hyde to be an evil, unforgiving criminal?

Write about:

+ how Stevenson presents Mr Hyde in this extract
+ how Stevenson presents Mr Hyde as an evil, unforgiving criminal in the novel as a whole

The extract

Read the extract from Chapter 4 titled The Carew Murder Case.

Presently her eye wandered to the other, and she was surprised to recognise in him a certain Mr Hyde, who had once visited her master,
and for whom she had conceived a dislike. He had in his hand a heavy cane, with which he was trifling;
but he answered never a word, and seemed to listen with an ill-contained impatience. And then all of a
sudden he broke out in a great flame of anger, stamping with his foot, brandishing the cane,
and carrying on (as the maid described it) like a madman. The very old gentleman took a step back,
with the air of one very much surprised and a trifle hurt; and at that Mr Hyde broke out of all bounds,
and clubbed him to the earth. And next moment, with ape-like fury, he was trampling his victim under foot,
and hailing down a storm of blows, under which the bones were audibly shattered and the body jumped upon the roadway.
At the horror of these sights and sounds, the maid fainted. """] #CREATING THE ARRAY THAT WILL STORE ALL OF THE KS4 BIOLOGY QUESTIONS AND 1 WILL BE RANDOMLY SELECTED

   windowKS4bio = Tk()                                                            #DEFINING THE KS4 BIOLOGY WINDOW 

   scrollbarY = Scrollbar(windowKS4bio)    #DEFING THE SCROLLBAR THAT WILL ASSIGNED TO THE WINDOW 
   scrollbarY.pack(side=RIGHT, fill=Y)   #TELLING THE PROGRAM WHERE TO PLACE THE SCROLLBAR
    
   windowKS4bio.resizable (0,0)                                                   #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
   windowKS4bio.resizable (width=FALSE, height=FALSE)                             #THE USER CANNOT CHANGE THE SIZE OF THE MENU  
   windowKS4bio.title("GRAND CENTRAL ENGLISH QUESTION GENERATOR - KS4 Litreture") #GIVING THE WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
   windowKS4bio.geometry("500x600")                                               #CONFIGURING THE FIXED SIZE OF THE WINDOW WHICH WILL ALWAYS BE THIS SIZE            
   windowKS4bio.configure(background='white')                                     #CONFIGURING THE BACKGROUND OF THE WINDOW TO BE WHITE

   time = datetime.datetime.now()                                                 #ALLOWS THE PROGRAM TO GATHER THE CURRENT TIME
       
   TIME=Label(windowKS4bio, text="SYSTEM TIME: "+str(time.strftime("%Y-%m-%d %H:%M")),bg="white") #CREATING A LABEL THAT WILL DISPLAY THE CURRENT TIME IN THE FORMAT Y-M-D AND H:M
   
   l=Label(windowKS4bio, text=" ",bg="white")                                                     #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE
   Q=Text(windowKS4bio, height=25, width=400, background="light grey", wrap=WORD, yscrollcommand=scrollbarY.set) #CREATING A LABEL THAT WILL SELECTED ONE OF THE QUESTIONS RANDOMLY AND THEN DISPLAY IT

   l1=Label(windowKS4bio, text=" ",bg="white")                                 #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE

   l2=Label(windowKS4bio, text="Do YOU want another question? ",bg="white")    #CREATING A LABEL THAT WILL ASK THE USER IF THEY WOULD LIKE ANOTHER QUESTION

   l3=Label(windowKS4bio, text=" ",bg="white")                                 #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE

   def KS4button():
       windowKS4bio.destroy()  #CLOSING THE WINDOW WITH THE USE OF THE '.destroy()' FUNCTION WITHIN TKINTER

   def KS4Button():
       windowKS4bio.destroy()  #CLOSING THE WINDOW WITH THE USE OF THE '.destroy()' FUNCTION WITHIN TKINTER
       KS4LIT()                #REPEATING THE FUNCTION SO THAT IT WILL GENERATE ANOTHER QUESTION
    
   b1=Button(windowKS4bio, text="   YES   ", fg="green", command=KS4Button) #CREATING A BUTTON THAT WILL RUN THE FUNCTION AGAIN ALLOWING FOR THE USER TO GET ANOTHER QUESTION  
   b2=Button(windowKS4bio, text="   NO    ", fg="red", command=KS4button)   #CREATING A BUTTON THAT WILL TAKE THE USER BACK TO THE MAIN MENU

   Q.insert(END,str(random.choice(LIT4))) 
   TIME.pack()                           #DISPLAYING THE CURRET TIME LABEL
   l.pack()                              #DISPLAYING THE LABEL WITHIN THE MENU WINDOW 
   Q.pack()                              #DISPLAYING THE RANDOMLY SELECTED QUESTION  
   l1.pack()                             #DISPLAYING THE LABEL WITHIN THE MENU WINDOW 
   l2.pack()                             #DISPLAYING THE 'Do YOU want another question?' LABEL
   l3.pack()                             #DISPLAYING THE LABEL WITHIN THE MENU WINDOW 
   b1.pack()                             #DISPLAYING THE 'Yes' BUTTON 
   b2.pack()                             #DISPLAYING THE 'No' BUTTON
   scrollbarY.config(command=Q.yview)

   windowKS4bio.mainloop()

def KS4LAN():

   LAN4=["""THE QUESTION

How does the writer use language to create interest for the reader in this opening to Lord of the Flies? (10 marks)

Extract

The boy with fair hair lowered himself down the last few feet of rock and began to pick his way toward the lagoon. Though he had taken off his school sweater and trailed it now from one hand, his grey shirt stuck to him and his hair was plastered to his forehead. All round him the long scar smashed into the jungle was a bath of heat. He was clambering heavily among the creepers and broken trunks when a bird, a vision of red and yellow, flashed upwards with a witch-like cry; and this cry was echoed by another.

“Hi!” it said. “Wait a minute!” The undergrowth at the side of the scar was shaken and a multitude of raindrops fell pattering.

“Wait a minute,” the voice said. “I got caught up.”

The fair boy stopped and jerked his stockings with an automatic gesture that made the jungle seem for a moment like the Home Counties.

Lord of the Flies, William Golding ""","""THE QUESTION

Refer to both Extract 1 and Extract 2.

Compare how the two writers convey different attitudes towards helping homeless people.

In your answer, you should:

+ compare their attitudes
+ compare the methods they use to convey their attitudes
+ support your ideas with quotations from both texts

Extract 1:

Spend a night on the streets for a Nottingham homeless charity by Ben Ireland, The Nottingham Post, September 10, 2015.

Sleeping bags and cardboard boxes at the ready, volunteers are preparing to brave the cold in a sponsored night on the streets for a Nottingham homeless charity.

Framework opens registration for its annual Big Sleep Out event in Sneinton Market, first launched in 1992, this week.

The 2015 theme is Robin Hood, and themed entries are expected in the traditional Box Factor competition for the best designed box on the night.

Fundraiser Sarah Cross said: "The Big Sleep Out is the most popular event in our annual calendar for two reasons: it helps raise money for a very important cause and is also great fun.

"It is a real family event and always has a great atmosphere. Taking part is truly an experience to remember and I look forward to welcoming people to this year's event."

Chris Kershaw, senior PR assistant at The Nottingham Building Society, is taking part in his fourth sleep out.

He said: "I think it's important that people experience the extreme conditions. We only have to do it for one night, but we must remember homeless people don't have the privilege to pick and choose when they sleep out."

Mr Kershaw, 39, of Spondon, said the charity was close to his heart because of mental health and addiction issues in his family.

"It might surprise readers, but the sleep out is actually really fun. Being homeless certainly isn't, but there's a real community effort in this event.

"One year I met a guy who went home at 11pm. When I asked him why he said he'd come down to say thank you because he used to live on the streets. That made me realise that the work the charity is doing really is helping."

Participants are asked to raise at least £50 in sponsorship. Last year's event brought in more than £30,000 to Framework's work preventing homelessness and helping people into accommodation.

Framework is also backing the Post's Good Deeds Nottsem> campaign.

This year's event takes place on Saturday, November 21 from 7.45pm to 7am on Sunday 22.

Spend a night on the streets for a Nottingham homeless charity, Ben Ireland for the Nottingham Post 2015

Extract 2:

Night Walks (1861). An essay by Charles Dickens – here Dickens writes about a homeless man and homeless children that he sees in London during the night.

Suddenly, a thing that in a moment more I should have trodden upon without seeing, rose up at my feet with a cry of loneliness and houselessness, the like of which I never heard. We then stood face to face looking at one another, frightened by one another. The creature was like a beetle-browed hair-lipped youth of twenty, and it had a loose bundle of rags on, which it held together with one of its hands. It shivered from head to foot, and its teeth chattered, and as it stared at me - persecutor, devil, ghost, whatever it thought me--it made with its whining mouth as if it were snapping at me, like a worried dog.

Intending to give this ugly object money, I put out my hand to stay it for it recoiled as it whined and snapped and laid my hand upon its shoulder. Instantly, it twisted out of its garment … and left me standing alone with its rags in my hands.

Covent-garden Market, when it was market morning, was wonderful company. But one of the worst night sights I know in London, is to be found in the children who prowl about this place; who sleep in the baskets, fight for the offal, dart at any object they think they can lay their thieving hands on, dive under the carts and barrows, dodge the constables, and are perpetually making a blunt pattering on the pavement of the Piazza with the rain of their naked feet.

A painful and unnatural result comes of the comparison one is forced to institute between the growth of corruption as displayed in the so much improved and cared for fruits of the earth, and the growth of corruption as displayed in these all uncared for (except inasmuch as ever-hunted) savages.

Night Walks, Charles Dickens 1861 ""","""THE QUESTION

Compare how the two writers convey their attitudes towards food and the people they are visiting.

In your answer you should:

+ compare their different attitudes
+ compare the methods they use to convey their attitudes
+ support your ideas with references to both texts

Extract A
Here is an extract from a cookery book published in 1855, Soyer’s Shilling Cookery for the People. The writer, Alexis Soyer describes a visit to a house in St Giles, a poor area of London.

Having but little confidence in what they would provide, I bought a quarter of a pound of ground coffee, intending giving them a lesson in how to make coffee. On my arrival, I was received like a princess in a fairy land. The little parlour was not only clean, but ornamented, at a cost of a few pence, with wall flowers from the neighbouring garden (the best in the world, Covent Garden), generously dispensing their perfume over pyramids of muffins and crumpets. Having cordially shaken hands with my host, I set cheerfully to work, and got hold of an old pitcher, but clean; in it I put the coffee and placed it close before the fire, begging the old lady to keep turning it round, and stirring it til the powder was hot. I then poured three quarts of boiling water, allowed it to stand for ten minutes, and then poured it out into the cups, with the best milk that could be got, and sugar.

Soyer’s Shilling Cookery for the People, Alexis Soyer

Extract B
Here is an extract from a restaurant review written in 2016.

I reserved our table three months ago. This might seem extreme. But if you’re going to eat at a restaurant where the food is hand-picked from its very own walled-garden, I’ve discovered that a window seat is essential. I like to see precisely where my food has come from. And I’m convinced it makes the flavours more intense.

Besides, (restaurant name) has developed such a reputation for quality that if you don’t get your booking in quick, you won’t get a table at all.

It’s the first time my dining companion has been here. She is suitably wowed by the winding lanes we walk down to reach the restaurant. (It seems too ironic to drive to an establishment where the food miles are practically zero.) And she’s impressed by the view of the Mendips that greets us at the gate.

Before we go indoors, we wander through the walled-garden, admiring rows of velvety Cavolo Nero, feathered plumes of carrots, earthy globes of beets. This really is food at its freshest.

At the door we are welcomed by the most cheerful waiter I’ve ever met. His broad smile and enthusiastic discussion of the menu suggest that this is someone entirely suited to his work. I trust him immediately. In fact he makes me want to throw caution to the wind and I find myself forgoing choice completely and entrusting him to recommend a starter and a main.

‘Are you feeling OK?’ asks my companion.

‘Don’t worry,’ I say. ‘I’ll choose my own dessert.’

Restaurant review, 2016 """] #CREATING THE ARRAY THAT WILL STORE ALL OF THE KS4 CHEMISTRY QUESTIONS AND 1 WILL BE RANDOMLY SELECTED

   windowKS4chem = Tk()                                                              #DEFINING THE KS4 CHEMISTRY WINDOW 

   scrollbarY = Scrollbar(windowKS4chem)    #DEFING THE SCROLLBAR THAT WILL ASSIGNED TO THE WINDOW 
   scrollbarY.pack(side=RIGHT, fill=Y)   #TELLING THE PROGRAM WHERE TO PLACE THE SCROLLBAR
    
   windowKS4chem.resizable (0,0)                                                     #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
   windowKS4chem.resizable (width=FALSE, height=FALSE)                               #THE USER CANNOT CHANGE THE SIZE OF THE MENU  
   windowKS4chem.title("GRAND CENTRAL ENGLISH QUESTION GENERATOR - KS4 Language")    #GIVING THE WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
   windowKS4chem.geometry("500x600")                                                 #CONFIGURING THE FIXED SIZE OF THE WINDOW WHICH WILL ALWAYS BE THIS SIZE            
   windowKS4chem.configure(background='white')                                       #CONFIGURING THE BACKGROUND OF THE WINDOW TO BE WHITE

   time = datetime.datetime.now()                                                    #ALLOWS THE PROGRAM TO GATHER THE CURRENT TIME
       
   TIME=Label(windowKS4chem, text="SYSTEM TIME: "+str(time.strftime("%Y-%m-%d %H:%M")),bg="white") #CREATING A LABEL THAT WILL DISPLAY THE CURRENT TIME IN THE FORMAT Y-M-D AND H:M
   
   l=Label(windowKS4chem, text=" ",bg="white")                                  #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE
   Q=Text(windowKS4chem, height=25, width=400, background="light grey", wrap=WORD, yscrollcommand=scrollbarY.set)                      #CREATING A LABEL THAT WILL SELECTED ONE OF THE QUESTIONS RANDOMLY AND THEN DISPLAY IT

   l1=Label(windowKS4chem, text=" ",bg="white")                                 #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE

   l2=Label(windowKS4chem, text="Do YOU want another question? ",bg="white")    #CREATING A LABEL THAT WILL ASK THE USER IF THEY WOULD LIKE ANOTHER QUESTION

   l3=Label(windowKS4chem, text=" ",bg="white")                                 #CREATING A LABEL THAT WILL DISPLAY NOTHING SO WILL ACT LIKE A ONE LINE SPACE

   def KS4button():
       windowKS4chem.destroy()  #CLOSING THE WINDOW WITH THE USE OF THE '.destroy()' FUNCTION WITHIN TKINTER

   def KS4Button():
       windowKS4chem.destroy()  #CLOSING THE WINDOW WITH THE USE OF THE '.destroy()' FUNCTION WITHIN TKINTER
       KS4LAN()                #REPEATING THE FUNCTION SO THAT IT WILL GENERATE ANOTHER QUESTION
    
   b1=Button(windowKS4chem, text="   YES   ", fg="green", command=KS4Button) #CREATING A BUTTON THAT WILL RUN THE FUNCTION AGAIN ALLOWING FOR THE USER TO GET ANOTHER QUESTION  
   b2=Button(windowKS4chem, text="   NO    ", fg="red", command=KS4button)   #CREATING A BUTTON THAT WILL TAKE THE USER BACK TO THE MAIN MENU

   Q.insert(END,str(random.choice(LAN4)))  
   TIME.pack()            #DISPLAYING THE CURRET TIME LABEL
   l.pack()               #DISPLAYING THE LABEL WITHIN THE MENU WINDOW 
   Q.pack()               #DISPLAYING THE RANDOMLY SELECTED QUESTION  
   l1.pack()              #DISPLAYING THE LABEL WITHIN THE MENU WINDOW 
   l2.pack()              #DISPLAYING THE 'Do YOU want another question?' LABEL
   l3.pack()              #DISPLAYING THE LABEL WITHIN THE MENU WINDOW 
   b1.pack()              #DISPLAYING THE 'Yes' BUTTON 
   b2.pack()              #DISPLAYING THE 'No' BUTTON

   windowKS4chem.mainloop()

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
