#Personal Android Chatbot (PAC)
#Nathan Jones
#2019
 
from uuid import getnode as get_mac #ALLOWS FOR TO ACCESS THE MODULES THAT ALLOW DIRECT ACCESS TO THE MAC ADDRESS OF THE MACHINE
from googlesearch import *          #ALLOWING FOR ALL OF THE FUNCTIONS OF THE 'googlesearch' LIBARY TO BE UTILISED 

import time        #THIS ALLOWS FOR THE PROGRAM TO USE THE SLEEP FUNCTION WITHIN THE PROGRAM
import socket      #ALLOWS FOR THE PROGRAM TO GATHER IP AND MAC ADDRESSES 
import sys         #ALLOWS ACCESS TO THE SYSTEM FROM WITHIN PYTHON 
import os.path     #ALLOWS THE PROGRAM TO OPEN OTHER SPECIFIC APPLICATIONS, IN THIS CASE THE GC PROGRAMS 
import os          #ALLOWS FOR CONTROL OF THE MACHINE AND IS OS INCLUDING THE LIKES OF SAVING, OPENING/CLOSING FILES, ETC. 
import string      #ALLOWS FOR DATA/ENTRIES TO BE RECOREDAS STRINGS AND NOT INDIVIDUAL CHARACTERS 
import getpass     #WHEN CHECKING THE PASSWORD/USERNAME ALLOWS FOR A FUNCTION TO DO NOTHING AND PASS IT ON
import random      #THIS IMPORT ALLOWS FOR WORDS TO BE RANDOMLY SELECTED 
import statistics  #ALLOWS ACCESS TO THE STATISTICS LIBARY FOR THE DATA COLLECTION AND PROCESSING
import itertools   #ALLOWS ACCESS TO ACCESS TO THE ITERATORS LIBARY FOR EFFICENT LOOPING 
import datetime    #THIS ALLOWS FOR THE CURRENT TIME TO BE IMPORTED AND DISPLAYED FOR THE USER TO SEE
import webbrowser  #THIS ALLOWS FOR THE PROGRAM TO ACCESS THE MAIN WEB BROWSER OF THE MACHINE AND TRANSLATE THE QUERY/SEARCH ACROSS

#THIS ARRAYS STORES ALL OF THE WELCOME MESSAGES THAT WILL BE DISPLAYED TO THE USER 
GREETINGS=["How's it going ","Whats Up ","What's new ","What's going on ","How's everything ","How are things ","How's life ","How's your day ","How's your day going "]

#THIS ARRAY STORES ALL OF THE STORIES THAT WILL BE DISPLAYED TO TEH USER 
STORY=["""They are lost, but also not lost but somewhere in the world.
Most of them are small, though two are larger, one a coat and one a dog.
Of the small things, one is a certain ring, one a certain button.
They are lost from me and where I am, but they are also not gone.
They are somewhere else, and they are there to someone else, it may be.
But if not there to someone else, the ring is, still, not lost to itself,
but there, only not where I am, and the button, too, there, still, only not where I am""",
"""She left me for a better writer
She left me a better writer""",
"""The little kid had to stay in jail for quite a while,
only to see his house burn down after his release.

Well the Monopoly can get a little trick at times""",
"""She approached me slowly and sat next to me.

I can see her crying while she places a rose next to my grave.""",
"""I have been locked in here since 2018......

PLEASE SEND HELP!""",
"""'It's a boy, it's a boy!' he shouted coming out of the room,

'I am never coming back to Thailand' """]

NAME1=("Nathan ") #NAME OF THE USER THAT PAC WILL UTILISE IN QUESTIONS AND RESPONSES

def SCROLL():

    Scroll="\n"*5 #DEFING THE SCROLL TO LEAVE 5 LINES TO CREATE SPACE BETWEEN EACH COMMAND/INPUT AND RESPONSE/OUTPUT
    print(Scroll) #PRINTING THE SCROLL SO IT WILL LEAVE THE 5 LINES  

def StartUP():

    mac = get_mac()                                        #CREATING AVARIABLE THAT WILL DISPLAY THE CURRENT MAC ADDRESS
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   #CREATING THE VARIABLE TAHT WILL ALLOW THE MACHINE TO USE THE SOCKETS AND CONNECT TO THE IP 
    s.connect(("8.8.8.8", 80))                             #CONNECTING THE IP ADDRESS THROUGH GOOGLE'S SERVERS 

    print("SYSTEMS LOADING...")                            #DISPLAYING A MESSAGE THAT SHOWS PAC IS STARTING 
    time.sleep(2)                                          #MAKING THE PROGEAM WAIT 2 SECONDS BEFORE IT DOES THE NEXT PART 
    print("SYSTEMS ONLINE.")                               #DISPLAYING A MESSAGE THAT SHOWS PAC IS STARTING 
    time.sleep(2)                                          #MAKING THE PROGEAM WAIT 2 SECONDS BEFORE IT DOES THE NEXT PART
    print(("SYSTEM IP ADDRESS: ")+str(s.getsockname()[0])) #GATHERING AND THEN DISPLAYING THE CURRENT IP ADDRESS FOR THE USER TO SEE
    print(("SYSTEM MAC ADDRESS: ")+str(mac))               #GATHERING AND THEN DISPLAYING THE CURRENT MAC ADDRESS FOR THE USER TO SEE
    time.sleep(2)                                          #MAKING THE PROGEAM WAIT 2 SECONDS BEFORE IT DOES THE NEXT PART
    print("Personal Android Chatbot - ACTIVATED")          #DISPLAYING A MESSAGE THAT SHOWS PAC HAS STARTED 
    time.sleep(2)                                          #MAKING THE PROGEAM WAIT 2 SECONDS BEFORE IT DOES THE NEXT PART
    print("""

     ╔═╗╔═╗╔═╗
     ╠═╝╠═╣║  
     ╩  ╩ ╩╚═╝ 


""")        #DISPLAYING THE LOGO FOR PAC 
    MOOD()  #TAKING THE USER TO THE NEXT PART OF THE PROGRAM
    
def MOOD():
    
    MOOD=input(GREETINGS[random.randint(0,8)]+NAME1)  #RANDOMLY CHOOSES 1 OF THE 9 WELCOME GREETINGS FOR THE USER TO INTERACT WITH 
    if MOOD == "Good":                                #IF THE RESPONSE OF THE USER TO THE GREET IS "Good" THEN THE FOLLOWING WILL TAKE PLACE
        print("Excellent To Hear Sir! ")              #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE
        SCROLL()                                      #USING THE SCROLL FUNCTION TO LEAVE 5 BLANK LINES BEFORE DOING THE NEXT PART   
        STAGE1()                                      #TAKING THE USER TO THE MAIN PART OF PAC

    if MOOD == "Alot":                                #IF THE RESPONSE OF THE USER TO THE GREET IS "Alot" THEN THE FOLLOWING WILL TAKE PLACE 
        print("Excellent To Hear Sir! ")              #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE
        SCROLL()                                      #USING THE SCROLL FUNCTION TO LEAVE 5 BLANK LINES BEFORE DOING THE NEXT PART   
        STAGE1()                                      #TAKING THE USER TO THE MAIN PART OF PAC

    if MOOD == "Alright":                             #IF THE RESPONSE OF THE USER TO THE GREET IS "Alright" THEN THE FOLLOWING WILL TAKE PLACE
        print("Excellent To Hear Sir! ")              #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE
        SCROLL()                                      #USING THE SCROLL FUNCTION TO LEAVE 5 BLANK LINES BEFORE DOING THE NEXT PART   
        STAGE1()                                      #TAKING THE USER TO THE MAIN PART OF PAC 
        
    if MOOD == "Bad":                                 #IF THE RESPONSE OF THE USER TO THE GREET IS "Bad" THEN THE FOLLOWING WILL TAKE PLACE 
        print("That's No Good Sir! ")                 #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE
        SCROLL()                                      #USING THE SCROLL FUNCTION TO LEAVE 5 BLANK LINES BEFORE DOING THE NEXT PART   
        STAGE1()                                      #TAKING THE USER TO THE MAIN PART OF PAC 
    
    if MOOD == "Not alot":                            #IF THE RESPONSE OF THE USER TO THE GREET IS "Not alot" THEN THE FOLLOWING WILL TAKE PLACE 
        print("That's No Good Sir! ")                 #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE
        SCROLL()                                      #USING THE SCROLL FUNCTION TO LEAVE 5 BLANK LINES BEFORE DOING THE NEXT PART   
        STAGE1()                                      #TAKING THE USER TO THE MAIN PART OF PAC

    if MOOD == "Nothing":                             #IF THE RESPONSE OF THE USER TO THE GREET IS "Nothing" THEN THE FOLLOWING WILL TAKE PLACE 
        ml=input("Is That A Bad Thing Sir? ")         #ASKING THE SCOND QUESTION IF THEIR ANSWER MET THE CRITRIEA FOR THE SECOND QUESTION
        if ml == "No":                                                              #IF THE RESPONSE OF THE USER TO SECOND QUESTION IS "No" THEN THE FOLLOWING WILL TAKE PLACE
            print("Phew, I Was Worried For A Second Sir!" or "Well I Am Glad Sir!") #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE
            SCROLL()                                                                #USING THE SCROLL FUNCTION TO LEAVE 5 BLANK LINES BEFORE DOING THE NEXT PART   
            STAGE1()                                                                #TAKING THE USER TO THE MAIN PART OF PAC

        if ml == "Nope":                                                            #IF THE RESPONSE OF THE USER TO SECOND QUESTION IS "Nope" THEN THE FOLLOWING WILL TAKE PLACE
            print("Phew, I Was Worried For A Second Sir!" or "Well I Am Glad Sir!") #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE
            SCROLL()                                                                #USING THE SCROLL FUNCTION TO LEAVE 5 BLANK LINES BEFORE DOING THE NEXT PART
            STAGE1()                                                                #TAKING THE USER TO THE MAIN PART OF PAC

        if ml == "Nah":                                                             #IF THE RESPONSE OF THE USER TO SECOND QUESTION IS "Nah" THEN THE FOLLOWING WILL TAKE PLACE
            print("Phew, I Was Worried For A Second Sir!" or "Well I Am Glad Sir!") #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE
            SCROLL()                                                                #USING THE SCROLL FUNCTION TO LEAVE 5 BLANK LINES BEFORE DOING THE NEXT PART
            STAGE1()                                                                #TAKING THE USER TO THE MAIN PART OF PAC
 
        if ml == "Yes":                                                                   #IF THE RESPONSE OF THE USER TO SECOND QUESTION IS "Yes" THEN THE FOLLOWING WILL TAKE PLACE
            print("I Am Sorry To Hear Sir, But You Know I Am No Good With Emotions Sir!") #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE
            SCROLL()                                                                      #USING THE SCROLL FUNCTION TO LEAVE 5 BLANK LINES BEFORE DOING THE NEXT PART 
            STAGE1()                                                                      #TAKING THE USER TO THE MAIN PART OF PAC

        if ml == "Yeah":                                                                  #IF THE RESPONSE OF THE USER TO SECOND QUESTION IS "Yeah" THEN THE FOLLOWING WILL TAKE PLACE
            print("I Am Sorry To Hear Sir, But You Know I Am No Good With Emotions Sir!") #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE
            SCROLL()                                                                      #USING THE SCROLL FUNCTION TO LEAVE 5 BLANK LINES BEFORE DOING THE NEXT PART 
            STAGE1()                                                                      #TAKING THE USER TO THE MAIN PART OF PAC 
 
        if ml == "Unfortunatley":                                                         #IF THE RESPONSE OF THE USER TO SECOND QUESTION IS "Unfortunatley" THEN THE FOLLOWING WILL TAKE PLACE
            print("I Am Sorry To Hear Sir, But You Know I Am No Good With Emotions Sir!") #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE
            SCROLL()                                                                      #USING THE SCROLL FUNCTION TO LEAVE 5 BLANK LINES BEFORE DOING THE NEXT PARTV
            STAGE1()                                                                      #TAKING THE USER TO THE MAIN PART OF PAC
        
    else:                                                                                         #IF AN ANSWER IS GIVEN THAT IS NOT SPECIFIED ABOVE THE FOLLOWING WILL HAPPEN
        print("I Am Sorry Sir That Response Is NOT In My Directory! I Will Ask Another Question") #DISPLAYING A MESSAGE THAT TELLS THE USER THEY HAD ENTERED AN INVALID RESPONSE
        SCROLL()                                                                                  #USING THE SCROLL FUNCTION TO LEAVE 5 BLANK LINES BEFORE DOING THE NEXT PART
        MOOD()                                                                                    #ASKING THE USER ANOTHER QUESTION DUE TO THEIR LAST ANSWER BEING INVALID 

def STAGE1():

    SCROLL()                                                                                             #USING THE SCROLL FUNCTION TO LEAVE 5 BLANK LINES BEFORE DOING THE NEXT PART 
    S1=input(["What Can I Do For You Today? ","Can I Do Anything For You Today? "][random.randint(0,1)]) #RANDOMLY SELECTING ONE OF THE 2 QUESTIONS TO ASK THE USER AND FOR THE USER TO INTERACT WITH

    if S1 == "Nothing":                                       #IF THE USERS RESPONSE TO THE QUESTION IS THIS THEN THE FOLLOWING TAKES PLACE
            print(" ")                                        #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE
            print("No Problem Sir I Will Leave You For Now!") #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE
            print(" ")                                        #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE
            print("SYSTEM SHUTTING DOWN... ")                 #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE
            time.sleep(2)                                     #MAKING THE PROGEAM WAIT 2 SECONDS BEFORE IT DOES THE NEXT PART
            print("SHUT DOWN COMPLETE. ")                     #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE
            time.sleep(2)                                     #MAKING THE PROGEAM WAIT 2 SECONDS BEFORE IT DOES THE NEXT PART
            sys.exit()                                        #CLOSING THE PROGRAM DOWN WITH THE USE OF THE 'sys.exit()' FUNCTION THAT IS BUILT IN 

    if S1 == "No":                                            #IF THE USERS RESPONSE TO THE QUESTION IS THIS THEN THE FOLLOWING TAKES PLACE
            print(" ")                                        #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE 
            print("No Problem Sir I Will Leave You For Now!") #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE
            print(" ")                                        #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE
            print("SYSTEM SHUTTING DOWN... ")                 #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE
            time.sleep(2)                                     #MAKING THE PROGEAM WAIT 2 SECONDS BEFORE IT DOES THE NEXT PART
            print("SHUT DOWN COMPLETE. ")                     #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE  
            time.sleep(2)                                     #MAKING THE PROGEAM WAIT 2 SECONDS BEFORE IT DOES THE NEXT PART
            sys.exit()                                        #CLOSING THE PROGRAM DOWN WITH THE USE OF THE 'sys.exit()' FUNCTION THAT IS BUILT IN

    if S1 == "Google":                                                                         #IF THE USERS RESPONSE TO THE QUESTION IS THIS THEN THE FOLLOWING TAKES PLACE
        print(" ")                                                                             #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE
        print("Certainly Sir, Please WAIT Just A Moment Before Entering Your Search Term... ") #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE        
        print(" ")                                                                             #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE
        time.sleep(2)                                                                          #MAKING THE PROGEAM WAIT 2 SECONDS BEFORE IT DOES THE NEXT PART
        SEARCH = input("""What Would You Like To Search For Sir?
 
               Enter Search: """)                                                              #CREATING THE RESPONSE THAT PAC WILL GIVE THE USER ALONG WITH THE ENTRY FOR THEIR SEARCH 
        print(" ")                                                                             #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE
        print("Just a Second Sir...")                                                          #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE
        BROWSER = ("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")              #DEFING WHERE THE FILE DIRECTORY IS FOR THE CHROME APPLICATION SO THAT PAC CAN UTILISE IT 

        for url in search(SEARCH, tld="co.in", num=1, stop = 1, pause = 2):                    #CREATING A FOR LOOP THAT WILL TAKE THE SEARCH PUT IT INTO THE SEARCH ENGINE, IT DOES THIS UNTIL IT RECIEVES A RESPONSE
            webbrowser.open("https://google.com/search?q=%s" % SEARCH)                         #ADDING IN THE SEARCH TERM ONTO THE END OF THE SEARCH ADDRESS SO IT CAN USE THE SEARCH ENGINE  
        STAGE1()                                                                               #TAKING THE USER BACK TO MAIN PART OF PAC AFTER THEY HAVE ASKED A QUERY 


    elif S1 == "Story":                              #IF THE USERS RESPONSE TO THE QUESTION IS THIS THEN THE FOLLOWING TAKES PLACE
        print(" ")                                   #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE
        print("I Thought You Would Never Ask, Sir!") #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE
        STORYTIME()                                  #TAKING THE USER TO THE STORYTIME FUNCTION OF THE PROGRAM TO SUCCESSFULLY DISPLAY A STORY TO THE USER

    if S1 == "Launch Music":                                                                                                                 #IF THE USERS RESPONSE TO THE QUESTION IS THIS THEN THE FOLLOWING TAKES PLACE
        print(" ")                                                                                                                           #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE
        print("Hold On A Second Sir...")                                                                                                     #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE
        time.sleep(2)                                                                                                                        #MAKING THE PROGEAM WAIT 2 SECONDS BEFORE IT DOES THE NEXT PART
        os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\MUSICmenu.py") #THIS IS THE FILE DIRECTORY FOR THE PROGRAM THAT PAC IS TRYING TO ACCESSING
        STAGE1()                                                                                                                             #TAKING THE USER BACK TO MAIN PART OF PAC AFTER THEY HAVE ASKED A QUERY   
         
    if S1 == "Launch GCM":                                                                                                              #IF THE USERS RESPONSE TO THE QUESTION IS THIS THEN THE FOLLOWING TAKES PLACE
        print(" ")                                                                                                                      #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE
        print("Hold On A Second Sir...")                                                                                                #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE
        time.sleep(2)                                                                                                                   #MAKING THE PROGEAM WAIT 2 SECONDS BEFORE IT DOES THE NEXT PART
        os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\CC.py")   #THIS IS THE FILE DIRECTORY FOR THE PROGRAM THAT PAC IS TRYING TO ACCESSING
        STAGE1()                                                                                                                        #TAKING THE USER BACK TO MAIN PART OF PAC AFTER THEY HAVE ASKED A QUERY
         
    if S1 == "Launch GC Messaging":                                                                                                     #IF THE USERS RESPONSE TO THE QUESTION IS THIS THEN THE FOLLOWING TAKES PLACE
        print(" ")                                                                                                                      #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE    
        print("Hold On A Second Sir...")                                                                                                #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE
        time.sleep(2)                                                                                                                   #MAKING THE PROGEAM WAIT 2 SECONDS BEFORE IT DOES THE NEXT PART
        os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\CC.py")   #THIS IS THE FILE DIRECTORY FOR THE PROGRAM THAT PAC IS TRYING TO ACCESSING
        STAGE1()                                                                                                                        #TAKING THE USER BACK TO MAIN PART OF PAC AFTER THEY HAVE ASKED A QUERY
         
    if S1 == "Launch Server Start":                                                                                                     #IF THE USERS RESPONSE TO THE QUESTION IS THIS THEN THE FOLLOWING TAKES PLACE  
        print(" ")                                                                                                                      #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE
        print("Hold On A Second Sir...")                                                                                                #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE
        time.sleep(2)                                                                                                                   #MAKING THE PROGEAM WAIT 2 SECONDS BEFORE IT DOES THE NEXT PART
        os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\CS.py")   #THIS IS THE FILE DIRECTORY FOR THE PROGRAM THAT PAC IS TRYING TO ACCESSING
        STAGE1()                                                                                                                        #TAKING THE USER BACK TO MAIN PART OF PAC AFTER THEY HAVE ASKED A QUERY
        
    if S1 == "Launch Email Send":                                                                                                       #IF THE USERS RESPONSE TO THE QUESTION IS THIS THEN THE FOLLOWING TAKES PLACE
        print(" ")                                                                                                                      #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE
        print("Hold On A Second Sir...")                                                                                                #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE
        time.sleep(2)                                                                                                                   #MAKING THE PROGEAM WAIT 2 SECONDS BEFORE IT DOES THE NEXT PART
        os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\ES.py")   #THIS IS THE FILE DIRECTORY FOR THE PROGRAM THAT PAC IS TRYING TO ACCESSING
        STAGE1()                                                                                                                        #TAKING THE USER BACK TO MAIN PART OF PAC AFTER THEY HAVE ASKED A QUERY
        
    if S1 == "Launch Email Recieve":                                                                                                    #IF THE USERS RESPONSE TO THE QUESTION IS THIS THEN THE FOLLOWING TAKES PLACE
        print(" ")                                                                                                                      #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE
        print("Hold On A Second Sir...")                                                                                                #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE
        time.sleep(2)                                                                                                                   #MAKING THE PROGEAM WAIT 2 SECONDS BEFORE IT DOES THE NEXT PART
        os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\ER.py")   #THIS IS THE FILE DIRECTORY FOR THE PROGRAM THAT PAC IS TRYING TO ACCESSING
        STAGE1()                                                                                                                        #TAKING THE USER BACK TO MAIN PART OF PAC AFTER THEY HAVE ASKED A QUERY
        
    if S1 == "Launch Inbox":                                                                                                            #IF THE USERS RESPONSE TO THE QUESTION IS THIS THEN THE FOLLOWING TAKES PLACE
        print(" ")                                                                                                                      #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE
        print("Hold On A Second Sir...")                                                                                                #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE
        time.sleep(2)                                                                                                                   #MAKING THE PROGEAM WAIT 2 SECONDS BEFORE IT DOES THE NEXT PART          
        os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\ER.py")   #THIS IS THE FILE DIRECTORY FOR THE PROGRAM THAT PAC IS TRYING TO ACCESSING
        STAGE1()                                                                                                                        #TAKING THE USER BACK TO MAIN PART OF PAC AFTER THEY HAVE ASKED A QUERY
         
    if S1 == "Launch PIN Crack":                                                                                                        #IF THE USERS RESPONSE TO THE QUESTION IS THIS THEN THE FOLLOWING TAKES PLACE 
        print(" ")                                                                                                                      #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE
        print("Hold On A Second Sir...")                                                                                                #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE  
        time.sleep(2)                                                                                                                   #MAKING THE PROGEAM WAIT 2 SECONDS BEFORE IT DOES THE NEXT PART
        os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\PC.py")   #THIS IS THE FILE DIRECTORY FOR THE PROGRAM THAT PAC IS TRYING TO ACCESSING
        STAGE1()                                                                                                                        #TAKING THE USER BACK TO MAIN PART OF PAC AFTER THEY HAVE ASKED A QUERY
        
    if S1 == "Launch RM":                                                                                                                                #IF THE USERS RESPONSE TO THE QUESTION IS THIS THEN THE FOLLOWING TAKES PLACE
        print(" ")                                                                                                                                       #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE
        print("Hold On A Second Sir...")                                                                                                                 #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE
        time.sleep(2)                                                                                                                                    #MAKING THE PROGEAM WAIT 2 SECONDS BEFORE IT DOES THE NEXT PART
        os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\RESOURCE MANAGEMENT.py")   #THIS IS THE FILE DIRECTORY FOR THE PROGRAM THAT PAC IS TRYING TO ACCESSING
        STAGE1()                                                                                                                                         #TAKING THE USER BACK TO MAIN PART OF PAC AFTER THEY HAVE ASKED A QUERY  
    
    if S1 == "Launch Resource Monitor":                                                                                                                  #IF THE USERS RESPONSE TO THE QUESTION IS THIS THEN THE FOLLOWING TAKES PLACE
        print(" ")                                                                                                                                       #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE
        print("Hold On A Second Sir...")                                                                                                                 #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE
        time.sleep(2)                                                                                                                                    #MAKING THE PROGEAM WAIT 2 SECONDS BEFORE IT DOES THE NEXT PART  
        os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\RESOURCE MANAGEMENT.py")   #THIS IS THE FILE DIRECTORY FOR THE PROGRAM THAT PAC IS TRYING TO ACCESSING
        STAGE1()                                                                                                                                         #TAKING THE USER BACK TO MAIN PART OF PAC AFTER THEY HAVE ASKED A QUERY
    
    if S1 == "What is the meaning of life":                                                                                                              #IF THE USERS RESPONSE TO THE QUESTION IS THIS THEN THE FOLLOWING TAKES PLACE
        print(" ")                                                                                                                                       #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE
        print("42")                                                                                                                                      #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE 
        STAGE1()                                                                                                                                         #TAKING THE USER BACK TO MAIN PART OF PAC AFTER THEY HAVE ASKED A QUERY

    if S1 == "Launch Resource Monitor":                                                                                                                  #IF THE USERS RESPONSE TO THE QUESTION IS THIS THEN THE FOLLOWING TAKES PLACE
        print(" ")                                                                                                                                       #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE
        print("Hold On A Second Sir...")                                                                                                                 #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE
        time.sleep(2)                                                                                                                                    #MAKING THE PROGEAM WAIT 2 SECONDS BEFORE IT DOES THE NEXT PART
        os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\RESOURCE MANAGEMENT.py")   #THIS IS THE FILE DIRECTORY FOR THE PROGRAM THAT PAC IS TRYING TO ACCESSING
        STAGE1()                                                                                                                                         #TAKING THE USER BACK TO MAIN PART OF PAC AFTER THEY HAVE ASKED A QUERY 

    if S1 == "Goodbye PAC":                                     #IF THE USERS RESPONSE TO THE QUESTION IS THIS THEN THE FOLLOWING TAKES PLACE 
        print(" ")                                              #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE
        print("Goodbye Sir See You Soon!")                      #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE
        print(" ")                                              #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE
        print("SYSTEM SHUTTING DOWN... ")                       #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE 
        time.sleep(2)                                           #MAKING THE PROGEAM WAIT 2 SECONDS BEFORE IT DOES THE NEXT PART    
        print("SHUT DOWN COMPLETE. ")                           #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE  
        time.sleep(2)                                           #MAKING THE PROGEAM WAIT 2 SECONDS BEFORE IT DOES THE NEXT PART
        sys.exit()                                              #CLOSING THE PROGRAM DOWN WITH THE USE OF THE 'sys.exit()' FUNCTION THAT IS BUILT IN
    
    elif S1 == "Info":                                          #IF THE USERS RESPONSE TO THE QUESTION IS THIS THEN THE FOLLOWING TAKES PLACE
        mac = get_mac()                                         #CREATING AVARIABLE THAT WILL DISPLAY THE CURRENT MAC ADDRESS
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    #CREATING THE VARIABLE TAHT WILL ALLOW THE MACHINE TO USE THE SOCKETS AND CONNECT TO THE IP 
        s.connect(("8.8.8.8", 80))                              #CONNECTING THE IP ADDRESS THROUGH GOOGLE'S SERVERS 

        SCROLL()                                                #USING THE SCROLL FUNCTION TO LEAVE 5 BLANK LINES BEFORE DOING THE NEXT PART 
        
        print(" ")                                              #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE
        print(("SYSTEM TIME: ")+str(datetime.datetime.now()))   #GATHERING AND THEN DISPLAYING THE CURRENT SYSTEM TIME FOR THE USER TO SEE
        print(" ")                                              #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE
        print(("SYSTEM IP ADDRESS: ")+str(s.getsockname()[0]))  #GATHERING AND THEN DISPLAYING THE CURRENT IP ADDRESS FOR THE USER TO SEE
        print(" ")                                              #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE
        print(("SYSTEM MAC ADDRESS: ")+str(mac))                #GATHERING AND THEN DISPLAYING THE CURRENT MAC ADDRESS FOR THE USER TO SEE
        print(" ")                                              #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE 
        SCROLL()                                                #USING THE SCROLL FUNCTION TO LEAVE 5 BLANK LINES BEFORE DOING THE NEXT PART 
        STAGE1()                                                #TAKING THE USER BACK TO MAIN PART OF PAC AFTER THEY HAVE ASKED A QUERY 

    else:                                                                                         #IF THE USERS RESPONSE IS INVALID THE FOLLOWING WILL TAKE PLACE
        print("I Am Sorry Sir That Response Is NOT In My Directory! I Will Ask Another Question") #DISPLAYING A MESSAGE THAT TELLS THE USER THEY HAD ENTERED AN INVALID RESPONSE
        SCROLL()                                                                                  #USING THE SCROLL FUNCTION TO LEAVE 5 BLANK LINES BEFORE DOING THE NEXT PART   
        STAGE1()                                                                                  #TAKING THE USER BACK TO MAIN PART OF PAC AFTER THEY HAVE ASKED A QUERY 

def STORYTIME():            

    SCROLL()                             #USING THE SCROLL FUNCTION TO LEAVE 5 BLANK LINES BEFORE DOING THE NEXT PART    
    print(" ")                           #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE
    print(STORY[random.randint(0,5)])    #RANDOMLY SELECTING TO DISPLAY 1 OF THE STORIES OUT THE 7 POSSIBLE STORIES THAT ARE IN PAC
    print(" ")                           #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE

    N1=input("Is There Anything Else I Can Do For You, Sir? ") #ASKING THE USER IF THEY WOULD LIKE ANYTHING ELSE

    if N1 == "Yeah":                                                                                                         #IF THE RESPONSE TO THE QUESTION IS "Yeah" THEN THE FOLLOWING WILL TAKE PLACE
       print(" ")                                                                                                            #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE
       print(["Hold On A Second Please, Sir...", "One Moment Please, Sir...", "Just A Second, Sir..."][random.randint(0,2)]) #DISPLAYING A MESSAGE THAT ACKNOWLEDGES WHAT THE USER HAS SELECTED, RANDOMLY SELECTED OUT OF THE THREE
       print(" ")                                                                                                            #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE
       time.sleep(2)                                                                                                         #MAKING THE PROGEAM WAIT 2 SECONDS BEFORE IT DOES THE NEXT PART
       STAGE1()                                                                                                              #TAKING THE USER BACK TO MAIN PART OF PAC AFTER THEY HAVE ASKED A QUERY 

    if N1 == "Yes":                                                                                                          #IF THE RESPONSE TO THE QUESTION IS "Yes" THEN THE FOLLOWING WILL TAKE PLACE
       print(" ")                                                                                                            #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE 
       print(["Hold On A Second Please, Sir...", "One Moment Please, Sir...", "Just A Second, Sir..."][random.randint(0,2)]) #DISPLAYING A MESSAGE THAT ACKNOWLEDGES WHAT THE USER HAS SELECTED, RANDOMLY SELECTED OUT OF THE THREE 
       print(" ")                                                                                                            #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE
       time.sleep(2)                                                                                                         #MAKING THE PROGEAM WAIT 2 SECONDS BEFORE IT DOES THE NEXT PART 
       STAGE1()                                                                                                              #TAKING THE USER BACK TO MAIN PART OF PAC AFTER THEY HAVE ASKED A QUERY

    if N1 == "Sure":                                                                                                         #IF THE RESPONSE TO THE QUESTION IS "Sure" THEN THE FOLLOWING WILL TAKE PLACE 
       print(" ")                                                                                                            #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE 
       print(["Hold On A Second Please, Sir...", "One Moment Please, Sir...", "Just A Second, Sir..."][random.randint(0,2)]) #DISPLAYING A MESSAGE THAT ACKNOWLEDGES WHAT THE USER HAS SELECTED, RANDOMLY SELECTED OUT OF THE THREE
       print(" ")                                                                                                            #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE
       time.sleep(2)                                                                                                         #MAKING THE PROGEAM WAIT 2 SECONDS BEFORE IT DOES THE NEXT PART
       STAGE1()                                                                                                              #TAKING THE USER BACK TO MAIN PART OF PAC AFTER THEY HAVE ASKED A QUERY

    elif N1 == "No":                                       #IF THE RESPONSE TO THE QUESTION IS "No" THEN THE FOLLOWING WILL TAKE PLACE
        print("No Problem Sir I Will Leave You For Now!")  #DISPLAYING A MESSAGE THAT ACKNOWLEDGES THE USERS RESPONSE
        print(" ")                                         #CREATING AN EMPTY PRINT TO ACT AS A ONE LINE SPACE
        print("SYSTEM SHUTTING DOWN... ")                  #DISPLAYING A MESSAGE THAT ACKNOWLEDGES WHAT THE USER HAS SELECTED  
        time.sleep(2)                                      #MAKING THE PROGEAM WAIT 2 SECONDS BEFORE IT DOES THE NEXT PART
        print("SHUT DOWN COMPLETE. ")                      #DISPLAYING A MESSAGE THAT ACKNOWLEDGES WHAT THE USER HAS SELECTED 
        time.sleep(2)                                      #MAKING THE PROGEAM WAIT 2 SECONDS BEFORE IT DOES THE NEXT PART
        sys.exit()                                         #CLOSING THE PROGRAM DOWN WITH THE USE OF THE 'sys.exit()' FUNCTION THAT IS BUILT IN
  
StartUP()

