import requests
from bs4 import BeautifulSoup



class Stopgame:
    URL = "https://stopgame.ru/"

    def update_game(self, game):
        request = requests.get(Stopgame.URL+"search",params={"s":game.get_name(), "where": "games"})
        # print(request.text)
        soup = BeautifulSoup(request.text, "html.parser")
        try:
            rate_sg = float(soup.find("div", {"data-key":"0"}).find("span", class_="_users-rating__total_sh7r2_1").text) * 2
            rate_kol = int(soup.find("div", {"data-key":"0"}).find("span", class_="_users-rating__count_sh7r2_1").text[0: -7].replace("\xa0", ""))
            # print(rate_sg, rate_kol, game.rate, game.rate_num)
            game.set_rate(round((rate_sg*rate_kol + game.get_rate()*game.rate_num)/(rate_kol+game.rate_num), 1))
            game.rate_num += rate_kol
            cat_sg = soup.find("div", {"data-key":"0"}).findAll("div", class_="_info-grid__value_sh7r2_200")[1].findAll("a")

            for cat in cat_sg[:2]:
                text = cat.text
                if text == "Экшн":
                    text = "Экшен"
                if text not in game.cat:
                    game.cat.append(text)
        except:
            pass
        return game

    def update_games(self, games):
        for i in range(len(games)):
            try:
                games[i] = self.update_game(games[i])
            except:
                pass

        return games



