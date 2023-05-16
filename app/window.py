from PyQt6 import uic

from others.generate_paths import resource_path


class Window:
    gm = {}

    def __init__(self, path, wind_name):
        Form, Windows = uic.loadUiType(path)
        self.windows = Windows()
        self.form = Form()
        self.form.setupUi(self.windows)
        Window.gm[wind_name] = {"windows" : self.windows, "form" : self.form, "object": self }
        self.file = open("parser/games.txt", encoding='utf-8')
        self.readlines = self.file.readlines()
        for i in range(len(self.readlines)):
            self.readlines[i] = self.readlines[i].strip().split("\t")

    def open_wind(self):

        self.windows.show()


    def close_wind(self):

        self.windows.hide()





