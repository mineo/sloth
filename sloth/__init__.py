import sys
import PyQt4.QtGui

from .sloth import Sloth
from .mainwindow import MainWindow

def main():
    app = Sloth()
    ui = MainWindow()
    window = PyQt4.QtGui.QMainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
