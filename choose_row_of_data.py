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
        self.col_num = 4
        self.uic.tableWidget.setColumnCount(self.col_num)

        # state 2: add checkBox to tableWidget================
        for row in range(6):
            chkBoxItem = QTableWidgetItem()
            chkBoxItem.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
            chkBoxItem.setCheckState(Qt.CheckState.Unchecked)
            chkBoxItem.setText("Choose row {}".format(row))
            self.uic.tableWidget.setItem(row, 0, chkBoxItem)

        # state 3: checkbox signal control========================
        self.uic.tableWidget.cellChanged.connect(self.onCellChanged)

    def show_data(self, data):
        self.uic.label.setText(data)

    def onCellChanged(self, row, column):
        item = self.uic.tableWidget.item(row, column)
        boxcheck = item.checkState()

        # # .....method 1: single operation..............
        # if row == 0 and column == 0 and boxcheck == Qt.CheckState.Checked:
        #     try:
        #         print("checked row: ", row)
        #         # read from this row''''''''''''
        #         list = []
        #         for _col in range(1, self.col_num):
        #             item = self.uic.tableWidget.item(0, _col)
        #             list.append(item.text())
        #         print(str(list))
        #     except:
        #         print("no data")
        #
        # elif row == 0 and column == 0 and boxcheck == Qt.CheckState.Unchecked:
        #     print("unchecked row: ", row)
        #     # write for this row
        #     for _col in range(1, self.col_num):
        #         chkBoxItem = QTableWidgetItem()
        #         chkBoxItem.setText("")
        #         self.uic.tableWidget.setItem(row, _col, chkBoxItem)

        # .....method 2: multi operation............
        if boxcheck == Qt.CheckState.Checked:
            try:
                print("checked row: ", row)
                # read from this row''''''''''''
                list = []
                for _col in range(1, self.col_num):
                    item = self.uic.tableWidget.item(row, _col)
                    list.append(item.text())
                print("row {}".format(row), str(list))
                data = str(list)
                self.show_data(data)

            except:
                print("no data")

        elif boxcheck == Qt.CheckState.Unchecked:
            self.uic.label.setText("")
            # print("unchecked row: ", row)
            # # write for this row
            # for _col in range(1, self.col_num):
            #     chkBoxItem = QTableWidgetItem()
            #     chkBoxItem.setText("")
            #     self.uic.tableWidget.setItem(row, _col, chkBoxItem)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
