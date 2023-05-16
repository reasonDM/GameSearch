

class Game:

    def __init__(self, name, cat, rate, rate_num, image = None):
        self.__name = name
        self.cat = cat
        self.__rate = rate
        self.rate_num = rate_num
        self.image = image

    def set_rate(self, rate):
        if rate > 10 or rate <0:
            raise ValueError(f"Неверное значение рейтинга, {rate}")
        else:
            self.__rate = rate

    def get_rate(self):
        return self.__rate


    def get_info(self):
        return f"Название игры {self.__name}, оценка игры {self.__rate} ({self.rate_num}), категории игры {self.cat}"

    def __repr__(self):
        return self.__name

    def get_name(self):
        return self.__name








