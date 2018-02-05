from tkinter import *
import functions


class Calculator(functions.Mixin):

    def __init__(self, master):
        self.master = master

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

        self.result_area_text = Label(master, text="The result is:").grid(row=0, column=6, sticky=W + E)

        self.type = Label(master, text="Simple version").grid(row=5, column=0, columnspan=6)

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

    def make_lambda(self, name, button):
        return lambda event=None: self.change_input_key(name, button)

    def bind_buttons(self):
        button_input = {"0": self.button0, "1": self.button1, "2": self.button2, "3": self.button3, "4": self.button4,
                        "5": self.button5, "6": self.button6, "7": self.button7, "8": self.button8, "9": self.button9,
                        ",": self.buttonDot, ".": self.buttonDot, "+": self.buttonPlus, "-": self.buttonMinus,
                        "*": self.buttonMulti, "/": self.buttonDiv, "(": self.buttonLeftPar, ")": self.buttonRightPar}

        for name, action in button_input.items():
            self.master.bind(name, self.make_lambda(name, action))

        self.master.bind('<BackSpace>', lambda event=None: self.change_action_key(self.clear_last(),
                                                                               self.buttonBackspace))
        self.master.bind('<Delete>', lambda event=None: self.change_action_key(self.write_area.delete(0, END),
                                                                               self.buttonC))
        self.master.bind('<Return>', lambda event=None: self.change_action_key(self.equal(), self.buttonEqual))
        self.master.bind('=', lambda event=None: self.change_action_key(self.equal(), self.buttonEqual))
        self.master.bind('^', lambda event=None: self.change_action_key(self.square(), self.buttonSquare))

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


root = Tk()

a = Calculator(root)

root.mainloop()
