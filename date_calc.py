from tkinter import *
import functions


class Date_calc(functions.Mixin):
    def __init__(self, master):

        self.master = master

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

