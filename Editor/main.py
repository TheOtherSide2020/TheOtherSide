# Main Class for the The Other Side Backend Editor
# PYQT5, Python 3.8, PYDesigner and pyui5
# Version 0
# By Ruchi Hendre, rhendre


import json
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from Editor.Screens import Screen1


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Screen1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
