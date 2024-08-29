import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from TREN import Tren


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Главная страница.ui', self)
        self.pushButton_2.clicked.connect(self.zup)

    def zup(self):
        value = self.comboBox_3.currentText()
        if value == "Ледовая Арена":
            self.ru = Tren(1)
            self.ru.show()
        if value == "Большой зал":
            self.ru = Tren(2)
            self.ru.show()
        if value == "Теннисный зал":
            self.ru = Tren(3)
            self.ru.show()
        if value == "Тренажерный зал":
            self.ru = Tren(4)
            self.ru.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
