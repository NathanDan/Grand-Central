#Grand Central Calculator
#Nathan Jones & Mohamed Akil
#2019

from tkinter import *           #ALLOWING FOR ALL OF THE FUNCTIONS OF THE 'googlesearch' LIBARY TO BE UTILISED 
class Application(Frame):

    def __init__(self, master):
        
        super(Application, self).__init__(master)   #CREATING THE MAIN WINDOW OF THE CALCULATOR
        self.task = ""                              #CREATING THE PART THAT WILL KEEP CURRENT CALCULATIONS IN, TO BEGIN WITH IT WILL BE EMPTY
        self.UserIn = StringVar()                   #CREATING THE PART THAT WILL STORE THE VALUES TAHT HAVE BEEN ENTERED
        self.grid()                                 #CREATING THE GRID LAYOUT OF THE CALCULATOR
        self.create_widgets()                       #CREATING THE PART OF THE PROGRAM THAT WILL CREATE AND HOULSE THE BUTTONS 

    def create_widgets(self):

        self.user_input = Entry(self, bg = "light grey", bd = 29,                    #CREATING THE ENTRY WINDOW THAT WILL DISPLAY THE NUMBERS AND EVERYTHING THAT HAS BEEN INPUTTED
        insertwidth = 4, width = 24,                                                 #DEFINGING HOW PARAMETERS OF THE BUTTON 
        font = ("Verdana", 20, "bold"), textvariable = self.UserIn, justify = RIGHT) #DEFINING WHAT IS GOING TO BE DISPLAYED WITHIN THE ACTUAL BUTTON
        self.user_input.grid(columnspan = 4)                                         #DISPLAYING THE TEXT INSIDE THE BUTTON ALONG WITH ITS COMMAND 
 
        self.user_input.insert(0, "0")                                               

        self.button1 = Button(self, bg = "light grey", bd = 12,                    #CREATING A BUTTON THAT WILL DISPLAY THE 7 BUTTON
        text = "7", padx = 33, pady = 25, font = ("Helvetica", 20, "bold"),        #DEFINING WHAT IS GOING TO BE DISPLAYED WITHIN THE ACTUAL BUTTON 
        command = lambda : self.buttonClick(7))                                    #DISPLAYING THE TEXT INSIDE THE BUTTON ALONG WITH ITS COMMAND 
        self.button1.grid(row = 2, column = 0, sticky = W)                         #ASSIGNING THE BUTTON TO BE ON THE LEFT HAND SIDE

        self.button2 = Button(self, bg = "light grey", bd = 12,                    #CREATING A BUTTON THAT WILL DISPLAY THE 8 BUTTON 
        text = "8",  padx = 35, pady = 25,                                         #DEFINING WHAT IS GOING TO BE DISPLAYED WITHIN THE ACTUAL BUTTON
        command = lambda : self.buttonClick(8), font = ("Helvetica", 20, "bold"))  #DISPLAYING THE TEXT INSIDE THE BUTTON ALONG WITH ITS COMMAND 
        self.button2.grid(row = 2, column = 1, sticky = W)                         #ASSIGNING THE BUTTON TO BE ON THE LEFT HAND SIDE

        self.button3 = Button(self, bg = "light grey", bd = 12,                    #CREATING A BUTTON THAT WILL DISPLAY THE 9 BUTTON 
        text = "9",  padx = 33, pady = 25,                                         #DEFINING WHAT IS GOING TO BE DISPLAYED WITHIN THE ACTUAL BUTTON
        command = lambda : self.buttonClick(9), font = ("Helvetica", 20, "bold"))  #DISPLAYING THE TEXT INSIDE THE BUTTON ALONG WITH ITS COMMAND
        self.button3.grid(row = 2, column = 2, sticky = W)                         #ASSIGNING THE BUTTON TO BE ON THE LEFT HAND SIDE 

        self.button4 = Button(self, bg = "light grey", bd = 12,                    #CREATING A BUTTON THAT WILL DISPLAY THE 4 BUTTON
        text = "4",  padx = 33, pady = 25,                                         #DEFINING WHAT IS GOING TO BE DISPLAYED WITHIN THE ACTUAL BUTTON
        command = lambda : self.buttonClick(4), font = ("Helvetica", 20, "bold"))  #DISPLAYING THE TEXT INSIDE THE BUTTON ALONG WITH ITS COMMAND
        self.button4.grid(row = 3, column = 0, sticky = W)                         #ASSIGNING THE BUTTON TO BE ON THE LEFT HAND SIDE 

        self.button5 = Button(self, bg = "light grey", bd = 12,                    #CREATING A BUTTON THAT WILL DISPLAY THE 5 BUTTON
        text = "5",  padx = 35, pady = 25,                                         #DEFINING WHAT IS GOING TO BE DISPLAYED WITHIN THE ACTUAL BUTTON
        command = lambda : self.buttonClick(5), font = ("Helvetica", 20, "bold"))  #DISPLAYING THE TEXT INSIDE THE BUTTON ALONG WITH ITS COMMAND
        self.button5.grid(row = 3, column = 1, sticky = W)                         #ASSIGNING THE BUTTON TO BE ON THE LEFT HAND SIDE

        self.button6 = Button(self, bg = "light grey", bd = 12,                    #CREATING A BUTTON THAT WILL DISPLAY THE 6 BUTTON
        text = "6",  padx = 33, pady = 25,                                         #DEFINING WHAT IS GOING TO BE DISPLAYED WITHIN THE ACTUAL BUTTON
        command = lambda : self.buttonClick(6), font = ("Helvetica", 20, "bold"))  #DISPLAYING THE TEXT INSIDE THE BUTTON ALONG WITH ITS COMMAND
        self.button6.grid(row = 3, column = 2, sticky = W)                         #ASSIGNING THE BUTTON TO BE ON THE LEFT HAND SIDE   

        self.button7 = Button(self, bg = "light grey", bd = 12,                    #CREATING A BUTTON THAT WILL DISPLAY THE 1 BUTTON
        text = "1",  padx = 33, pady = 25,                                         #DEFINING WHAT IS GOING TO BE DISPLAYED WITHIN THE ACTUAL BUTTON
        command = lambda : self.buttonClick(1), font = ("Helvetica", 20, "bold"))  #DISPLAYING THE TEXT INSIDE THE BUTTON ALONG WITH ITS COMMAND
        self.button7.grid(row = 4, column = 0, sticky = W)                         #ASSIGNING THE BUTTON TO BE ON THE LEFT HAND SIDE

        self.button8 = Button(self, bg = "light grey", bd = 12,                    #CREATING A BUTTON THAT WILL DISPLAY THE 2 BUTTON
        text = "2",  padx = 35, pady = 25,                                         #DEFINING WHAT IS GOING TO BE DISPLAYED WITHIN THE ACTUAL BUTTON  
        command = lambda : self.buttonClick(2), font = ("Helvetica", 20, "bold"))  #DISPLAYING THE TEXT INSIDE THE BUTTON ALONG WITH ITS COMMAND
        self.button8.grid(row = 4, column = 1, sticky = W)                         #ASSIGNING THE BUTTON TO BE ON THE LEFT HAND SIDE

        self.button9 = Button(self, bg = "light grey", bd = 12,                    #CREATING A BUTTON THAT WILL DISPLAY THE 3 BUTTON
        text = "3",  padx = 33, pady = 25,                                         #DEFINING WHAT IS GOING TO BE DISPLAYED WITHIN THE ACTUAL BUTTON
        command = lambda : self.buttonClick(3), font = ("Helvetica", 20, "bold"))  #DISPLAYING THE TEXT INSIDE THE BUTTON ALONG WITH ITS COMMAND
        self.button9.grid(row = 4, column = 2, sticky = W)                         #ASSIGNING THE BUTTON TO BE ON THE LEFT HAND SIDE

        self.button9 = Button(self, bg = "light grey", bd = 12,                    #CREATING A BUTTON THAT WILL DISPLAY THE 0 BUTTON 
        text = "0",  padx = 33, pady = 25,                                         #DEFINING WHAT IS GOING TO BE DISPLAYED WITHIN THE ACTUAL BUTTON
        command = lambda : self.buttonClick(0), font = ("Helvetica", 20, "bold"))  #DISPLAYING THE TEXT INSIDE THE BUTTON ALONG WITH ITS COMMAND
        self.button9.grid(row = 5, column = 0, sticky = W)                         #ASSIGNING THE BUTTON TO BE ON THE LEFT HAND SIDE

        self.Addbutton = Button(self, bg = "light grey", bd = 12,                    #CREATING A BUTTON THAT WILL DISPLAY THE ADDITION BUTTON
        text = "+",  padx = 36, pady = 25,                                           #DEFINING WHAT IS GOING TO BE DISPLAYED WITHIN THE ACTUAL BUTTON
        command = lambda : self.buttonClick("+"), font = ("Helvetica", 20, "bold"))  #DISPLAYING THE TEXT INSIDE THE BUTTON ALONG WITH ITS COMMAND
        self.Addbutton.grid(row = 2, column = 3, sticky = W)                         #ASSIGNING THE BUTTON TO BE ON THE LEFT HAND SIDE 

        self.Subbutton = Button(self, bg = "light grey", bd = 12,                    #CREATING A BUTTON THAT WILL DISPLAY THE SUBTRACTION BUTTON
        text = "-",  padx = 39, pady = 25,                                           #DEFINING WHAT IS GOING TO BE DISPLAYED WITHIN THE ACTUAL BUTTON
        command = lambda : self.buttonClick("-"), font = ("Helvetica", 20, "bold"))  #DISPLAYING THE TEXT INSIDE THE BUTTON ALONG WITH ITS COMMAND
        self.Subbutton.grid(row = 3, column = 3, sticky = W)                         #ASSIGNING THE BUTTON TO BE ON THE LEFT HAND SIDE
                    
        self.Multbutton = Button(self, bg = "light grey", bd = 12,                   #CREATING A BUTTON THAT WILL DISPLAY THE MULTIPLICATION BUTTON  
        text = "*",  padx = 38, pady = 25,                                           #DEFINING WHAT IS GOING TO BE DISPLAYED WITHIN THE ACTUAL BUTTON
        command = lambda : self.buttonClick("*"), font = ("Helvetica", 20, "bold"))  #DISPLAYING THE TEXT INSIDE THE BUTTON ALONG WITH ITS COMMAND
        self.Multbutton.grid(row = 4, column = 3, sticky = W)                        #ASSIGNING THE BUTTON TO BE ON THE LEFT HAND SIDE

        self.Divbutton = Button(self, bg = "light grey", bd = 12,                    #CREATING A BUTTON THAT WILL DISPLAY THE DIVISION BUTTON
        text = "/",  padx = 39, pady = 25,                                           #DEFINING WHAT IS GOING TO BE DISPLAYED WITHIN THE ACTUAL BUTTON 
        command = lambda : self.buttonClick("/"), font = ("Helvetica", 20, "bold"))  #DISPLAYING THE TEXT INSIDE THE BUTTON ALONG WITH ITS COMMAND 
        self.Divbutton.grid(row = 5, column = 3, sticky = W)                         #ASSIGNING THE BUTTON TO BE ON THE LEFT HAND SIDE

        self.Equalbutton = Button(self, bg = "light grey", bd = 12,                  #CREATING A BUTTON THAT WILL DISPLAY THE EQUAL BUTTON
        text = "=",  padx = 100, pady = 25,                                          #DEFINING WHAT IS GOING TO BE DISPLAYED WITHIN THE ACTUAL BUTTON
        command = self.CalculateTask, font = ("Helvetica", 20, "bold"))              #DISPLAYING THE TEXT INSIDE THE BUTTON ALONG WITH ITS COMMAND  
        self.Equalbutton.grid(row = 5, column = 1, sticky = W, columnspan = 2)       #ASSIGNING THE BUTTON TO BE ON THE LEFT HAND SIDE

        
        self.Clearbutton = Button(self, bg = "light grey", bd = 12,                                       #CREATING A BUTTON THAT WILL DISPLAY THE EQUAL BUTTON
        text = "AC", font = ("Helvetica", 20, "bold"), width = 28, padx = 7, command = self.ClearDisplay) #DEFINING WHAT IS GOING IN THE BUTTON AND DISPLAYING IT
        self.Clearbutton.grid(row = 1, columnspan = 4, sticky = W)                                        #ASSIGNING THE BUTTON TO BE ON THE LEFT HAND SIDE

    def buttonClick(self, number):               #WHEN A BUTTON HAS BEEN PRESSED THE FOLLOWING WILL TAKE PLACE 
        self.task = str(self.task) + str(number) #TAKING THE NUMBER AND STORING IT UNTIL CALLED AGAIN
        self.UserIn.set(self.task)               #STORING THE NUMBER

    def CalculateTask(self):                     #ONCE ONE OF THE CALCULATIONS BUTTONS HAS BEEN PRESSED THE FOLLOWING WILL TAKE PLACE 
        self.data = self.user_input.get()        
        try:
            self.answer = eval(self.data)        
            self.displayText(self.answer)        #DISPLAYING THE ANSWER FOR THE USER
            self.task = self.answer              #DEFINING WHAT TEH ANSWER IS  

        except SyntaxError as e:
            self.displayText("Invalid Syntax!")  #THIS IS IF AN INVALID RESPONSE IS GIVEN BY THE USER AND THE ERROR MESSAGE WILL DISPLAY
            self.task = ""                       #

    def displayText(self, value):                #DISPLAYING THE ACTUAL TEXT IN THE CALCULATOR
        self.user_input.delete(0, END)           
        self.user_input.insert(0, value)         #DISPLAYING THE VALUES TAHT HAVE BEEN ENTERED 

    def ClearDisplay(self):                      #ONCE THE ALL CLEAR BUTTON HAS BEEN PRESSED THE FOLLOWING WILL TAKE PLACE
        self.task = ""                           #SETTING THE TASK BACK TO BEING EMPTY
        self.user_input.delete(0, END)           #CLEARING ALL SUMS
        self.user_input.insert(0, "0")           #CLEARING ALL OF THE DISPLAY WINDOW SO IT IS EMPTY     


calculator = Tk()                                      #DEFINING WHAT THE WINDOW WILL BE KNOWN AS 
calculator.title("Calculator")                         #DEFINING THE TITLE OF THE WINDOW
app = Application(calculator)                          #CREATING THE APPLICATION VARIABLE 
calculator.resizable(width = False, height = False)    #MEANS THAT THE WINDOW CAN NOT BE RESIZED BY THE USER  

calculator.mainloop()
