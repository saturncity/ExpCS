from tkinter import *


class MainWindow:
    def __init__(self, dimensions="990x540", label="Welcome to my first GUI program"):
        """dimensions format (int x int), label format ('str')"""
        self.frame = Tk()
        # self.frame.config(bg="gold1")
        self.frame.title("Python GUI Intro")
        self.frame.geometry(f"{dimensions}")
        # self.frame.resizable(False, False)  # prevent resizing

        self.label_welcome = Label(text=f"{label}", bg="paleturquoise1", fg="black")

        self.label_welcome.pack()

        self.label_firstint = Label(text="Enter first number: ")
        self.label_secondint = Label(text="Enter second number: ")

        self.text_firstint = Entry()
        self.text_secondint = Entry()

        self.label_firstint.pack()
        self.text_firstint.pack()
        self.label_secondint.pack()
        self.text_secondint.pack()

        self.button_sum = Button(text="Click to add both numbers",command=self.sum)
        self.button_sum.pack()

        self.button_subtract = Button(text="Click to subtract both numbers", command=self.subtract)
        self.button_subtract.pack()

        self.button_multiply = Button(text="Click to multiply both numbers", command=self.multiply)
        self.button_multiply.pack()

        self.button_div = Button(text="Click to div both numbers", command=self.div)
        self.button_div.pack()

        self.label_result = Label(text="Result", bg="aquamarine1", fg="black")
        self.label_result.pack()


    def run(self):
        """run the mainloop (whatever that means)"""
        self.frame.mainloop()


    def sum(self):
        """get data from text boxes then add then return as result"""
        firstnumber = int(self.text_firstint.get())
        secondnumber = int(self.text_secondint.get())
        total = firstnumber+secondnumber
        self.label_result.config(text=total)


    def subtract(self):
        firstnumber = int(self.text_firstint.get())
        secondnumber = int(self.text_secondint.get())
        total = firstnumber - secondnumber
        self.label_result.config(text=total)


    def multiply(self):
        firstnumber = int(self.text_firstint.get())
        secondnumber = int(self.text_secondint.get())
        total = firstnumber * secondnumber
        self.label_result.config(text=total)


    def div(self):
        firstnumber = int(self.text_firstint.get())
        secondnumber = int(self.text_secondint.get())
        total = firstnumber / secondnumber
        self.label_result.config(text=total)


app = MainWindow()
app.run()
