import sys

from .queuehandler import QueueHandler
from .downloader import Downloader
from PyQt4 import QtGui, QtCore

class Sloth(QtGui.QApplication):
    def __init__(self):
        sys.modules["PyQt4.QtGui"].__dict__["qApp"] = self
        QtGui.QApplication.__init__(self, sys.argv)

        self.queuehandler = QueueHandler()
        self.downloader = Downloader()

        QtCore.QCoreApplication.setOrganizationName("RP")
        QtCore.QCoreApplication.setApplicationName("Sloth")
        self.config = QtCore.QSettings()
