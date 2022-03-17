from tkinter import *


class TicTacToe:
    def __init__(self, root):
        """Hide the root window. Then, define a window with a title. Make a canvas, place the canvas then define the
        background image. Then define the exit and restart buttons. And also define the images for the x, o tiles.
        As well as the x victory background, o victory background and the no victory background. Also define the winning
        patterns and clear the board. Finally, move onto the start function."""
        self.root = root
        self.root.withdraw()
        self.current_window = Toplevel()
        self.current_window.title("TicTacToe")
        self.current_window.geometry("500x524")

        self.canvas = Canvas(self.current_window, width=500, height=524, borderwidth=0, highlightthickness=0)
        self.canvas.pack()

        self.image_tictactoe_background = PhotoImage(file="assets/TicTacToe/tictactoe_background.png")

        self.button_exit = Button(self.canvas, text="Exit", command=self.open_main_window)
        self.button_restart = Button(self.canvas, text="Start Over", command=self.start)

        self.image_x = PhotoImage(file="assets/TicTacToe/image_x.png")
        self.image_o = PhotoImage(file="assets/TicTacToe/image_o.png")

        self.image_victory_x = PhotoImage(file="assets/TicTacToe/x_victory.png")
        self.image_victory_o = PhotoImage(file="assets/TicTacToe/o_victory.png")
        self.image_victory_tie = PhotoImage(file="assets/TicTacToe/no_victory.png")

        # winning combinations
        self.solutions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        self.game_board = []

        self.start()

    def open_main_window(self):
        """Destroy the current window, then create an instance of the MainWindow class."""
        self.current_window.destroy()
        from MainWindow import MainWindow
        MainWindow(self.root)

    def start(self):
        """Clearing the board then move onto the self.show_buttons() function"""
        # place background
        self.canvas.create_image(0, 0, image=self.image_tictactoe_background, anchor="nw")

        # clear all buttons
        for i in range(0, 9):
            self.destroy_button(i)

        # reset board to defaults
        self.game_board = [{"tile": "", "pos_x": 84, "pos_y": 108}, {"tile": "", "pos_x": 250, "pos_y": 108},
                           {"tile": "", "pos_x": 416, "pos_y": 108},
                           {"tile": "", "pos_x": 84, "pos_y": 274}, {"tile": "", "pos_x": 250, "pos_y": 274},
                           {"tile": "", "pos_x": 416, "pos_y": 274},
                           {"tile": "", "pos_x": 84, "pos_y": 436}, {"tile": "", "pos_x": 250, "pos_y": 436},
                           {"tile": "", "pos_x": 416, "pos_y": 436}]

        # starting 'x' turn
        self.turn = "x"

        # begin next function
        self.show_buttons()

    def show_buttons(self, ):
        """Places all buttons. After this function nothing happens in the code until a button is triggered."""
        # place the exit and restart buttons
        self.button_exit.place(x=4, y=4, height=16, width=244)
        self.button_restart.place(x=252, y=4, height=16, width=244)

        # place button at its predefined coords 0 with the command to trigger the tile 0. lambda is used here so that
        # it is possible to provide the command with arguments.
        self.t0 = Button(self.canvas, text="PLACE X", command=lambda: self.trigger_tile(0))
        self.t0.place(x=self.game_board[0]["pos_x"], y=self.game_board[0]["pos_y"], height=138, width=138,
                      anchor=CENTER)

        self.t1 = Button(self.canvas, text="PLACE X", command=lambda: self.trigger_tile(1))
        self.t1.place(x=self.game_board[1]["pos_x"], y=self.game_board[1]["pos_y"], height=138, width=138,
                      anchor=CENTER)

        self.t2 = Button(self.canvas, text="PLACE X", command=lambda: self.trigger_tile(2))
        self.t2.place(x=self.game_board[2]["pos_x"], y=self.game_board[2]["pos_y"], height=138, width=138,
                      anchor=CENTER)

        self.t3 = Button(self.canvas, text="PLACE X", command=lambda: self.trigger_tile(3))
        self.t3.place(x=self.game_board[3]["pos_x"], y=self.game_board[3]["pos_y"], height=138, width=138,
                      anchor=CENTER)

        self.t4 = Button(self.canvas, text="PLACE X", command=lambda: self.trigger_tile(4))
        self.t4.place(x=self.game_board[4]["pos_x"], y=self.game_board[4]["pos_y"], height=138, width=138,
                      anchor=CENTER)

        self.t5 = Button(self.canvas, text="PLACE X", command=lambda: self.trigger_tile(5))
        self.t5.place(x=self.game_board[5]["pos_x"], y=self.game_board[5]["pos_y"], height=138, width=138,
                      anchor=CENTER)

        self.t6 = Button(self.canvas, text="PLACE X", command=lambda: self.trigger_tile(6))
        self.t6.place(x=self.game_board[6]["pos_x"], y=self.game_board[6]["pos_y"], height=138, width=138,
                      anchor=CENTER)

        self.t7 = Button(self.canvas, text="PLACE X", command=lambda: self.trigger_tile(7))
        self.t7.place(x=self.game_board[7]["pos_x"], y=self.game_board[7]["pos_y"], height=138, width=138,
                      anchor=CENTER)

        self.t8 = Button(self.canvas, text="PLACE X", command=lambda: self.trigger_tile(8))
        self.t8.place(x=self.game_board[8]["pos_x"], y=self.game_board[8]["pos_y"], height=138, width=138,
                      anchor=CENTER)
        return

    def trigger_tile(self, tile):
        """When tile is triggered, set the tile to the current player's turn. Then, destroy the button, place the
        respective image there and then change the turn. After that check if a player has won."""
        self.game_board[tile]["tile"] = self.turn  # Set the tile of the pressed button to the current players' turn.

        # using the custom functions
        self.destroy_button(tile)
        self.place_image(tile)
        self.change_turn()

        # check for victory
        self.check_win()

        return

    def change_turn(self):
        """If it is 'x''s turn, then change it to 'o''s turn. If its 'o''s turn then change it to 'x''s turn. After
        changing the self.turn variable. It will, try to change the configuration of each button to let it display the
        correct 'PLACE _' on the button. After this, return."""
        if self.turn == "x":
            # change turns
            self.turn = "o"

            # change text on buttons.
            # in a try and except so that it won't fail when it tries to configure a button that isn't there/
            try:
                self.t0.config(text="PLACE O")
            except TclError:
                pass
            try:
                self.t1.config(text="PLACE O")
            except TclError:
                pass
            try:
                self.t2.config(text="PLACE O")
            except TclError:
                pass
            try:
                self.t3.config(text="PLACE O")
            except TclError:
                pass
            try:
                self.t4.config(text="PLACE O")
            except TclError:
                pass
            try:
                self.t5.config(text="PLACE O")
            except TclError:
                pass
            try:
                self.t6.config(text="PLACE O")
            except TclError:
                pass
            try:
                self.t7.config(text="PLACE O")
            except TclError:
                pass
            try:
                self.t8.config(text="PLACE O")
            except TclError:
                pass
        elif self.turn == "o":
            # change turns
            self.turn = "x"

            # change text on buttons.
            # in a try and except so that it won't fail when it tries to configure a button that isn't there/
            try:
                self.t0.config(text="PLACE X")
            except TclError:
                pass
            try:
                self.t1.config(text="PLACE X")
            except TclError:
                pass
            try:
                self.t2.config(text="PLACE X")
            except TclError:
                pass
            try:
                self.t3.config(text="PLACE X")
            except TclError:
                pass
            try:
                self.t4.config(text="PLACE X")
            except TclError:
                pass
            try:
                self.t5.config(text="PLACE X")
            except TclError:
                pass
            try:
                self.t6.config(text="PLACE X")
            except TclError:
                pass
            try:
                self.t7.config(text="PLACE X")
            except TclError:
                pass
            try:
                self.t8.config(text="PLACE X")
            except TclError:
                pass
        return

    def destroy_button(self, button):
        """Take the button to be destroyed. Then delete the associated button"""
        # again, in a try and except so that it won't fail to delete something that isn't there.
        if button == 0:
            try:
                self.t0.destroy()
            except AttributeError:
                pass
            return
        elif button == 1:
            try:
                self.t1.destroy()
            except AttributeError:
                pass
            return
        elif button == 2:
            try:
                self.t2.destroy()
            except AttributeError:
                pass
            return
        elif button == 3:
            try:
                self.t3.destroy()
            except AttributeError:
                pass
            return
        elif button == 4:
            try:
                self.t4.destroy()
            except AttributeError:
                pass
            return
        elif button == 5:
            try:
                self.t5.destroy()
            except AttributeError:
                pass
            return
        elif button == 6:
            try:
                self.t6.destroy()
            except AttributeError:
                pass
            return
        elif button == 7:
            try:
                self.t7.destroy()
            except AttributeError:
                pass
            return
        elif button == 8:
            try:
                self.t8.destroy()
            except AttributeError:
                pass
            return
        else:
            return

    def place_image(self, tile):
        """Place the current players' PhotoImage on the tile they picked and at the coordinates pre-defined."""
        if self.turn == "x":
            self.canvas.create_image(self.game_board[tile]["pos_x"], self.game_board[tile]["pos_y"], image=self.image_x,
                                     anchor="center")
            return
        elif self.turn == "o":
            self.canvas.create_image(self.game_board[tile]["pos_x"], self.game_board[tile]["pos_y"], image=self.image_o,
                                     anchor="center")
            return
        return

    def check_win(self):
        """First checks for winning solutions from the self.solutions. Then, check for tie by checking if every tile
        is filled."""
        for combo in self.solutions:
            # for each winning combo in the pre-determined solutions.
            if self.game_board[combo[0]]["tile"] == "x" and self.game_board[combo[1]]["tile"] == "x" and \
                    self.game_board[combo[2]]["tile"] == "x":
                # check if all slots are filled by a winning players' tile.
                self.victory("x")
                return
            elif self.game_board[combo[0]]["tile"] == "o" and self.game_board[combo[1]]["tile"] == "o" and \
                    self.game_board[combo[2]]["tile"] == "o":
                self.victory("o")
                return

        # set counter to 0
        counter = 0
        for i in range(0, 9):
            if self.game_board[i]["tile"] != "":
                # if tile is filled then add 1 to counter
                counter = counter + 1
        if counter == 9:
            # if all tiles are filled and there is no win then show the tie screen.
            self.victory("tie")
            return
        return

    def victory(self, winner):
        """Destroys buttons then places an image respective to the arguments provided."""
        # clear buttons
        for i in range(0, 9):
            self.destroy_button(i)

        # if x won
        if winner == "x":
            # show x victory image
            self.canvas.create_image(0, 0, image=self.image_victory_x, anchor="nw")
            return
        elif winner == "o":
            self.canvas.create_image(0, 0, image=self.image_victory_o, anchor="nw")
            return
        elif winner == "tie":
            self.canvas.create_image(0, 0, image=self.image_victory_tie, anchor="nw")
            return
        else:
            return

