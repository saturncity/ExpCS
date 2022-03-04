#  do not grade this i was just testing cursor tracking

from tkinter import *


class TestWindow:
    def __init__(self, root):
        self.root = root
        self.root.withdraw()
        self.current_window = Toplevel()
        self.current_window.title("Test Window")

        self.img = PhotoImage(file="C:/Users/Jason Aaren Lenz/pycharmProjects/ExpCS/OOP/GUI_Intro/python.png")
        self.canvas = Canvas(self.current_window, width=500, height=500)
        self.create_img = self.canvas.create_image(200, 100, image=self.img)
        self.canvas.pack()
        self.canvas.bind('<Motion>', self.mouse_coords)

    def mouse_coords(self, event):
        print(f"({event.x}, {event.y})")
        self.canvas.coords(self.create_img, event.x, event.y)


root = Tk()
app = TestWindow(root)
root.mainloop()

# from tkinter import *
#
# def Mousecoords(event):
#     pointxy = (event.x, event.y) # get the mouse position from event
#     print(pointxy)
#     canvas.coords(cimg, pointxy) # move the image to mouse postion
#
# root = Tk()
# img = PhotoImage(file="C:/Users/Jason Aaren Lenz/pycharmProjects/ExpCS/OOP/GUI_Intro/python.png")
# canvas = Canvas(width=1000, height=1000)
# cimg = canvas.create_image(200, 100, image=img)
# canvas.pack()
# canvas.bind('<Motion>', Mousecoords) # track mouse movement
# root.mainloop()
