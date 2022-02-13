from re import X
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("PyQt5 Application")
        self.setGeometry(200,200,500,500)
        self.InitUI()

    def InitUI(self):
        self.label_name = QtWidgets.QLabel(self)
        self.label_name.setText("Product Name")
        self.label_name.move(20,20)
        self.text_name = QtWidgets.QLineEdit(self)
        self.text_name.move(120,20)

        self.label_price = QtWidgets.QLabel(self)
        self.label_price.setText("Price")
        self.label_price.move(20,80)
        self.text_price = QtWidgets.QLineEdit(self)
        self.text_price.move(120,80)

        button_save = QtWidgets.QPushButton(self)
        button_save.setText("Save")
        button_save.move(120,140)

        self.label_result = QtWidgets.QLabel(self)
        self.label_result.setText("Sonuç")
        self.label_result.resize(300,30)
        self.label_result.move(120,200)

        button_save.clicked.connect(self.clicked)

    def clicked(self):
        print(self.label_result.setText(f"Product Name:{self.text_name.text()} \nPrice: ${self.text_price.text()}"))

def window():
    app=QtWidgets.QApplication(sys.argv)
    win=MainWindow()
    win.show()
    sys.exit(app.exec_())

window()


