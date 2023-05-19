from app.window import Window


class Suggest(Window):
    def __init__(self, path, wind_name):
        super().__init__(path, wind_name)
        self.form.suggestBack.clicked.connect(self.close_search)
        print(self.all_cats())

    def close_search(self):
        Window.gm["Menu_wind"]["object"].open_wind()
        self.close_wind()

    def all_cats(self):
        all_cats = []
        for i in range(len(self.readlines)):
            all_cats += self.readlines[i][1].split(",")
        print(set(all_cats))
