import sys
# Импортируем  интерфейс
from mainwindow import *
from math import pow
from PyQt5 import QtCore, QtGui, QtWidgets

g = 9.81


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Начало кода:
        self.ui.btnResult.clicked.connect(self.getPlotnost)

    # функция которая выполняется при нажатии на кнопку
    def getPlotnost(self):
        try:
            GlubinaNapora = int(self.ui.GlubinaNapora.text())
            if GlubinaNapora >= 1200:
                Kb = 1.05
            else:
                Kb = 1.5
            DavleniePlasta = int(self.ui.DavleniePlasta.text())
            r = round((Kb * DavleniePlasta * pow(10, 6)) / (g * GlubinaNapora), 1)
            self.ui.Plotnost.setText(str(r))
        except:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите корректные данные!')
            msg.setIcon(msg.Warning)
            msg.exec()

            # Конец кода


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())