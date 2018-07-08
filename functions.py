
import sys
# Импортируем  интерфейс
from Tablica import *
from Trubi import *
from Plotnost import *
from math import pow,ceil
from PyQt5 import QtCore, QtGui, QtWidgets
g=9.81


class Plotnost(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = PlUi_MainWindow()
        self.ui.setupUi(self)


class Truba(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = TrUi_MainWindow()
        self.ui.setupUi(self)


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent= None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Начало кода:
        self.ui.TrubiOpisanie.clicked.connect(self.on_pushButton_clicked)
        self.dialog = Truba(self)
    def on_pushButton_clicked(self):
        self.dialog.show()

        self.ui. btnPlotnost.clicked.connect(self.on_pushButton1_clicked)
        self.dialog1 = Plotnost(self)

    def on_pushButton1_clicked(self):
        self.dialog1.show()


    def openWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        seld.ui.setupUi(self.window)
        self.window.show()
    # функция которая выполняется при нажатии на кнопку 
    def getPlotnost(self):
        try:
            GlubinaNapora = int(self.ui.GlubinaNapora.text())
            if GlubinaNapora>=1200:
                Kb=1.05
            else:
                Kb=1.5
            DavleniePlasta = float(self.ui.DavleniePlasta.text())
            r = round(ceil((Kb*DavleniePlasta*pow(10,6))/(g*GlubinaNapora))/10)*10
           # DiametrDolota=float(self.ui.DiametrDolota.text())
            #self.ui.Plotnost.setText(str(r))
          #  Q1(int(self.ui.DiametrDolota.text()))
        except:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите корректные данные!')
            msg.setIcon(msg.Warning)
            msg.exec()     

        # Конец кода

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())