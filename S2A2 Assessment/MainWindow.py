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

        # display the apps using the display_apps() function.
        # self.applications = App()
        # self.displayed_apps = []
        # self.display_apps()

        self.button_lanuch = Button(self.canvas, text="open tictactoe", command=self.open_tictactoe)
        self.button_lanuch.place(x=100, y=100)

        Snake = {"image": {"filename": "Snake.png", "posx": ""}}
    #
    # def display_apps(self):
    #     # OLDTODO: Documentation.
    #     self.total_apps_displayed = 0
    #     while self.total_apps_displayed < self.applications.get_total_apps():
    #         self.displayed_apps.append(PhotoImage(
    #             file="assets/apps/" + self.applications.get_filename(self.total_apps_displayed)))
    #         self.canvas.create_image(self.next_free_position(),  # coords of free pos using its respective function.
    #                                  image=self.displayed_apps[self.total_apps_displayed],
    #                                  anchor="nw")
    #
    #         # OLDTODO: Place button for every app.
    #
    #         self.total_apps_displayed = self.total_apps_displayed + 1
    #
    # def next_free_position(self):
    #     # OLDTODO: Documentation.
    #     next_x = (self.total_apps_displayed - ((math.ceil(len(self.displayed_apps) / 4) - 1) * 4)) * 98 + 15
    #     next_y = (math.floor(self.total_apps_displayed / 4) * 122) + 15
    #     return next_x, next_y

    def open_tictactoe(self):
        from TicTacToe import TicTacToe
        TicTacToe(self.root)
        self.current_window.destroy()


root = Tk()
app = MainWindow(root)
root.mainloop()
