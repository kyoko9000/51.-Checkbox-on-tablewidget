# ************************** man hinh loai 2 *************************
import sys

from PyQt5 import QtCore
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QProxyStyle, QStyle
from gui import Ui_MainWindow


class CheckBoxStyle(QProxyStyle):
    def subElementRect(self, element, option, widget=None):
        r = super().subElementRect(element, option, widget)
        if element == QStyle.SE_ItemViewItemCheckIndicator:
            r.moveCenter(option.rect.center())
        return r


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.tableWidget.setColumnCount(3)
        self.uic.tableWidget.setRowCount(5)
        for row in range(5):
            checkbox_item = QTableWidgetItem()
            checkbox_item.setCheckState(QtCore.Qt.Unchecked)
            self.uic.tableWidget.setItem(row, 0, checkbox_item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    checkbox_style = CheckBoxStyle(app.style())
    app.setStyle(checkbox_style)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
