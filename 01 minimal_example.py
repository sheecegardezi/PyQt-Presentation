import sys
from PyQt5 import QtWidgets

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    label = QtWidgets.QLabel("Hello, World!")
    label.show()
    app.exec()
