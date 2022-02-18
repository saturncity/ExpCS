from tkinter import *


class Window:
    def __init__(self):
        """Opens a new 'unit converter' window that inputs a number from the user then, they can request to convert
        it to another unit."""
        self.frame = Tk()
        self.frame.geometry("500x500")
        self.frame.title("Unit Converter")

        self.label_title = Label(text="Welcome to Jason's Fahrenheit to Celsius Converter!", bg="aquamarine1",
                                 fg="black")

        self.label_input = Label(text="Input your number to convert here (Celsius or Fahrenheit):")
        self.text_input = Entry()

        self.button_celsius = Button(text="Convert Input to Celsius", command=self.convert_to_celsius)
        self.button_fahrenheit = Button(text="Convert Input to Fahrenheit", command=self.convert_to_fahrenheit)

        self.label_result = Label(text="")

        self.label_title.pack()
        self.line_skip()
        self.label_input.pack()
        self.text_input.pack()
        self.line_skip()
        self.button_celsius.pack()
        self.button_fahrenheit.pack()
        self.line_skip()
        self.label_result.pack()

    def run(self):
        """Runs the mainloop."""
        self.frame.mainloop()

    def line_skip(self):
        """Skip lines to improve the GUI experience."""
        self.label_line = Label(text="")
        self.label_line.pack()

    def convert_to_celsius(self):
        """Converts number given (presumably a number in fahrenheit) to celsius using ((intake - 32) * (5 / 9))."""
        intake = int(self.text_input.get())
        result = ((intake - 32) * (5 / 9))
        self.label_result.config(text=(f"{result}°c"), bg="gold", fg="black")

    def convert_to_fahrenheit(self):
        """Converts number given (presumably a number in celsius) to fahrenheit using ((intake * (9 / 5)) + 32)."""
        intake = int(self.text_input.get())
        result = ((intake * (9 / 5)) + 32)
        self.label_result.config(text=(f"{result}°f"), bg="gold", fg="black")


app = Window()
app.run()
