import ast
import json
from tkinter import *


class Snake:
    def __init__(self, root):
        """Hide the root. Set the current_window on top. Set the title, geometry of the current_window. Then create a
        canvas for more relaxed placement of buttons, labels and others. After create the exit button and place it at
        the top left. Create the view list button. Then create a empty list where the answers can be stored. Finally,
        begin."""
        self.root = root
        self.root.withdraw()
        self.current_window = Toplevel()
        self.current_window.title("MALWARE_VIRUS.exe")
        self.current_window.geometry("1000x250")

        self.canvas = Canvas(self.current_window, width=1000, height=250, borderwidth=0, highlightthickness=0)
        self.canvas.pack()

        self.button_exit = Button(self.canvas, text="Force Quit", command=self.open_main_menu)
        self.button_exit.place(x=7, y=7, anchor=NW)

        self.button_view_list = Button(self.canvas, text="Send Data to Admin Console", command=self.view_list)
        self.button_view_list.place(x=87, y=227, anchor=CENTER)

        self.answers = []
        self.data = []
        self.read_file("user_data.txt")

        self.task_1()

    def write_to_file(self, file_name):
        with open(file_name, 'w') as file_out:
            json.dump(self.data, file_out)
        return

    def read_file(self, file_name):
        with open(file_name, 'r') as file_in:
            self.data = ast.literal_eval(file_in.read())
        return

    def open_main_menu(self):
        """Start by removing the current_window. Then, import the Main Menu class. Finally, create an instance of the
        Menu. """
        self.current_window.destroy()
        from MainWindow import MainWindow
        MainWindow(self.root)

    def validate(self, n):
        f"""Luhn Algorithm is used to check if a credit card number is valid.

        AndreinaAndreina. 'Implementation of Luhn Formula.' Stack Overflow, 19 Nov. 2018,
        https://stackoverflow.com/a/53381527.

        \n\t1: Doubling every 2nd number.
        \n\t2: If the doubled number is two digits then add the two values together. ie. 8*2, 16, (1+6), 7
        \n\t3: Add all numbers together then check if the sum is divisible by 10 with no remainder. If there is no
        remainder then its technically a valid number, if it has a remainder then the CCN is invalid.
        
        \tExample:
        \n12367
        \n1+(2*2)+3+(6*2)+7
        \n1+4+3+(1+2)+7
        \n18 % 10
        \n8 is the remainder so this is not a valid CCN
        """
        r = [int(ch) for ch in str(n)][::-1]
        return (sum(r[0::2]) + sum(sum(divmod(d * 2, 10)) for d in r[1::2])) % 10 == 0

    def view_list(self):
        """Skip 100 Lines. Print formatted text."""
        for i in range(100):
            print()
        for user in self.data:
            print(
                f'{user[0]["name"]} \n\t- Born in: {user[1]["born_in"]} \n\t- Favorite Pet Name: '
                f'{user[2]["favorite_pet"]} \n\t- Mothers Maiden Name: {user[3]["mothers_maiden_name"]} \n\t- Credit '
                f'Card Number: {user[4]["credit_card_number"]}\n')
        return

    def task_1(self):
        """Obtain Name"""
        # create text asking user for name
        self.text_question_1 = Label(self.canvas, text="What is your name?", fg="black", bg="aquamarine1")
        self.text_question_1.place(x=500, y=17, anchor=CENTER)

        # create field where user can enter info
        self.entry_question_1 = Entry(self.canvas)
        self.entry_question_1.place(x=500, y=47, anchor=CENTER)

        # create a button that moves onto the next task (task 2)
        self.button_question_1 = Button(self.canvas, text="Submit Answer", command=self.task_2)
        self.button_question_1.place(x=500, y=227, anchor=CENTER)

    def task_2(self):
        """Obtain Security Question 1"""
        # append the previous answer to the list
        self.answers.append({'name': self.entry_question_1.get()})

        # delete previous objects
        self.text_question_1.destroy()
        self.entry_question_1.destroy()
        self.button_question_1.destroy()

        # ask user where they were born
        self.text_question_2 = Label(self.canvas, text="In what city were you born?", fg="black", bg="gold")
        self.text_question_2.place(x=500, y=17, anchor=CENTER)

        self.entry_question_2 = Entry(self.canvas)
        self.entry_question_2.place(x=500, y=47, anchor=CENTER)

        # move onto task 3
        self.button_question_2 = Button(self.canvas, text="Submit Answer", command=self.task_3)
        self.button_question_2.place(x=500, y=227, anchor=CENTER)

    def task_3(self):
        """Obtain Security Question 2"""
        self.answers.append({'born_in': self.entry_question_2.get()})

        self.text_question_2.destroy()
        self.entry_question_2.destroy()
        self.button_question_2.destroy()

        # ask user the name of their favorite pet
        self.text_question_3 = Label(self.canvas, text="What is/was the name of your favorite pet?", fg="black",
                                     bg="gold")
        self.text_question_3.place(x=500, y=17, anchor=CENTER)

        self.entry_question_3 = Entry(self.canvas)
        self.entry_question_3.place(x=500, y=47, anchor=CENTER)

        # move onto task 4
        self.button_question_3 = Button(self.canvas, text="Submit Answer", command=self.task_4)
        self.button_question_3.place(x=500, y=227, anchor=CENTER)

    def task_4(self):
        """Obtain Security Question 3"""
        self.answers.append({'favorite_pet': self.entry_question_3.get()})

        self.text_question_3.destroy()
        self.entry_question_3.destroy()
        self.button_question_3.destroy()

        # ask user what their mother's maiden name was
        self.text_question_4 = Label(self.canvas, text="What is your mother's maiden name?", fg="black", bg="gold")
        self.text_question_4.place(x=500, y=17, anchor=CENTER)

        self.entry_question_4 = Entry(self.canvas)
        self.entry_question_4.place(x=500, y=47, anchor=CENTER)

        # move onto task 5
        self.button_question_4 = Button(self.canvas, text="Submit Answer", command=self.task_5)
        self.button_question_4.place(x=500, y=227, anchor=CENTER)

    def task_5(self):
        """Obtain Credit Card Number"""
        self.answers.append({'mothers_maiden_name': self.entry_question_4.get()})

        self.text_question_4.destroy()
        self.entry_question_4.destroy()
        self.button_question_4.destroy()

        # ask user to enter credit card number
        self.text_question_5 = Label(self.canvas, text="Please enter your Credit Card Number", fg="white", bg="crimson")
        self.text_question_5.place(x=500, y=17, anchor=CENTER)

        self.entry_question_5 = Entry(self.canvas)
        self.entry_question_5.place(x=500, y=47, anchor=CENTER)

        # create a error field to be configured later
        self.text_error_5 = Label(self.canvas)
        self.text_error_5.place(x=500, y=100, anchor=CENTER)

        # move onto task 6 (final)
        self.button_question_5 = Button(self.canvas, text="Submit Answer", command=self.task_6)
        self.button_question_5.place(x=500, y=227, anchor=CENTER)

    def task_6(self):
        """Validate CCN, Goodbye Message, Save Data"""
        try:
            # attempt to use the self.validate() function to check if the integer in field is a valid CCN
            if not self.validate(int(self.entry_question_5.get())):
                self.text_error_5.config(text="Invalid CCN (Hint: 5555555555554444 is a valid CCN)", fg="white",
                                         bg="red")
                return
        except ValueError:
            # if given a ValueError (when It's impossible to convert field to string) then it will catch the error
            # and run this code instead. This code just prints an error message.
            self.text_error_5.config(text="Not a valid number.", fg="white", bg="red")
            return

        self.answers.append({'credit_card_number': self.entry_question_5.get()})

        self.text_question_5.destroy()
        self.entry_question_5.destroy()
        self.text_error_5.destroy()
        self.button_question_5.destroy()

        # print final message
        self.text_goodbye = Label(self.canvas, text="You have satisfied The Snake. In order to keep him happy, "
                                                    "you must not go to the bank and do not cancel/pause your credit "
                                                    "card.", fg="white", bg="crimson")
        self.text_goodbye.place(x=500, y=125, anchor=CENTER)

        # send answers to data list
        self.data.append(self.answers)
        self.write_to_file("user_data.txt")
