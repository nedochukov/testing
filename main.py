import sys

from PyQt5 import QtWidgets
from mainWindow import Ui_testing


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_testing()
        self.ui.setupUi(self)

app = QtWidgets.QApplication([])
application = MyWindow()
application.show()
sys.exit(app.exec())
