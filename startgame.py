__author__ = 'androideka'

import sys
from PySide import QtCore, QtGui
from bowler import Bowler
import mainwindow
import bowler_score
import random


class Ui_StartGame(object):

    bowler_dict = {}
    player_num = 0

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
        self.button_start_game = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        self.button_start_game.setObjectName("button_start_game")
        self.horizontalLayout_3.addWidget(self.button_start_game)
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
        self.player_name = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.player_name.setObjectName("player_name")
        self.horizontalLayout_6.addWidget(self.player_name)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.button_add_new_bowler = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_add_new_bowler.setMinimumSize(QtCore.QSize(20, 20))
        self.button_add_new_bowler.setObjectName("button_add_new_bowler")
        self.horizontalLayout_6.addWidget(self.button_add_new_bowler)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.player_list = QtGui.QListWidget(self.verticalLayoutWidget)
        self.player_list.setObjectName("player_list")
        self.verticalLayout.addWidget(self.player_list)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(StartGame)
        QtCore.QMetaObject.connectSlotsByName(StartGame)

        QtGui.QWidget.connect(self.button_add_new_bowler, QtCore.SIGNAL("pressed()"),
                              self.add_bowler)

        QtGui.QWidget.connect(self.button_start_game, QtCore.SIGNAL("pressed()"),
                              self.launch_mainapp)

        QtGui.QWidget.connect(mainapp.ui.button_bowl, QtCore.SIGNAL("pressed()"),
                              self.bowl)

        self.player_list.addItem("Matt")
        matt = Bowler('Matt')
        self.bowler_dict[0] = matt
        self.player_num += 1

    def add_bowler(self):
        name = self.player_name.text()
        if name:
            self.player_list.addItem(name)
            bowler = Bowler(name)
            self.bowler_dict[self.player_num] = bowler
        self.player_num += 1
        self.player_name.clear()

    def launch_mainapp(self):
        for i in range(self.player_list.count()):
            player = BowlerScore()
            player.ui.player_name.setText(self.player_list.item(i).text())
            player.ui.cum_score.setText('0')
            mainapp.ui.verticalLayout.addWidget(player)
        mainapp.show()
        intro.hide()

    def bowl(self):
        bowler_name = mainapp.ui.current_bowler.text()
        mainapp.bowl(self.bowler_dict, bowler_name)

    def retranslateUi(self, StartGame):
        StartGame.setWindowTitle(QtGui.QApplication.translate("StartGame", "Crimson Application", None, QtGui.QApplication.UnicodeUTF8))
        self.welcome.setText(QtGui.QApplication.translate("StartGame", "Welcome to Matt\'s resume!", None, QtGui.QApplication.UnicodeUTF8))
        self.button_start_game.setText(QtGui.QApplication.translate("StartGame", "Let\'s Bowl!", None, QtGui.QApplication.UnicodeUTF8))
        self.label_add_player.setText(QtGui.QApplication.translate("StartGame", "Enter Player Names Below:", None, QtGui.QApplication.UnicodeUTF8))
        self.button_add_new_bowler.setText(QtGui.QApplication.translate("StartGame", "Add New Bowler", None, QtGui.QApplication.UnicodeUTF8))


class ControlStartWidget(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(ControlStartWidget, self).__init__(parent)
        self.ui = Ui_StartGame()
        self.ui.setupUi(self)


class ControlMainWindow(QtGui.QMainWindow):

    bowlers = {}
    next_bowler = Bowler('')

    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)

    def bowl(self, bowlers, name):
        if not self.next_bowler.get_name():
            self.next_bowler = bowlers[0]
        if not self.bowlers:
            self.bowlers = bowlers
        print self.bowlers
        index = 0
        for key in self.bowlers.keys():
            bowler = self.bowlers[key]
            if bowler.get_name() == name:
                index = key
        current_bowler_index = index
        current_bowler = self.bowlers[current_bowler_index]
        if current_bowler.get_name() == 'Matt':
            pins_left = 0
        else:
            if len(current_bowler.get_current_frame()) == 0:
                pins_left = random.randint(0, 10)
            else:
                pins_left = random.randint(0, 10 - current_bowler.get_current_frame()[0])
        strike_spare_or_open = self.next_bowler.bowl(pins_left)
        print 'Current frame: ' + str(current_bowler.current_frame)
        print current_bowler.get_total_score()
        print current_bowler.get_frame_scores()
        self.update_score(current_bowler_index)
        if strike_spare_or_open and len(self.bowlers) > 1:
            self.next_bowler = self.get_next_bowler(current_bowler_index)
            self.ui.current_bowler.setText(self.next_bowler.get_name())

    def update_score(self, bowler_index):
        print intro.ui.bowler_dict
        # So ugly... Please forgive me
        bowler = self.bowlers[bowler_index]
        index = 0
        for i in range(len(intro.ui.bowler_dict)):
            if intro.ui.bowler_dict[i] == bowler.get_name():
                index = i
        print 'Index: ' + str(index)
        print 'Widget: ' + str(mainapp.ui.verticalLayout.itemAt(index))
        bowler_score_widget = mainapp.ui.verticalLayout.itemAt(index)
        frame = len(bowler.frames)
        return False

    def get_next_bowler(self, bowler_index):
        if bowler_index == len(self.bowlers) - 1:
            bowler_index = 0
        else:
            bowler_index += 1
        return self.bowlers[bowler_index]


class BowlerScore(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(BowlerScore, self).__init__(parent)
        self.ui = bowler_score.Ui_bowler_score()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainapp = ControlMainWindow()
    intro = ControlStartWidget()
    intro.show()
    sys.exit(app.exec_())