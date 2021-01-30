#Nathan Jones
#GRAND CENTRAL v3 - FM MSTR EDITION
#July 2018

from datetime import datetime

import time
import sys
import os.path
import os
import string 
import random
import statistics
import itertools
import datetime

#global variables - FRUIT MACHINE
FRUIT=['CHERRY','BELL','LEMON','ORANGE','STAR','SKULL']
SKULL_COUNT=0
CHERRY_COUNT=0
BELL_COUNT=0
LEMON_COUNT=0
ORANGE_COUNT=0
STAR_COUNT=0
PENCE=100
ROUND=0

#global variables - GAME MESSAGE WIN/LOOSE
LOOSE=["Unlucky on the GAME! Better luck next time!","Maybe next time!","Sooooo close, but so far...","It just wasnt your day today!"]
WIN=["WELL DONE ON THE GAME! You Smashed it!","That was one hell of a game!","CONGRATULATIONS ON WINNING!","That was an IMPRESSIVE GAME! Well Done!"]
win=False

def Message():

    if win == True:

        print(WIN[random.randint(0,3)])
        print(" ")
        MACHINE()

    elif win == False:

        print(LOOSE[random.randint(0,3)])
        print(" ")
        MACHINE()

def SCROLL():

    Scroll="\n"*70
    print(Scroll)

def SCROLL2():

    Scroll2="\n"*10
    print(Scroll2)

def SCROLL3():

    Scroll3="\n"*28
    print(Scroll3)      


def FRUIT_MACHINE():

    print("""
███████╗██████╗ ██╗   ██╗██╗████████╗                   
██╔════╝██╔══██╗██║   ██║██║╚══██╔══╝                   
█████╗  ██████╔╝██║   ██║██║   ██║                      
██╔══╝  ██╔══██╗██║   ██║██║   ██║                      
██║     ██║  ██║╚██████╔╝██║   ██║                      
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝   ╚═╝                      
                                                        
███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗
████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝
██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗  
██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝  
██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗
╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝
                                                        
""")

    SCROLL2()
    MACHINE()

def MACHINE():

    global PENCE
    global ROUND

    print(("SYSTEM TIME: ")+str(datetime.datetime.now()))
    print(" ")
    print("####################################")
    print("#       Welcome to the MENU        #")
    print("#                                  #")
    print("#            ?. HELP               #")
    print("#                                  #")
    print("#            1. PLAY               #")
    print("#                                  #")
    print("#            Q. QUIT               #")
    print("#                                  #")
    print("####################################")

    answer=input("What option do you choose? ")

    if answer == "?":
       Scroll2="\n"*5
       SCROLL2()
       HELP()

    elif answer == "1":
       SCROLL()
       PENCE = PENCE - 20
       ROUND = ROUND + 1
       GAME()

    elif answer == "Q" or "q":
       SCROLL()
       print("GOODBYE!...")
       print(" ")
       print("LOADING...")
       time.sleep(5)
       SCROLL()
       os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\TK_MSTR_v3.py")
       sys.exit()

    else:
       SCROLL()
       print(answer)
       print(" ")
       print("INVALID ANSWER! - TRY AGAIN")
       print(" ")
       MACHINE()

def GAME():

   SCROLL()
   global SKULL_COUNT
   global CHERRY_COUNT
   global BELL_COUNT
   global LEMON_COUNT
   global ORANGE_COUNT
   global STAR_COUNT
   global PENCE
   global ROUND

   print(("SYSTEM TIME: ")+str(datetime.datetime.now()))
   print(" ")
   print(("ROUND: ")+str(ROUND))
   print(("MONEY REMAINING: " )+str(PENCE))
   Spin1 = random.choice(FRUIT)
   Spin2 = random.choice(FRUIT)
   Spin3 = random.choice(FRUIT)

   print("         ")
   print("*********")
   print("         ")
   print("SPIN ONE:")
   print("         ")
   print(Spin1)
   print("         ")
   print("*********")
   print("         ")
   print("SPIN TWO:")
   print("         ")
   print(Spin2)
   print("         ")
   print("*********")
   print("         ")
   print("SPIN THREE:")
   print("         ")
   print(Spin3)
   print("         ")
   print("*********")

        
   if PENCE == 0:
       win=False
       SCROLL2() 
       print("GAME LOST")
       print("YOUR COIN TOTAL:") 
       print(PENCE)
       print("ROUND NUMBER:") 
       print(ROUND)
       PENCE = 100
       ROUND = 0
       SCROLL2()
       print(" ")
       if win == True:
            print(WIN[random.randint(0,3)])
            print(" ")     
       elif win == False:
            print(LOOSE[random.randint(0,3)])
            print(" ")
       time.sleep(5)
       SCROLL()
       os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\TK_MSTR_v3.py")
       sys.exit()
   
   if PENCE < 20:
       win=True
       GAME()
   
   if (Spin1) == ("CHERRY"):
      CHERRY_COUNT = CHERRY_COUNT +1

   if (Spin1) == ("BELL"):
      BELL_COUNT = BELL_COUNT +1

   if (Spin1) == ("LEMON"):
      LEMON_COUNT = LEMON_COUNT +1

   if (Spin1) == ("ORANGE"):
      ORANGE_COUNT = ORANGE_COUNT +1

   if (Spin1) == ("STAR"):
      STAR_COUNT = STAR_COUNT +1

   elif (Spin1) == ("SKULL"):
      SKULL_COUNT = SKULL_COUNT +1



   if (Spin2) == ("CHERRY"):
      CHERRY_COUNT = CHERRY_COUNT +1

   if (Spin2) == ("BELL"):
      BELL_COUNT = BELL_COUNT +1

   if (Spin2) == ("LEMON"):
      LEMON_COUNT = LEMON_COUNT +1

   if (Spin2) == ("ORANGE"):
      ORANGE_COUNT = ORANGE_COUNT +1

   if (Spin2) == ("STAR"):
      STAR_COUNT = STAR_COUNT +1

   elif (Spin2) == ("SKULL"):
      SKULL_COUNT = SKULL_COUNT +1


   if (Spin3) == ("CHERRY"):
      CHERRY_COUNT = CHERRY_COUNT +1

   if (Spin3) == ("BELL"):
      BELL_COUNT = BELL_COUNT +1

   if (Spin3) == ("LEMON"):
      LEMON_COUNT = LEMON_COUNT +1

   if (Spin3) == ("ORANGE"):
      ORANGE_COUNT = ORANGE_COUNT +1

   if (Spin3) == ("STAR"):
      STAR_COUNT = STAR_COUNT +1

   elif (Spin3) == ("SKULL"):
      SKULL_COUNT = SKULL_COUNT +1
      

   elif SKULL_COUNT == 2:
      print("MONEY LOST")
      PENCE = PENCE - PENCE

   elif SKULL_COUNT == 3:
      win=False
      SCROLL2() 
      print("GAME LOST")
      print("YOUR COIN TOTAL:") 
      print(PENCE)
      print("ROUND NUMBER:") 
      print(ROUND)
      PENCE = 100
      ROUND = 0
      SCROLL2()
      print(" ")
      if win == True:
          print(WIN[random.randint(0,3)])
          print(" ")
      elif win == False:
          print(LOOSE[random.randint(0,3)])
          print(" ")
      time.sleep(5)
      SCROLL()
      os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\TK_MSTR_v3.py")
      sys.exit()


   if CHERRY_COUNT == 2:
      print("GAME WON! +40")
      PENCE = PENCE + 40

   if BELL_COUNT == 2:
      print("GAME WON! +40")
      PENCE = PENCE + 40  

   if LEMON_COUNT == 2:
      print("GAME WON! +20")
      PENCE = PENCE + 20

   if ORANGE_COUNT == 2:
      print("GAME WON! +40")
      PENCE = PENCE + 40

   if STAR_COUNT == 2:
      print("GAME WON! +60") 
      PENCE = PENCE + 60

      
  
   if CHERRY_COUNT == 3:
      print("GAME WON! +100")
      PENCE = PENCE + 100

   if BELL_COUNT == 3:
      print("GAME WON! +60")
      PENCE = PENCE + 60  

   if LEMON_COUNT == 3:
      print("GAME WON! +20")
      PENCE = PENCE + 20

   if ORANGE_COUNT == 3:
      print("GAME WON! +80")
      PENCE = PENCE + 80

   if STAR_COUNT == 3:
      print("GAME WON! +120") 
      PENCE = PENCE + 120



   SCROLL2()
   print("*********")
   print("SKULL COUNT:")
   print(SKULL_COUNT)
   print("*********")

   print("CHERRY COUNT:")
   print(CHERRY_COUNT)
   print("*********")

   print("BELL COUNT:")
   print(BELL_COUNT)
   print("*********")

   print("LEMON COUNT:")
   print(LEMON_COUNT)
   print("*********")

   print("ORANGE COUNT:")
   print(ORANGE_COUNT)
   print("*********")

   print("STAR COUNT:")
   print(STAR_COUNT)
   print("*********")



   answer=input("PLAY AGAIN? Y/N: ")
   if answer == "Y" or "y":
      PENCE = PENCE - 20
      SKULL_COUNT = 0
      CHERRY_COUNT = 0
      BELL_COUNT = 0
      LEMON_COUNT = 0
      ORANGE_COUNT = 0
      STAR_COUNT = 0
      ROUND = ROUND + 1
      GAME()
   
   if answer == "N" or "n":

       SCROLL()
       print(("SYSTEM TIME: ")+str(datetime.datetime.now()))
       print(" ")
       print("YOUR COIN TOTAL:") 
       print(PENCE)
       print("ROUND NUMBER:") 
       print(ROUND)
       PENCE = 100
       ROUND = 0
       SCROLL2()
       print(" ")
       if win == True:
           print(WIN[random.randint(0,3)])
           print(" ")     
       elif win == False:
           print(LOOSE[random.randint(0,3)])
           print(" ")
       time.sleep(5)
       SCROLL()
       os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\TK_MSTR_v3.py")
       sys.exit()
       
     
   else:

      SCROLL()
      print(" ")
      print("INVALID ANSWER!")
      print(" ")
      MACHINE()
      
FRUIT_MACHINE()      
    
