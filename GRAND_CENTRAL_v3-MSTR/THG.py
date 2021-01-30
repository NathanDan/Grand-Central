#Nathan Jones
#GRAND CENTRAL - THG MSTR EDITION
#2018

from datetime import datetime #ALLOWING THE DATE AND TIME TO BE DISPLAYED

import time         #THIS ALLOWS FOR THE PROGRAM TO USE THE SLEEP FUNCTION WITHIN THE PROGRAM
import sys          #ALLOWS ACCESS TO THE SYSTEM FROM WITHIN PYTHON 
import os.path      #ALLOWS THE PROGRAM TO OPEN OTHER SPECIFIC APPLICATIONS, IN THIS CASE THEGC MAIN MENU
import os           #ALLOWS FOR CONTROL OF THE MACHINE AND IS OS INCLUDING THE LIKES OF SAVING, OPENING/CLOSING FILES, ETC.
import string       #ALLOWS FOR DATA/ENTRIES TO BE RECOREDAS STRINGS AND NOT INDIVIDUAL CHARACTERS
import random       #THIS IMPORT ALLOWS FOR WORDS/LOCATIONS TO BE RANDOMLY SELECTED 
import statistics   #ALLOWS ACCESS TO THE STATISTICS LIBARY FOR THE DATA COLLECTION AND PROCESSING
import itertools    #ALLOWS ACCESS TO ACCESS TO THE ITERATORS LIBARY FOR EFFICENT LOOPING 
import datetime     #THIS ALLOWS FOR THE CURRENT TIME TO BE IMPORTED AND DISPLAYED FOR THE USER TO SEE 

Glo_Xsize=8         #SETTING THE SIZE OF THE X AXIS OF THE GRID TO BE 8             
Glo_Ysize=8         #SETTING THE SIZE OF THE Y AXIS OF THE GRID TO BE 8        
Glo_BADcount=5      #SETTING THE BANDIT COUNT IN THE GRID TO BE 5         
Glo_TRECHcount=0    #SETTING THE TREASURE CHEST COUNT IN THE GRID TO BE 10        
Glo_COINcount=0     #SETTING THE DEFAULT COIN COUNT OF THE PLAYER TO BE 0        
Glo_PLAYERx=0       #SETTING THE DEFAULT X POSITION OF THE PLAYER WHICH WILL BE IN THE BOTTOM LEFT OF THE SCREEN DUE TO ARRAY'S IN PYTHON STARTING AT 0 AND GOING FROM LEFT OT RIGHT        
Glo_PLAYERy=7       #SETTING THE DEFAULT Y POSITION OF THE PLAYER WHICH WILL BE IN THE BOTTOM LEFT OF THE SCREEN DUE TO ARRAY'S IN PYTHON STARTING AT 0 AND GOING FROM TOP TO BOTTOM        
Glo_Grid=[]         #CREATING AN EMPTY ARRAY FOR THE GRID OF THE TREASURE HUNT GAME       
Glo_DEBUG=False     #SETTING THE DEFAULT VALUE FOR THE DEBUG VARIABLE TO FALSE SO THAT ON A NORMAL GAME IT WILL NOT SHOW THE POSITIONS TO THE PLAYERS

LOOSE=["Unlucky on the GAME! Better luck next time!","Maybe next time!","Sooooo close, but so far...","It just wasn't your day today!"]               #LOSE MESSAGES - RANDOMLY SELECTED
WIN=["WELL DONE ON THE GAME! You Smashed it!","That was one hell of a game!","CONGRATULATIONS ON WINNING!","That was an IMPRESSIVE GAME! Well Done!"] #WIN MESSAGES - RANDOMLY SELECTED 
win=False                      #SETTING THE DEFAULT VALUE FOR WIN TO BE FALSE        
time = datetime.datetime.now() #ALLOWS GRAND CENTRAL TO GATHER THE CURRENT TIME 

def TREASURE_HUNT():

    print("""
████████╗██████╗ ███████╗ █████╗ ███████╗██╗   ██╗██████╗ ███████╗          
╚══██╔══╝██╔══██╗██╔════╝██╔══██╗██╔════╝██║   ██║██╔══██╗██╔════╝          
   ██║   ██████╔╝█████╗  ███████║███████╗██║   ██║██████╔╝█████╗            
   ██║   ██╔══██╗██╔══╝  ██╔══██║╚════██║██║   ██║██╔══██╗██╔══╝            
   ██║   ██║  ██║███████╗██║  ██║███████║╚██████╔╝██║  ██║███████╗          
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝          
                                                                            
██╗  ██╗██╗   ██╗███╗   ██╗████████╗     ██████╗  █████╗ ███╗   ███╗███████╗
██║  ██║██║   ██║████╗  ██║╚══██╔══╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
███████║██║   ██║██╔██╗ ██║   ██║       ██║  ███╗███████║██╔████╔██║█████╗  
██╔══██║██║   ██║██║╚██╗██║   ██║       ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
██║  ██║╚██████╔╝██║ ╚████║   ██║       ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝        ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝

""")
    menu() #TAKING THE PLAYER TO THE MENU OF THE GAME 

def Message():

    if win == True:                       #IF THE WIN VARIABLE IS SET TO TRUE THEN THE FOLLOWING WILL TAKE PLACE 
        print(WIN[random.randint(0,3)])   #SELECTING AT RANDOM AND THEN DISPLAYING ONE OF THE WINNING MESSAGES  
        print(" ")                        #PRINTING AN EMPTY SPACE TO ACT AS A SPACE
        menu()                            #TAKING THE PLAYER TO THE MENU OF THE GAME  

    elif win == False:                    #IF THE WIN VARIABLE IS SET TO FALSE THEN THE FOLLOWING WILL TAKE PLACE 
        print(LOOSE[random.randint(0,3)]) #SELECTING AT RANDOM AND THEN DISPLAYING ONE OF THE WINNING MESSAGES 
        print(" ")                        #PRINTING AN EMPTY SPACE TO ACT AS A SPACE 
        menu()                            #TAKING THE PLAYER TO THE MENU OF THE GAME 

def GridMaker():
    global Glo_Xsize                    #GIVING THE FUNCTION ACCESS TO 'Glo_Xsize' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY 
    global Glo_Ysize                    #GIVING THE FUNCTION ACCESS TO 'Glo_Ysize' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global Glo_BADcount                 #GIVING THE FUNCTION ACCESS TO 'Glo_BADcount' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global Glo_TRECHcount               #GIVING THE FUNCTION ACCESS TO 'Glo_TRECHcount' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global Glo_PLAYERx                  #GIVING THE FUNCTION ACCESS TO 'Glo_PLAYERx' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY    
    global Glo_PLAYERy                  #GIVING THE FUNCTION ACCESS TO 'Glo_PLAYERy' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY 
    global Glo_Grid                     #GIVING THE FUNCTION ACCESS TO 'Glo_Grid' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    Glo_Grid=[]                         #MAKING SURE THAT THE ARRAY OF 'Glo_Grid' IS EMPTY SO THAT IT CAN MAKE THE GRID

    for Y in range(1,Glo_Ysize +1):     #WHILST THE Y SIZE IS STILL IN RANGE SO THIS CASE 8 IT WILL CONTINUE TO DO THE FOLLOWING
        GridROW=[]                      #DETERMINING THE SIZE OF THE GRID 

        for X in range(1,Glo_Xsize +1): #WHILST THE Y SIZE IS STILL IN RANGE SO THIS CASE 8 IT WILL CONTINUE TO DO THE FOLLOWING
            GridROW.append("| ")        #CREATING THE GRID BOUNDARIES AND LINES THAT WILL MAKE UP THE GRID

        Glo_Grid.append(GridROW)        #COMBINING ALL THE DATA TOGETHER TO PRODUCE THE GRID TAHT THE USER WILL SEE

     
    for TC in range(0,Glo_TRECHcount):                  #WHILST THE TCS ARE STILL IN RANGE SO THIS CASE 10 IT WILL CONTINUE TO DO THE FOLLOWING - WHICH IS RANDOMLY PLACING THE CHESTS           
        used=True                                       #SETTING THE LOCAL VARIABLE TO TRUE 
        while used:                                     #WHILST USED IS EQUAL TO TRUE THE WHILE-LOOP WILL CONTINUE TO RUN  
            Xloc=random.randrange(0,Glo_Ysize)          #RANDOMLY ALLOCATING THE POSITIONS OF THE TREASURE CHESTS WITH THE GRID OF THE Y AXIS
            Yloc=random.randrange(0,Glo_Xsize)          #RANDOMLY ALLOCATING THE POSITIONS OF THE TREASURE CHESTS WITH THE GRID ON THE X AXIS

            if Xloc!=Glo_PLAYERx and Yloc!=Glo_PLAYERy: #MAKING SURE THAT THERE ARE NO TREASURE CHESTS WHERE THE PLAYER WILL BEGIN IN THE BOTTOM LEFT HAND CORNER  
                if Glo_Grid[Xloc][Yloc]== "| ":         #IF THERE IS AN EMPTY SQUARE ON THE GRID THEN THE FOLLOWING WILL HAPPEN
                    Glo_Grid[Xloc][Yloc]="|1"           #THIS IS THE SQUARE CONTAINING A TREASURE CHEST WILL LOOK LIKE - THE USER WILL NOT BE ABLE TO SEE THEM IN NORMAL MODE 
                    used=False                          #SETTING USED TO FALSE WHICH WILL STOP THE WHILE-LOOP


    for B in range(0,Glo_BADcount):                     #WHILST THE BS ARE STILL IN RANGE SO THIS CASE 5 IT WILL CONTINUE TO DO THE FOLLOWING - WHICH IS RANDOMLY PLACING THE BANDITS
        used=True                                       #SETTING THE LOCAL VARIABLE TO TRUE 
        while used:                                     #WHILST USED IS EQUAL TO TRUE THE WHILE-LOOP WILL CONTINUE TO RUN  
            Xloc=random.randrange(0,Glo_Ysize)          #RANDOMLY ALLOCATING THE POSITIONS OF THE BANDITS WITH THE GRID OF THE Y AXIS
            Yloc=random.randrange(0,Glo_Xsize)          #RANDOMLY ALLOCATING THE POSITIONS OF THE BANDITS WITH THE GRID OF THE X AXIS

            if Xloc!=Glo_PLAYERx and Yloc!=Glo_PLAYERy: #MAKING SURE THAT THERE ARE NO BANDITS WHERE THE PLAYER WILL BEGIN IN THE BOTTOM LEFT HAND CORNER 
                if Glo_Grid[Xloc][Yloc]== "| ":         #IF THERE IS AN EMPTY SQUARE ON THE GRID THEN THE FOLLOWING WILL HAPPEN
                    Glo_Grid[Xloc][Yloc]="|B"           #THIS IS THE SQUARE CONTAINING A BANDITS WILL LOOK LIKE - THE USER WILL NOT BE ABLE TO SEE THEM IN NORMAL MODE
                    used=False                          #SETTING USED TO FALSE WHICH WILL STOP THE WHILE-LOOP

def DispGrid():
    global Glo_Grid              #GIVING THE FUNCTION ACCESS TO 'Glo_Grid' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global Glo_Xsize             #GIVING THE FUNCTION ACCESS TO 'Glo_Xsize' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY 
    global Glo_Ysize             #GIVING THE FUNCTION ACCESS TO 'Glo_Ysize' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global Glo_BADcount          #GIVING THE FUNCTION ACCESS TO 'Glo_BADcount' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY    
    global Glo_TRECHcount        #GIVING THE FUNCTION ACCESS TO 'Glo_TRECHcount' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global Glo_COINcount         #GIVING THE FUNCTION ACCESS TO 'Glo_COINcount' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global Glo_PLAYERx           #GIVING THE FUNCTION ACCESS TO 'Glo_PLAYERx' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY    
    global Glo_PLAYERy           #GIVING THE FUNCTION ACCESS TO 'Glo_PLAYERy' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY 
                   
    print(("SYSTEM TIME: ")+str(time.strftime("%Y-%m-%d %H:%M"))) #DISPLAYING THE CURRENT TIME IN THE FORMAT OF: Y-M-D H:M
    print(" ")                                                    #PRINTING AN EMPTY SPACE TO ACT AS A SPACE
    BORDER=" "                                                    
    for X in range(0,Glo_Xsize):  #FOR THE X SIZE IT WILL DO THIS FOR-LOOP THAT MANY TIMES 
        BORDER=BORDER+"--"        #CREATING THE HORIZONTEL BORDERS INBETWEEN THE VERTICAL BORDERS "|" WHICH WILL LOOK LIKE "--" 
    BORDER=BORDER+"-"             #MAKING SURE THAT THERE IS ONLY ONE ON THE ENDS SO THAT THE HORIZONTEL BORDERS STAY WITHIN THE GRID
 
    for Y in range(0,Glo_Ysize):  #FOR THE Y SIZE IT WILL DO THIS FOR-LOOP THAT MANY TIMES 
        ROW=" "                   

        for X in range(0,Glo_Xsize):              #FOR THE X SIZE IT WILL DO THIS FOR-LOOP THAT MANY TIMES
            if X==Glo_PLAYERx and Y==Glo_PLAYERy: #IF THE PLAYER IS ON THE GRID THEN THE FOLLOWING WIL HAPPEN
                ROW=ROW+"|P"                      #CREATING THE SQUARE THAT WILL DISPLAY WERE THE PLAYER IS IN THE GRID
            else:                                 #IF ANYTHING ELSE THE FOLLOWING TAKES PLACE
                if Glo_DEBUG==True:               #IF THE DEBUG MODE IS ON IT WILL DO THE FOLLOWING
                    ROW=ROW+Glo_Grid[X][Y]        #SHOW EVERYTHING ON THE GRID  
                else:                             #IF ANYTHING ELSE IT WILL DO THE FOLLOWING 
                    ROW=ROW+"| "                  #CREATING THE VERTICAL BORDERS TO SEPERATE THE SQUARES FROM EACH ONE  

        print(BORDER)  #DISPLAYING THE VERTICAL BORDERS SO THAT THE USER CAN SEE THEM
        print(ROW+"|") #DISPLAYING THE ROWS IN THE GRID SO THAT THE USER CAN SEE THEM
    
    print(BORDER)                                       #DISPLAYING THE LAST SET OF VERTICAL BORDERS TO COMPLETE THE GRID  
    print("COIN TOTAL: "+str(Glo_COINcount))            #DISPLAYING THE COIN COUNT FOR THE USER TO SEE - THIS IS THE CASE WETHER IN DEBUG OR NOT 
    print(" ")                                          #PRINTING AN EMPTY SPACE TO ACT AS A SPACE 
    if Glo_DEBUG==True:                                 #IF THE DEBUG MODE IS ACTIVATED THE FOLLOWING WILL TAKE PLACE
        print("******************")                     #CREATING A BORDER WITH THE USE OF '*' 
        print("    DEBUG VEIW    ")                     #CREATING THE TOP OF THE DEBUG OPTIONS
        print("******************")                     #CREATING A BORDER WITH THE USE OF '*'
        print("Treasure Chests: "+str(Glo_TRECHcount))  #DISPLAYING THE CURRENT NUMBERS OF TREASURE CHESTS LEFT IN THE GRID
        print("Bandit Count: "+str(Glo_BADcount))       #DISPLAYING THE CURRENT NUMBERS OF BANDITS LEFT IN THE GRID 
        print("Player X Position: "+str(Glo_PLAYERx))   #DISPLAYING THE CURRENT X POSITION OF THE PLAYER IN THE GRID   
        print("Player Y Position: "+str(Glo_PLAYERy))   #DISPLAYING THE CURRENT Y POSITION OF THE PLAYER IN THE GRID 
        print("******************")                     #CREATING A BORDER WITH THE USE OF '*'    
 
def CHECK():
    global Glo_Grid              #GIVING THE FUNCTION ACCESS TO 'Glo_Grid' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY 
    global Glo_Xsize             #GIVING THE FUNCTION ACCESS TO 'Glo_Xsize' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global Glo_Ysize             #GIVING THE FUNCTION ACCESS TO 'Glo_Ysize' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global Glo_PLAYERx           #GIVING THE FUNCTION ACCESS TO 'Glo_PLAYERx' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY  
    global Glo_PLAYERy           #GIVING THE FUNCTION ACCESS TO 'Glo_PLAYERy' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY 
    global Glo_BADcount          #GIVING THE FUNCTION ACCESS TO 'Glo_BADcount' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY 
    global Glo_TRECHcount        #GIVING THE FUNCTION ACCESS TO 'Glo_TRECHcount' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY  
    global Glo_COINcount         #GIVING THE FUNCTION ACCESS TO 'Glo_COINcount' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global win                   #GIVING THE FUNCTION ACCESS TO 'win' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY

    if Glo_Grid[Glo_PLAYERx][Glo_PLAYERy]=="|B":             #IF THE USER LANDS ON A SQUARE CONTAINING A BANDIT THEN THE COIN COUNT IS SET TO 0
        Glo_COINcount=0                                      #SETTING THE COIN COUNT TO 0
        print("A BANDIT HAS JUST TAKEN ALL OF YOUR COINS! ") #DISPLAYING A MESSAGE THAT WILL TELL THE PLAYER THAT ALL OF THEIR COINS HAVE BEEN TAKEN AWAY

    if Glo_Grid[Glo_PLAYERx][Glo_PLAYERy]=="|1":             #IF THE USER LANDS ON A SQUARE CONTAINING A TREASURE CHEST THEN 10 COINS ARE ADDED TO THE COIN COUNT  
        Glo_COINcount=Glo_COINcount+10                       #ADDS 10 COINS TO THE COIN COUNT  
        Glo_Grid[Glo_PLAYERx][Glo_PLAYERy]="|2"              #CHANGES THE SQUARE TO 2 TO SO THE USER HAS ALREADY LANDED ON THAT SQUARE ONCE 
        print("YOU FOUND A TREASURE CHEST! +10 COINS ")      #DISPLAYING A MESSAGE THAT WILL TELL THE PLAYER THAT THEY HAVE GAINED 10 COINS

    elif Glo_Grid[Glo_PLAYERx][Glo_PLAYERy]=="|2":           #IF THE USER LANDS ON A SQUARE CONTAINING A TREASURE CHEST THEN 10 COINS ARE ADDED TO THE COIN COUNT  
        Glo_COINcount=Glo_COINcount+10                       #ADDS 10 COINS TO THE COIN COUNT 
        Glo_Grid[Glo_PLAYERx][Glo_PLAYERy]="|3"              #CHANGES THE SQUARE TO 3 TO SHOW THAT THE PLAYER HAS LANDED ON THAT SQUARE TWICE 
        print("YOU FOUND A TREASURE CHEST! +10 COINS ")      #DISPLAYING A MESSAGE THAT WILL TELL THE PLAYER THAT THEY HAVE GAINED 10 COINS

    elif Glo_Grid[Glo_PLAYERx][Glo_PLAYERy]=="|3":           #IF THE USER LANDS ON A SQUARE CONTAINING A TREASURE CHEST THEN 10 COINS ARE ADDED TO THE COIN COUNT  
        Glo_COINcount=Glo_COINcount+10                       #ADDS 10 COINS TO THE COIN COUNT
        Glo_Grid[Glo_PLAYERx][Glo_PLAYERy]="|B"              #CHANGES THE SQUARE TO B TO SHOW THAT THE PLAYER HAS LANDED ON THAT SQUARE THREE TIMES - AND THIS SQUARE NOW BECOMES A BANDIT
        print("YOU FOUND A TREASURE CHEST! +10 COINS ")      #DISPLAYING A MESSAGE THAT WILL TELL THE PLAYER THAT THEY HAVE GAINED 10 COINS

    if Glo_COINcount >99:                    #IF THE COIN COUNT IS GREATER THAN 99 THE FOLLOWING WILL TAKE PLACE
        Scroll()                             #USING THE SCROLL FUNCTION THAT WILL SCROLL THE SCREEN 70 LINES 
        print("YOU HAVE WON! ")              #DISPLAYING A YOU HAVE WON MESSAGE 
        print("YOUR COIN TOTAL:")            #DISPLAYING A HEADER FOR THE COIN TOTAL
        print(Glo_COINcount)                 #DISPLAYING THE COIN TOTAL 
        print("YOUR BANDIT TOTAL:")          #DISPLAYING A HEADER FOR THE AMOUNT OF BANDITS
        print(Glo_BADcount)                  #DISPLAYING THE BANDIT TOTAL
        print("YOUR TREASURE CHEST COUNT:")  #DISPLAYING A HEADER FOR HOW MANY TREASURE CHESTS WERE COLLECTED
        print(Glo_TRECHcount)                #DISPLAYING HOW MANY TREASURE CHESTS WERE COLLECTED
        win=True                             #CHANGING THE WIN VARIABLE TO BE TRUE     

        answer=input("DO YOU WANT TO PLAY AGAIN? Y/N: ") #ASKING THE PLAYER IF THEY WOULD LIKE TO HAVE ANOTHER GAME OR NOT 

        if answer == "Y":              #IF THE PLAYERS SELECTS 'Y' THEN THE FOLLOWING WILL TAKE PLACE 
            Funct_Scroll()             #USING THE SCROLL FUNCTION THAT WILL SCROLL THE SCREEN 70 LINES 
            print("Here we go again!") #PRINTING A MESSAGE TO AKNOWLEDGE THE PLAYERS SELECTION 
            ADVmenu()                  #TAKING THE PLAYER BACK TO THE MENU
            
        elif answer == "N":            #IF THE ANSWER IS 'N' THEN THE FOLLOWING WILL TAKE PLACE 
            print(" ") 
            print("Good Bye!")         #PRINTING A GOOD BYE MESSAGE TO AKNOWLEDGE THE PLAYERS SELECTION 
            print(" ") 
            Message()                  #DISPLAYING EITHER A WIN/LOOSE MESSAGE JUST BEFORE THE GAME TAKES YOU BACK TO THE MENU 
            menu()                     #TAKING THE PLAYER BACK TO THE MAIN MENU

        else:                          #IF THE REPLY THAT THE USER GIVES IS NOT ONE OF THE ONES ABOVE THEN THE FOLLOWING WILL TAKE PLACE 
            PlayAgain()                #DISPLAYING THE QUESTON AGAIN AND WILL DISPLAY THE FOLLOWING MESSAGE TO THE PLAYER SO THEY KNOW WHAT HAPPENED   
            print("++++++++++++++++++++++++++++++++++++") #CREATING A BORDER WITH THE USE OF '+'
            print("     THAT IS NOT A VALID ANSWER     ") #DISPLAYING AN INVALID ANSWER MESSAGE SO THAT THE PLAYER KNOWS WHAT THEY HAVE ENTERED IS INVALID
            print("++++++++++++++++++++++++++++++++++++") #CREATING A BORDER WITH THE USE OF '+' 

    elif Glo_COINcount <100 and Glo_TRECHcount <1: #IF THE COIN COUNT IS BELOW 100 AND THERE IS LESS THAN 1 TREASURE CHEST LEFT THEN THE FOLLOWING WILL TAKE PLACE 
        Scroll()                                   #USING THE SCROLL FUNCTION THAT WILL SCROLL THE SCREEN 70 LINES 
        print("YOU HAVE LOST UNLUCKY! ")           #DISPLAYING A YOU HAVE LOST MESSAGE  
        print("YOUR COIN TOTAL:")                  #DISPLAYING A HEADER FOR THE COIN TOTAL
        print(Glo_COINcount)                       #DISPLAYING THE COIN TOTAL
        print("YOUR BANDIT TOTAL:")                #DISPLAYING A HEADER FOR THE AMOUNT OF BANDITS
        print(Glo_BADcount)                        #DISPLAYING THE BANDIT TOTAL
        print("YOUR TREASURE CHEST COUNT:")        #DISPLAYING A HEADER FOR HOW MANY TREASURE CHESTS WERE COLLECTED
        print(Glo_TRECHcount)                      #DISPLAYING HOW MANY TREASURE CHESTS WERE COLLECTED
        win=False                                  #CHANGING THE WIN VARIABLE TO BE FALSE   
        
    def PlayAgain():
        
        answer=input("DO YOU WANT TO PLAY AGAIN? Y/N: ") #ASKING THE PLAYER IF THEY WOULD LIKE TO HAVE ANOTHER GAME OR NOT 

        if answer == "Y":              #IF THE PLAYERS SELECTS 'Y' THEN THE FOLLOWING WILL TAKE PLACE 
            Scroll()                   #USING THE SCROLL FUNCTION THAT WILL SCROLL THE SCREEN 70 LINES 
            print("Here we go again!") #PRINTING A MESSAGE TO AKNOWLEDGE THE PLAYERS SELECTION 
            ADVmenu()                  #TAKING THE PLAYER BACK TO THE MENU
            
        elif answer == "N":            #IF THE ANSWER IS 'N' THEN THE FOLLOWING WILL TAKE PLACE 
            print(" ") 
            print("Good Bye!")         #PRINTING A GOOD BYE MESSAGE TO AKNOWLEDGE THE PLAYERS SELECTION 
            print(" ")                 #PRINTING AN EMPTY SPACE TO ACT AS A SPACE
            Message()                  #DISPLAYING EITHER A WIN/LOOSE MESSAGE JUST BEFORE THE GAME TAKES YOU BACK TO THE MENU 
            menu()                     #TAKING THE PLAYER BACK TO THE MAIN MENU

        else:                          #IF THE REPLY THAT THE USER GIVES IS NOT ONE OF THE ONES ABOVE THEN THE FOLLOWING WILL TAKE PLACE 
            PlayAgain()                #DISPLAYING THE QUESTON AGAIN AND WILL DISPLAY THE FOLLOWING MESSAGE TO THE PLAYER SO THEY KNOW WHAT HAPPENED   
            print("++++++++++++++++++++++++++++++++++++") #CREATING A BORDER WITH THE USE OF '+'
            print("     THAT IS NOT A VALID ANSWER     ") #DISPLAYING AN INVALID ANSWER MESSAGE SO THAT THE PLAYER KNOWS WHAT THEY HAVE ENTERED IS INVALID
            print("++++++++++++++++++++++++++++++++++++") #CREATING A BORDER WITH THE USE OF '+'
   
def xMOVE():
    global Glo_Grid              #GIVING THE FUNCTION ACCESS TO 'Glo_Grid' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global Glo_Xsize             #GIVING THE FUNCTION ACCESS TO 'Glo_Xsize' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global Glo_Ysize             #GIVING THE FUNCTION ACCESS TO 'Glo_Ysize' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global Glo_PLAYERx           #GIVING THE FUNCTION ACCESS TO 'Glo_PLAYERx' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global Glo_PLAYERy           #GIVING THE FUNCTION ACCESS TO 'Glo_PLAYERy' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global Glo_BADcount          #GIVING THE FUNCTION ACCESS TO 'Glo_BADcount' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global Glo_TRECHcount        #GIVING THE FUNCTION ACCESS TO 'Glo_TRECHcount' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY

    Xmove=input("""How many spaces would you like to Right or Left?
R3 = RIGHT 3 Spaces
or
L3 = LEFT 3 Spaces
                 :""")                 #ASKING THE PLAYER WHERE THEY WOULD LIKE TO MOVE LEFT OR RIGHT
    if len(Xmove)==2:                  #IF THE PLAYER HAS ENTERED 2 VALUES THE FOLLOWIN WILL TAKE PLACE
        if Xmove[:1].upper()=="R":     #IF THE PLAYERS RESPONSE CONTAINS AN 'R' THEN THE FOLLOWING WILL TAKE PLACE 
            distance=int(Xmove[-1:])   #MOVING THE PLAYER HOWEVER TO THE RIGHT HOW MANY SPACES THEY HAVE STATED 

        elif Xmove[:1].upper()=="L":   #IF THE PLAYERS RESPONSE CONTAINS AN 'L' THEN THE FOLLOWING WILL TAKE PLACE
            distance=0-int(Xmove[-1:]) #MOVING THE PLAYER HOWEVER TO THE LEFT HOW MANY SPACES THEY HAVE STATED  

        else:                          #IF ANYTHING OTHER THAN AN 'R' OR 'L' THEN IT WILL NOT COUNT AS A MOVE AND THE FOLLOWING WILL TAKE PLACE
            print("ILLEGAL MOVE!")     #DISPLAYING AN ILLEGAL MOVE MESSAGE         
            xMOVE()                    #REPEATING THE THE FUNCTION TO REPEAT THE MESSAGE    
            
        if Glo_PLAYERx+distance>Glo_Xsize-1 or Glo_PLAYERx+distance<0: #IF THE AMOUNT OF SPACES THAT THE PLAYER WANTS TO MOVE 'R'/'L' WILL PLACE THEM OUTSIDE THE GRID TEH FOLLOWING HAPPENS
            print("ILLEGAL MOVE!")                                     #DISPLAYING AN ILLEGAL MOVE MESSAGE   
            xMOVE()                                                    #REPEATING THE THE FUNCTION TO REPEAT THE MESSAGE    

        Glo_PLAYERx=Glo_PLAYERx+distance #TAKING THE VALUE THAT THE PLAYER WANTED TO MOVE AND NOW ACTUALLY POSITIONING TEH PLAYER ON THE GRID
        yMOVE()                    #TAKING THE PLAYER TO THE NEXT FUNCTION THAT CONTROLS THE 'Y' MOVE OF THE PLAYER 

def yMOVE():
    global Glo_Grid              #GIVING THE FUNCTION ACCESS TO 'Glo_Grid' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global Glo_Xsize             #GIVING THE FUNCTION ACCESS TO 'Glo_Xsize' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global Glo_Ysize             #GIVING THE FUNCTION ACCESS TO 'Glo_Ysize' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global Glo_PLAYERx           #GIVING THE FUNCTION ACCESS TO 'Glo_PLAYERx' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global Glo_PLAYERy           #GIVING THE FUNCTION ACCESS TO 'Glo_PLAYERy' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global Glo_BADcount          #GIVING THE FUNCTION ACCESS TO 'Glo_BADcount' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global Glo_TRECHcount        #GIVING THE FUNCTION ACCESS TO 'Glo_TRECHcount' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY

    Ymove=input("""How many spaces would you like to Up or Down?
U3 = UP 3 Spaces
or
D3 = Down 3 Spaces
                 :""")                 #ASKING THE PLAYER WHERE THEY WOULD LIKE TO MOVE UP OR DOWN
    if len(Ymove)==2:                  #IF THE PLAYER HAS ENTERED 2 VALUES THE FOLLOWIN WILL TAKE PLACE
        if Ymove[:1].upper()=="D":     #IF THE PLAYERS RESPONSE CONTAINS AN 'D' THEN THE FOLLOWING WILL TAKE PLACE
            distance=int(Ymove[-1:])   #MOVING THE PLAYER HOWEVER TO THE RIGHT HOW MANY SPACES THEY HAVE STATED

        elif Ymove[:1].upper()=="U":   #IF THE PLAYERS RESPONSE CONTAINS AN 'U' THEN THE FOLLOWING WILL TAKE PLACE
            distance=0-int(Ymove[-1:]) #MOVING THE PLAYER HOWEVER TO THE LEFT HOW MANY SPACES THEY HAVE STATED 

        else:                          #IF ANYTHING OTHER THAN AN 'D' OR 'U' THEN IT WILL NOT COUNT AS A MOVE AND THE FOLLOWING WILL TAKE PLACE 
            print("ILLEGAL MOVE!")     #DISPLAYING AN ILLEGAL MOVE MESSAGE
            yMOVE()                    #REPEATING THE THE FUNCTION TO REPEAT THE MESSAGE  
            
        if Glo_PLAYERy+distance>Glo_Ysize-1 or Glo_PLAYERy+distance<0: #IF THE AMOUNT OF SPACES THAT THE PLAYER WANTS TO MOVE 'D'/'U' WILL PLACE THEM OUTSIDE THE GRID TEH FOLLOWING HAPPENS
            print("ILLEGAL MOVE!")                                     #DISPLAYING AN ILLEGAL MOVE MESSAGE  
            yMOVE()                                                    #REPEATING THE THE FUNCTION TO REPEAT THE MESSAGE 

        Glo_PLAYERy=Glo_PLAYERy+distance #TAKING THE VALUE THAT THE PLAYER WANTED TO MOVE AND NOW ACTUALLY POSITIONING TEH PLAYER ON THE GRID
        Scroll()                   #USING THE SCROLL FUNCTION THAT WILL SCROLL THE SCREEN 70 LINES
        CHECK()                    #GOING TO THE CHECK FUNCTION - IF TEH CHECK FUNCTION RETURENS A WIN TRUE/FALSE THEN THE GAME WILL END THERE
        DispGrid()                 #THEN GOING TO THE DISPLAY GRID FUNCTION 
        xMOVE()                    #THEN THE X MOVE  
        yMOVE()                    #AND LASTLY THE Y MOVE
        
def menu():

    print(("         SYSTEM TIME: ")+str(time.strftime("%Y-%m-%d %H:%M"))) #DISPLAYING THE TIME IN THE FORMAT OF Y-M-D H:M
    print(" ")                                                             #PRINTING AN EMPTY SPACE TO ACT AS A SPACE 
    print("**************************************************")            #CREATING A BORDER WITH THE USE OF '*' 
    print("        Welcome to the Treasure Hunt GAME!        ")            #CREATING THE MENU SO THAT PLAYERS KNOW WHERE THEY ARE
    print("""**************************************************
    Please select one of the following:
    1.Continue
    2.Quit
**************************************************""")   #DISPLAYING THE OPTIONS FOR THE PLAYER TO CHOOSE FROM AND A BORDER MAD OUT OF '*'                    

    answer=input("         What option do you choose? ") #ASKING THE PLAYERS IF THEY WOULD LIKE TO CONTINUE ON TO THE NEXT MENU OR QUIT

    if answer == "1":             #IF THE PLAYER SELECTS OPTION 1 THEN THE FOLLOWING WILL TAKE PLACE 
        Scroll()                  #USING THE SCROLL FUNCTION THAT WILL SCROLL THE SCREEN 70 LINES
        print("Enjoy the game!")  #DISPLAYING A MESSAGE THAT WILL AKNOWLEDGE THE PLAYERS SELECTION 
        ADVmenu()                 #TAKING THE PLAYER TO THE NEXT MENU

    elif answer == "2":           #IF THE PLAYER SELECTS OPTION 2 THEN THE FOLLOWING WILL TAKE PLACE 
        Scroll()                  #USING THE SCROLL FUNCTION THAT WILL SCROLL THE SCREEN 70 LINES
        print("GOODBYE!...")      #DISPLAING A GOODBYE MESSAGE THAT WILL AKNOWLEDGE THE PLAYERS SELECTION 
        print(" ")                 
        print("LOADING...")       #DISPLAYING A LOADING MESSAGE WHILST THE PROGRAM CLOSES
        time.sleep(5)             #WAITING 5 SECONDS BEFORE DOING THE NEXT BIT, IN THIS CASE EXITING TO THIR TK MAIN MENU
        os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\TK_MSTR_v3.py") #FILE DIRECTORY GC MAIN MENU 
        sys.exit()                #CLOSING THE TREASURE HUNT GAME 

    else:                         #IF THE REPLY THAT THE USER GIVES IS NOT ONE OF THE ONES ABOVE THEN THE FOLLOWING WILL TAKE PLACE 
        menu()                    #TAKING THE USER BACK TO THE MENU SO THEY CAN ANSWER AGAIN AND THE MESSAGE BELOW WILL BE DISPLAYED SO THAT THE USER KNOWS WHY THEY HAVE BEEN TAKEN BACK    
        print("++++++++++++++++++++++++++++++++++++") #CREATING A BORDER WITH THE USE OF '+'
        print("""   THAT IS NOT A VALID ANSWER   """) #DISPLAYING AN INVALID ANSWER MESSAGE SO THAT THE PLAYER KNOWS WHAT THEY HAVE ENTERED IS INVALID
        print("++++++++++++++++++++++++++++++++++++") #CREATING A BORDER WITH THE USE OF '+'
        
def Scroll():

    Scroll="\n"*70 #DEFINING HOW MANY LINES THE SCROLL FUNCTION WILL LEAVE 
    print(Scroll)  #ACTUALLY DISPLAYING THE SCROLL 

def ADVmenu():
    global Glo_DEBUG
    
    Scroll()                                                               #USING THE SCROLL FUNCTION THAT WILL SCROLL THE SCREEN 70 LINES
    
    print(("         SYSTEM TIME: ")+str(time.strftime("%Y-%m-%d %H:%M"))) #DISPLAYING THE TIME IN THE FORMAT OF Y-M-D H:M
    print(" ")                                                             #PRINTING AN EMPTY SPACE TO ACT AS A SPACE 
    print("**************************************************")            #CREATING A BORDER WITH THE USE OF '*' 
    print("        Welcome to the Treasure Hunt GAME!        ")            #CREATING THE MENU SO THAT PLAYERS KNOW WHERE THEY ARE
    print("""**************************************************
    Please select one of the following:
1.Normal
2.Debug

B. BACK
**************************************************""")   #DISPLAYING THE OPTIONS FOR THE PLAYER TO CHOOSE FROM AND A BORDER MAD OUT OF '*'     
    answer=input("What option do you choose? ")          #ASKING THE PLAYERS IF THEY WOULD LIKE TO PLAY DEBUG/NORMAL MODE OR GO BACK TO THE PREVIOUS MENU

    if answer == "1":                  #IF THE PLAYER SELECTS OPTION 1 THEN THE FOLLOWING WILL TAKE PLACE
        Scroll()                       #USING THE SCROLL FUNCTION THAT WILL SCROLL THE SCREEN 70 LINES
        print(" ++ Normal Mode ++ ")   #DISPLAYING NORMAL MODE SO THE USER KNOWS WHICH MODE THEY SELECTED  
        GridMaker()                    #STARTING OFF AT THE GRID MAKER FUNCTION WHICH MAKES THE GRID AND EVERYTHING IN IT
        DispGrid()                     #FOLLOWED BY THE DISPLAY GRID FUNCTION THAT ULTIMATLEY DISPLAYS THE GRID FOR THE USER TO VISUALISE 
        xMOVE()                        #FOLLOWED BY THE X MOVE FUNCTION THAT ALLOWS THE USER TO INPUT THEIR X MOVE ON THE GRID
        yMOVE()                        #FOLLOWED BY THE Y MOVE FUNCTION THAT ALLOWS THE USER TO INPUT THEIR Y MOVE ON THE GRID

    elif answer == "2":                #IF THE PLAYER SELECTS OPTION 2 THEN THE FOLLOWING WILL TAKE PLACE
        Scroll()                       #USING THE SCROLL FUNCTION THAT WILL SCROLL THE SCREEN 70 LINES 
        print("++ DEBUG MODE ON ++")   #DISPLAYING MODE MODE SO THE USER KNOWS WHICH MODE THEY SELECTED
        Glo_DEBUG=True                 #SETTING THE DEBUG VARIABLE TO BE TRUE SO THAT ALL POSTIONS WILL BE DISPLAYED TO THE USER
        GridMaker()                    #STARTING OFF AT THE GRID MAKER FUNCTION WHICH MAKES THE GRID AND EVERYTHING IN IT
        DispGrid()                     #FOLLOWED BY THE DISPLAY GRID FUNCTION THAT ULTIMATLEY DISPLAYS THE GRID FOR THE USER TO VISUALISE
        xMOVE()                        #FOLLOWED BY THE X MOVE FUNCTION THAT ALLOWS THE USER TO INPUT THEIR X MOVE ON THE GRID
        yMOVE()                        #FOLLOWED BY THE Y MOVE FUNCTION THAT ALLOWS THE USER TO INPUT THEIR Y MOVE ON THE GRID

    elif answer == "B" or "b":         #IF THE PLAYER SELECTS OPTION B THEN THE FOLLOWING WILL TAKE PLACE 
        menu()                         #TAKING THE USER BACK TO THE PREVIOUS MENU AS TEHY HAVE SELECTED THE BACK OPTION 
        
    else:                                             #IF THE USER DOES NOT ENTER A VALID RESPONSE THEN THE FOLLOWING WILL TAKE PLACE 
        Scroll()                                      #USING THE SCROLL FUNCTION THAT WILL SCROLL THE SCREEN 70 LINES
        print("++++++++++++++++++++++++++++++++++++") #CREATING A BORDER WITH THE USE OF '+'
        print("""   THAT IS NOT A VALID ANSWER   """) #DISPLAYING AN INVALID ANSWER MESSAGE SO THAT THE PLAYER KNOWS WHAT THEY HAVE ENTERED IS INVALID
        print("++++++++++++++++++++++++++++++++++++") #CREATING A BORDER WITH THE USE OF '+'
        ADVmenu()                                     #TAKING THE USER BACK TO THE MENU SO THAT THEY CAN RESPOND TO THE MENU AGAIN 
   
TREASURE_HUNT()
