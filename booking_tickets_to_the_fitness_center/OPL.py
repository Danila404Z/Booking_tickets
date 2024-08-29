import sys
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDateTimeEdit, QFileDialog
from PyQt5.QtCore import QDate, QDateTime, QTime
import sqlite3


class Opl(QMainWindow):
    def __init__(self, id, count, stoem, vr, dt, title):
        super().__init__()
        uic.loadUi('Оплата.ui', self)
        self.pushButton_2.clicked.connect(self.pro)
        self.pushButton.clicked.connect(self.nas)
        self.pushButton_3.clicked.connect(self.check)
        self.id = id
        self.count = count
        self.title = title
        self.stoem = stoem
        self.dt = dt
        self.vr = vr
        self.v = str(self.stoem) + "руб."
        self.textEdit_33.append(self.v)
        self.cons = sqlite3.connect('db111.db')
        curs = self.cons.cursor()
        cur = self.cons.cursor()

    def nas(self):
        self.hide()

    def pro(self):
        res = 0
        count = 0
        count1 = 0
        g = self.textEdit.toPlainText()
        for i in g:
            if int(i) % 2 == 0:
                res = (int(i) * 2)
                if res > 9:
                    count += res - 9
                else:
                    count += res
            else:
                count1 += int(i)
        if (count + count1) % 10 == 0 and len(g) == 16:
            self.label_4.setText("Успешно!")
        else:
            self.label_4.setText("Номер карты неправильный!")

        if self.label_4.text() == "Успешно!":
            self.label_3.setText('Ваш чек:')
            self.label_5.setText('------------------\n'
                                 f'Дата: {self.dt}\n'
                                 f'Билет в: {self.title}\n'
                                 f'Продолжительность: {self.vr}\n'
                                 f'Кол-во человек: {self.count}\n'
                                 'Оплата по карте\n'
                                 '------------------\n'
                                 f'Итого: {self.stoem}руб.\n'
                                 '------------------')

            curs = self.cons.cursor()
            querys = f'INSERT INTO save(namber, pr) VALUES("{g}","{self.v}")'
            curs.execute(querys)
            self.cons.commit()
            cur = self.cons.cursor()
            query = 'UPDATE zal SET count=(SELECT count FROM zal WHERE id = ?)-? WHERE id = ?'
            cur.execute(query, (self.id, self.count, self.id))
            self.cons.commit()
        else:
            pass

    def check(self):
        if self.label_4.text() == "Успешно!":
            n = QFileDialog().getSaveFileName(self, 'Сохранить', '../', 'txt(*.txt)')[0]
            if not n:
                pass
            else:
                with open(n, 'w') as file:
                    file.write('------------------\n')
                    file.write(f'Дата: {self.dt}\n')
                    file.write(f'Билет в: {self.title}\n')
                    file.write(f'Продолжительность: {self.vr}\n')
                    file.write(f'Кол-во человек: {self.count}\n')
                    file.write('Оплата по карте\n')
                    file.write('------------------\n')
                    file.write(f'Итого: {self.stoem}руб.\n')
                    file.write('------------------')
        else:
            pass

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.label_6.setText('Введите карту и нажмине "Бронь"')

