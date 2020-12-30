import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sqlite3


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('coffee.ui', self)
        self.con = sqlite3.connect('coffee.db')

        cur = self.con.cursor()
        result = cur.execute("""select * from coffee""").fetchall()
        self.tb.setColumnCount(len(result[0]))
        self.tb.setRowCount(len(result))
        print(result)
        self.tb.setHorizontalHeaderLabels(['id', 'сорт', 'степень обжарки', 'молотый\в зернах',
                                           'вкус', 'цена', 'объем упаковки'])
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.tb.setItem(i, j, QTableWidgetItem(f'{result[i][j]}'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
