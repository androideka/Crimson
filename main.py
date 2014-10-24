__author__ = 'mrose'

import sys
from PySide import QtCore, QtGui
import bowler


app = QtGui.QApplication(sys.argv)
label = QtGui.QLabel("Hello World")
label.show()
app.exec_()
sys.exit()