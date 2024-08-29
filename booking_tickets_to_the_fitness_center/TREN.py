import sys
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDateTimeEdit
from PyQt5.QtCore import QDate, QDateTime, QTime
import sqlite3
from PyQt5.QtGui import QPixmap

from OPL import Opl


class Tren(QMainWindow):
    def __init__(self, idu):
        super().__init__()
        uic.loadUi('Тренажерный зал.ui', self)

        self.con = sqlite3.connect('db111.db')
        cur = self.con.cursor()
        query = 'SELECT id, title, price, count FROM zal WHERE id=?'
        self.n = cur.execute(query, (idu,)).fetchall()[0]
        self.textEdit_30.append(self.n[1])
        self.k = 0.0

        val = self.textEdit_30.toPlainText()
        if val == "Ледовая Арена":
            self.label_2.setPixmap(QPixmap('ЛД.png'))
        if val == "Большой зал":
            self.label_2.setPixmap(QPixmap('БЗ.png'))
        if val == "Теннисный зал":
            self.label_2.setPixmap(QPixmap('НТ.png'))
        if val == "Тренажерный зал":
            self.label_2.setPixmap(QPixmap('ТЗ.png'))

        self.pushButton_3.clicked.connect(self.opl)
        self.pushButton_4.clicked.connect(self.nas)
        self.pushButton_2.clicked.connect(self.opl1)
        self.label_47.setText(f"Осталось мест: {self.n[3]}")

    def opl1(self):
        self.col_vo = int(self.spinBox_73.text())
        self.vrema = list(map(lambda x: int(x), self.vrema_73.text().split(":")))
        self.vr = self.vrema_73.text()
        self.data = self.data_73.text()
        self.k = 0
        if self.col_vo > self.n[3]:
            self.textEdit_32.setText("Превышение ограничения по кол-ву человек")
        else:
            self.label_47.setText(f"Осталось мест: {self.n[3]}")
            self.k = self.col_vo * self.n[2] * self.vrema[0] + (self.vrema[1] // 1.7)
            self.a = str(self.k) + "руб."
            if self.k != 0.0:
                self.textEdit_32.clear()
                self.textEdit_32.append(self.a)
                print(self.a)
            else:
                pass

    def opl(self):
        if self.k != 0.0:
            self.op = Opl(self.n[0], self.col_vo, self.k, self.vr, self.data, self.n[1])
            self.op.show()
        else:
            pass

    def mousePressEvent(self, event):
        if (event.button() == Qt.LeftButton):
            self.label.setText('Сначала нужно посчитать стоимость')

    def nas(self):
        self.hide()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
