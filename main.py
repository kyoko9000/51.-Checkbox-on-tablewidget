# ************************** man hinh loai 2 *************************
import sys
# pip install pyqt6
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        # state 1: add row and column=========================
        self.uic.tableWidget.setRowCount(8)
        self.uic.tableWidget.setColumnCount(4)

        # state 2: add checkBox to tableWidget================
        for row in range(6):
            chkBoxItem = QTableWidgetItem()
            chkBoxItem.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
            chkBoxItem.setCheckState(Qt.CheckState.Unchecked)
            chkBoxItem.setText("Choose row {}".format(row))
            self.uic.tableWidget.setItem(row, 0, chkBoxItem)

        # state 3: checkbox signal control========================
        self.uic.tableWidget.cellChanged.connect(self.onCellChanged)

    def onCellChanged(self, row, column):
        item = self.uic.tableWidget.item(row, column)
        boxcheck = item.checkState()

        # .....method 1: single operation..............
        if row == 0 and column == 0 and boxcheck == Qt.CheckState.Checked:
            print("checked", row, column)
            chkBoxItem = QTableWidgetItem()
            chkBoxItem.setText("Choose row")
            self.uic.tableWidget.setItem(0, 1, chkBoxItem)

        elif row == 0 and column == 0 and boxcheck == Qt.CheckState.Unchecked:
            print("unchecked", row, column)
            chkBoxItem = QTableWidgetItem()
            chkBoxItem.setText("")
            self.uic.tableWidget.setItem(0, 1, chkBoxItem)

        # .....method 2: multi operation............
        # if boxcheck == Qt.CheckState.Checked:
        #     print("checked", row, column)
        #     chkBoxItem = QTableWidgetItem()
        #     chkBoxItem.setText("checked")
        #     self.uic.tableWidget.setItem(row, column + 1, chkBoxItem)
        #
        # elif row == 0 and column == 0 and boxcheck == Qt.CheckState.Unchecked:
        #     print("unchecked", row, column)
        #     chkBoxItem = QTableWidgetItem()
        #     chkBoxItem.setText("")
        #     self.uic.tableWidget.setItem(0, 1, chkBoxItem)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
