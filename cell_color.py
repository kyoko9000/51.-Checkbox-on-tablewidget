# ************************** man hinh loai 2 *************************
import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        # state 1: add row and column=========================
        self.uic.tableWidget.setRowCount(8)
        self.uic.tableWidget.setColumnCount(4)
        item = QTableWidgetItem("6")
        self.uic.tableWidget.setItem(0, 1, item)
        self.item = self.uic.tableWidget.item(0, 1)
        self.uic.tableWidget.cellChanged.connect(self.change_number)

    def change_number(self):
        print(self.item.text())
        if self.item.text() == "0":
            brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            self.item.setBackground(brush)
            self.uic.tableWidget.setItem(0, 1, self.item)
        else:
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            self.item.setBackground(brush)
            self.uic.tableWidget.setItem(0, 1, self.item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
