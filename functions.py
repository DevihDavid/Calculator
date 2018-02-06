from math import *
import re
from tkinter import *
from tkinter.messagebox import showerror


class Mixin:


    def error(self):
        showerror("ERROR", "You typed wrong character.\n Try again!")

    def equal(self, event=None):
        equation = self.write_area.get()
        if re.search('[a-zA-Z,]+', equation) or equation == "" or re.search('[+\-/.]{2,}', equation) \
                or re.search('^[+\-*/.]', equation) or re.search('[+\-*/.]$', equation) \
                or re.search('[*]{3,}', equation):
            self.error()
            self.write_area.delete(0, END)
        else:
            self.result_area.insert(1.0, self.write_area.get() + "=" + str(eval(compile(equation, '<string>', 'eval'))) + "\n")
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(eval(compile(equation, '<string>', 'eval'))))

    def clear_last(self, event=None):
        get_length = len(self.write_area.get())
        self.write_area.delete(get_length - 1)


    def clear(self, event=None):
        self.write_area.delete(0, END)
        self.result_area.delete(1.0, END)

    def square(self):
        equation = self.write_area.get()
        if re.search('[a-zA-Z,]+', equation) or equation == "" or re.search('[+\-/.]{2,}', equation) \
                or re.search('^[+\-*/.]', equation) or re.search('[+\-*/.]$', equation) \
                or re.search('[*]{3,}', equation):
            self.error()
            self.write_area.delete(0, END)
        else:
            result = eval(compile(equation, '<string>', 'eval')) ** 2
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(result))
            self.result_area.insert(1.0, equation + "**2" + "=" + str(result) + "\n")

    def squareY(self, event=None):
        equation = self.write_area.get()
        if re.search('[a-zA-Z,]+', equation) or equation == "" or re.search('[+\-/.]{2,}', equation) \
                or re.search('^[+\-*/.]', equation) or re.search('[+\-*/.]$', equation) \
                or re.search('[*]{3,}', equation):
            self.error()
            self.write_area.delete(0, END)
        else:
            check = self.write_area.get()
            check2 = re.search(r'\d+', check).span()
            if len(check) == check2[1]:
                self.write_area.insert(END, "**")
            elif self.write_area.get()[0] == "(":
                self.write_area.insert(END, "**(")
            else:
                self.write_area.insert(0, "(")
                self.write_area.insert(END, ")**(")

    def sqrt(self):
        equation = self.write_area.get()
        if re.search('[a-zA-Z,]+', equation) or equation == "" or re.search('[+\-/.]{2,}', equation) \
                or re.search('^[+\-*/.]', equation) or re.search('[+\-*/.]$', equation) \
                or re.search('[*]{3,}', equation):
            self.error()
            self.write_area.delete(0, END)
        else:
            number = eval(compile(self.write_area.get(), '<string>', 'eval'))
            self.result_area.insert(1.0, "√(" + self.write_area.get() + ")=" + str(sqrt(number)) + "\n")
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(number))

    def c_factorial(self):
        equation = self.write_area.get()
        if re.search('[a-zA-Z,]+', equation) or equation == "" or re.search('[+\-/.]{2,}', equation) \
                or re.search('^[+\-*/.]', equation) or re.search('[+\-*/.]$', equation) \
                or re.search('[*]{3,}', equation):
            self.error()
            self.write_area.delete(0, END)
        else:
            result = factorial(eval(compile(equation, '<string>', 'eval')))
            self.result_area.insert(1.0, self.write_area.get() + "!=" + str(result) + "\n")
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(result))

    def exponent(self):
        equation = self.write_area.get()
        if re.search('[a-zA-Z,]+', equation) or equation == "" or re.search('[+\-/.]{2,}', equation) \
                or re.search('^[+\-*/.]', equation) or re.search('[+\-*/.]$', equation) \
                or re.search('[*]{3,}', equation):
            self.error()
            self.write_area.delete(0, END)
        else:
            result = exp(eval(compile(equation, '<string>', 'eval')))
            self.result_area.insert(1.0, "e**"+ equation + "=" + str(result) + "\n")
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(result))

    def raise_10(self):
        equation = self.write_area.get()
        if re.search('[a-zA-Z,]+', equation) or equation == "" or re.search('[+\-/.]{2,}', equation) \
                or re.search('^[+\-*/.]', equation) or re.search('[+\-*/.]$', equation) \
                or re.search('[*]{3,}', equation):
            self.error()
            self.write_area.delete(0, END)
        else:
            result = 10 ** eval(compile(equation, '<string>', 'eval'))
            self.result_area.insert(1.0, "10**" + equation + "=" + str(result) + "\n")
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(result))

    def c_log(self):
        equation = self.write_area.get()
        if re.search('[a-zA-Z,]+', equation) or equation == "" or re.search('[+\-/.]{2,}', equation) \
                or re.search('^[+\-*/.]', equation) or re.search('[+\-*/.]$', equation) \
                or re.search('[*]{3,}', equation):
            self.error()
            self.write_area.delete(0, END)
        else:
            result = log10(eval(compile(equation, '<string>', 'eval')))
            self.result_area.insert(1.0, "log(" + equation + ")=" + str(result) + "\n")
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(result))

    def c_ln(self):
        equation = self.write_area.get()
        if re.search('[a-zA-Z,]+', equation) or equation == "" or re.search('[+\-/.]{2,}', equation) \
                or re.search('^[+\-*/.]', equation) or re.search('[+\-*/.]$', equation) \
                or re.search('[*]{3,}', equation):
            self.error()
            self.write_area.delete(0, END)
        else:
            result = log((eval(compile(equation, '<string>', 'eval'))), e)
            self.result_area.insert(1.0, "ln(" + equation + ")=" + str(result) + "\n")
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(result))

    def c_sin(self):
        equation = self.write_area.get()
        if re.search('[a-zA-Z,]+', equation) or equation == "" or re.search('[+\-/.]{2,}', equation) \
                or re.search('^[+\-*/.]', equation) or re.search('[+\-*/.]$', equation) \
                or re.search('[*]{3,}', equation):
            self.error()
            self.write_area.delete(0, END)
        else:
            result = sin((eval(compile(equation, '<string>', 'eval'))))
            self.result_area.insert(1.0, "sin(" + equation + ")=" + str(result) + "\n")
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(result))

    def c_cos(self):
        equation = self.write_area.get()
        if re.search('[a-zA-Z,]+', equation) or equation == "" or re.search('[+\-/.]{2,}', equation) \
                or re.search('^[+\-*/.]', equation) or re.search('[+\-*/.]$', equation) \
                or re.search('[*]{3,}', equation):
            self.error()
            self.write_area.delete(0, END)
        else:
            result = cos((eval(compile(equation, '<string>', 'eval'))))
            self.result_area.insert(1.0, "cos(" + equation + ")=" + str(result) + "\n")
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(result))

    def c_tg(self):
        equation = self.write_area.get()
        if re.search('[a-zA-Z,]+', equation) or equation == "" or re.search('[+\-/.]{2,}', equation) \
                or re.search('^[+\-*/.]', equation) or re.search('[+\-*/.]$', equation) \
                or re.search('[*]{3,}', equation):
            self.error()
            self.write_area.delete(0, END)
        else:
            result = tg((eval(compile(equation, '<string>', 'eval'))))
            self.result_area.insert(1.0, "tg(" + equation + ")=" + str(result) + "\n")
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(result))

    def c_ctg(self):
        equation = self.write_area.get()
        if re.search('[a-zA-Z,]+', equation) or equation == "" or re.search('[+\-/.]{2,}', equation) \
                or re.search('^[+\-*/.]', equation) or re.search('[+\-*/.]$', equation) \
                or re.search('[*]{3,}', equation):
            self.error()
            self.write_area.delete(0, END)
        else:
            result = ctg((eval(compile(equation, '<string>', 'eval'))))
            self.result_area.insert(1.0, "ctg(" + equation + ")=" + str(result) + "\n")
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(result))

    def c_arcsin(self):
        equation = self.write_area.get()
        if re.search('[a-zA-Z,]+', equation) or equation == "" or re.search('[+\-/.]{2,}', equation) \
                or re.search('^[+\-*/.]', equation) or re.search('[+\-*/.]$', equation) \
                or re.search('[*]{3,}', equation) or float(equation) >= -1 or float(equation) <= 1:
            self.error()
            self.write_area.delete(0, END)
        else:
            result = asin((eval(compile(equation, '<string>', 'eval'))))
            self.result_area.insert(1.0, "arcsin(" + equation + ")=" + str(result) + "\n")
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(result))

    def c_arccos(self):
        equation = self.write_area.get()
        if re.search('[a-zA-Z,]+', equation) or equation == "" or re.search('[+\-/.]{2,}', equation) \
                or re.search('^[+\-*/.]', equation) or re.search('[+\-*/.]$', equation) \
                or re.search('[*]{3,}', equation) or float(equation) >= -1 or float(equation) <= 1:
            self.error()
            self.write_area.delete(0, END)
        else:
            result = acos((eval(compile(equation, '<string>', 'eval'))))
            self.result_area.insert(1.0, "arccos(" + equation + ")=" + str(result) + "\n")
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(result))

    def c_arctg(self):
        equation = self.write_area.get()
        if re.search('[a-zA-Z,]+', equation) or equation == "" or re.search('[+\-/.]{2,}', equation) \
                or re.search('^[+\-*/.]', equation) or re.search('[+\-*/.]$', equation) \
                or re.search('[*]{3,}', equation) or float(equation) >= -1 or float(equation) <= 1:
            self.error()
            self.write_area.delete(0, END)
        else:
            result = atg((eval(compile(equation, '<string>', 'eval'))))
            self.result_area.insert(1.0, "arctg(" + equation + ")=" + str(result) + "\n")
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(result))

    def c_arcctg(self):
        equation = self.write_area.get()
        if re.search('[a-zA-Z,]+', equation) or equation == "" or re.search('[+\-/.]{2,}', equation) \
                or re.search('^[+\-*/.]', equation) or re.search('[+\-*/.]$', equation) \
                or re.search('[*]{3,}', equation) or float(equation) >= -1 or float(equation) <= 1:
            self.error()
            self.write_area.delete(0, END)
        else:
            result = acos((eval(compile(equation, '<string>', 'eval'))))
            self.result_area.insert(1.0, "arccos(" + equation + ")=" + str(result) + "\n")
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(result))


