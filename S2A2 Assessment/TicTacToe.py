from tkinter import *


class TicTacToe:
    def __init__(self, root):
        """documentation"""
        self.root = root
        self.root.withdraw()
        self.current_window = Toplevel()
        self.current_window.title("TicTacToe")
        self.current_window.geometry("500x524")

        self.canvas = Canvas(self.current_window, width=500, height=524, borderwidth=0, highlightthickness=0)
        self.canvas.pack()

        self.image_tictactoe_background = PhotoImage(file="assets/tictactoe_background-alt.png")

        self.button_exit = Button(self.canvas, text="Exit", command=self.open_main_window)
        self.button_restart = Button(self.canvas, text="Start Over", command=self.start)

        self.image_x = PhotoImage(file="assets/image_x.png")
        self.image_o = PhotoImage(file="assets/image_o.png")

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
        self.canvas.create_image(0, 0, image=self.image_tictactoe_background, anchor="nw")
        self.button_exit.place(x=4, y=4, height=16, width=244)
        self.button_restart.place(x=252, y=4, height=16, width=244)

        self.t0 = Button(self.canvas, text="PLACE X (0)", command=lambda: self.trigger_tile(0))
        self.t0.place(x=self.game_board[0]["pos_x"], y=self.game_board[0]["pos_y"], height=138, width=138,
                      anchor=CENTER)

        self.t1 = Button(self.canvas, text="PLACE X (1)", command=lambda: self.trigger_tile(1))
        self.t1.place(x=self.game_board[1]["pos_x"], y=self.game_board[1]["pos_y"], height=138, width=138,
                      anchor=CENTER)

        self.t2 = Button(self.canvas, text="PLACE X (2)", command=lambda: self.trigger_tile(2))
        self.t2.place(x=self.game_board[2]["pos_x"], y=self.game_board[2]["pos_y"], height=138, width=138,
                      anchor=CENTER)

        self.t3 = Button(self.canvas, text="PLACE X (3)", command=lambda: self.trigger_tile(3))
        self.t3.place(x=self.game_board[3]["pos_x"], y=self.game_board[3]["pos_y"], height=138, width=138,
                      anchor=CENTER)

        self.t4 = Button(self.canvas, text="PLACE X (4)", command=lambda: self.trigger_tile(4))
        self.t4.place(x=self.game_board[4]["pos_x"], y=self.game_board[4]["pos_y"], height=138, width=138,
                      anchor=CENTER)

        self.t5 = Button(self.canvas, text="PLACE X (5)", command=lambda: self.trigger_tile(5))
        self.t5.place(x=self.game_board[5]["pos_x"], y=self.game_board[5]["pos_y"], height=138, width=138,
                      anchor=CENTER)

        self.t6 = Button(self.canvas, text="PLACE X (6)", command=lambda: self.trigger_tile(6))
        self.t6.place(x=self.game_board[6]["pos_x"], y=self.game_board[6]["pos_y"], height=138, width=138,
                      anchor=CENTER)

        self.t7 = Button(self.canvas, text="PLACE X (7)", command=lambda: self.trigger_tile(7))
        self.t7.place(x=self.game_board[7]["pos_x"], y=self.game_board[7]["pos_y"], height=138, width=138,
                      anchor=CENTER)

        self.t8 = Button(self.canvas, text="PLACE X (8)", command=lambda: self.trigger_tile(8))
        self.t8.place(x=self.game_board[8]["pos_x"], y=self.game_board[8]["pos_y"], height=138, width=138,
                      anchor=CENTER)

    def trigger_tile(self, tile):
        """documentation"""
        self.game_board[tile]["tile"] = self.turn  # Set the tile of the pressed button to the current players' turn.

        # Using the custom functions
        self.destroy_button(tile)
        self.place_image(tile)
        self.change_turn()

    def change_turn(self):
        """If the its 'x''s turn, then change it to 'o''s turn. If its 'o''s turn then change it to 'x''s turn. After
        changing the self.turn variable. It will, try to change the configuration of each button to let it display the
        correct 'PLACE _' on the button. After this, return."""
        if self.turn == "x":
            self.turn = "o"
            try:
                self.t0.config(text="PLACE O")
            except:
                pass
            try:
                self.t1.config(text="PLACE O")
            except:
                pass
            try:
                self.t2.config(text="PLACE O")
            except:
                pass
            try:
                self.t3.config(text="PLACE O")
            except:
                pass
            try:
                self.t4.config(text="PLACE O")
            except:
                pass
            try:
                self.t5.config(text="PLACE O")
            except:
                pass
            try:
                self.t6.config(text="PLACE O")
            except:
                pass
            try:
                self.t7.config(text="PLACE O")
            except:
                pass
            try:
                self.t8.config(text="PLACE O")
            except:
                pass
        elif self.turn == "o":
            self.turn = "x"
            try:
                self.t0.config(text="PLACE X")
            except:
                pass
            try:
                self.t1.config(text="PLACE X")
            except:
                pass
            try:
                self.t2.config(text="PLACE X")
            except:
                pass
            try:
                self.t3.config(text="PLACE X")
            except:
                pass
            try:
                self.t4.config(text="PLACE X")
            except:
                pass
            try:
                self.t5.config(text="PLACE X")
            except:
                pass
            try:
                self.t6.config(text="PLACE X")
            except:
                pass
            try:
                self.t7.config(text="PLACE X")
            except:
                pass
            try:
                self.t8.config(text="PLACE X")
            except:
                pass
        return

    def destroy_button(self, button):
        """Take the button to be destroyed. Then delete the associated button"""
        if button == 0:
            self.t0.destroy()
            return
        elif button == 1:
            self.t1.destroy()
            return
        elif button == 2:
            self.t2.destroy()
            return
        elif button == 3:
            self.t3.destroy()
            return
        elif button == 4:
            self.t4.destroy()
            return
        elif button == 5:
            self.t5.destroy()
            return
        elif button == 6:
            self.t6.destroy()
            return
        elif button == 7:
            self.t7.destroy()
            return
        elif button == 8:
            self.t8.destroy()
            return
        else:
            return

    def place_image(self, tile):
        if self.turn == "x":
            self.canvas.create_image(self.game_board[tile]["pos_x"], self.game_board[tile]["pos_y"], image=self.image_x,
                                     anchor="center")
            return
        elif self.turn == "o":
            self.canvas.create_image(self.game_board[tile]["pos_x"], self.game_board[tile]["pos_y"], image=self.image_o,
                                     anchor="center")
            return
        return


root = Tk()
app = TicTacToe(root)
root.mainloop()
