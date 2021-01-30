#Nathan Jones
#GRAND CENTRAL v3 - SQC TEACH EDITION
#2018

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

def SCROLL():

    Scroll="\n"*70
    print(Scroll)

def SCROLL2():

    Scroll2="\n"*10
    print(Scroll2)

def SCROLL3():

    Scroll3="\n"*28
    print(Scroll3)      


def SCIENCE_QUESTIONS():

    print("""
███████╗ ██████╗██╗███████╗███╗   ██╗ ██████╗███████╗                        
██╔════╝██╔════╝██║██╔════╝████╗  ██║██╔════╝██╔════╝                        
███████╗██║     ██║█████╗  ██╔██╗ ██║██║     █████╗                          
╚════██║██║     ██║██╔══╝  ██║╚██╗██║██║     ██╔══╝                          
███████║╚██████╗██║███████╗██║ ╚████║╚██████╗███████╗                        
╚══════╝ ╚═════╝╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝╚══════╝                        
                                                                             
 ██████╗ ██╗   ██╗███████╗███████╗████████╗██╗ ██████╗ ███╗   ██╗            
██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║            
██║   ██║██║   ██║█████╗  ███████╗   ██║   ██║██║   ██║██╔██╗ ██║            
██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║   ██║██║   ██║██║╚██╗██║            
╚██████╔╝╚██████╔╝███████╗███████║   ██║   ██║╚██████╔╝██║ ╚████║            
 ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝            
                                                                             
 ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝ 

""")
   
    FUNCT_MENU()

def SCROLL2():

    Scroll="\n"*5
    print(Scroll)

def FUNCT_MENU():

    print(("SYSTEM TIME: ")+str(datetime.datetime.now()))
    print(" ")
    print("####################################")
    print("#       Welcome to the MENU        #")
    print("#                                  #")
    print("#            ?. HELP               #")
    print("#                                  #")
    print("#          1. Key Stage 1          #")
    print("#          2. Key Stage 2          #")
    print("#          3. Key Stage 3          #")
    print("#          4. Key Stage 4          #")
    print("#                                  #")
    print("#            ~. LOG OUT            #")
    print("#            Q. QUIT               #")
    print("#                                  #")
    print("####################################")

    answer=input("What option do you choose? ")

    if answer == "?":
       Scroll2="\n"*5
       SCROLL2()
       Funct_HELP()

    elif answer == "1":
       SCROLL()
       Funct_KS1()

    elif answer == "2":
       SCROLL()
       Funct_KS2()

    elif answer == "3":
       SCROLL()
       Funct_KS3()

    elif answer == "4":
       SCROLL()
       Funct_KS4()

    elif answer == "~":
       SCROLL() 
       os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\TK_LOGIN_v3.py")
       sys.exit()

    elif answer == "Q" or "q":
       SCROLL()
       print("GOODBYE!...")
       print(" ")
       print("LOADING...")
       time.sleep(5)
       SCROLL()
       os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-TEACH\\TK_TEACH_v3.py")
       sys.exit()
       
    

    else:
       SCROLL()
       print(answer)
       print(" ")
       print("INVALID ANSWER! - TRY AGAIN")
       print(" ")
       FUNCT_MENU()

def Funct_HELP():

   print(("SYSTEM TIME: ")+str(datetime.datetime.now()))
   print(" ")
   print(""" HELP!

The program is designed to randomly select a science question for the
give topic and Key Stage you have asked for.

It does this by YOU the user selecting which Key Stage and Topic you
would like and then the question is randomly selected from the question
database which is pre-loaded with exisitng questions for each Key Stage
and Topic.

If YOU end up in the wrong Key Stage YOU can simply type 'B' to return
back to the previous menu.

Once a question has been given the program will then ask you if you would
like another question or not, if 'N' is selected then you will return back
to the Key Stage menu, but if you select 'Y' then another randomly selected
question will be given. - This process will continue until you select 'N'.
""")

   answer=input("Would you like to return to the menu? Y/N ")

   if answer == "Y" or "y":
       print(" ")
       print("LOADING...")
       print(" ")
       FUNCT_MENU()

   elif answer == "N" or "n":
       print(" ")
       Funct_HELP()

   else:
       print(answer)
       print(" ")
       print("INVALID ANSWER - TRY AGAIN")
       print(" ")
       Funct_HELP()

def Funct_KS1():

   KS1=["""
Toni wants to do an investigation in her class. She is going to ask people a question.

Which one of these questions would be the best one to investigate?
 
Do you know what a rainbow is?
Do you like the colour blue?
Do you like rainbows?
Which colour in the rainbow do you like best?""",
       """
Scientists investigate all these questions.

But which one of these questions could you investigate in a school?
 
What are the rocks on the planet Mars made from?
Why are there no green plants at the bottom of the oceans?
Why are there fewer parrots in the Amazon rain-forest?
What sort of places do woodlice like to live in?""",
        """
Tanya has had a cold. She has an idea for an investigation.

What do you think it is?
 
Which type of tissue is smallest?
Which type of tissue is the most colourful?
Which type of tissue is stretchiest?
Which type of tissue is the most absorbent?""",
        """
Anna knows that plants grow quicker in the summer than the winter.

Which one of these questions would be fun for Anna to investigate?
 
Do children grow quicker in the summer than the winter?
Do children grow?
Do children grow older each year?
Do children have birthdays?""",
        """
Which one of these is a question you could investigate in science?
 
Can a pencil be used to write with?
Are pencils alive?
How are pencils made?
What can you draw with a pencil?""",
        """
Which one of these questions would you have to investigate outdoors?
 
How quickly does grass grow again after it has been mown?
What is the best way to grow cress?
How much water do plants need?
How deep should I plant bean seeds?""",
        """
Which one of these questions could you investigate at school?
 
Which is the stretchiest modelling clay?
Which is the nicest modelling clay?
Who makes modelling clay?
How much modelling clay have we got?""",
        """
All of these are questions. Some have simple answers.

But which one could you investigate?
 
How many months are there in a year?
Which month in the year is the warmest?
Which is the shortest month in the year?
Which is the first month of the year?""",
        """
Which one of these questions would be good to ask in science?
 
Which word is longest - reptile, bird or mammal?
What are the differences between reptiles, birds and mammals?
Can you draw a reptile?
What is a good story about a bird?""",
        """
Sasha has decided to investigate this question: ‘What is the best material to make an umbrella?’

Sasha decides to put the question another way. Which is the best question for him to ask?
 
Which material is heaviest and lets the water through?
Which material is lightest and waterproof?
Which material is most colourful?
Which material is lightest and most colourful?"""]

   print(("SYSTEM TIME: ")+str(datetime.datetime.now()))
   print(" ")
   print("WELCOME TO KS1!")
   print(" ")
   print("KEY STAGE 1 SCIENCE QUESTION IS")
   print(random.choice(KS1))
   print(" ")
   answer=input("Do YOU want another question? Y/N ")

   if answer == "Y":
       print("LOADING... ")
       SCROLL2()
       Funct_KS1()

   elif answer == "N":
       SCROLL()
       print("LOADING...")
       SCROLL2()
       FUNCT_MENU()

   else:
       SCROLL() 
       FUNCT_MENU()
       
       

def Funct_KS2():


   KS2=["""
Sam goes to the duck pond with his grandad.

Two of the ducks come out of the pond.

Describe how a duck’s feet are adapted for swimming.""",
        """
Peter goes to the duck pond with his grandad and his dog.

CIRCLE TWO to show two things that are true about a dog and
a duck.

They both have fur.    They both move.

They both lay eggs.    They both breathe.""",
        """
Explain why the female duck needs to stay hidden when
she is in her nest.""",
        """
Tom sees some piles of soil on the grass near the pond.

Grandad tells him that the piles of soil are made by
animals called moles.

Describe how a feature of the mole helps the mole to
live underground.""",
        """
Which word cannot be used to describe a mole?
Circle ONE word.

  prey   producer   predator   consumer""",
        """
Class 6 have collected different types of seed.

They blow the seeds with a fan.
This disperses the seeds.

They measure how far each seed travels.

What equipment can measure how far the seeds travel?""",
        """
The seeds can be blown by the children’s mouths or with a fan.

Explain why the fan helps to make the test fair.""",
        """
The children dispersed the seeds with a fan.
The fan disperses seeds like the wind does in nature.

Name ONE other way seeds are dispersed in nature.""",
        """
Class 6 are investigating how grass grows.
They grow grass on grass heads filled with sand.
They keep their grass heads standing in dishes of water so they do not
dry out.

All plants need water to grow.

Name TWO other things that all plants need to grow.""",
        """
Some children give their grass head a hat.
They keep all other conditions the same.

The children predict that when the grass under the hat grows, it will look
more yellow than the grass not covered by the hat.

Give ONE reason why the grass under the hat might look more yellow.""",
        """
Smallpox and cowpox are diseases. People who catch smallpox can die.

Dr Jenner discovered how to stop people catching smallpox.

What sort of statement did Dr Jenner make? Circle ONE word.

  explanation   prediction   comparison   observation
"""]

   print(("SYSTEM TIME: ")+str(datetime.datetime.now()))
   print(" ")
   print("WELCOME TO KS2!")
   print(" ")
   print("KEY STAGE 2 SCIENCE QUESTION IS")
   print(random.choice(KS2))
   print(" ")
   answer=input("Do YOU want another question? Y/N ")   

   if answer == "Y":
       print("LOADING... ")
       SCROLL2()
       Funct_KS2()

   elif answer == "N":
       SCROLL()
       print("LOADING...")
       SCROLL2()
       FUNCT_MENU()

   else:
       SCROLL() 
       FUNCT_MENU()   

def Funct_KS3():

    KS3=["""
Jack and Aneesa dropped a steel ball into trays of damp sand.
They measured the depth of the craters made by the steel ball.

Their results are shown in the table below:

   Height the ball was               Depth of crater (cm)
    dropped from (cm)          Jack’s results   Aneesa’s results
                                
        10                      1.1   1.2              0.8
        20                      1.4   1.5              1.4
        30                      1.6   1.6              1.5
        40                      1.8   1.7              1.8
        50                      2.0   2.1              2.1

(a) Use information in the table to answer the questions below.

    (i) What was the independent variable that Jack and Aneesa changed
        in their investigation?

    (ii) Why was Jack’s investigation better than Aneesa’s?""",
         """
Mark and Jo dropped a steel ball into trays of damp sand.
They measured the depth of the craters made by the steel ball.

Their results are shown in the table below:

   Height the ball was               Depth of crater (cm)
    dropped from (cm)          Jack’s results   Aneesa’s results
                                
        10                      1.1   1.2              0.8
        20                      1.4   1.5              1.4
        30                      1.6   1.6              1.5
        40                      1.8   1.7              1.8
        50                      2.0   2.1              2.1

(a)  Look at the results in the table.

     What is the relationship between the height the ball was dropped from
     and the depth of the crater?


(b) Jo said that they made sure the investigation was fair.

    Suggest two variables they must have kept the same to make their
    investigation fair.

    1.

    2.""",
         """
 A gannet is a type of sea bird.

(a) When a gannet flies at a constant height above the sea, there is a downward
    force of 30 N on the gannet.

    What is the size of the upward force on the gannet?

    Tick the correct ONE.
    
            less than 30 N
            exactly 30 N
            more than 30 N
            need more information""",
         """
(a) To catch food, the gannet dives down into the sea.

    What is the useful energy transfer when the gannet dives?
    Choose words from the box below.
    
    +--------+-------------------------+-------+---------+------+
    |thermal | gravitational potential | sound | kinetic | light|
    +--------+-------------------------+-------+---------+------+

    When the gannet dives,______________________ energy is
    transferred to ______________________ energy.
""",
         """
 (a)Gannets have pockets of air between their muscles and their skin.
    Suggest how this is a good adaptation for gannets when they hit the
    water at fast speeds.


(b) The gannet releases energy through respiration.
    An aeroplane also releases energy when fossil fuels burn.

Write two other ways that respiration and burning are similar.
1.

2.""",
         """
(a) The table below contains descriptions of parts of the human reproductive system.
    Complete the table to give the name of each part.

        name of part  |                 description
                      |
                      |  the tube that carries an egg to the uterus
                      |         the organ that produces sperm
                      |        the organ that produces the egg
    """,
         """
Complete the sentences below by filling in the gaps.

    In humans, normal pregnancy lasts for ____ months.
    When the foetus is ready to be born, muscles in the
    uterus wall start to          .

    After the baby is born, the _________________ connecting the
    foetus to the mother is cut.""",
         """
 Josh has a helium-filled balloon.

(a) He wants to calculate the speed of his balloon as it rises to the ceiling.

    (i) What two measurements should he take to calculate the average speed
        of his balloon?
    1.

    2.

    (ii) How can he use these measurements to calculate the speed of
        his balloon?

""",
         """
A sample of air in a balloon is cooled.

Complete the sentences below using words from the box.

    You may use each word more than once.

    +----------+-----------+---------------+
    |increases | decreases | stays the same|
    +----------+-----------+---------------+
    
    When the air is cooled, the volume of the air ______________________ and
    the mass of the air ______________________.

    When the air is cooled, the density of the air _________________________.
""",
         """
Jenny is doing her homework.

    (a) When Jenny writes, the pencil exerts a force of 5 N on the paper.

        The area of the pencil in contact with the paper is 0.5 mm2.

        Calculate the pressure of the pencil on the paper.
        Give the unit
        """]

    print(("SYSTEM TIME: ")+str(datetime.datetime.now()))
    print(" ")
    print("BIOLOGY KEY SATGE 3 QUESTION IS")
    print(random.choice(KS3))
    print(" ")
    answer=input("Do YOU want another question? Y/N ")   

    if answer == "Y":
        print("LOADING... ")
        SCROLL2()
        Funct_KS3()

    elif answer == "N":
        SCROLL()
        print("LOADING...")
        SCROLL()
        FUNCT_MENU()

    else:
        SCROLL() 
        FUNCT_MENU()

       
def Funct_KS4():

   print(("SYSTEM TIME: ")+str(datetime.datetime.now()))
   print(" ")
   print("####################################")
   print("#          Welcome to KS4          #")
   print("#                                  #")
   print("#           ?. HELP                #")
   print("#                                  #")
   print("#          1. Biology              #")
   print("#          2. Chemistry            #")
   print("#          3. Physics              #")
   print("#                                  #")
   print("#           B. BACK                #")
   print("#                                  #")
   print("####################################")

   answer=input("What option do you choose? ")   

   if answer == "?":
      SCROLL2()
      Funct_HELP()

   elif answer == "1":
       print(" ")
       SCROLL()
       print("LOADING...")
       print(" ")
       Funct_BIO4()

   elif answer == "2":
       print(" ")
       SCROLL()
       print("LOADING...")
       print(" ")
       Funct_CHEM4()

   elif answer == "3":
       print(" ")
       SCROLL()
       print("LOADING...")
       print(" ")
       Funct_PHY4()

   elif answer == "B" or "b":
      SCROLL()
      FUNCT_MENU()
   
   else:
       print("INVALID ANSWER - TRY AGAIN")
       SCROLL2()
       Funct_KS4()

def Funct_BIO4():

    BIO4=["""
Some students investigated the effect of pH on the digestion of boiled egg white by an
enzyme called pepsin. Egg white contains protein.

 The students:

 - put a glass tube containing boiled egg white into a test tube
 - added a solution containing pepsin at pH 7
 - set up six more tubes with solutions of pepsin at different pH values
 - left the test tubes for 24 hours at room temperature.

    (i)Name the product of protein digestion.


    (ii) What type of enzyme digests protein?
         Circle ONE.

             amylase
             lipase
            protease  """,
         """
      The egg white in each tube was 50 mm long at the start of the investigation.
      Table 1 shows the students’ results.

              Table 1

            pH   |   Length in mm of boiled
                 |  egg white after 24 hours
                 |
            1    |            38
            2    |            20
            3    |            34
            4    |            45
            5    |            50
            6    |            50
            7    |            50

   (i) At which pH did the pepsin work best?

       pH ________


    (ii) The answer you gave in part (a)(i) may not be the exact pH at which pepsin works
         best.

         What could the students do to find a more accurate value for this pH?

        Explain why

        """,
         """
In this question you will be assessed on using good English, organising
information clearly and using specialist terms where appropriate.

         Diffusion is an important process in animals and plants.

         The movement of many substances into and out of cells occurs by diffusion.

         Describe why diffusion is important to animals and plants.

         In your answer you should refer to:

         -animals
         -plants
         -examples of the diffusion of named substances.
         """,
         """
After running for several minutes, the athlete’s leg muscles began to ache.
This ache was caused by a high concentration of lactic acid in the muscles.

         The equation shows how lactic acid is made.

              glucose ----> lactic acid (+ energy)

     Name the process that makes lactic acid in the athlete’s muscles.
     """,
         """
The bladder wrack has many air bladders.
The air bladders help the bladder wrack to float upwards when the sea covers it.

    Suggest how this helps the bladder wrack to survive.
    """,
         """
Phenylketonuria (PKU) is an inherited condition. PKU makes people ill.

   PKU is caused by a recessive allele.
       (i) What is an allele?

      (ii) What is meant by recessive?""",
         """
The number of fish in the oceans is decreasing.

Table 1 shows information about the mass of fish caught by UK fishermen between
2002 and 2010.

                                Table 1


         Mass of fish caught by       Mass of fish caught by       Percentage of
 Year      UK fishermen from            UK fishermen from        fish caught from
               ALL SOURCES              SUSTAINABLE SOURCES          sustainable
          in thousands of tonnes       in thousands of tonnes          sources
 
 2002            690.0                        427.8                     62.0
 2004            655.0                        396.6                     60.5
 2006            619.0                        386.0                     62.4
 2008            589.0                        436.1                     74.0
 2010            611.5                        465.0

    (i) Calculate the percentage of fish caught from sustainable sources in 2010.


    (ii) Describe the pattern in Table 1 for the mass of fish caught from all sources.
         Suggest reasons for this pattern.""",
         """
In a fish farm, large numbers of fish are grown in cages in the sea.

    Why do fish in the cages grow faster than fish of the same species that are free
    in the sea?

    You should refer to energy in your answer.
    """,
         """
In this question you will be assessed on using good English, organising
information clearly and using specialist terms where appropriate.

    Deforestation affects the environment.

    Deforestation is causing a change in the amounts of different gases in the atmosphere.
    This change causes global warming and climate change.

    Give the reasons why deforestation is taking place.

    Describe how deforestation is causing the change in the amounts of different gases
    in the atmosphere.
""",
         """
Blood is part of the circulatory system.

      (a) (i) Give one function of white blood cells.


         (ii) Which of the following is a feature of platelets?
             Circle ONE.

                 They have a nucleus.
                 They contain haemoglobin.
                 They are small fragments of cells.

     (b) Urea is transported by the blood plasma from where it is made to where the urea is
         excreted.

        Complete the following sentence.

        Blood plasma carries urea from where it is made in the __________ 
        to the ________________ where the urea is removed from the blood."""]

    print(("SYSTEM TIME: ")+str(datetime.datetime.now()))
    print(" ")
    print("BIOLOGY KEY SATGE 4 QUESTION IS")
    print(random.choice(BIO4))
    print(" ")
    answer=input("Do YOU want another question? Y/N ")   

    if answer == "Y":
        print("LOADING... ")
        SCROLL2()
        Funct_BIO4()

    elif answer == "N":
        SCROLL()
        print("LOADING...")
        SCROLL2()
        Funct_KS4()

    else:
        SCROLL() 
        Funct_KS4()   

def Funct_CHEM4():

    CHEM4=["""
(i) Athletes sometimes take drugs because the drugs improve their performance. One of  
    these drugs is ephedrine.

        Ephedrine has the formula:

                C(10) H(15) N(O)

        What relative molecular mass (Mr) would be recorded by GC-MS if ephedrine was
        present in a blood sample taken from an athlete?

        Show clearly how you work out your answer.
        Relative atomic masses: H = 1; C = 12; N = 14; O = 16.

        Relative molecular mass = ________________

(ii) Another drug is amphetamine which has the formula:

                    C(9) H(13) N

        The relative molecular mass (Mr) of amphetamine is 135.
        Calculate the percentage by mass of nitrogen in amphetamine.
        Relative atomic mass: N = 14

        Percentage of nitrogen = ________________ % """,
         """
Athletes are regularly tested for drugs at international athletics events.

    (i) An instrumental method such as GC-MS is better than methods such as titration.

        Suggest two reasons why.


    (ii) When a blood sample is taken from an athlete the sample is often split into two portions.
         Each portion is tested at a different laboratory.

         Suggest why. """,
         """
Waste water from some industrial processes contains metal ions, such as chromium ions.
These metal ions must be removed from the water before the water is returned to a river.

    (a) A method of removing chromium ions (Cr3+) from water is represented by this equation.
        Balance the equation.

        Cr3+(aq) + ________________ OH-(aq) ----> Cr(OH)3(s) 


    (b) Suggest a suitable chemical that could be added to the water to provide the OHñ
        ions.

 
    (c) Explain how chromium ions are removed from the water.""",
         """
Ammonia is a gas at room temperature.

    (a)Explain why ammonia has a low boiling point.

Ammonia dissolves in water to form a solution with a pH of about 10.

    (b)(i) Name the ion in the ammonia solution that causes the pH of 10.

                               ________________ion

Ammonium nitrate is made by reacting ammonia with an acid.

       (ii) Name the acid.
                               ______________acid""",
         """
A sword is about 3400 years old. It is made of an alloy called bronze.

    Bronze is made from copper and tin.
    Bronze made better swords than pure copper. This is because bronze is harder than
    pure copper.

    Explain why bronze is harder than pure copper.
    Your answer should include details of:

    - how the atoms are arranged in pure copper and bronze
    - why pure copper is relatively soft
    - why bronze is harder. """,
         """
Drinks bottle is made of thermosoftening plastic.

    Drinks bottles of this type can be recycled.

    Describe and explain how these used plastic bottles can be changed into new plastic
    objects. """,
         """
Aspirin tablets have important medical uses.

    Aspirin is made when salicylic acid reacts with ethanoic anhydride.
    The equation for this reaction is:

         C(7) H(6) O(3) + C(4) H(6) O(3) ----> C(9) H(8) O(4) + CH(3)COOH
                salicylic acid                     aspirin

     Calculate the maximum mass of aspirin that could be made from 100 g of salicylic acid.
     Show clearly how you work out your answer.
     The relative formula mass (Mr) of salicylic acid is 138.
     The relative formula mass (Mr) of aspirin is 180.
 
 Maximum mass of aspirin = ______________ g 
""",
         """
Drain Buster is used to clear and degrease drains. Sodium hydroxide is the main
chemical substance in Drain Buster.

    A student planned an experiment to find the concentration of the sodium hydroxide
    solution in Drain Buster.

     The teacher had to dilute the Drain Buster before the student could use it.

     Explain why.""",
         """
In this question you will be assessed on using good English, organising information
clearly and using specialist terms where appropriate.

     The student wanted to find the volume of hydrochloric acid that reacts with a known
     volume of diluted Drain Buster.

     Describe how the student could do this by titration.
     In your description you should include:

        - the names of pieces of apparatus used
        - the names of the substances used
        - a risk assessment. """,
         """
Water is a natural resource. Drinking water in some parts of the UK is soft, but in other
parts drinking water is hard. Calcium ions in water cause water to be hard.

    There are two types of hard water, permanent hard water and temporary hard water.

    - Permanent hard water can be caused by calcium sulfate (CaSO4) dissolved in the
      water.
    - Temporary hard water can be caused by calcium hydrogencarbonate (Ca(HCO3)2)
      dissolved in the water.

    Temporary hard water causes the formation of scale on heating elements.

        (i) Explain how scale forms on heating elements.
 
        (ii) Suggest why scale on heating elements causes problems. """]

    print(("SYSTEM TIME: ")+str(datetime.datetime.now()))
    print(" ")
    print("CHEMISTRY KEY STAGE 4 QUESTION IS")
    print(random.choice(CHEM4))
    print(" ")
    answer=input("Do YOU want another question? Y/N ")   

    if answer == "Y":
        print("LOADING... ")
        SCROLL2()
        Funct_CHEM4()

    elif answer == "N":
        SCROLL()
        print("LOADING...")
        SCROLL2()
        Funct_KS4()

    else:
        SCROLL() 
        Funct_KS4()   

def Funct_PHY4():

    PHY4=["""
A student designed the circuit below to measure temperature using a thermistor.

To calibrate the thermistor to measure temperature, the student placed the thermistor in
a beaker of water at 0°C and took the voltmeter reading. The student then heated the
water slowly with a Bunsen burner. The student recorded the reading on the voltmeter
every 10 °C.

      (i) Before calibrating the thermistor the student completed a risk assessment.

             Write down ONE possible hazard that the student should have written in the risk
             assessment and what the student should do to reduce the risk of the hazard causing
             an injury.

       (ii) At 0 °C the reading on the ammeter is 0.5A.
            Calculate the reading on the voltmeter at 0 °C.
            Write down the equation you use, and then show clearly how you work out your answer.

            Voltmeter reading = ________________ V """,
         """
The chart shows the average radiation dose that a person in the UK receives each
year from natural background radiation.

        The doses are measured in millisieverts (mSv).

                    Food & Drink = 0.30
                    Buildings & Soil = 0.4
                    Cosmic Rays = 0.4
                    Radon = 0.90
    
       Some types of job increase the radiation dose a worker receives.
       People working as aircrew receive an increased radiation dose due to flying at high
       altitude.

    (i) The radiation dose from which source of background radiation is increased by flying?


    (ii) The following table gives the average additional radiation dose received by aircrew
         flying to various destinations from London.

                   Flight time   Average additional
    Destination     in hours       radiation dose
                                       in mSv

    Edinburgh          1                0.004
    Istanbul           5                0.025
    Toronto            8                0.050
   Los Angeles         11               0.065
     Tokyo             13               0.075

 What is the relationship between flight time and average additional radiation dose?
 
    (iii) A flight from London to Jamaica takes 10 hours.

             Estimate the likely value for the average additional radiation dose received by people
             on this flight.

            Average additional radiation dose = ________________  mSv
            Give a reason for your answer.
            """,
         """
In the early part of the 20th century scientists used the 'plum pudding' model to explain
the structure of the atom.

     (i) What did scientists think that the 'pudding' part of the atom was?

     (ii) Following the work of Geiger and Marsden, the 'plum pudding' model of the atom was
          replaced by the 'nuclear model' of the atom.

          Explain why it is sometimes necessary for scientists to replace a scientific model.
          """,
         """
Two vehicles have the same mass and identical engines.
    
    Explain why the top speed of the car is greater than the top speed of the van.""",
         """
In the UK mains electricity is a 230 volt a.c. supply.

    (a) What is the frequency of the a.c. mains electricity in the UK?

    (b)(i) What is an electric current?
 
    (ii) Explain the difference between an a.c. (alternating current) electricity supply and a
         d.c. (direct current) electricity supply.
 

    (c) A householder has a 10.8 kW electric shower installed in the bathroom.

        Calculate the current drawn from the mains electricity supply by the shower.
        Write down the equation you use, and then show clearly how you work out your answer.

        Current = ________________ A """,
         """
A car has a mass of 1200 kg.

    Calculate the kinetic energy of the car when it travels at a speed of 12 m/s.
    Write down the equation you use, and then show clearly how you work out your answer.
 
    Kinetic energy = ________________ J """,
         """
Use words from the box to complete the following sentence.

    +---------------+--------+------+-------+
    |ciliary muscle | cornea | iris | pupil |
    +---------------+--------+------+-------+
            
    The shape of the lens is changed by the ________________________________ ,this
    allows the lens together with the ______________________________ to focus light
    onto the retina. """,
         """
Give two similarities between an eye and a camera.

    1.

    2.
""",
         """
Both X-ray machines and CT scanners are used to produce images of the body.

    Before switching on the X-ray machine, the radiographer goes behind a screen.

    Explain why the radiographer does this.
    """,
         """
The following is an extract from a newspaper article.

            X-rays cause 700 new cancers each year in the UK
        Each year there are about 125 000 new cancer cases in the UK, of
           which about 700 may be due to the use of X-rays to diagnose
                             illness.

        The article was reporting on a scientific research project first published in a medical
        journal.

        (i)What evidence would the scientists have collected to come to the conclusion that X-rays
           can cause cancer?

       (ii)Explain the advantage of a CT scan compared to an X-ray. """]

    print(("SYSTEM TIME: ")+str(datetime.datetime.now()))
    print(" ")
    print("PHYSICS KEY STAGE 4 QUESTION IS")
    print(random.choice(PHY4))
    print(" ")
    answer=input("Do YOU want another question? Y/N ")   

    if answer == "Y":
        print("LOADING... ")
        SCROLL2()
        Funct_PHY4()

    elif answer == "N":
        SCROLL()
        print("LOADING...")
        SCROLL2()
        Funct_KS4()

    else:
        SCROLL() 
        Funct_KS4()

SCIENCE_QUESTIONS()
