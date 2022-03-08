# TODO: Implement cursor tracking everywhere and clicking to remove the need for buttons.

from tkinter import *


class TestWindow:  # cursor tracking test
    def __init__(self, root):
        self.root = root
        self.root.withdraw()
        self.current_window = Toplevel()
        self.current_window.title("Test Window")

        self.img = PhotoImage(file="../OOP/GUI_Intro/python.png")
        self.canvas = Canvas(self.current_window, width=1000, height=1000)
        self.create_img = self.canvas.create_image(200, 100, image=self.img)
        self.canvas.pack()
        self.canvas.bind('<Motion>', self.mouse_coords)

    def mouse_coords(self, event):
        print(f"({event.x}, {event.y})")
        self.canvas.coords(self.create_img, event.x, event.y)

# class TestWindow:
#     def __init__(self, root):
#             self.root = root
#             self.root.withdraw()
#             self.current_window = Toplevel()
#             self.current_window.title("Test Window")

root = Tk()
app = TestWindow(root)
root.mainloop()