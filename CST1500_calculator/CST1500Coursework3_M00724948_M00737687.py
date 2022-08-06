'''
COURSEWORK3 CST1500
M00724948 Sebastian Sokalski
M00737687 Sebastian Gastol
'''
from tkinter import * # import everything from tkinter librart
import math # import math module
import threading # import threading module
# create Interface for calculator program which inherit from Tk library


class Calc(Tk):
    def __init__(self): # initialize the class
        super().__init__()  # override constructor of the superclass
        self.title('Calculator') # set the title for tk window
        self.frame_display = Frame(self) # create frame for calculator display
        self.frame_display.pack() # use pack geometry manager to organise position of the display
        self.value = StringVar() # create variable for the display
        self.value.set('0') # assign starting variable for the display and set it to '0'
        self.display = Entry(self.frame_display, font=('digital-7', 36, 'bold'), # create entry object
                             textvariable=self.value, fg='lightblue', bg='grey', bd=30, width=18, justify=RIGHT)
        self.display.pack() # use pack geometry manager to organise position of the display
        self.factorial_value = 1 # set starting factorial value
        self.frame_keyboard = Frame(self) # create frame for the keyboard
        self.frame_keyboard.pack() # use pack geometry manager to organise position of the display
        self.buttons = '7,8,9,+,SIN,4,5,6,-,COS,1,2,3,*,TAN,0,.,C,/,!,(,),E,**,=' # variable to store values of the buttons
        self.eval_op = '+,-,*,**,.,/,(,)' # variable to store mathematical operations which can be evalueted using eval function
        self.math_op = {'SIN':math.sin, 'COS':math.cos,'TAN':math.tan, 'E':math.e} # create dictionary with additional math functions
        font = ('arial', 36, 'bold') # set default font value
        for i, button in enumerate(self.buttons.split(',')): # create keyboard
            if button.isdigit() or button in self.eval_op: # crete button objects for numeric section and functions that can be calculated using eval funtion
                self.button = Button(self.frame_keyboard, text=button, command=lambda j=button: self.input(j))
                if button.isdigit(): # configure properies of digit buttons
                    self.button.config(bg='#d4c696', activebackground='#696455', activeforeground='#e6cb6c')
                else: # configure properties of function buttons
                    self.button.config(bg='#a32626', activebackground='#4a1b1b', activeforeground='#b80707')
            elif button in self.math_op: # create button objects for buttons from self.math_op dictionary
                self.button = Button(self.frame_keyboard, text=button, command=lambda j=button: self.calc_math(j))
                # configure properties for object buttons from self.math_op
                self.button.config(bg='#a32626', activebackground='#4a1b1b', activeforeground='#b80707')
            elif button == '!': # create button object for factorial function and configure its properites
                self.button = Button(self.frame_keyboard, text=button, command=self.factorial)
                self.button.config(bg='#a32626', activebackground='#4a1b1b', activeforeground='#b80707')
            else: # create button objects for equal and clear sign and configure their properties
                self.button = Button(self.frame_keyboard, text=button, command=lambda j=button: self.eval(j))
                self.button.config(bg='#e68f17', activebackground='#9c6a24', activeforeground='#ff9808')
            self.button.config(font=font, bd=4) # configure font and border size for all the buttons
            # use grid geometry manager to generate location for the button objects
            self.button.grid(column=i % 5, row=i - (i % 5), sticky='nsew', padx=2, pady=2)

    def factorial(self): # create factorial methods
        # define threading function
        def factorial_exec(argument, counter=1):
            while counter <= argument: # keep multiplying while counter smaller than argument
                lock.acquire() # set lock for the critical section to prevent unpredictable changes
                self.factorial_value *= counter # operation on the critical section
                counter += 1 # increase the value of the counter
                lock.release() # release the lock

        lock = threading.Lock() # create lock object
        try: # ensure the correct value is assigned to the num variable
            num = int(self.value.get())
            part1 = threading.Thread(target=factorial_exec, args=(num // 2,)) # create first thread
            part2 = threading.Thread(target=factorial_exec, args=(num, num // 2 + 1)) # create the second thread
            part1.start() # start first thread
            part2.start() # start the second thread
            part1.join() # join threads
            part2.join()
            self.value.set(self.factorial_value) # sent result of factorial calculation to the display
            self.factorial_value = 1 # set factorial value back to 1
        except:
            self.value.set('ERROR') # show error on the display when input error occurred

    def input(self, value): # create method for button input
        if self.value.get() == '0' and value != '.': # ensure 0 is not overriden when '.' is input
            self.value.set(value)
        else:
            self.display.insert('end', value) # input the value from the keyboard

    def calc_math(self, operation): # crete calc function
        try: # if math function has argument
            # get the value from the variable linked to the display,
            # convert to float and apply function from self.math_op dictionary and sent result to the display
            self.value.set(self.math_op[operation](float(self.value.get())))
        except: # if no argument provided to math function value set display to value received from math function
            if self.value.get() == '0': # clear display before inserting value from the math function
                self.value.set('')
            self.display.insert('end',self.math_op[operation]) # add value of the math function to the display

    def eval(self, symbol): # calculate the value of the screen
        if symbol == 'C':
            self.value.set('0') # set display to 0 if C pressed
        else:
            try: # provide error handling for incorrectly inputed expressions
                self.value.set(eval(self.display.get())) # evaluate value of the expression from the display
            except: # display error messages for incorrectly inputed expressions
                self.value.set('ERROR')


if __name__ == '__main__': # start the main function
    root = Calc() # create Calc object
    root.mainloop() # prevent root object from being garbage collected