from tkinter import *


class TicTacToe:
    def __init__(self, root):
        """documentation"""
        self.root = root
        self.root.withdraw()
        self.current_window = Toplevel()
        self.current_window.title("TacTacToe")
        self.current_window.geometry("500x524")

        self.canvas = Canvas(self.current_window, width=500, height=524, borderwidth=0, highlightthickness=0)
        self.canvas.pack()

        self.image_tictactoe_background = PhotoImage(file="assets/tictactoe_background.png")
        self.canvas.create_image(0, 0, image=self.image_tictactoe_background, anchor="nw")

        self.button_exit = Button(self.canvas, text="Exit", command=self.open_main_window)
        self.button_exit.place(x=4, y=4, height=16, width=244)

        self.button_restart = Button(self.canvas, text="Start Over", command=self.start)
        self.button_restart.place(x=252, y=4, height=16, width=244)

        self.game_board = []
        self.start()

    def open_main_window(self):
        """documentation"""
        from MainWindow import MainWindow
        self.current_window.destroy()
        MainWindow(self.root)

    def start(self):
        """documentation"""
        self.game_board = [{"tile": "", "coordinates": (125, 125)}, {"tile": "", "coordinates": (250, 125)}, {"tile": "", "coordinates": (375, 125)},
                           {"tile": "", "coordinates": (125, 250)}, {"tile": "", "coordinates": (250, 250)}, {"tile": "", "coordinates": (375, 250)},
                           {"tile": "", "coordinates": (125, 375)}, {"tile": "", "coordinates": (250, 375)}, {"tile": "", "coordinates": (375, 375)},]
        self.display_board()

    def display_board(self):
        self.image_x = PhotoImage(file="assets/image_x.png")
        self.image_o = PhotoImage(file="assets/image_o.png")

        for i in range(len(self.gameboard)):
            if self.gameboard[i]["tile"] == "":
                # make button

            elif self.gameboard[i]["tile"] == "x":
                # make x
                pass
            elif self.gameboard[i]["tile"] == "o":
                # make o
                pass





# root = Tk()
# app = TicTacToe(root)
# root.mainloop()