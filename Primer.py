from PyQt5.QtWidgets import (QTreeWidget, QTreeWidgetItem, QPushButton, QLabel,QWidget, QVBoxLayout, QApplication, QLineEdit,QComboBox)
from PyQt5.QtCore import pyqtSlot
import sys
from Tablica import *
class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent= None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


    def init_ui(self):
        # Creating the required widgets
        self.vboxLayout = QVBoxLayout()
        self.treeWidget = QTreeWidget()
        self.label = QLabel("I'm going to inform you about the buttons")
        # Adding the widgets
        self.vboxLayout.addWidget(self.treeWidget)
        self.vboxLayout.addWidget(self.label)

        self.topLevelItem = QTreeWidgetItem()

        # Creating top level and child widgets
        self.topLevelButton= QComboBox()

        self.childButton_1 = QPushButton("Child 1")
        self.childButton_2 = QPushButton("Child 2")
        self.childButton_3 = QPushButton("Child 3")
        self.childLineEdit = QLineEdit()
        self.childLineEdit.setPlaceholderText("Add Text Here")

        # Adding the child to the top level item
        self.childItems = []
        for i in range(4):
            self.childItems.append(QTreeWidgetItem())
            self.topLevelItem.addChild(self.childItems[i])

        self.treeWidget.addTopLevelItem(self.topLevelItem)
        self.treeWidget.setItemWidget(self.topLevelItem, 0, self.topLevelButton)

        # Replacing the child items with widgets
        self.treeWidget.setItemWidget(self.childItems[0], 0, self.childButton_1)
        self.treeWidget.setItemWidget(self.childItems[1], 0, self.childButton_2)
        self.treeWidget.setItemWidget(self.childItems[2], 0, self.childButton_3)
        self.treeWidget.setItemWidget(self.childItems[3], 0, self.childLineEdit)


        # Setting the layout

        self.setLayout(self.vboxLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    treeWidgetDialog = MyWin()
    treeWidgetDialog.show()
    sys.exit(app.exec_())