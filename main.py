import sys
from PySide import QtGui, QtCore
import mainwindow
import startgame


class ControlStartWidget(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(ControlStartWidget, self).__init__(parent)
        self.ui = startgame.Ui_StartGame()
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
    mainapp = ControlMainWindow()
    sys.exit(app.exec_())