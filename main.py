import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect("coffee.sqlite")

        self.push_get.clicked.connect(self.select_data)
        self.pushButton_add.clicked.connect(self.add_data)
        self.pushButton_up.clicked.connect(self.up_data)
        self.pushButton_del.clicked.connect(self.del_data)

    def select_data(self):
        cur = self.connection.cursor()
        res = cur.execute('''
        SELECT *
        FROM coffee
        ''')

        name_title = ["id", "название сорта", "степень обжарки", "молотый/в зернах",
                      "описание вкуса", "цена", "объем упаковки"]
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(name_title)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1)

        # Заполняем таблицу элементами
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def add_data(self):
        self.form = Form(self, None)
        self.form.add()
        self.form.show()

    def up_data(self):
        try:
            row_items = []
            index = self.tableWidget.selectedIndexes()
            id = self.tableWidget.model().data(index[0])
            title_sort = self.tableWidget.model().data(index[1])
            stepen_obj = self.tableWidget.model().data(index[2])
            val = self.tableWidget.model().data(index[3])
            sence = self.tableWidget.model().data(index[4])
            cena = self.tableWidget.model().data(index[5])
            v = self.tableWidget.model().data(index[6])
            row_items.append(title_sort)
            row_items.append(stepen_obj)
            row_items.append(val)
            row_items.append(sence)
            row_items.append(cena)
            row_items.append(v)
            if id:
                self.form = Form(self, row_items)
                self.form.up()
                self.form.show()
        except IndexError:
            pass

    def del_data(self):
        try:
            index = self.tableWidget.selectedIndexes()
            id = self.tableWidget.model().data(index[0])
            if id:
                cur = self.connection.cursor()
                cur.execute('''
                        DELETE
                        FROM coffee
                        WHERE ID = ?
                        ''', (id,))
                self.connection.commit()
                self.select_data()
        except IndexError:
            pass


class Form(QDialog):
    def __init__(self, main, row_items):
        super().__init__()
        if row_items is not None:
            self.row_items = row_items
        self.self_main = main
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.connection = sqlite3.connect("coffee.sqlite")

    def add(self):
        self.pushButton_ok.clicked.connect(self.add_data)

    def add_data(self):
        name_sort = self.lineEdit_sort.text()
        stepen = self.lineEdit_stepen.text()
        value = self.comboBox.currentText()
        text = self.lineEdit_text.text()
        cene = self.lineEdit_cene.text()
        v = self.lineEdit_v.text()

        cur = self.connection.cursor()
        cur.execute('''
        INSERT INTO coffee(name_sort,stepen,value,text,cene,v) VALUES(?,?,?,?,?,?)
        ''', (name_sort, stepen, value, text, cene, v))
        self.connection.commit()

        self.self_main.select_data()
        self.close()

    def up(self):
        self.pushButton_ok.clicked.connect(self.up_data)
        self.lineEdit_sort.setText(self.row_items[0])
        self.lineEdit_stepen.setText(self.row_items[1])
        self.lineEdit_text.setText(self.row_items[3])
        self.lineEdit_cene.setText(self.row_items[4])
        self.lineEdit_v.setText(self.row_items[5])

    def up_data(self):
        index = self.self_main.tableWidget.selectedIndexes()
        id = self.self_main.tableWidget.model().data(index[0])

        name_sort = self.lineEdit_sort.text()
        stepen = self.lineEdit_stepen.text()
        value = self.comboBox.currentText()
        text = self.lineEdit_text.text()
        cene = self.lineEdit_cene.text()
        v = self.lineEdit_v.text()

        cur = self.connection.cursor()
        cur.execute('''
                UPDATE coffee
                SET name_sort = ?, stepen = ?, value = ?, text = ?, cene = ?, v = ?
                WHERE ID = ?
                ''', (name_sort, stepen, value, text, cene, v, id))
        self.connection.commit()

        self.self_main.select_data()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())