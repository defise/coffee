import sys
import sqlite3
from PyQt6 import QtWidgets, uic


class CoffeeDatabaseApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(CoffeeDatabaseApp, self).__init__()
        uic.loadUi('main.ui', self)
        self.loadButton = self.findChild(QtWidgets.QPushButton, 'loadButton')
        self.loadButton.clicked.connect(self.load_coffee_data)

        self.coffeeTable = self.findChild(QtWidgets.QTableWidget, 'coffeeTable')

    def load_coffee_data(self):
        self.coffeeTable.setRowCount(0)
        conn = sqlite3.connect('coffee.sqlite')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM coffee")
        rows = cursor.fetchall()

        for row in rows:
            rowPosition = self.coffeeTable.rowCount()
            self.coffeeTable.insertRow(rowPosition)
            for column, data in enumerate(row):
                self.coffeeTable.setItem(rowPosition, column, QtWidgets.QTableWidgetItem(str(data)))

        conn.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CoffeeDatabaseApp()
    window.show()
    sys.exit(app.exec())
