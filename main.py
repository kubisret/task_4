import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect("coffee.sqlite")
        self.pushButton.clicked.connect(self.select_data)

    def select_data(self):
        cur = self.connection.cursor()
        res = cur.execute('''
        SELECT name_sort, stepen, value, text, cene, v
        FROM coffee
        ''')

        name_title = ["название сорта", "степень обжарки", "молотый/в зернах"
                                                    "описание вкуса", "цена", "объем упаковки"]
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(name_title)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1)

        # Заполним размеры таблицы
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        # Заполняем таблицу элементами
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())