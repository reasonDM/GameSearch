from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QMessageBox

from app.Menu import Menu
from app.search import Search
from app.suggest import Suggest


win = QApplication([])
wind_suggest = Suggest("designers/Menu.ui", "suggest_wind")
wind_search = Search("designers/search.ui", "search_wind")
wind_menu = Menu("designers/face.ui", "Menu_wind")
wind_menu.open_wind()
win.exec()

