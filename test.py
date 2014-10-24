__author__ = 'androideka'

import sys
from PySide import QtCore, QtGui


app = QApplication(sys.argv)
label = QLabel("Hello World")
label.show()
app.exec_()
sys.exit()