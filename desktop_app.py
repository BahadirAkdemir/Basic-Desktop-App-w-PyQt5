from re import X
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

def window():
    app=QtWidgets.QApplication(sys.argv)
    win=QtWidgets.QMainWindow()
    win.setWindowTitle("PyQt5 Application")
    win.setGeometry(200,200,500,500)
    win.show()
    sys.exit(app.exec_())

window()


