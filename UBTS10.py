import sys
from Trubi import *
from math import pow,ceil
from PyQt5 import QtCore, QtGui, QtWidgets

#dn=203
#dm=203
#delta=56.5
#l0=9
#lm=0
#Km=1.05
class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent= None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.ButtonRaschet.clicked.connect(self.Diametr)

    def Diametr(self):
        dn= int(self.ui.DiametrNaruzh1.text())
        delta = float(self.ui.Tolshina1.text())
        db=(dn-2*delta)/1000
        self.ui.VnutrneniyDiametr1.setText(str(db))



if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())