from tkinter import *
import math
import tkinter.messagebox

root = Tk()
root.title('Scientific Calculator')
root.configure(background='powder blue')
root.resizable(width=False, height=False)
root.geometry('480x568+0+0')

calc = Frame(root)
calc.pack()


class Calc():
    def __init__(self):
        self.total = 0
        self.current = ''
        self.input_value = True
        self.check_sum = False
        self.op = ''
        self.result = False

    def number_enter(self, num):
        self.result = False
        first_number = txt_display.get()
        second_number = str(num)
        if self.input_value:
            self.current = second_number
            self.input_value = False
        else:
            if second_number == '.':
                if second_number in first_number:
                    return
            self.current = first_number + second_number
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txt_display.get())

    def display(self, value):
        txt_display.delete(0, END)
        txt_display.insert(0, value)

    def valid_function(self):
        if self.op == 'add':
            self.total += self.current
        if self.op == 'sub':
            self.total -= self.current
        if self.op == 'multi':
            self.total *= self.current
        if self.op == 'divide':
            self.total /= self.current
        if self.op == 'mod':
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operations(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def clear_entry(self):
        self.result = False
        self.current = '0'
        self.display(0)
        self.input_value = True

    def all_clear_entry(self):
        self.clear_entry()
        self.total = 0

    def math_pm(self):
        self.result = False
        self.current = -(float(txt_display.get()))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txt_display.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txt_display.get())))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txt_display.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txt_display.get())))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(txt_display.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txt_display.get())))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txt_display.get())))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(txt_display.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(txt_display.get()))
        self.display(self.current)

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(float(txt_display.get()))
        self.display(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(float(txt_display.get()))
        self.display(self.current)

    def expm1(self):
        self.result = False
        self.current = math.expm1(float(txt_display.get()))
        self.display(self.current)

    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(txt_display.get()))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txt_display.get()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(txt_display.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(txt_display.get()))
        self.display(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(float(txt_display.get()))
        self.display(self.current)


added_value = Calc()

txt_display = Entry(calc, font=('arial', 20, 'bold'), bg='powder blue', bd=30, width=28, justify=RIGHT)
txt_display.grid(row=0, column=0, columnspan=4, pady=1)
txt_display.insert(0, '0')

number_pad = '789456123'
i = 0
btn = []
for j in range(2, 5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font=('arial', 20, 'bold'), bd=4, text=number_pad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]['command'] = lambda x=number_pad[i]: added_value.number_enter(x)
        i += 1

# ========================================STANDARD Calc================================================================

btn_clear = Button(calc, text=chr(67), width=6, height=2, font=('arial', 20, 'bold'),
                   bd=4, bg='powder blue', command=added_value.clear_entry).grid(row=1, column=0, pady=1)
btn_all_clear = Button(calc, text=chr(67) + chr(69), width=6, height=2, font=('arial', 20, 'bold'),
                       bd=4, bg='powder blue', command=added_value.all_clear_entry).grid(row=1, column=1, pady=1)
btn_sq = Button(calc, text='√', width=6, height=2, font=('arial', 20, 'bold')
                , bd=4, bg='powder blue', command=added_value.squared).grid(row=1, column=2, pady=1)
btn_add = Button(calc, text='+', width=6, height=2, font=('arial', 20, 'bold')
                 , bd=4, bg='powder blue', command=lambda: added_value.operations('add')).grid(row=1, column=3, pady=1)
btn_sub = Button(calc, text='-', width=6, height=2, font=('arial', 20, 'bold')
                 , bd=4, bg='powder blue', command=lambda: added_value.operations('sub')).grid(row=2, column=3, pady=1)
btn_multi = Button(calc, text='*', width=6, height=2, font=('arial', 20, 'bold')
                   , bd=4, bg='powder blue', command=lambda: added_value.operations('multi')).grid(row=3, column=3,
                                                                                                   pady=1)
btn_div = Button(calc, text=chr(247), width=6, height=2, font=('arial', 20, 'bold')
                 , bd=4, bg='powder blue', command=lambda: added_value.operations('divide')).grid(row=4, column=3,
                                                                                                  pady=1)
btn_zero = Button(calc, text='0', width=6, height=2, font=('arial', 20, 'bold')
                  , bd=4, bg='powder blue', command=lambda: added_value.number_enter(0)).grid(row=5, column=0, pady=1)
btn_dot = Button(calc, text='.', width=6, height=2, font=('arial', 20, 'bold')
                 , bd=4, bg='powder blue', command=lambda: added_value.number_enter('.')).grid(row=5, column=1, pady=1)
btn_pm = Button(calc, text=chr(177), width=6, height=2, font=('arial', 20, 'bold')
                , bd=4, bg='powder blue', command=added_value.math_pm).grid(row=5, column=2, pady=1)
btn_equals = Button(calc, text='=', width=6, height=2, font=('arial', 20, 'bold')
                    , bd=4, bg='powder blue', command=added_value.sum_of_total).grid(row=5, column=3, pady=1)

# =============================SCIENTIFIC Calc=====================================================================

btn_pi = Button(calc, text='π', width=6, height=2, font=('arial', 20, 'bold'),
                bd=4, bg='powder blue', command=added_value.pi).grid(row=1, column=4, pady=1)
btn_cos = Button(calc, text='cos', width=6, height=2, font=('arial', 20, 'bold'),
                 bd=4, bg='powder blue', command=added_value.cos()).grid(row=1, column=5, pady=1)
btn_tan = Button(calc, text='tan', width=6, height=2, font=('arial', 20, 'bold')
                 , bd=4, bg='powder blue', command=added_value.tan).grid(row=1, column=6, pady=1)
btn_sin = Button(calc, text='sin', width=6, height=2, font=('arial', 20, 'bold')
                 , bd=4, bg='powder blue', command=added_value.sin).grid(row=1, column=7, pady=1)
btn_2pi = Button(calc, text='2π', width=6, height=2, font=('arial', 20, 'bold')
                 , bd=4, bg='powder blue', command=added_value.tau).grid(row=2, column=4, pady=1)
btn_cosh = Button(calc, text='cosh', width=6, height=2, font=('arial', 20, 'bold')
                  , bd=4, bg='powder blue', command=added_value.cosh).grid(row=2, column=5, pady=1)
btn_tan_h = Button(calc, text='tanh', width=6, height=2, font=('arial', 20, 'bold')
                   , bd=4, bg='powder blue', command=added_value.tanh).grid(row=2, column=6, pady=1)
btn_sin_h = Button(calc, text='sinh', width=6, height=2, font=('arial', 20, 'bold')
                   , bd=4, bg='powder blue', command=added_value.sinh).grid(row=2, column=7, pady=1)
btn_log = Button(calc, text='log', width=6, height=2, font=('arial', 20, 'bold')
                 , bd=4, bg='powder blue', command=added_value.log).grid(row=3, column=4, pady=1)
btn_exp = Button(calc, text='Exp', width=6, height=2, font=('arial', 20, 'bold')
                 , bd=4, bg='powder blue', command=added_value.exp).grid(row=3, column=5, pady=1)
btn_mod = Button(calc, text='Mod', width=6, height=2, font=('arial', 20, 'bold')
                 , bd=4, bg='powder blue', command=added_value).grid(row=3, column=6, pady=1)
btn_e = Button(calc, text='e', width=6, height=2, font=('arial', 20, 'bold')
               , bd=4, bg='powder blue', command=added_value.e).grid(row=3, column=7, pady=1)
btn_log2 = Button(calc, text='log2', width=6, height=2, font=('arial', 20, 'bold')
                  , bd=4, bg='powder blue', command=added_value.log2).grid(row=4, column=4, pady=1)
btn_deg = Button(calc, text='deg', width=6, height=2, font=('arial', 20, 'bold')
                 , bd=4, bg='powder blue', command=added_value.degrees).grid(row=4, column=5, pady=1)
btn_acosh = Button(calc, text='acosh', width=6, height=2, font=('arial', 20, 'bold')
                   , bd=4, bg='powder blue', command=added_value.acosh).grid(row=4, column=6, pady=1)
btn_asinh = Button(calc, text='asinh', width=6, height=2, font=('arial', 20, 'bold')
                   , bd=4, bg='powder blue', command=added_value.asinh).grid(row=4, column=7, pady=1)
btn_log10 = Button(calc, text='log10', width=6, height=2, font=('arial', 20, 'bold')
                   , bd=4, bg='powder blue', command=added_value.log10).grid(row=5, column=4, pady=1)
btn_log1p = Button(calc, text='log1p', width=6, height=2, font=('arial', 20, 'bold')
                   , bd=4, bg='powder blue', command=added_value.log1p).grid(row=5, column=5, pady=1)
btn_expm1 = Button(calc, text='expm1', width=6, height=2, font=('arial', 20, 'bold')
                   , bd=4, bg='powder blue', command=added_value.expm1).grid(row=5, column=6, pady=1)
btn_lgamma = Button(calc, text='lgamma', width=6, height=2, font=('arial', 20, 'bold')
                    , bd=4, bg='powder blue', command=added_value.lgamma).grid(row=5, column=7, pady=1)

lbl_display = Label(calc, text='Scientific Calculator', font=('arial', 30, 'bold'), justify=CENTER)
lbl_display.grid(row=0, column=4, columnspan=4)


# ============================MENU and Function====================================================================


def i_exit():
    i_exit = tkinter.messagebox.askyesno('Scientific Calculator', 'Confirm if you want to exit')
    if i_exit > 0:
        root.destroy()
        return


def scientific():
    root.resizable(width=False, height=False)
    root.geometry('1000x540+0+0')


def standard():
    root.resizable(width=False, height=False)
    root.geometry('500x540+0+0')


menu_bar = Menu(calc)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Standard', command=standard)
file_menu.add_command(label='Scientific', command=scientific)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=i_exit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Cut')
edit_menu.add_command(label='Copy')
edit_menu.add_separator()
edit_menu.add_command(label='Paste')

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='View Help')

root.config(menu=menu_bar)
root.mainloop()
