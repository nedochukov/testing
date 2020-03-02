import sys
import mysql.connector
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from mainWindow import Ui_testing


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_testing()
        self.ui.setupUi(self)

        self.db_cnx = 0
        self.db_cursor = 0
        self.connect2db()

        self.ui.testing_tabWidget.setTabEnabled(1, False)  # Неактивна вкладка при старті
        self.ui.testing_tabWidget.setTabEnabled(2, False)  # неактивна вкладка при старті
        self.ui.testing_tabWidget.setTabEnabled(3, False)  # Неактивна вкладка при старті

        self.ui.sig_in_pushButton.clicked.connect(self.Sig_in_btnClick)

    # конектор для бази данних
    def connect2db(self):
        self.db_cnx = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="admin",
            password="1",
            database="test"
        )
        self.db_cursor = self.db_cnx.cursor()

    # клік на кнопку входу першої вкладки
    def Sig_in_btnClick(self):
        login, password = 0, 0
        login = self.ui.login_lineEdit.text()
        password = self.ui.password_lineEdit.text()
        self.sigIn(login, password,)

    # Check login and password in database
    def sigIn(self, login, password,):
        self.db_cursor.execute("SELECT * FROM users WHERE login='" + login + "' AND password='" + password)
        result = self.db_cursor.fetchall()
        count = self.db_cursor.rowcount
        if result > 0:
            self.ui.user_label.setText("Success!")
            self.ui.user_label.adjustSize()
        else:
            self.ui.user_label.setText("Wrong login or password!")
            self.ui.user_label.adjustSize()


# create main window
def main():
    app: QApplication = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
