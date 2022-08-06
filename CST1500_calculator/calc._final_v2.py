from tkinter import *
import math
import threading





num = 50
factorial_value=1
lock = threading.Lock()

part1 = threading.Thread(target=factorial, args=(num//2,))

part2 = threading.Thread(target=factorial, args=(num, num//2+1))

part1.start()
part2.start()
part1.join()
part2.join()
print(factorial_value)


class Calc(Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.label_text = 'Choose one'

        self.frame_display = Frame(self)
        self.frame_display.pack()
        self.value = StringVar()
        self.value.set('0')
        self.display = Entry(self.frame_display, font=('arial', 32, 'bold'), textvariable=self.value, fg='lime', bg='grey', bd=30, width=18, justify=RIGHT)
        self.display.pack()

        self.frame_keyboard = Frame(self)
        self.frame_keyboard.pack()

        self.buttons = '7,8,9,+,SIN,4,5,6,-,COS,1,2,3,*,TAN,0,.,C,/,!,(,),E,**,='

        font = ('arial', 36, 'bold')
        self.eval_op = '+,-,*,**,.,/,(,)'
        self.math_op = {'SIN':math.sin, 'COS':math.cos,'TAN':math.tan,'!': 'factorial', 'E':math.e}

        for i, button in enumerate(self.buttons.split(',')):
            if button.isdigit() or button in self.eval_op:
                self.button = Button(self.frame_keyboard, text=button, font=font, bd=4, \
                                 command=lambda j=button: self.input(j))

            elif button in self.math_op:
                self.button = Button(self.frame_keyboard, text=button, font=font, bd=4, \
                                     command=lambda j=button: self.calc_math(j))
            else:
                self.button = Button(self.frame_keyboard, text=button, font=font, bd=4, \
                                     command=lambda j=button: self.eval(j))
            self.button.grid(column=i % 5, row=i - (i % 5), sticky='nsew', padx=2, pady=2)

    def factorial(argument, counter=1):
        global factorial_value
        while counter <= argument:
            incr = counter
            lock.acquire()
            factorial_value = factorial_value * counter
            counter += 1
            lock.release()

    def input(self, value):
        if self.value.get() == '0':
            self.value.set(value)
        else:
            self.display.insert('end', value)

    def calc_math(self, operation):
        if operation == '!':
            self.value.set(f'{self.kutas()}')
        else:
            try:
                self.value.set(self.math_op[operation](float(self.value.get())))
            except:
                self.display.insert('end',self.math_op[operation])

    def eval(self, symbol):
        if symbol == 'C':
            self.value.set('0')
        else:
            self.value.set(eval(self.display.get()))


if __name__ == '__main__':
    root = Calc()
    root.mainloop()
