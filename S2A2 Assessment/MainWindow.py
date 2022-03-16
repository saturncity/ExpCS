import math
from tkinter import *

from Apps import App


class MainWindow:
    def __init__(self, root):
        """This is the primary "Main Hub" class. It creates a window, creates a canvas, displays a background, displays
        all app icons, adds buttons below icons to open an app. When an app is opened, the current window gets
        destroyed and calls the next class to display the next menu."""
        #  create a root, hide the root, create a window with the title "Main Menu" and with custom dimensions.
        self.root = root
        self.root.withdraw()
        self.current_window = Toplevel()
        self.current_window.title("Main Menu")  # TODO: Think of a creative 'Main Menu' name for this app.
        self.current_window.geometry("414x896")  # dimensions (pixels) of the iphone 11 pro max when divided by 3

        '''
        What are Canvases?
        
        Here is where we create a canvas. A canvas is like a label, button and others in the sense that that you can
        put anything on it but in the case of a canvas you can also use coordinates to place an object where ever it
        needs to go, and it allows the placement of any object to be anywhere including overlapping each other.
        '''
        #  make and pack the canvas
        self.canvas = Canvas(self.current_window, width=414, height=896, borderwidth=0, highlightthickness=0)
        self.canvas.pack()

        #  put the image on the canvas in 0, 0 then anchor it to the north-west point of the image.
        self.image_background = PhotoImage(file="assets/background.png")
        self.canvas.create_image(0, 0, image=self.image_background, anchor="nw")

        self.display_apps()

    def display_apps(self):
        self.image_tictactoe = PhotoImage(file="assets/apps/TicTacToe.png")
        self.canvas.create_image(7, 7, image=self.image_tictactoe, anchor=NW)
        self.button_tictactoe = Button(self.canvas, text="TicTacToe", command=self.open_tictactoe)
        self.button_tictactoe.place(x=7, y=105, width=90)

        self.image_snake = PhotoImage(file="assets/apps/Snake.png")
        self.canvas.create_image(105, 7, image=self.image_snake, anchor=NW)
        self.button_snake = Button(self.canvas, text="The Snake", command=self.open_snake)
        self.button_snake.place(x=105, y=105, width=90)

    def open_tictactoe(self):
        from TicTacToe import TicTacToe
        TicTacToe(self.root)
        self.current_window.destroy()

    def open_snake(self):
        return


root = Tk()
app = MainWindow(root)
root.mainloop()
