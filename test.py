__author__ = 'androideka'

import sys
from PySide import QtCore, QtGui


app = QtGui.QApplication(sys.argv)
label = QtGui.QLabel("Hello World")
label.show()
app.exec_()
sys.exit()