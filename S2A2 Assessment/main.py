from tkinter import *


class MainWindow():
    def __init__(self, root):
        """do documentation"""
        #  create a window
        self.root = root
        self.root.withdraw()
        self.current_window = Toplevel()
        self.current_window.title("Main Menu")
        self.current_window.geometry("414x896")

        #  create a canvas. a canvas is like a regular window, but you are able to over-lap any item.
        self.canvas = Canvas(self.current_window, width=414, height=896)  # iphone 11 pro max resolution (/3)
        self.canvas.pack()

        #  put the file on the canvas in 0, 0 then anchor it to the north-west point of the image.
        self.image = PhotoImage(file="assets/background.png")
        self.canvas.create_image(0, 0, image=self.image, anchor="nw")


root = Tk()
app = MainWindow(root)
root.mainloop()
