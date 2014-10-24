# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Oct 24 13:53:31 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PySide import QtCore, QtGui


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, 29, 401, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.mainScoreboard = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.mainScoreboard.setContentsMargins(0, 0, 0, 0)
        self.mainScoreboard.setObjectName("mainScoreboard")
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 0, 401, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.currentBowler = QtGui.QLabel(self.horizontalLayoutWidget)
        self.currentBowler.setObjectName("currentBowler")
        self.horizontalLayout.addWidget(self.currentBowler)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.button_Bowl = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.button_Bowl.setObjectName("button_Bowl")
        self.horizontalLayout.addWidget(self.button_Bowl)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 25))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.currentBowler.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.button_Bowl.setText(QtGui.QApplication.translate("MainWindow", "Bowl!", None, QtGui.QApplication.UnicodeUTF8))

    class ControlMainWindow(QtGui.QMainWindow):
        def __init__(self, parent=None):
            super(ControlMainWindow, self).__init__(parent)
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)

    if __name__ == "__main__":
        app = QtGui.QApplication(sys.argv)
        bowling_app = ControlMainWindow()
        bowling_app.show()
        sys.exit(app.exec_())

