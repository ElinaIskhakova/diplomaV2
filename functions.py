
import sys
# Импортируем  интерфейс
from Tablica import *
from Trubi import *
from Plotnost import *
from math import *
from PyQt5 import QtCore, QtGui, QtWidgets
q=0.6
htk=8
pPorodi=2300
Md=1800
pV=1000
K=0.9
g=9.81


def Q1(Dd):
    return floor(q*pi*(Dd/1000)**2/4*1000)


def Q2(Dd, Dok):
    DchasticShlaka = round((0.002 + 0.037 * Dd / 1000), 3)
    v = round(4 * sqrt(DchasticShlaka * (pPorodi - 1200) / 1200), 2)
    kKavern = round(sqrt((2 * htk + Dok) / Dd), 3)
    Doc = round(kKavern * Dd / 1000, 3)
    Skp = round(pi * (Doc ** 2 - ( 147/ 1000) ** 2) / 4, 3)
    Q2 = round(1.15 * v * Skp, 3) * 1000
    return Q2


def Q3():
    Md = 1800
    pV = 1000
    K = 0.9
    Q3 = round(30 * pow(10, -3) * sqrt(Md * pV / (1.8* pow(10, 3) * 1200 * K)), 3) * 1000
    return Q3


def MaxQr(Q1,Q2,Q3):
    Qr = max(Q1, Q2, Q3)
    return Qr

def RaschetPlotnost(GlubinaNapora,DavleniePlasta):
    if GlubinaNapora >= 1200:
        Kb = 1.05
    else:
        Kb = 1.5
    r =  round(ceil((Kb*DavleniePlasta*pow(10,6))/(g*GlubinaNapora))/10)*10
    return r

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
        self.ui.btnPlotnost.clicked.connect(self.on_pushButton_clicked)

        self.dialog = Plotnost(self)
    def on_pushButton_clicked(self):
        try:
            T= RaschetPlotnost(int(self.ui.GlubinaNapora.text()),float(self.ui.DavleniePlasta.text()))
            self.dialog.ui.lineEditPlotnost.setText(str(T))
            Q1text= Q1(float(self.ui.DiametrDolota.text()))
            self.dialog.ui.lineEditQ1.setText(str(Q1text))
            Q2text=Q2(float(self.ui.DiametrDolota.text()),float(self.ui.DiametrKolonni.text()))
            self.dialog.ui.lineEditQ2.setText(str(Q2text))
            Q3text=Q3()
            self.dialog.ui.lineEditQ3.setText(str(Q3text))
            MaxQrtext= MaxQr(Q1text,Q2text,Q3text)
            self.dialog.ui.lineEditQp.setText(str(MaxQrtext))
            self.dialog.show()
        except:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите корректные данные!')
            msg.setIcon(msg.Warning)
            msg.exec()


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())