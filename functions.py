from math import *
import re
from tkinter import *


class Mixin:


    def equal(self, event=None):
        equation = self.write_area.get()
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
        result = eval(compile(equation, '<string>', 'eval')) ** 2
        self.write_area.delete(0, END)
        self.write_area.insert(0, str(result))
        self.result_area.insert(1.0, equation + "**2" + "=" + str(result) + "\n")

    def squareY(self, event=None):
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
        number = eval(compile(self.write_area.get(), '<string>', 'eval'))
        self.result_area.insert(1.0, "√(" + self.write_area.get() + ")=" + str(sqrt(number)) + "\n")
        self.write_area.delete(0, END)
        self.write_area.insert(0, str(number))
