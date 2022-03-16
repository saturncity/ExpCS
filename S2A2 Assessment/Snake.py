from tkinter import *


class Snake:
    def __init__(self, root):
        """documentation"""
        self.root = root
        self.root.withdraw()
        self.current_window = Toplevel()
        self.current_window.title("MALWARE_VIRUS.exe")
        self.current_window.geometry("1000x250")

        self.canvas = Canvas(self.current_window, width=500, height=524, borderwidth=0, highlightthickness=0)
        self.canvas.pack()