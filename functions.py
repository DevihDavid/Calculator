from math import *
import re
from tkinter import *
from tkinter.messagebox import showerror
import datetime




class Mixin:

    def error(self):
        showerror("ERROR", "You typed wrong character.\n Try again!")

    def check_error(self):
        equation = self.write_area.get()

        return re.search('[a-zA-Z,]+', equation) or equation == "" or re.search('[+\-/.]{2,}', equation) \
        or re.search('^[+*/.]', equation) or re.search('[+\-*/.]$', equation) \
        or re.search('[*]{3,}', equation)

    def equal(self, event=None):
        equation = self.write_area.get()
        if self.check_error():
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
        if self.check_error():
            self.error()
            self.write_area.delete(0, END)
        else:
            result = eval(compile(equation, '<string>', 'eval')) ** 2
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(result))
            self.result_area.insert(1.0, equation + "**2" + "=" + str(result) + "\n")

    def squareY(self, event=None):
        equation = self.write_area.get()
        if self.check_error():
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
        if self.check_error():
            self.error()
            self.write_area.delete(0, END)
        else:
            number = eval(compile(self.write_area.get(), '<string>', 'eval'))
            self.result_area.insert(1.0, "√(" + self.write_area.get() + ")=" + str(sqrt(number)) + "\n")
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(number))

    def c_factorial(self):
        equation = self.write_area.get()
        if self.check_error():
            self.error()
            self.write_area.delete(0, END)
        else:
            result = factorial(eval(compile(equation, '<string>', 'eval')))
            self.result_area.insert(1.0, self.write_area.get() + "!=" + str(result) + "\n")
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(result))

    def exponent(self):
        equation = self.write_area.get()
        if self.check_error():
            self.error()
            self.write_area.delete(0, END)
        else:
            result = exp(eval(compile(equation, '<string>', 'eval')))
            self.result_area.insert(1.0, "e**"+ equation + "=" + str(result) + "\n")
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(result))

    def raise_10(self):
        equation = self.write_area.get()
        if self.check_error():
            self.error()
            self.write_area.delete(0, END)
        else:
            result = 10 ** eval(compile(equation, '<string>', 'eval'))
            self.result_area.insert(1.0, "10**" + equation + "=" + str(result) + "\n")
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(result))

    def c_log(self):
        equation = self.write_area.get()
        if self.check_error():
            self.error()
            self.write_area.delete(0, END)
        else:
            result = log10(eval(compile(equation, '<string>', 'eval')))
            self.result_area.insert(1.0, "log(" + equation + ")=" + str(result) + "\n")
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(result))

    def c_ln(self):
        equation = self.write_area.get()
        if self.check_error():
            self.error()
            self.write_area.delete(0, END)
        else:
            result = log((eval(compile(equation, '<string>', 'eval'))), e)
            self.result_area.insert(1.0, "ln(" + equation + ")=" + str(result) + "\n")
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(result))

    def c_sin(self):
        equation = self.write_area.get()
        if self.check_error():
            self.error()
            self.write_area.delete(0, END)
        else:
            result = sin((eval(compile(equation, '<string>', 'eval'))))
            self.result_area.insert(1.0, "sin(" + equation + ")=" + str(result) + "\n")
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(result))

    def c_cos(self):
        equation = self.write_area.get()
        if self.check_error():
            self.error()
            self.write_area.delete(0, END)
        else:
            result = cos((eval(compile(equation, '<string>', 'eval'))))
            self.result_area.insert(1.0, "cos(" + equation + ")=" + str(result) + "\n")
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(result))

    def c_tg(self):
        equation = self.write_area.get()
        if self.check_error():
            self.error()
            self.write_area.delete(0, END)
        else:
            result = tg((eval(compile(equation, '<string>', 'eval'))))
            self.result_area.insert(1.0, "tg(" + equation + ")=" + str(result) + "\n")
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(result))

    def c_ctg(self):
        equation = self.write_area.get()
        if self.check_error():
            self.error()
            self.write_area.delete(0, END)
        else:
            result = ctg((eval(compile(equation, '<string>', 'eval'))))
            self.result_area.insert(1.0, "ctg(" + equation + ")=" + str(result) + "\n")
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(result))

    def c_arcsin(self):
        equation = self.write_area.get()
        if self.check_error() or float(equation) >= -1 or float(equation) <= 1:
            self.error()
            self.write_area.delete(0, END)
        elif float(equation) >= -1 or float(equation) <= 1:
            showerror("ERROR", "You must number beetwen -1 and 1.\n Try again!")
        else:
            result = asin((eval(compile(equation, '<string>', 'eval'))))
            self.result_area.insert(1.0, "arcsin(" + equation + ")=" + str(result) + "\n")
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(result))

    def c_arccos(self):
        equation = self.write_area.get()
        if self.check_error() or float(equation) >= -1 or float(equation) <= 1:
            self.error()
            self.write_area.delete(0, END)
        elif float(equation) >= -1 or float(equation) <= 1:
            showerror("ERROR", "You must number beetwen -1 and 1.\n Try again!")
        else:
            result = acos((eval(compile(equation, '<string>', 'eval'))))
            self.result_area.insert(1.0, "arccos(" + equation + ")=" + str(result) + "\n")
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(result))

    def c_arctg(self):
        equation = self.write_area.get()
        if self.check_error() or float(equation) >= -1 or float(equation) <= 1:
            self.error()
            self.write_area.delete(0, END)
        elif float(equation) >= -1 or float(equation) <= 1:
            showerror("ERROR", "You must number beetwen -1 and 1.\n Try again!")
        else:
            result = atg((eval(compile(equation, '<string>', 'eval'))))
            self.result_area.insert(1.0, "arctg(" + equation + ")=" + str(result) + "\n")
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(result))

    def c_arcctg(self):
        equation = self.write_area.get()
        if self.check_error():
            self.error()
            self.write_area.delete(0, END)
        elif float(equation) >= -1 or float(equation) <= 1:
            showerror("ERROR", "You must number beetwen -1 and 1.\n Try again!")
        else:
            result = acos((eval(compile(equation, '<string>', 'eval'))))
            self.result_area.insert(1.0, "arccos(" + equation + ")=" + str(result) + "\n")
            self.write_area.delete(0, END)
            self.write_area.insert(0, str(result))

    def set_current_date(self):
        months_dict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July",
                       8: "August",
                       9: "September", 10: "October", 11: "November", 12: "December"}

        current_date = datetime.datetime.now()
        current_day = current_date.day
        current_month = current_date.month
        current_year = current_date.year

        self.day_choose.delete(0, END)
        self.day_choose.insert(0, str(current_day))
        self.day2_choose.delete(0, END)
        self.day2_choose.insert(0, str(current_day))

        self.month_choose.delete(0, END)
        self.month_choose.insert(0, months_dict[current_month])
        self.month2_choose.delete(0, END)
        self.month2_choose.insert(0, months_dict[current_month])

        self.year_choose.delete(0, END)
        self.year_choose.insert(0, str(current_year))
        self.year2_choose.delete(0, END)
        self.year2_choose.insert(0, str(current_year))

    def check_date_correctness(self):
        init_day = self.day_choose.get()
        final_day = self.day2_choose.get()
        init_month = self.month_choose.get()
        final_month = self.month2_choose.get()
        init_year = self.year_choose.get()
        final_year = self.year2_choose.get()

        even_months = ["April", "June", "September", "November"]

        if init_month in even_months and int(init_day) > 30 or final_month in even_months and int(final_day) > 30:
            self.result_area2.delete(0, END)
            showerror("ERROR!", "This month has got only 30 days!")
        elif init_month == "February" and int(init_year) % 4 != 0 and int(init_day) > 28 or \
                final_month == "February" and int(final_year) % 4 != 0 and int(final_day) > 28:
            self.result_area2.delete(0, END)
            showerror("ERROR!", "This is not the leap year.\nIt has only 28 days.")
        elif int(init_year) % 4 == 0 and int(init_day) > 29 or int(final_year) % 4 == 0 and int(final_day) > 29:
            self.result_area2.delete(0, END)
            showerror("ERROR!", "This is the leap year.\nIt has only 29 days.")
        else:
            self.days_diff()

    def days_diff(self):
        months2 = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8,
                   "September": 9, "October": 10, "November": 11, "December": 12}
        date1 = datetime.date(int(self.year_choose.get()), months2[self.month_choose.get()], int(self.day_choose.get()))
        date2 = datetime.date(int(self.year2_choose.get()), months2[self.month2_choose.get()],
                              int(self.day2_choose.get()))

        diff = date2 - date1

        if diff.days < 0:
            showerror("ERROR!", "Days difference can't be negative.\nTry again!")
            self.result_area2.delete(0, END)
        elif diff.days == 0:
            self.result_area2.delete(0, END)
            self.result_area2.insert(0, "These dates are the same.")
        else:
            self.result_area2.delete(0, END)
            self.result_area2.insert(0, str(diff.days) + " days/s between them.")

    def clean_date(self):
        self.result_area2.delete(0, END)

    def clear_buttons(self):
        try:
            button_to_clear = [self.button0, self.button1, self.button2, self.button3, self.button4, self.button5,
                               self.button6, self.button7, self.button8, self.button9, self.buttonDot,
                               self.buttonEqual, self.buttonLeftPar, self.buttonRightPar, self.buttonSqrt,
                               self.buttonSquare,
                               self.buttonSquareY, self.buttonPlus, self.buttonMinus, self.buttonDiv,
                               self.buttonMulti, self.buttonC, self.buttonCE, self.buttonBackspace,
                               self.write_area, self.result_area, self.result_area_text, self.scrollbarX,
                               self.scrollbarY, self.type_science, self.buttonN, self.buttonE, self.button10,
                               self.buttonlogx, self.buttonln, self.button_put_e, self.buttonP, self.buttonSin,
                               self.buttonCos, self.buttonTg, self.buttonCtg, self.buttonArcsin,
                               self.buttonArccos, self.buttonArctg, self.buttonArcctg]

            for name in button_to_clear:
                name.grid_remove()
        except AttributeError:
            try:
                things_to_remove = [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6,
                                    self.button7, self.button8, self.button9, self.button0, self.buttonDot,
                                    self.buttonEqual, self.buttonPlus, self.buttonMinus, self.buttonMulti,
                                    self.buttonDiv, self.buttonSquare, self.buttonSquareY, self.buttonRightPar,
                                    self.buttonLeftPar, self.buttonC, self.buttonCE, self.buttonBackspace,
                                    self.buttonSqrt, self.write_area, self.result_area, self.result_area_text,
                                    self.type, self.scrollbarX, self.scrollbarY]

                for name in things_to_remove:
                    name.grid_remove()
            except AttributeError:
                button_to_clear = [self.initial, self.day, self.month, self.year, self.sep1, self.sep2, self.sep3,
                                   self.day_choose, self.day2_choose, self.month_choose, self.month2_choose,
                                   self.year_choose, self.year2_choose, self.final, self.result_text, self.result_area2,
                                   self.info, self.buttonClean, self.buttonGo]

                for name in button_to_clear:
                    name.grid_remove()







