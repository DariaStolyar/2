import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        a = self.lineEdit.text()
        db_name = "coffee.sqlite"
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM coffee
        WHERE id = ?""", (a,)).fetchall()
        self.label_2.setText("Сорт: " + result[0][1] + "\
        \nОбжарка: " + result[0][2] + "\
        \nТип: " + result[0][3] + "\
        \nВкус: " + result[0][4] + "\
        \nЦена: " + str(result[0][5]) + "\
        \nВес: " + str(result[0][6]))
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())