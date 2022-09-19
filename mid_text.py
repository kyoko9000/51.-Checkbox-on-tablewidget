# ************************** man hinh loai 2 *************************
import sys

from PyQt5.QtCore import Qt
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.uic.tableWidget.setRowCount(5)
        self.uic.tableWidget.setColumnCount(4)
        for i in range(5):
            item = QTableWidgetItem("hello")
            item.setTextAlignment(Qt.AlignCenter)
            self.uic.tableWidget.setItem(i, 1, item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())