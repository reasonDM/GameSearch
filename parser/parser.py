from parse_igropad import Igropad
from parse_playground import Playground
from parse_stopgame import Stopgame
from datetime import datetime

pg = Playground()
sg = Stopgame()
ip = Igropad()


with open("games1.txt", "w", encoding="utf-8") as f:
    for i in range(1, 598):
        games = pg.get_games_by_page(i)
        games = sg.update_games(games)
        games = ip.update_games(games)

        for game in games:
            f.write(
                f"{game.get_name()}\t{','.join(game.cat)}\t{game.get_rate()}\t{game.rate_num}\n"
            )
        print(f"Page {i} done!")
