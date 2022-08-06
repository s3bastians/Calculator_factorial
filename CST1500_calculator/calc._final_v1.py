from tkinter import *
import math

class Calc(Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.label_text = 'Choose one'

        self.frame_display = Frame(self)
        self.frame_display.pack()
        self.value = StringVar()
        self.display = Entry(self.frame_display, font=('arial', 32, 'bold'), textvariable=self.value, fg='lime', bg='grey', bd=30, width=18, justify=RIGHT)
        self.display.pack()

        self.frame_keyboard = Frame(self)
        self.frame_keyboard.pack()

        self.buttons_num = '789456123'

        i = 0
        font = ('arial', 36, 'bold')
        for row in range(3):
            for col in range(3):
                self.button = Button(self.frame_keyboard, text=self.buttons_num[i], font= font, \
                                     bd=4, command=lambda j=self.buttons_num[i]: self.set_display(j))
                self.button.grid(column=col, row=row,  sticky='nsew', padx=2, pady=2)
                i += 1

        self.buttons_math = ['+', '-', '*', '/', '.']

        for i, op in enumerate(self.buttons_math):
            self.button = Button(self.frame_keyboard, text=op, \
                                 font=font, bd=4, command=lambda j=op: self.set_display(j))
            self.button.grid(column=3, row=i, sticky='nsew', padx=2, pady=2)

        s = Button(self.frame_keyboard, text='=', bd=4, font=font, command=lambda: self.value.set(eval(self.value.get())))
        s.grid(row=4, column=0, columnspan=3, sticky='nsew', padx=2, pady=2)

        self.buttons_bottom = [0, '(', ')']

        for i, op in enumerate(self.buttons_bottom):
            self.button = Button(self.frame_keyboard, text=op,\
                                 font=font, bd=4, command=lambda j=op: self.set_display(j))
            self.button.grid(column=i,row=3, sticky='nsew', padx=2, pady=2)

        self.functions_buttons = ['SIN', 'COS', 'E', 'PI', 'C']
        self.functions = [math.sin, math.cos, math.e, math.pi, 0]

        for i, op in enumerate(self.functions_buttons):
            if i < 4:
                self.button = Button(self.frame_keyboard, text=op,\
                                 font=font, bd=4, command=lambda j=self.functions[i]: self.calc_math(j))
            else:
                self.button = Button(self.frame_keyboard, text=op, \
                                     font=font, bd=4, command=lambda: self.value.set(0))
            self.button.grid(column=4, row=i, sticky='nsew', padx=2, pady=2)

    def calc_math(self, operation):
        if operation in [math.sin, math.cos]:
            self.value.set(operation(float(self.value.get())))
        elif operation == math.pi:
            self.set_display(math.pi)
        else:
           self.set_display(math.e)


    def set_display(self, value):
        self.display.insert('end',str(value))


    def sey_hello(self):
        self.label.configure(text='Hello World!', bd=30,)

if __name__ == '__main__':
    root = Calc()
    root.mainloop()
