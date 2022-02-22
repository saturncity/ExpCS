from tkinter import *

class Window1:
    def __init__(self, root):
        self.root = root
        self.root.withdraw()
        self.current_window = Toplevel()
        self.current_window.title("Window 1")
        self.current_window.geometry("300x200")

        self.label_welcome = Label(self.current_window, text="Press da button")
        self.button_open_window_2 = Button(self.current_window, text="Go to Window 2", command=self.open_window_2)

        self.label_welcome.pack()
        self.button_open_window_2.pack()

    def open_window_2(self):
        Window2(self.root)
        self.current_window.destroy()


class Window2:
    def __init__(self, root):
        self.root = root
        self.root.withdraw()
        self.current_window = Toplevel()
        self.current_window.title("Window 2")
        self.current_window.geometry("300x200")

        self.label_welcome = Label(self.current_window, text="Press da button")
        self.button_open_window_2 = Button(self.current_window, text="Go to Window 1", command=self.open_window_1)

        self.label_welcome.pack()
        self.button_open_window_2.pack()

    def open_window_1(self):
        Window1(self.root)
        self.current_window.destroy()


root = Tk()
app = Window1(root)
root.mainloop()
