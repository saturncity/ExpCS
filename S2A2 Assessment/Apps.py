# TODO: Rename this whole class, I dont think that Apps and Applications are the appropriate variable names.
#  Otherwise, documentation is done.

from os import listdir


class App:
    def __init__(self):
        f"""Accesses the list of apps within the directory of assets/apps. Has the functions:
        \nget_filename(index) = Returns the filename (str) of the index provided.
        \nget_filename_index(filename) = Returns the index (int) of filename provided. (can include .png or just raw""" \
        """ filename.)
        \nget_total_apps() = Returns the length (int) of all files within the assets/apps directory"""
        self.applications = listdir('./assets/apps')
        self.applications.sort()

    def get_filename(self, index):
        """Returns the filename (str) of the index provided."""
        return self.applications[index]

    def get_filename_index(self, filename):
        """Returns the index (int) of filename provided. (can include .png or just raw filename.)"""
        if filename.endswith(".png"):
            return self.applications.index(filename)
        else:
            return self.applications.index(filename + ".png")

    def get_total_apps(self):
        """Returns the length (int) of all files within the assets/apps directory"""
        return len(self.applications)


print("You are meant to start the application by launching the MainWindow.py file!")
