# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(843, 1125)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralWidget)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, -494, 810, 1605))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.GlubinaNachala = QtWidgets.QLineEdit(self.groupBox)
        self.GlubinaNachala.setObjectName("GlubinaNachala")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.GlubinaNachala)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.GlubinaKontsa = QtWidgets.QLineEdit(self.groupBox)
        self.GlubinaKontsa.setObjectName("GlubinaKontsa")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.GlubinaKontsa)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.GlubinaNapora = QtWidgets.QLineEdit(self.groupBox)
        self.GlubinaNapora.setObjectName("GlubinaNapora")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.GlubinaNapora)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.DavleniePlasta = QtWidgets.QLineEdit(self.groupBox)
        self.DavleniePlasta.setObjectName("DavleniePlasta")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.DavleniePlasta)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.GlubinaSlabogoPlasta = QtWidgets.QLineEdit(self.groupBox)
        self.GlubinaSlabogoPlasta.setObjectName("GlubinaSlabogoPlasta")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.GlubinaSlabogoPlasta)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.DavlenieRazriva = QtWidgets.QLineEdit(self.groupBox)
        self.DavlenieRazriva.setObjectName("DavlenieRazriva")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.DavlenieRazriva)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(758, 17))
        self.label_7.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_7.setAutoFillBackground(False)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.SpanningRole, self.label_7)
        self.PredelNasosa = QtWidgets.QLineEdit(self.groupBox)
        self.PredelNasosa.setObjectName("PredelNasosa")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.PredelNasosa)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.SpanningRole, self.label_8)
        self.PredelDavlenie = QtWidgets.QLineEdit(self.groupBox)
        self.PredelDavlenie.setObjectName("PredelDavlenie")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.PredelDavlenie)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.SposobBureniya = QtWidgets.QComboBox(self.groupBox)
        self.SposobBureniya.setObjectName("SposobBureniya")
        self.SposobBureniya.addItem("")
        self.SposobBureniya.addItem("")
        self.SposobBureniya.addItem("")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.SposobBureniya)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.KodTurbobura = QtWidgets.QLineEdit(self.groupBox)
        self.KodTurbobura.setObjectName("KodTurbobura")
        self.formLayout.setWidget(19, QtWidgets.QFormLayout.LabelRole, self.KodTurbobura)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(20, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.ShifrUBT = QtWidgets.QLineEdit(self.groupBox)
        self.ShifrUBT.setObjectName("ShifrUBT")
        self.formLayout.setWidget(21, QtWidgets.QFormLayout.LabelRole, self.ShifrUBT)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(22, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.KodUBT = QtWidgets.QLineEdit(self.groupBox)
        self.KodUBT.setObjectName("KodUBT")
        self.formLayout.setWidget(23, QtWidgets.QFormLayout.LabelRole, self.KodUBT)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(24, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.DlinaUBT = QtWidgets.QLineEdit(self.groupBox)
        self.DlinaUBT.setObjectName("DlinaUBT")
        self.formLayout.setWidget(25, QtWidgets.QFormLayout.LabelRole, self.DlinaUBT)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(26, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.ShifrTrubi = QtWidgets.QLineEdit(self.groupBox)
        self.ShifrTrubi.setObjectName("ShifrTrubi")
        self.formLayout.setWidget(27, QtWidgets.QFormLayout.LabelRole, self.ShifrTrubi)
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(28, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.KodTrubi = QtWidgets.QLineEdit(self.groupBox)
        self.KodTrubi.setObjectName("KodTrubi")
        self.formLayout.setWidget(29, QtWidgets.QFormLayout.LabelRole, self.KodTrubi)
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(30, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.DiametrDolota = QtWidgets.QLineEdit(self.groupBox)
        self.DiametrDolota.setObjectName("DiametrDolota")
        self.formLayout.setWidget(31, QtWidgets.QFormLayout.LabelRole, self.DiametrDolota)
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setObjectName("label_17")
        self.formLayout.setWidget(32, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.GlubinaSkvazhini = QtWidgets.QLineEdit(self.groupBox)
        self.GlubinaSkvazhini.setObjectName("GlubinaSkvazhini")
        self.formLayout.setWidget(33, QtWidgets.QFormLayout.LabelRole, self.GlubinaSkvazhini)
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setObjectName("label_18")
        self.formLayout.setWidget(34, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.DiametrKolonni = QtWidgets.QLineEdit(self.groupBox)
        self.DiametrKolonni.setObjectName("DiametrKolonni")
        self.formLayout.setWidget(35, QtWidgets.QFormLayout.LabelRole, self.DiametrKolonni)
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setObjectName("label_19")
        self.formLayout.setWidget(36, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.KodNasosa = QtWidgets.QLineEdit(self.groupBox)
        self.KodNasosa.setObjectName("KodNasosa")
        self.formLayout.setWidget(37, QtWidgets.QFormLayout.LabelRole, self.KodNasosa)
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setObjectName("label_20")
        self.formLayout.setWidget(38, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.KodObvyazki = QtWidgets.QLineEdit(self.groupBox)
        self.KodObvyazki.setObjectName("KodObvyazki")
        self.formLayout.setWidget(39, QtWidgets.QFormLayout.LabelRole, self.KodObvyazki)
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setObjectName("label_21")
        self.formLayout.setWidget(40, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.TipNasosa = QtWidgets.QComboBox(self.groupBox)
        self.TipNasosa.setObjectName("TipNasosa")
        self.TipNasosa.addItem("")
        self.TipNasosa.addItem("")
        self.formLayout.setWidget(42, QtWidgets.QFormLayout.LabelRole, self.TipNasosa)
        self.label_22 = QtWidgets.QLabel(self.groupBox)
        self.label_22.setObjectName("label_22")
        self.formLayout.setWidget(43, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.VPZ = QtWidgets.QLineEdit(self.groupBox)
        self.VPZ.setObjectName("VPZ")
        self.formLayout.setWidget(44, QtWidgets.QFormLayout.LabelRole, self.VPZ)
        self.label_27 = QtWidgets.QLabel(self.groupBox)
        self.label_27.setEnabled(True)
        self.label_27.setWordWrap(False)
        self.label_27.setObjectName("label_27")
        self.formLayout.setWidget(45, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.NapryagSdvigaTo = QtWidgets.QLineEdit(self.groupBox)
        self.NapryagSdvigaTo.setObjectName("NapryagSdvigaTo")
        self.formLayout.setWidget(46, QtWidgets.QFormLayout.LabelRole, self.NapryagSdvigaTo)
        self.label_28 = QtWidgets.QLabel(self.groupBox)
        self.label_28.setObjectName("label_28")
        self.formLayout.setWidget(47, QtWidgets.QFormLayout.LabelRole, self.label_28)
        self.StructVyazkostN = QtWidgets.QLineEdit(self.groupBox)
        self.StructVyazkostN.setObjectName("StructVyazkostN")
        self.formLayout.setWidget(48, QtWidgets.QFormLayout.LabelRole, self.StructVyazkostN)
        self.label_29 = QtWidgets.QLabel(self.groupBox)
        self.label_29.setObjectName("label_29")
        self.formLayout.setWidget(49, QtWidgets.QFormLayout.LabelRole, self.label_29)
        self.label_30 = QtWidgets.QLabel(self.groupBox)
        self.label_30.setWordWrap(True)
        self.label_30.setObjectName("label_30")
        self.formLayout.setWidget(51, QtWidgets.QFormLayout.SpanningRole, self.label_30)
        self.label_31 = QtWidgets.QLabel(self.groupBox)
        self.label_31.setObjectName("label_31")
        self.formLayout.setWidget(54, QtWidgets.QFormLayout.LabelRole, self.label_31)
        self.Plotnost = QtWidgets.QLineEdit(self.groupBox)
        self.Plotnost.setObjectName("Plotnost")
        self.formLayout.setWidget(55, QtWidgets.QFormLayout.LabelRole, self.Plotnost)
        self.btnResult = QtWidgets.QPushButton(self.groupBox)
        self.btnResult.setObjectName("btnResult")
        self.formLayout.setWidget(56, QtWidgets.QFormLayout.LabelRole, self.btnResult)
        self.VidOperacii = QtWidgets.QComboBox(self.groupBox)
        self.VidOperacii.setObjectName("VidOperacii")
        self.VidOperacii.addItem("")
        self.VidOperacii.addItem("")
        self.formLayout.setWidget(50, QtWidgets.QFormLayout.LabelRole, self.VidOperacii)
        self.DlinaSkvazhinkZaboy = QtWidgets.QLineEdit(self.groupBox)
        self.DlinaSkvazhinkZaboy.setObjectName("DlinaSkvazhinkZaboy")
        self.formLayout.setWidget(53, QtWidgets.QFormLayout.LabelRole, self.DlinaSkvazhinkZaboy)
        self.gridLayout_2.addWidget(self.groupBox, 0, 1, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.addWidget(self.scrollArea_2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 843, 25))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Гидравлическая промывка скважин"))
        self.groupBox.setTitle(_translate("MainWindow", "Таблица исходных данных"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Глубина начала L<span style=\" vertical-align:sub;\">n </span>(м)</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Глубина конца L<span style=\" vertical-align:sub;\">k </span>(м)</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Глубина напорного пласта L<span style=\" vertical-align:sub;\">пл </span>(м)</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>Давление пласта P<span style=\" vertical-align:sub;\">пл </span>(МПа)</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>Глубина слабого пласта L<span style=\" vertical-align:sub;\">сл </span>(м)</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>Давление гидро-разрыва Р<span style=\" vertical-align:sub;\">гр </span>(МПа)</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p>Предельно допустимое значение на насосах - рекомендуемая подача насосов Р<span style=\" vertical-align:sub;\">доп</span> (МПа)</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p>Предельно допустимые потери давления в заколонном пространстве Р<span style=\" vertical-align:sub;\">к.доп </span>(МПа)</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "Способ бурения"))
        self.SposobBureniya.setItemText(0, _translate("MainWindow", "турб"))
        self.SposobBureniya.setItemText(1, _translate("MainWindow", "долото"))
        self.SposobBureniya.setItemText(2, _translate("MainWindow", "роторный"))
        self.label_10.setText(_translate("MainWindow", "Код турбобура"))
        self.label_11.setText(_translate("MainWindow", "Шифр УБТ"))
        self.label_12.setText(_translate("MainWindow", "Код УБТ"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p>Длина УБТ (м)</p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "Шифр бурильной трубы"))
        self.label_15.setText(_translate("MainWindow", "Код бурильной трубы"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p>Диаметр долота (мм)</p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p>Глубина обсаженной части скважины (м)</p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p>Внутренний диаметр обсадной колонны (мм)</p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "Код насоса"))
        self.label_20.setText(_translate("MainWindow", "Код обвязки насосов"))
        self.label_21.setText(_translate("MainWindow", "Тип привода насоса (дизельный или электрический)"))
        self.TipNasosa.setItemText(0, _translate("MainWindow", "Дизельный"))
        self.TipNasosa.setItemText(1, _translate("MainWindow", "Электрический"))
        self.label_22.setText(_translate("MainWindow", "Модель жидкости - Бингама (ВПЖ)"))
        self.label_27.setText(_translate("MainWindow", "<html><head/><body><p>Динамическое напряжение сдвига τ<span style=\" vertical-align:sub;\">0  </span>(Па)</p></body></html>"))
        self.label_28.setText(_translate("MainWindow", "<html><head/><body><p>Структурная вязкость η (Па*с)</p></body></html>"))
        self.label_29.setText(_translate("MainWindow", "Вид технологической операции"))
        self.label_30.setText(_translate("MainWindow", "Соотношение длин колонны в скважине к глубине забоя ( в расчетный момент времени проведения операции)"))
        self.label_31.setText(_translate("MainWindow", "Расчетная плотность:"))
        self.btnResult.setText(_translate("MainWindow", "Расчет"))
        self.VidOperacii.setItemText(0, _translate("MainWindow", "подъем"))
        self.VidOperacii.setItemText(1, _translate("MainWindow", "спуск"))

