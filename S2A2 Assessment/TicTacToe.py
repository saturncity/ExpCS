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

        self.button_exit = Button(self.canvas, text="Exit", command=self.open_main_window)
        self.button_restart = Button(self.canvas, text="Start Over", command=self.start)

        self.image_x = PhotoImage(file="assets/image_x.png")
        self.image_o = PhotoImage(file="assets/image_o.png")

        self.game_board = []
        self.buttons = []
        self.turn = ""

        self.start()

    def open_main_window(self):
        """documentation"""
        from MainWindow import MainWindow
        self.current_window.destroy()
        MainWindow(self.root)

    def start(self):
        """documentation"""
        self.game_board = [{"tile": "", "pos_x": 84, "pos_y": 108}, {"tile": "", "pos_x": 250, "pos_y": 108},
                           {"tile": "", "pos_x": 416, "pos_y": 108},
                           {"tile": "", "pos_x": 84, "pos_y": 274}, {"tile": "", "pos_x": 250, "pos_y": 274},
                           {"tile": "", "pos_x": 416, "pos_y": 274},
                           {"tile": "", "pos_x": 84, "pos_y": 436}, {"tile": "", "pos_x": 250, "pos_y": 436},
                           {"tile": "", "pos_x": 416, "pos_y": 436}]
        self.turn = "x"
        self.show_buttons()

    def show_buttons(self, ):
        """documentation"""
        self.canvas.delete("all")

        self.canvas.create_image(0, 0, image=self.image_tictactoe_background, anchor="nw")
        self.button_exit.place(x=4, y=4, height=16, width=244)
        self.button_restart.place(x=252, y=4, height=16, width=244)

        counter = 0
        for tile in self.game_board:
            if tile["tile"] == "":
                self.buttons.append(
                    Button(self.canvas, text="PLACE " + self.turn.upper(), command=lambda: self.change_tile(tile)))
                self.buttons[counter].place(x=tile["pos_x"], y=tile["pos_y"], height=138, width=138, anchor=CENTER)

            counter = counter + 1


        print(self.buttons)

    def change_tile(self, tile):
        """documentation"""
        tile["tile"] = self.turn
        if self.turn == "x":
            self.turn = "o"
        elif self.turn == "o":
            self.turn = "x"
        self.show_buttons()


root = Tk()
app = TicTacToe(root)
root.mainloop()
