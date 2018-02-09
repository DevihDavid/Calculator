from tkinter import *
import functions
from math import e, pi
import datetime
from tkinter.messagebox import showerror
import te
import normal_calc


class Calculator(functions.Mixin):

    def __init__(self, master):
        self.master = master

        top_menu = Menu(master)
        master.config(menu=top_menu)

        calc_type = Menu(top_menu)
        top_menu.add_cascade(label="Calculator", menu=calc_type)
        calc_type.add_command(label="Simple", command=self.test)
        calc_type.add_command(label="Scientific", command=self.test)
        calc_type.add_command(label="Date calculation", command=self.test)

        converter = Menu(top_menu)
        top_menu.add_cascade(label="Converter", menu=converter)
        converter.add_command(label="Currency")
        converter.add_separator()
        converter.add_command(label="Volume")
        converter.add_command(label="Length")
        converter.add_command(label="Weight and mass")
        converter.add_command(label="Temperature")
        converter.add_command(label="Energy")
        converter.add_command(label="Area")
        converter.add_command(label="Speed")
        converter.add_command(label="Time")
        converter.add_command(label="Power")
        converter.add_command(label="Pressure")
        converter.add_command(label="Angle")
        converter.add_command(label="Data")

        self.write_area = Entry(master, justify=RIGHT)
        self.write_area.grid(row=0, columnspan=6, sticky=W + E, ipady=6, pady=6)

        self.scrollbarY = Scrollbar(master, orient=VERTICAL, command=self.result_area_yview)
        self.scrollbarY.grid(row=1, rowspan=4, column=7, sticky=N + S)
        self.scrollbarX = Scrollbar(master, orient=HORIZONTAL, command=self.result_area_xview)
        self.scrollbarX.grid(row=5, column=6, sticky=W + E)

        self.result_area = Text(master, width=40, height=10, wrap=NONE)
        self.result_area.grid(row=1, rowspan=4, column=6)
        self.result_area['yscrollcommand'] = self.scrollbarY.set
        self.result_area['xscrollcommand'] = self.scrollbarX.set

        self.result_area_text = Label(master, text="The result is:")
        self.result_area_text.grid(row=0, column=6, sticky=W + E)

        self.type = Label(master, text="Simple version")
        self.type.grid(row=5, column=0, columnspan=2)

        self.button0 = self.create_and_place_button_input("0", 4, 1)
        self.button1 = self.create_and_place_button_input("1", 3, 0)
        self.button2 = self.create_and_place_button_input("2", 3, 1)
        self.button3 = self.create_and_place_button_input("3", 3, 2)
        self.button4 = self.create_and_place_button_input("4", 2, 0)
        self.button5 = self.create_and_place_button_input("5", 2, 1)
        self.button6 = self.create_and_place_button_input("6", 2, 2)
        self.button7 = self.create_and_place_button_input("7", 1, 0)
        self.button8 = self.create_and_place_button_input("8", 1, 1)
        self.button9 = self.create_and_place_button_input("9", 1, 2)
        self.buttonPlus = self.create_and_place_button_input("+", 1, 3)
        self.buttonMinus = self.create_and_place_button_input("-", 2, 3)
        self.buttonMulti = self.create_and_place_button_input("*", 3, 3)
        self.buttonDot = self.create_and_place_button_input(".", 4, 0)
        self.buttonDiv = self.create_and_place_button_input("/", 4, 3)
        self.buttonLeftPar = self.create_and_place_button_input("(", 4, 4)
        self.buttonRightPar = self.create_and_place_button_input(")", 4, 5)

        self.buttonSquare = self.create_and_place_button_action("x²", 1, 4, self.square)
        self.buttonC = self.create_and_place_button_action("C", 2, 5, lambda: self.write_area.delete(0, END))
        self.buttonSqrt = self.create_and_place_button_action("√", 2, 4, self.sqrt)
        self.buttonBackspace = self.create_and_place_button_action("←", 1, 5, self.clear_last)
        self.buttonSquareY = self.create_and_place_button_action("xʸ", 3, 4, self.squareY)
        self.buttonCE = self.create_and_place_button_action("CE", 3, 5, self.clear)
        self.buttonEqual = self.create_and_place_button_action("=", 4, 2, self.equal)

        self.bind_buttons()

    def create_and_place_button_input(self, value, row, column):
        button = Button(text=value, height=2, width=8, command=lambda: self.write_area.insert(END, value))
        button.grid(row=row, column=column)
        return button

    def create_and_place_button_action(self, text, row, column, action):
        button = Button(text=text, height=2, width=8, command=action)
        button.grid(row=row, column=column)
        return button

    def make_lambda_input(self, name, button):
        return lambda event=None: self.change_input_key(name, button)

    def bind_buttons(self):
        button_input = {"0": self.button0, "1": self.button1, "2": self.button2, "3": self.button3, "4": self.button4,
                        "5": self.button5, "6": self.button6, "7": self.button7, "8": self.button8, "9": self.button9,
                        ".": self.buttonDot, "+": self.buttonPlus, "-": self.buttonMinus, "*": self.buttonMulti,
                        "/": self.buttonDiv, "(": self.buttonLeftPar, ")": self.buttonRightPar}

        for name, action in button_input.items():
            self.master.bind(name, self.make_lambda_input(name, action))

        self.master.bind('<BackSpace>', lambda event=None: self.change_action_key(self.clear_last(),
                                                                               self.buttonBackspace))
        self.master.bind('<Delete>', lambda event=None: self.change_action_key(self.write_area.delete(0, END),
                                                                               self.buttonC))
        self.master.bind('<Return>', lambda event=None: self.change_action_key(self.equal(), self.buttonEqual))
        self.master.bind('=', lambda event=None: self.change_action_key(self.equal(), self.buttonEqual))
        self.master.bind('^', lambda event=None: self.change_action_key(self.square(), self.buttonSquare))
        self.master.bind(',', lambda event=None: self.change_input_key(".", self.buttonDot))

    def change_input_key(self, value, button):
        self.write_area.insert(END, value)
        button.config(relief=SUNKEN)
        button.after(120, lambda: button.config(relief=RAISED))

    def change_action_key(self, action, button):
        action
        button.config(relief=SUNKEN)
        button.after(120, lambda: button.config(relief=RAISED))

    def result_area_yview(self, *L):
        op, howMany = L[0], L[1]

        if op == 'scroll':
            units = L[2]
            self.result_area.yview_scroll(howMany, units)
        elif op == 'moveto':
            self.result_area.yview_moveto(howMany)

    def result_area_xview(self, *L):
        op, howMany = L[0], L[1]

        if op == 'scroll':
            units = L[2]
            self.result_area.xview_scroll(howMany, units)
        elif op == 'moveto':
            self.result_area.xview_moveto(howMany)


    def scientific_calc(self):
        buttons_to_clear = []
        try:
            buttons_to_remove = [self.buttonBackspace, self.buttonC, self.buttonCE, self.type, self.result_area_text]

            for name in buttons_to_remove:
                name.grid_remove()

            def create_and_place_button_sc(value, row, column, command):
                button = Button(text=value, height=2, width=8, command=command)
                button.grid(row=row, column=column)
                return button

            self.buttonN = create_and_place_button_sc("n!", 1, 5, self.c_factorial)
            self.buttonE = create_and_place_button_sc("eˣ", 2, 5, self.exponent)
            self.button10 = create_and_place_button_sc("10ˣ", 3, 5, self.raise_10)
            self.buttonlogx = create_and_place_button_sc("logx", 1, 6, self.c_log)
            self.buttonln = create_and_place_button_sc("ln", 2, 6, self.c_ln)
            self.button_put_e = create_and_place_button_sc("e", 3, 6, lambda: self.write_area.insert(END, str(e)))
            self.buttonP = create_and_place_button_sc("Π", 4, 6, lambda: self.write_area.insert(END, str(pi)))
            self.buttonSin = create_and_place_button_sc("sin", 1, 7, self.c_sin)
            self.buttonCos = create_and_place_button_sc("cos", 2, 7, self.c_cos)
            self.buttonTg = create_and_place_button_sc("tg", 3, 7, self.c_tg)
            self.buttonCtg = create_and_place_button_sc("ctg", 4, 7, self.c_ctg)
            self.buttonArcsin = create_and_place_button_sc("arcsin", 1, 8, self.c_arcsin)
            self.buttonArccos = create_and_place_button_sc("arccos", 2, 8, self.c_arcctg)
            self.buttonArctg = create_and_place_button_sc("arctg", 3, 8, self.c_arctg)
            self.buttonArcctg = create_and_place_button_sc("arcctg", 4, 8, self.c_arcctg)
            self.buttonBackspace = self.create_and_place_button_action("←", 1, 9, self.clear_last)
            self.buttonC = self.create_and_place_button_action("C", 2, 9, lambda: self.write_area.delete(0, END))
            self.buttonCE = self.create_and_place_button_action("CE", 3, 9, self.clear)

            self.scrollbarY.grid(row=1, rowspan=4, column=11, sticky=N + S)
            self.scrollbarX.grid(row=5, column=10, sticky=W + E)

            self.result_area.grid(row=1, rowspan=4, column=10)

            self.result_area_text = Label(text="The result is:")
            self.result_area_text.grid(row=0, column=10, sticky=W + E)

            self.type2 = Label(text="Scientific version", anchor=W)
            self.type2.grid(row=5, column=4, columnspan=6)

            self.write_area.grid(row=0, columnspan=10, sticky=W + E, ipady=6, pady=6)
        except AttributeError:
            buttons_to_remove = [self.initial, self.day, self.month, self.year, self.sep1, self.sep2, self.sep3,
                                 self.day_choose, self.day2_choose, self.month_choose, self.month2_choose,
                                 self.year_choose, self.year2_choose, self.final, self.result_text, self.result_area2,
                                 self.info, self.buttonClean, self.buttonGo]

            for name in buttons_to_remove:
                name.grid_remove()

    def simple_calc(self):
        try:
            buttons_to_remove = [self.buttonN, self.buttonE, self.button10, self.buttonlogx, self.buttonln,
                                 self.button_put_e, self.buttonP, self.buttonSin, self.buttonCos, self.buttonTg,
                                 self.buttonCtg, self.buttonArcsin, self.buttonArccos, self.buttonArctg,
                                 self.buttonArcctg, self.buttonBackspace, self.buttonC, self.buttonCE, self.type2]

            for name in buttons_to_remove:
                name.grid_remove()

            self.buttonBackspace = self.create_and_place_button_action("←", 1, 5, self.clear_last)
            self.buttonC = self.create_and_place_button_action("C", 2, 5, lambda: self.write_area.delete(0, END))
            self.buttonCE = self.create_and_place_button_action("CE", 3, 5, self.clear)
            self.type = Label(text="Simple version")
            self.type.grid(row=5, column=0, columnspan=6)


        except AttributeError:
            date_remove = [self.initial, self.day, self.month, self.year, self.sep1, self.sep2, self.sep3,
                           self.day_choose, self.day2_choose, self.month_choose, self.month2_choose, self.year_choose,
                           self.year2_choose, self.final, self.result_text, self.result_area2, self.info,
                           self.buttonClean, self.buttonGo]

            for name in date_remove:
                name.grid_remove()

            self.write_area = Entry(justify=RIGHT)
            self.write_area.grid(row=0, columnspan=6, sticky=W + E, ipady=6, pady=6)

            self.scrollbarY = Scrollbar(orient=VERTICAL, command=self.result_area_yview)
            self.scrollbarY.grid(row=1, rowspan=4, column=7, sticky=N + S)
            self.scrollbarX = Scrollbar(orient=HORIZONTAL, command=self.result_area_xview)
            self.scrollbarX.grid(row=5, column=6, sticky=W + E)

            self.result_area = Text(width=40, height=10, wrap=NONE)
            self.result_area.grid(row=1, rowspan=4, column=6)
            self.result_area['yscrollcommand'] = self.scrollbarY.set
            self.result_area['xscrollcommand'] = self.scrollbarX.set

            self.result_area_text = Label(text="The result is:")
            self.result_area_text.grid(row=0, column=6, sticky=W + E)

            self.type = Label(text="Simple version")
            self.type.grid(row=5, column=0, columnspan=6)

            self.button0 = self.create_and_place_button_input("0", 4, 1)
            self.button1 = self.create_and_place_button_input("1", 3, 0)
            self.button2 = self.create_and_place_button_input("2", 3, 1)
            self.button3 = self.create_and_place_button_input("3", 3, 2)
            self.button4 = self.create_and_place_button_input("4", 2, 0)
            self.button5 = self.create_and_place_button_input("5", 2, 1)
            self.button6 = self.create_and_place_button_input("6", 2, 2)
            self.button7 = self.create_and_place_button_input("7", 1, 0)
            self.button8 = self.create_and_place_button_input("8", 1, 1)
            self.button9 = self.create_and_place_button_input("9", 1, 2)
            self.buttonPlus = self.create_and_place_button_input("+", 1, 3)
            self.buttonMinus = self.create_and_place_button_input("-", 2, 3)
            self.buttonMulti = self.create_and_place_button_input("*", 3, 3)
            self.buttonDot = self.create_and_place_button_input(".", 4, 0)
            self.buttonDiv = self.create_and_place_button_input("/", 4, 3)
            self.buttonLeftPar = self.create_and_place_button_input("(", 4, 4)
            self.buttonRightPar = self.create_and_place_button_input(")", 4, 5)

            self.buttonSquare = self.create_and_place_button_action("x²", 1, 4, self.square)
            self.buttonC = self.create_and_place_button_action("C", 2, 5, lambda: self.write_area.delete(0, END))
            self.buttonSqrt = self.create_and_place_button_action("√", 2, 4, self.sqrt)
            self.buttonBackspace = self.create_and_place_button_action("←", 1, 5, self.clear_last)
            self.buttonSquareY = self.create_and_place_button_action("xʸ", 3, 4, self.squareY)
            self.buttonCE = self.create_and_place_button_action("CE", 3, 5, self.clear)
            self.buttonEqual = self.create_and_place_button_action("=", 4, 2, self.equal)

    def date_calc(self):
        try:
            things_to_remove = [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6,
                                self.button7, self.button8, self.button9, self.button0, self.buttonDot, self.buttonEqual,
                                self.buttonPlus, self.buttonMinus, self.buttonMulti, self.buttonDiv, self.buttonSquare,
                                self.buttonSquareY, self.buttonRightPar, self.buttonLeftPar, self.buttonC, self.buttonCE,
                                self.buttonBackspace, self.buttonSqrt, self.write_area, self.result_area,
                                self.result_area_text, self.type, self.scrollbarX, self.scrollbarY, self.buttonN,
                                self.buttonE, self.button10, self.button_put_e, self.buttonln, self.buttonlogx,
                                self.buttonSin, self.buttonCos, self.buttonTg, self.buttonCtg, self.buttonArcsin,
                                self.buttonArccos, self.buttonArcctg, self.buttonArctg, self.buttonP]

            for name in things_to_remove:
                name.grid_remove()
        except AttributeError:
            things_to_remove = [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6,
                                self.button7, self.button8, self.button9, self.button0, self.buttonDot, self.buttonEqual,
                                self.buttonPlus, self.buttonMinus, self.buttonMulti, self.buttonDiv, self.buttonSquare,
                                self.buttonSquareY, self.buttonRightPar, self.buttonLeftPar, self.buttonC, self.buttonCE,
                                self.buttonBackspace, self.buttonSqrt, self.write_area, self.result_area,
                                self.result_area_text, self.type, self.scrollbarX, self.scrollbarY]

            for name in things_to_remove:
                name.grid_remove()

        self.initial = Label(text="Initial date", justify=LEFT)
        self.initial.grid(row=0, column=0, columnspan=5)
        self.day = Label(text="Day")
        self.day.grid(row=1, column=1)
        self.sep1 = Label(text="        ")
        self.sep1.grid(row=1, column=0)
        self.month = Label(text="Month")
        self.month.grid(row=1, column=3)
        self.sep2 = Label(text="        ")
        self.sep2.grid(row=1, column=2)
        self.year = Label(text="Year")
        self.year.grid(row=1, column=5)
        self.sep3 = Label(text="        ")
        self.sep3.grid(row=1, column=4)

        self.day_choose = Spinbox(from_=1, to=31, increment=1, justify=LEFT, width=7, wrap=True)
        self.day_choose.grid(row=2, column=1)

        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]

        self.month_choose = Spinbox(values=months, justify=LEFT, width=11, wrap=True)
        self.month_choose.grid(row=2, column=3)

        years = [x for x in range(1, 3001)]
        self.year_choose = Spinbox(values=years, justify=LEFT, width=7, wrap=True)
        self.year_choose.grid(row=2, column=5)
        self.year_choose.delete(0, END)
        self.year_choose.insert(0, "2018")

        self.final = Label(text="Final date", justify=LEFT)
        self.final.grid(row=3, column=0, columnspan=5)

        self.day2_choose = Spinbox(from_=1, to=31, increment=1, justify=LEFT, width=7, wrap=True)
        self.day2_choose.grid(row=4, column=1)

        self.month2_choose = Spinbox(values=months, justify=LEFT, width=11, wrap=True)
        self.month2_choose.grid(row=4, column=3)

        years2 = [x for x in range(1, 3001)]
        self.year2_choose = Spinbox(values=years2, justify=LEFT, width=7, wrap=True)
        self.year2_choose.grid(row=4, column=5)
        self.year2_choose.delete(0, END)
        self.year2_choose.insert(0, "2018")

        self.result_text = Label(text="Difference", justify=LEFT)
        self.result_text.grid(row=5, column=0, columnspan=5)

        self.result_area2 = Entry(justify=LEFT)
        self.result_area2.grid(row=6, columnspan=5, sticky=W + E, ipady=6, padx=8)

        self.info = Label(text="Date calculator", justify=LEFT)
        self.info.grid(row=7, column=0, columnspan=5)

        self.buttonGo = Button(text="Go!", width=7, height=1, command=self.check_date_correctness)
        self.buttonGo.grid(row=6, column=5)
        self.buttonClean = Button(text="Clean", width=7, height=1, command=self.clean_date)
        self.buttonClean.grid(row=6, column=6)
        self.master.bind('<Return>', lambda event=None: self.change_action_key(self.check_date_correctness(),
                                                                               self.buttonGo))
        self.master.bind('<Delete>', lambda event=None: self.change_action_key(self.clean_date(), self.buttonClean))
        self.set_current_date()

    def test(self):
        try:
            button_to_clear = [self.button0, self.button1, self.button2, self.button3, self.button4, self.button5,
                               self.button6, self.button7, self.button8, self.button9, self.buttonDot, self.buttonEqual,
                               self.buttonLeftPar, self.buttonRightPar, self.buttonSqrt, self.buttonSquare,
                               self.buttonSquareY, self.buttonPlus, self.buttonMinus, self.buttonDiv,
                               self.buttonMulti, self.buttonC, self.buttonCE, self.buttonBackspace,
                               self.write_area, self.result_area, self.result_area_text, self.scrollbarX,
                               self.scrollbarY, self.type_science, self.buttonN, self.buttonE, self.button10,
                               self.buttonlogx, self.buttonln, self.button_put_e, self.buttonP, self.buttonSin,
                               self.buttonCos, self.buttonTg, self.buttonCtg, self.buttonArcsin,
                               self.buttonArccos, self.buttonArctg, self.buttonArcctg]

            for name in button_to_clear:
                name.grid_remove()

            normal = normal_calc.Normal_calc(root)

        except AttributeError:
            try:
                button_to_clear = [self.button0, self.button1, self.button2, self.button3, self.button4, self.button5,
                                   self.button6, self.button7, self.button8, self.button9, self.buttonDot, self.buttonEqual,
                                   self.buttonLeftPar, self.buttonRightPar, self.buttonSqrt, self.buttonSquare,
                                   self.buttonSquareY, self.buttonPlus, self.buttonMinus, self.buttonDiv,
                                   self.buttonMulti, self.buttonC, self.buttonCE, self.buttonBackspace,
                                   self.write_area, self.result_area, self.result_area_text, self.scrollbarX,
                                   self.scrollbarY, self.type]

                for name in button_to_clear:
                    name.grid_remove()
                science = te.Scientific_calc(root)

            except AttributeError:
                button_to_clear = [self.initial, self.day, self.month, self.year, self.sep1, self.sep2, self.sep3,
                                   self.day_choose, self.day2_choose, self.month_choose, self.month2_choose,
                                   self.year_choose, self.year2_choose, self.final, self.result_text, self.result_area2,
                                   self.info, self.buttonClean, self.buttonGo]

                for name in button_to_clear:
                    name.grid_remove()


root = Tk()

a = Calculator(root)

root.mainloop()
