# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startgame.ui'
#
# Created: Fri Oct 24 15:08:53 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PySide import QtCore, QtGui
from bowler import Bowler
import mainwindow
import bowler_score


class Ui_StartGame(object):
    def setupUi(self, StartGame):
        StartGame.setObjectName("StartGame")
        StartGame.resize(400, 300)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(StartGame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(9, 10, 381, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.welcome = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome.setObjectName("welcome")
        self.horizontalLayout_2.addWidget(self.welcome)
        self.horizontalLayoutWidget_3 = QtGui.QWidget(StartGame)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(40, 240, 321, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.start_game = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        self.start_game.setObjectName("start_game")
        self.horizontalLayout_3.addWidget(self.start_game)
        self.verticalLayoutWidget = QtGui.QWidget(StartGame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 60, 361, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_add_player = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_add_player.setObjectName("label_add_player")
        self.verticalLayout.addWidget(self.label_add_player)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_6.addWidget(self.lineEdit)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.add_new_bowler = QtGui.QPushButton(self.verticalLayoutWidget)
        self.add_new_bowler.setObjectName("add_new_bowler")
        self.horizontalLayout_6.addWidget(self.add_new_bowler)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.player_list = QtGui.QListWidget(self.verticalLayoutWidget)
        self.player_list.setObjectName("player_list")
        self.verticalLayout.addWidget(self.player_list)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(StartGame)
        QtCore.QMetaObject.connectSlotsByName(StartGame)

        QtGui.QWidget.connect(self.add_new_bowler, QtCore.SIGNAL("pressed()"),
                              self.add_bowler)
        self.player_list.addItem("Matt")
        QtGui.QWidget.connect(self.start_game, QtCore.SIGNAL("pressed()"),
                              self.launch_main)

    def add_bowler(self):
        name = self.lineEdit.text()
        if name:
            self.player_list.addItem(name)
        self.lineEdit.clear()

    def launch_main(self):
        bowlers = []
        for i in range(self.player_list.count()):
            bowler = Bowler(self.player_list.item(i))
            bowlers.append(bowler)
            self.verticalLayout.addWidget(QtGui.QWidget(), 0, QtCore.QAlignment(0))
        main.show()

    def retranslateUi(self, StartGame):
        StartGame.setWindowTitle(QtGui.QApplication.translate("StartGame", "Crimson Application", None, QtGui.QApplication.UnicodeUTF8))
        self.welcome.setText(QtGui.QApplication.translate("StartGame", "Welcome to Matt\'s resume!", None, QtGui.QApplication.UnicodeUTF8))
        self.start_game.setText(QtGui.QApplication.translate("StartGame", "Let\'s Bowl!", None, QtGui.QApplication.UnicodeUTF8))
        self.label_add_player.setText(QtGui.QApplication.translate("StartGame", "Enter Player Names Below:", None, QtGui.QApplication.UnicodeUTF8))
        self.add_new_bowler.setText(QtGui.QApplication.translate("StartGame", "Add New Bowler", None, QtGui.QApplication.UnicodeUTF8))


class ControlStartWidget(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(ControlStartWidget, self).__init__(parent)
        self.ui = Ui_StartGame()
        self.ui.setupUi(self)


class ControlMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    intro = ControlStartWidget()
    intro.show()
    main = ControlMainWindow()
    sys.exit(app.exec_())