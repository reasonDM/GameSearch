from window import Window


class Menu(Window):
    def __init__(self, path, wind_name):
        super().__init__(path, wind_name)
        self.form.search_button.clicked.connect(self.open_search)
        self.form.suggest_button.clicked.connect(self.open_suggest)

    def open_search(self):
        Window.gm["search_wind"]["object"].open_wind()
        self.close_wind()

    def open_suggest(self):
        Window.gm["suggest_wind"]["object"].open_wind()
        self.close_wind()
