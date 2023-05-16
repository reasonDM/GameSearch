from PyQt6.QtWidgets import QTableWidgetItem

from app.window import Window


class Search(Window):

    def __init__(self, path, wind_name):
        super().__init__(path, wind_name)
        self.form.searchBack.clicked.connect(self.close_search)
        # self.file = open("parser/games.txt", encoding='utf-8')
        # self.readlines = self.file.readlines()
        # for i in range(len(self.readlines)):
        #     self.readlines[i] = self.readlines[i].strip().split("\t")

        self.form.lineEdit.textChanged.connect(self.search)
        self.form.rate_button.clicked.connect(self.sort_rate)
        self.form.alf_button.clicked.connect(self.alf_sort)
        self.form.rate_numButton.clicked.connect(self.sortNum_rate)
        print(self.all_cats())
        self.form.comboBox.currentIndexChanged.connect(self.search)



    def close_search(self):
        Window.gm["Menu_wind"]["object"].open_wind()
        self.close_wind()

    def search(self):
        search_res = self.form.lineEdit.text()
        max_games = 1000
        n = 0
        if search_res == "":
            self.form.tableWidget.setRowCount(max_games)
            for i in range(len(self.readlines)):
                if self.readlines[i][1].lower().find(self.form.comboBox.currentText().lower()) != -1 or self.form.comboBox.currentText().lower() == "все":
                    name = self.readlines[i][0]
                    item = QTableWidgetItem(name)
                    self.form.tableWidget.setItem(n, 0, item)
                    cat = self.readlines[i][1]
                    item = QTableWidgetItem(cat)
                    self.form.tableWidget.setItem(n, 1, item)
                    rate = self.readlines[i][2]
                    item = QTableWidgetItem(rate)
                    self.form.tableWidget.setItem(n, 2, item)
                    rate_num = self.readlines[i][3]
                    item = QTableWidgetItem(rate_num)
                    self.form.tableWidget.setItem(n, 3, item)
                    n += 1
                    max_games -= 1
                if max_games == 0:
                    break
        else:
            max_games = 1000
            n = 0
            self.form.tableWidget.setRowCount(max_games)
            for i in range(len(self.readlines)):
                if self.readlines[i][0].lower().find(search_res.lower()) != -1 and (self.readlines[i][1].lower().find(self.form.comboBox.currentText().lower()) != -1 or self.form.comboBox.currentText().lower() == "все"):
                    name = self.readlines[i][0]
                    item = QTableWidgetItem(name)
                    self.form.tableWidget.setItem(n, 0, item)
                    cat = self.readlines[i][1]
                    item = QTableWidgetItem(cat)
                    self.form.tableWidget.setItem(n, 1, item)
                    rate = self.readlines[i][2]
                    item = QTableWidgetItem(rate)
                    self.form.tableWidget.setItem(n, 2, item)
                    rate_num = self.readlines[i][3]
                    item = QTableWidgetItem(rate_num)
                    self.form.tableWidget.setItem(n, 3, item)
                    n+=1
            self.form.tableWidget.setRowCount(n)

    def sort_rate(self):
        search_res = self.form.lineEdit.text()
        max_games = 1000
        join = []
        if search_res == "":
            for i in range(len(self.readlines)):
                if self.readlines[i][1].lower().find(
                    self.form.comboBox.currentText().lower()) != -1 or self.form.comboBox.currentText().lower() == "все":
                    join.append(self.readlines[i])

        else:
            max_games = 1000
            n = 0
            for i in range(len(self.readlines)):
                if self.readlines[i][0].lower().find(search_res.lower()) != -1 and (self.readlines[i][1].lower().find(self.form.comboBox.currentText().lower()) != -1 or self.form.comboBox.currentText().lower() == "все"):
                    join.append(self.readlines[i])
                    n += 1
        join.sort(key = lambda x: -float(x[2]))
        self.form.tableWidget.setRowCount(len(join))
        for i in range(len(join)):
            name = join[i][0]
            item = QTableWidgetItem(name)
            self.form.tableWidget.setItem(i, 0, item)
            cat = join[i][1]
            item = QTableWidgetItem(cat)
            self.form.tableWidget.setItem(i, 1, item)
            rate = join[i][2]
            item = QTableWidgetItem(rate)
            self.form.tableWidget.setItem(i, 2, item)
            rate_num = join[i][3]
            item = QTableWidgetItem(rate_num)
            self.form.tableWidget.setItem(i, 3, item)

    def alf_sort(self):
        search_res = self.form.lineEdit.text()
        max_games = 1000
        join = []
        if search_res == "":
            for i in range(len(self.readlines)):
                if self.readlines[i][1].lower().find(
                        self.form.comboBox.currentText().lower()) != -1 or self.form.comboBox.currentText().lower() == "все":
                    join.append(self.readlines[i])

        else:
            max_games = 1000
            n = 0
            for i in range(len(self.readlines)):
                if self.readlines[i][0].lower().find(search_res.lower()) != -1 and (self.readlines[i][1].lower().find(self.form.comboBox.currentText().lower()) != -1 or self.form.comboBox.currentText().lower() == "все"):
                    join.append(self.readlines[i])
                    n += 1
        join.sort(key=lambda x: x[0])
        self.form.tableWidget.setRowCount(len(join))
        for i in range(len(join)):
            name = join[i][0]
            item = QTableWidgetItem(name)
            self.form.tableWidget.setItem(i, 0, item)
            cat = join[i][1]
            item = QTableWidgetItem(cat)
            self.form.tableWidget.setItem(i, 1, item)
            rate = join[i][2]
            item = QTableWidgetItem(rate)
            self.form.tableWidget.setItem(i, 2, item)
            rate_num = join[i][3]
            item = QTableWidgetItem(rate_num)
            self.form.tableWidget.setItem(i, 3, item)

    def sortNum_rate(self):
        search_res = self.form.lineEdit.text()
        max_games = 1000
        join2 = []
        if search_res == "":
            for i in range(len(self.readlines)):
                if self.readlines[i][1].lower().find(
                        self.form.comboBox.currentText().lower()) != -1 or self.form.comboBox.currentText().lower() == "все":
                    join2.append(self.readlines[i])

        else:
            max_games = 1000
            n = 0
            for i in range(len(self.readlines)):
                if self.readlines[i][0].lower().find(search_res.lower()) != -1 and (self.readlines[i][1].lower().find(self.form.comboBox.currentText().lower()) != -1 or self.form.comboBox.currentText().lower() == "все"):
                    join2.append(self.readlines[i])
                    n += 1
        join2.sort(key = lambda x: -int(x[3]))
        self.form.tableWidget.setRowCount(len(join2))
        for i in range(len(join2)):
            name = join2[i][0]
            item = QTableWidgetItem(name)
            self.form.tableWidget.setItem(i, 0, item)
            cat = join2[i][1]
            item = QTableWidgetItem(cat)
            self.form.tableWidget.setItem(i, 1, item)
            rate = join2[i][2]
            item = QTableWidgetItem(rate)
            self.form.tableWidget.setItem(i, 2, item)
            rate_num = join2[i][3]
            item = QTableWidgetItem(rate_num)
            self.form.tableWidget.setItem(i, 3, item)

    def all_cats(self):
        allCats = []
        for i in range(len(self.readlines)):
            allCats += self.readlines[i][1].split(",")
        allCats = ["Все"] + sorted(list(set(allCats)))
        self.form.comboBox.addItems(allCats)

    def choose_cat(self):
        max_games = 1000
        join_cat = []
        n = 0
        self.form.tableWidget.setRowCount(max_games)
        for i in range(len(self.readlines)):
            if self.readlines[i][1].lower().find(self.form.comboBox.currentText().lower()) != -1 or self.form.comboBox.currentText().lower() == "все":
                name = self.readlines[i][0]
                item = QTableWidgetItem(name)
                self.form.tableWidget.setItem(n, 0, item)
                cat = self.readlines[i][1]
                item = QTableWidgetItem(cat)
                self.form.tableWidget.setItem(n, 1, item)
                rate = self.readlines[i][2]
                item = QTableWidgetItem(rate)
                self.form.tableWidget.setItem(n, 2, item)
                rate_num = self.readlines[i][3]
                item = QTableWidgetItem(rate_num)
                self.form.tableWidget.setItem(n, 3, item)
                n+=1
            if n == 1000:
                break

        self.form.tableWidget.setRowCount(n)







