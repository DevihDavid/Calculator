from tkinter import *
import functions
from math import e, pi


class Calculator(functions.Mixin):

    def __init__(self, master):
        self.master = master

        top_menu = Menu(master)
        master.config(menu=top_menu)

        calc_type = Menu(top_menu)
        top_menu.add_cascade(label="Calculator", menu=calc_type)
        calc_type.add_command(label="Simple", command=self.simple_calc)
        calc_type.add_command(label="Scientific", command=self.scientific_calc)
        calc_type.add_command(label="Date calculation")

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

        self.type = Label(text="Scientific version", anchor=W)
        self.type.grid(row=5, column=4, columnspan=6)

        self.write_area.grid(row=0, columnspan=10, sticky=W + E, ipady=6, pady=6)

    def simple_calc(self):
        buttons_to_remove = [self.buttonN, self.buttonE, self.button10, self.buttonlogx, self.buttonln,
                             self.button_put_e, self.buttonP, self.buttonSin, self.buttonCos, self.buttonTg,
                             self.buttonCtg, self.buttonArcsin, self.buttonArccos, self.buttonArctg,
                             self.buttonArcctg, self.buttonBackspace, self.buttonC, self.buttonCE, self.type]

        for name in buttons_to_remove:
            name.grid_remove()

        self.type = Label(text="Simple version", anchor=W)
        self.type.grid(row=5, column=0, columnspan=6)
        self.buttonBackspace = self.create_and_place_button_action("←", 1, 5, self.clear_last)
        self.buttonC = self.create_and_place_button_action("C", 2, 5, lambda: self.write_area.delete(0, END))
        self.buttonCE = self.create_and_place_button_action("CE", 3, 5, self.clear)

        self.scrollbarY.grid(row=1, rowspan=4, column=7, sticky=N + S)
        self.scrollbarX.grid(row=5, column=6, sticky=W + E)

        self.result_area.grid(row=1, rowspan=4, column=6)

        self.result_area_text.grid(row=0, column=6, sticky=W + E)

        self.type = Label(text="Simple version", anchor=W)
        self.type.grid(row=5, column=0, columnspan=6)

        self.write_area.grid(row=0, columnspan=6, sticky=W + E, ipady=6, pady=6)


root = Tk()

a = Calculator(root)

root.mainloop()
