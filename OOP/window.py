from tkinter import *


class MainWindow:
    def __init__(self, dimensions="990x540", label="Welcome to my first GUI program"):
        """dimensions format (int x int), label format ('str')"""
        self.frame = Tk()
        self.frame.title("Python GUI Intro")
        self.frame.geometry(f"{dimensions}")
        self.label_welcome = Label(text=f"{label}")
        self.label_welcome.pack()


    def run(self):
        """run the mainloop (whatever that means)"""
        self.frame.mainloop()


app = MainWindow()
app.run()
