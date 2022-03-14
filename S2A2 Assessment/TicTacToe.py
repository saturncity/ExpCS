from tkinter import *


class TicTacToe:
    def __init__(self, root):
        """documentation"""
        self.root = root
        self.root.withdraw()
        self.current_window = Toplevel()
        self.current_window.title("TacTacToe")
        self.current_window.geometry("500x524")

        self.image_x = PhotoImage(file="assets/image_x.png")
        self.image_o = PhotoImage(file="assets/image_o.png")

        self.canvas = Canvas(self.current_window, width=500, height=524, borderwidth=0, highlightthickness=0)
        self.canvas.pack()

        self.image_tictactoe_background = PhotoImage(file="assets/tictactoe_background-alt.png")
        self.canvas.create_image(0, 0, image=self.image_tictactoe_background, anchor="nw")

        self.button_exit = Button(self.canvas, text="Exit", command=self.open_main_window)
        self.button_exit.place(x=4, y=4, height=16, width=244)

        self.button_restart = Button(self.canvas, text="Start Over", command=self.start)
        self.button_restart.place(x=252, y=4, height=16, width=244)

        self.game_board = []
        self.start()

        self.show_buttons()

    def open_main_window(self):
        """documentation"""
        from MainWindow import MainWindow
        self.current_window.destroy()
        MainWindow(self.root)

    def start(self):
        """documentation"""
        self.game_board = [{"tile": "", "pos_x": 84, "pos_y": 168}, {"tile": "", "pos_x": 250, "pos_y": 168}, {"tile": "", "pos_x": 416, "pos_y": 168},
                           {"tile": "", "pos_x": 84, "pos_y": 318}, {"tile": "", "pos_x": 250, "pos_y": 318}, {"tile": "", "pos_x": 416, "pos_y": 318},
                           {"tile": "", "pos_x": 84, "pos_y": 498}, {"tile": "", "pos_x": 250, "pos_y": 498}, {"tile": "", "pos_x": 416, "pos_y": 498}]
        self.display_board()

    def display_board(self):
        for i in range(len(self.game_board)):
            if self.game_board[i]["tile"] == "":
                # make button
                pass
            elif self.game_board[i]["tile"] == "x":
                # make x
                pass
            elif self.game_board[i]["tile"] == "o":
                # make o
                pass

    def show_buttons(self,):
        """documentation"""
        for tile in self.game_board:
            if tile["tile"] == "":
                Button(self.canvas, text="PLACE X", command=self.change_tile(tile)).place(x=tile["pos_x"], y=tile["pos_y"], height=50, width=100, anchor=CENTER)

    def change_tile(self, tile):
        """documentation"""
        pass

root = Tk()
app = TicTacToe(root)
root.mainloop()