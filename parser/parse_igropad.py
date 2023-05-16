import requests
from bs4 import BeautifulSoup


class Igropad:
    URL = "https://igropad.com"

    def update_game(self, game):
        request = requests.get(Igropad.URL+"/ru/search",params={"q":game.get_name().lower().replace(" ", "+"), "submit": "Найти"})
        # print(request.text)
        soup = BeautifulSoup(request.text, "html.parser")
        try:
            sub_URL = soup.find("div", class_="fields").find("h2", class_="field title f_title").find("a").get("href")
            request = requests.get(Igropad.URL+sub_URL)
            soup = BeautifulSoup(request.text, "html.parser")
            rate_ip = float(soup.find("div", class_= "rating_info_score good").text)
            rate_kol = int(soup.find("div", class_="rating_info_count").text[1:-1])
            # print(rate_ip, rate_kol)
            game.set_rate(round((rate_ip*rate_kol + game.get_rate()*game.rate_num)/(rate_kol+game.rate_num), 1))
            game.rate_num += rate_kol
            cat_ip = soup.findAll("div", class_="listbitmask_autolink games_genre")


            for cat in cat_ip[:2]:
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
                games[i] = self.update_game((games[i]))
            except:
                pass
        return games


