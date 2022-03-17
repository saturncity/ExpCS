from tkinter import *


class Snake:
    def __init__(self, root):
        """documentation"""
        self.root = root
        self.root.withdraw()
        self.current_window = Toplevel()
        self.current_window.title("MALWARE_VIRUS.exe")
        self.current_window.geometry("1000x250")

        self.canvas = Canvas(self.current_window, width=1000, height=250, borderwidth=0, highlightthickness=0)
        self.canvas.pack()

        self.exit_button = Button(self.canvas, text="Force Quit", command=self.open_main_menu)
        self.exit_button.place(x=7, y=7, anchor=NW)

        self.answers = []

        self.task_1()

    def open_main_menu(self):
        """Start by removing the current_window. Then, import the Main Menu class. Finally, create an instance of the
        Menu. """
        self.current_window.destroy()
        from MainWindow import MainWindow
        MainWindow(self.root)

    def validate(self, n):
        r = [int(ch) for ch in str(n)][::-1]
        return (sum(r[0::2]) + sum(sum(divmod(d * 2, 10)) for d in r[1::2])) % 10 == 0

    def task_1(self):
        self.text_question_1 = Label(self.canvas, text="What is your name?", fg="black", bg="aquamarine1")
        self.text_question_1.place(x=500, y=17, anchor=CENTER)

        self.entry_question_1 = Entry(self.canvas)
        self.entry_question_1.place(x=500, y=47, anchor=CENTER)

        self.button_question_1 = Button(self.canvas, text="Submit Answer", command=self.task_2)
        self.button_question_1.place(x=500, y=227, anchor=CENTER)

    def task_2(self):
        self.answers.append({'name': self.entry_question_1.get()})

        self.text_question_1.destroy()
        self.entry_question_1.destroy()
        self.button_question_1.destroy()

        self.text_question_2 = Label(self.canvas, text="In what city were you born?", fg="black", bg="gold")
        self.text_question_2.place(x=500, y=17, anchor=CENTER)

        self.entry_question_2 = Entry(self.canvas)
        self.entry_question_2.place(x=500, y=47, anchor=CENTER)

        self.button_question_2 = Button(self.canvas, text="Submit Answer", command=self.task_3)
        self.button_question_2.place(x=500, y=227, anchor=CENTER)

    def task_3(self):
        self.answers.append({'born_in': self.entry_question_2.get()})

        self.text_question_2.destroy()
        self.entry_question_2.destroy()
        self.button_question_2.destroy()

        self.text_question_3 = Label(self.canvas, text="What is/was the name of your favorite pet?", fg="black",
                                     bg="gold")
        self.text_question_3.place(x=500, y=17, anchor=CENTER)

        self.entry_question_3 = Entry(self.canvas)
        self.entry_question_3.place(x=500, y=47, anchor=CENTER)

        self.button_question_3 = Button(self.canvas, text="Submit Answer", command=self.task_4)
        self.button_question_3.place(x=500, y=227, anchor=CENTER)

    def task_4(self):
        self.answers.append({'born_in': self.entry_question_3.get()})

        self.text_question_3.destroy()
        self.entry_question_3.destroy()
        self.button_question_3.destroy()

        self.text_question_4 = Label(self.canvas, text="What is your mother's maiden name?", fg="black", bg="gold")
        self.text_question_4.place(x=500, y=17, anchor=CENTER)

        self.entry_question_4 = Entry(self.canvas)
        self.entry_question_4.place(x=500, y=47, anchor=CENTER)

        self.button_question_4 = Button(self.canvas, text="Submit Answer", command=self.task_5)
        self.button_question_4.place(x=500, y=227, anchor=CENTER)

    def task_5(self):
        self.answers.append({'born_in': self.entry_question_4.get()})

        self.text_question_4.destroy()
        self.entry_question_4.destroy()
        self.button_question_4.destroy()

        self.text_question_5 = Label(self.canvas, text="Please enter your Credit Card Number", fg="white", bg="red")
        self.text_question_5.place(x=500, y=17, anchor=CENTER)

        self.entry_question_5 = Entry(self.canvas)
        self.entry_question_5.place(x=500, y=47, anchor=CENTER)

        self.button_question_5 = Button(self.canvas, text="Submit Answer", command=self.task_6)
        self.button_question_5.place(x=500, y=227, anchor=CENTER)

    def task_6(self):
        if not self.validate(self.entry_question_5.get()):
            return

        self.answers.append({'credit_card_number': self.entry_question_5.get().strip})

        self.text_question_4.destroy()
        self.entry_question_4.destroy()
        self.button_question_4.destroy()

