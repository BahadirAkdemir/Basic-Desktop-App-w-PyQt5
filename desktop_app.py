from re import X
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


def window():
    app=QtWidgets.QApplication(sys.argv)
    win=QtWidgets.QMainWindow()
    win.setWindowTitle("PyQt5 Application")
    win.setGeometry(200,200,500,500)

    label_name = QtWidgets.QLabel(win)
    label_name.setText("Product Name")
    label_name.move(20,20)
    text_name = QtWidgets.QLineEdit(win)
    text_name.move(120,20)

    label_price = QtWidgets.QLabel(win)
    label_price.setText("Price")
    label_price.move(20,80)
    text_price = QtWidgets.QLineEdit(win)
    text_price.move(120,80)

    button_save = QtWidgets.QPushButton(win)
    button_save.setText("Save")
    button_save.move(120,140)

    def clicked():
        print("Product Name:",text_name.text(),"\nPrice: $",text_price.text())

    button_save.clicked.connect(clicked)





    win.show()
    sys.exit(app.exec_())

window()


