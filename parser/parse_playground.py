import requests
from bs4 import BeautifulSoup

from app.game import Game


class Playground:
    URL = "https://www.playground.ru/games?release=all&sort=user&p={}"

    def get_games_by_page(self, page):
        request = requests.get(Playground.URL.format(page))
        # print(request.url)
        soup = BeautifulSoup(request.text, "html.parser")
        games = []
        for item in soup.findAll("div", class_="item"):
            try:
                name = item.find("div", class_="info").find("div", class_="media-heading title").text.strip().replace(":", "").replace(".", "").replace(",","").replace(";", "").replace("/", "")
                cats = item.find("div", class_="info").find("div", class_="meta-info").findAll("a")
                if len(cats) < 2:
                    cat1 = [cats[0].text]
                else:
                    cat1 = [cats[0].text, cats[1].text]

                rate = float(item.find("div", class_="info").find("div", class_="footer").find("span", class_="value js-game-rating-value").text)
                rate_num = int(item.find("div", class_="info").find("div", class_="footer").find("span", class_="js-game-rating-count").text.replace(" ", ""))

                games.append(Game(name, cat1, rate, rate_num))
            except:
                pass

        return games