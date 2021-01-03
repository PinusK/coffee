import sqlite3
import sys
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import *


class MyWidg(QMainWindow):
    def __init__(self, *arg):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(279, 308)
        self.pbt = QPushButton(self)
        self.pbt.setGeometry(QtCore.QRect(180, 220, 75, 23))
        self.pbt.setText('добавить')
        self.lb1 = QLabel(self)
        self.lb1.setGeometry(QtCore.QRect(10, 10, 61, 21))
        self.lb1.setText('сорт')
        self.lb2 = QLabel(self)
        self.lb2.setGeometry(QtCore.QRect(10, 40, 101, 21))
        self.lb2.setText('степень обжарки')
        self.lb3 = QLabel(self)
        self.lb3.setGeometry(QtCore.QRect(0, 80, 91, 21))
        self.lb3.setText('молотый/в зернах')
        self.lb4 = QLabel(self)
        self.lb4.setGeometry(QtCore.QRect(10, 110, 61, 21))
        self.lb4.setText('вкус')
        self.lb5 = QLabel(self)
        self.lb5.setGeometry(QtCore.QRect(10, 140, 61, 21))
        self.lb5.setText('цена')
        self.lb6 = QLabel(self)
        self.lb6.setGeometry(QtCore.QRect(10, 170, 91, 21))
        self.lb6.setText('объем упаковки')
        self.lb7 = QLabel(self)
        self.lb7.setGeometry(QtCore.QRect(10, 220, 161, 21))
        self.lb7.setText('')
        self.comBox = QComboBox(self)
        self.comBox.setGeometry(QtCore.QRect(110, 80, 111, 22))
        self.comBox.addItems(["в зернах", "молотый"])
        self.lE1 = QLineEdit(self)
        self.lE1.setGeometry(QtCore.QRect(110, 10, 113, 20))
        self.lE2 = QLineEdit(self)
        self.lE2.setGeometry(QtCore.QRect(110, 40, 113, 20))
        self.lE3 = QLineEdit(self)
        self.lE3.setGeometry(QtCore.QRect(110, 110, 113, 20))
        self.lE4 = QLineEdit(self)
        self.lE4.setGeometry(QtCore.QRect(110, 110, 113, 20))
        self.lE5 = QLineEdit(self)
        self.lE5.setGeometry(QtCore.QRect(110, 140, 113, 20))
        self.lE6 = QLineEdit(self)
        self.lE6.setGeometry(QtCore.QRect(110, 170, 113, 20))
        self.s = arg[0]
        if arg[1]:
            self.pbt.clicked.connect(self.app)
        else:
            self.pbt.clicked.connect(self.upp)
            self.pbt.setText('Изменить')
            con = sqlite3.connect('coffee.db')
            cur = con.cursor()
            ind = 0
            self.lE1.setText(f'{self.s.tb.item(self.s.row, 1).text()}')
            self.lE2.setText(f'{self.s.tb.item(self.s.row, 2).text()}')
            if self.s.tb.item(self.s.row, 3).text() == 'молотый':
                ind = 1
            self.comBox.setCurrentIndex(ind)
            self.lE4.setText(f'{self.s.tb.item(self.s.row, 4).text()}')
            self.lE5.setText(f'{self.s.tb.item(self.s.row, 5).text()}')
            self.lE6.setText(f'{self.s.tb.item(self.s.row, 6).text()}')
            con.close()

    def app(self):
        tx = self.lE1.text()
        tx1 = self.lE2.text()
        tx2 = self.comBox.currentText()
        tx3 = self.lE4.text()
        tx4 = self.lE5.text()
        tx5 = self.lE6.text()
        if tx == '' or tx1 == '' or tx1.isalpha() or tx2 == '' or\
           tx3 == '' or tx4 == '' or tx4.isalpha() or tx5 == '' or tx5.isalpha():
            self.lb7.setText("Неправильно заполненная форма")
        else:
            con = sqlite3.connect('coffee.db')
            cur = con.cursor()
            z = cur.execute(f"""INSERT INTO coffee('сорт', 'степень_обжарки', 'молотый_в_зернах',
                                                   'вкус', 'цена', 'объем_упаковки')
            VALUES ('{tx}', '{tx1}', '{tx2}', '{tx3}', '{tx4}', '{tx5}')""")
            con.commit()
            cur = con.cursor()
            result = cur.execute("""select * from coffee""").fetchall()
            self.s.tb.setColumnCount(len(result[0]))
            self.s.tb.setRowCount(len(result))
            self.s.tb.setHorizontalHeaderLabels(['id', 'сорт', 'степень_обжарки', 'молотый_в_зернах',
                                                 'вкус', 'цена', 'объем_упаковки'])
            for i in range(len(result)):
                for j in range(len(result[i])):
                    self.s.tb.setItem(i, j, QTableWidgetItem(f'{result[i][j]}'))
            self.s.show()
            con.close()
            self.lb7.setText('')
            self.hide()

    def upp(self):
        tx = self.lE1.text()
        tx1 = self.lE2.text()
        tx2 = self.comBox.currentText()
        tx3 = self.lE4.text()
        tx4 = self.lE5.text()
        tx5 = self.lE6.text()
        if tx == '' or tx1 == '' or tx1.isalpha() or tx2 == '' or\
           tx3 == '' or tx4 == '' or tx4.isalpha() or tx5 == '' or tx5.isalpha():
            self.lb7.setText("Неправильно заполненная форма")
        else:
            con = sqlite3.connect('coffee.db')
            cur = con.cursor()
            id1 = self.s.tb.item(self.s.row, 0).text()
            z = cur.execute(f"""UPDATE coffee
            set сорт = '{tx}', степень_обжарки = '{tx1}',
            молотый_в_зернах = '{tx2}', вкус = '{tx3}',
            цена = '{tx4}', объем_упаковки = '{tx5}'
            where '{id1}' = id""")
            con.commit()
            cur = con.cursor()
            result = cur.execute("""select * from coffee""").fetchall()
            self.s.tb.setColumnCount(len(result[0]))
            self.s.tb.setRowCount(len(result))
            self.s.tb.setHorizontalHeaderLabels(['id', 'сорт', 'степень_обжарки', 'молотый_в_зернах',
                                                 'вкус', 'цена', 'объем_упаковки'])
            for i in range(len(result)):
                for j in range(len(result[i])):
                    self.s.tb.setItem(i, j, QTableWidgetItem(f'{result[i][j]}'))
            self.s.show()
            con.close()
            self.lb7.setText('')
            self.hide()



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(640, 518)
        self.pbt1_1 = QPushButton(self)
        self.pbt1_1.setGeometry(QtCore.QRect(50, 10, 75, 23))
        self.pbt1_1.setText('добавить')
        self.pbt1_1.clicked.connect(self.app_coffee)
        self.pbt1_2 = QPushButton(self)
        self.pbt1_2.setGeometry(QtCore.QRect(140, 10, 75, 23))
        self.pbt1_2.setText('изменить')
        self.pbt1_2.clicked.connect(self.upp_coffee)
        self.pbt1_3 = QPushButton(self)
        self.pbt1_3.setGeometry(QtCore.QRect(220, 10, 75, 23))
        self.pbt1_3.setText('удалить')
        self.pbt1_3.clicked.connect(self.del_coffee)
        self.tb = QTableWidget(self)
        self.tb.setGeometry(QtCore.QRect(20, 40, 581, 391))
        self.lb = QLabel(self)
        self.lb.setGeometry(QtCore.QRect(30, 450, 571, 16))
        self.lb.setText('')


        self.flag = 0

        self.con = sqlite3.connect('coffee.db')

        cur = self.con.cursor()
        result = cur.execute("""select * from coffee""").fetchall()
        self.tb.setColumnCount(len(result[0]))
        self.tb.setRowCount(len(result))
        self.tb.setHorizontalHeaderLabels(['id', 'сорт', 'степень_обжарки', 'молотый_в_зернах',
                                           'вкус', 'цена', 'объем_упаковки'])
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.tb.setItem(i, j, QTableWidgetItem(f'{result[i][j]}'))

        self.tb.cellClicked.connect(self.sign_flag)

    def app_coffee(self):
        self.lb.setText('')
        self.wd = MyWidg(self, 1)
        self.wd.show()

    def upp_coffee(self):
        if self.flag:
            self.lb.setText('')
            self.wd = MyWidg(self, 0)
            self.wd.show()
        else:
            self.lb.setText('Выберете ячейку')

    def del_coffee(self):
        if self.flag:
            valid = QMessageBox.question(
                self, '', "Действительно удалить элемент",
                QMessageBox.Yes, QMessageBox.No)
            if  valid == QMessageBox.Yes:
                self.lb.setText('')
                tx = self.tb.item(self.row, 0).text()
                con = sqlite3.connect('coffee.db')
                cur = con.cursor()
                result = cur.execute(f"""DELETE from coffee
                where id = '{tx}'""")
                con.commit()
                con.close()
                self.con = sqlite3.connect('coffee.db')

                cur = self.con.cursor()
                result = cur.execute("""select * from coffee""").fetchall()
                self.tb.setColumnCount(len(result[0]))
                self.tb.setRowCount(len(result))
                self.tb.setHorizontalHeaderLabels(['id', 'сорт', 'степень_обжарки', 'молотый_в_зернах',
                                                   'вкус', 'цена', 'объем_упаковки'])
                for i in range(len(result)):
                    for j in range(len(result[i])):
                        self.tb.setItem(i, j, QTableWidgetItem(f'{result[i][j]}'))
                self.show()
        else:
            self.lb.setText('Выберете ячейку')

    def sign_flag(self, row, col):
        self.flag = 1
        self.row = row
        self.col = col


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
