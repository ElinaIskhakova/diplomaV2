import sys
from Plotnost import *
from PyQt5 import QtCore, QtGui, QtWidgets
import LBTS311
import  KodTurbobura37 as KT
from math import pi,floor,sqrt,pow
q=0.6
htk=8
pPorodi=2300

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent= None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.Q1)
    def Q1(self):
        self.ui.lineEditQ1.setText(str(floor(q*pi*(Dd/1000)**2/4*1000)))
       # return floor(q*pi*(Dd/1000)**2/4*1000)
    def Q2(Dd,Dok):
        DchasticShlaka=round((0.002+0.037*Dd/1000),3)
        v=round(4*sqrt(DchasticShlaka*(pPorodi-1200)/1200),2)
        kKavern=round(sqrt((2*htk+Dok)/Dd),3)
        Doc=round(kKavern*Dd/1000,3)
        Skp=round(pi*(Doc**2-(LBTS311.dn/1000)**2)/4,3)
        Q2=round(1.15*v*Skp,3)*1000
        #return Q2
    def Q3():
        Md=1800
        pV=1000
        K=0.9
        Q3 = round(30 * pow(10, -3) * sqrt(Md * pV / (KT.Ms * pow(10, 3) * 1200 * K)),3)*1000
        return  Q3
    def MaxQr():
        Qr=max(Q1(269.9),Q2(269.9,279),Q3())
        return Qr


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())