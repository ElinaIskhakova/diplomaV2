# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Plotnost.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class PlUi_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(482, 328)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelRaschetPlotn = QtWidgets.QLabel(self.centralwidget)
        self.labelRaschetPlotn.setGeometry(QtCore.QRect(30, 40, 141, 16))
        self.labelRaschetPlotn.setObjectName("labelRaschetPlotn")
        self.lineEditPlotnost = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPlotnost.setEnabled(False)
        self.lineEditPlotnost.setGeometry(QtCore.QRect(170, 40, 113, 20))
        self.lineEditPlotnost.setObjectName("lineEditPlotnost")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 70, 41, 21))
        self.label.setObjectName("label")
        self.lineEditQ1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditQ1.setEnabled(False)
        self.lineEditQ1.setGeometry(QtCore.QRect(170, 70, 113, 20))
        self.lineEditQ1.setObjectName("lineEditQ1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 41, 21))
        self.label_2.setObjectName("label_2")
        self.lineEditQ2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditQ2.setEnabled(False)
        self.lineEditQ2.setGeometry(QtCore.QRect(170, 100, 113, 20))
        self.lineEditQ2.setObjectName("lineEditQ2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 51, 21))
        self.label_3.setObjectName("label_3")
        self.lineEditQ3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditQ3.setEnabled(False)
        self.lineEditQ3.setGeometry(QtCore.QRect(170, 130, 113, 20))
        self.lineEditQ3.setObjectName("lineEditQ3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 31, 31))
        self.label_4.setObjectName("label_4")
        self.lineEditQp = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditQp.setEnabled(False)
        self.lineEditQp.setGeometry(QtCore.QRect(170, 160, 113, 20))
        self.lineEditQp.setObjectName("lineEditQp")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 482, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Выбор плотности и предварительной подачи насосов"))
        self.labelRaschetPlotn.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Расчетная плотность:</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Q</span><span style=\" font-size:10pt; vertical-align:sub;\">1</span><span style=\" font-size:10pt;\">:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Q</span><span style=\" font-size:10pt; vertical-align:sub;\">2</span><span style=\" font-size:10pt;\">:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Q</span><span style=\" font-size:10pt; vertical-align:sub;\">3</span><span style=\" font-size:10pt;\">:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Q</span><span style=\" font-size:10pt; vertical-align:sub;\">p:</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Вычислить"))