import sys

from PyQt5 import QtWidgets, QtCore


class SecondWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)

        self.build()

    def build(self):
        self.mainLayout = QtWidgets.QVBoxLayout()

        self.edit = QtWidgets.QLineEdit(self)
        self.mainLayout.addWidget(self.edit)

        self.but1 = QtWidgets.QPushButton('close window', self)
        self.but1.clicked.connect(self.close_window)
        self.mainLayout.addWidget(self.but1)

        self.setLayout(self.mainLayout)

    def close_window(self):
        self.close()
        self.parent().edit.setText(self.edit.text())


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.secondWin = None
        self.build()

    def build(self):
        self.mainLayout = QtWidgets.QVBoxLayout()

        self.edit = QtWidgets.QLineEdit(self)
        self.mainLayout.addWidget(self.edit)

        self.but1 = QtWidgets.QPushButton('open window', self)
        self.but1.clicked.connect(self.open_win)
        self.mainLayout.addWidget(self.but1)

        self.setLayout(self.mainLayout)

    def open_win(self):
        if not self.secondWin:
            self.secondWin = SecondWindow(self)
        self.secondWin.edit.setText('текст переданный с первой формы')
        self.secondWin.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())