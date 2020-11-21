import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton



class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)


    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(60, 300, 100, 100)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(200, 60, 120, 120)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(0, 400, 155, 155)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(400, 40, 100, 100)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(250, 200, 90, 90)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(30, 63, 150, 150)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(400, 300, 100, 100)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(392, 400, 90, 90)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(600, 200, 130, 130)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(200, 430, 120, 120)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(500, 500, 70, 70)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

