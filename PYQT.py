import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QApplication
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import Qt, QPoint


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):


        self.setGeometry(500, 150, 900, 700)
        self.setWindowTitle('Расчет величин ei при промывке скважин на глубинах Lн и Lк')
        self.show()

    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawBrushes(qp)
        qp.end()


    def drawBrushes(self, qp):
        brush = QBrush(Qt.NoBrush)
        qp.setBrush(brush)
        qp.drawRect(150, 50, 40, 200)
        qp.drawRect(160, 250, 20, 160)
        qp.drawRect(155, 410, 30, 80)
        qp.drawRect(150, 490, 40, 50)
        qp.drawLine(50, 50, 290, 50)

        brush = QBrush(Qt.BDiagPattern)
        qp.setBrush(brush)
        qp.drawPolygon( QPoint(150, 540), QPoint(170, 560),
                        QPoint(130, 560))
        qp.drawPolygon( QPoint(190, 540), QPoint(170, 560),
                        QPoint(210, 560))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())