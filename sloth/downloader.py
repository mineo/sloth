import re

from PyQt4 import QtNetwork, QtCore

CRC32_RE = re.compile(".*(\([A-Fa-f0-9]{8,8}\)).*")

class Downloader(QtCore.QObject):

    fileDownloaded = QtCore.pyqtSignal(str)
    allDownloadsDone = QtCore.pyqtSignal()
    notFound = QtCore.pyqtSignal(str)
    error = QtCore.pyqtSignal(str)

    def __init__(self):
        """docstring for __init__"""
        QtCore.QObject.__init__(self)
        self.ftp = QtNetwork.QFtp()
        self.ftp.stateChanged.connect(self.stateChanged)
        self.ftp.listInfo.connect(self.listed)
        self.ftp.commandFinished.connect(self.commandFinished)
        self._files = {}
        self._clear()

    def enqueue(self, items):
        if self._items is None:
            self._items = items
            print items
            if not self.ftp.state in (QtNetwork.QFtp.Connected,
                    QtNetwork.QFtp.LoggedIn, QtNetwork.QFtp.Login):
                self.ftp.connectToHost("localhost")
        else:
            pass
            # TODO: merge the two *items*

    def _clear(self):
        self._current_item = None
        self._items = None
        self._list_after_cd = False

    def _find_next_file(self):
        """docstring for download"""
        if self._items is not None:
            try:
                self._current_item = self._items.popitem()
                self._list_after_cd = True
                self.ftp.cd(self._current_item[1][0] + "/" +
                    self._current_item[1])
            except KeyError:
                self._clear()

    def stateChanged(self, state):
        """docstring for stateChanged"""
        if state == QtNetwork.QFtp.Connected:
            QtCore.qDebug("Connected")
            self.ftp.login("anonymous", "foo@bar.tld")
        if state == QtNetwork.QFtp.LoggedIn:
            QtCore.qDebug("Logged in")
            self._find_next_file()

    def listed(self, _file):
        if self._current_item is not None:
            crc = self._current_item[0]
            if crc in _file.name().toLower():
                QtCore.qDebug("Found " + _file.name())
                self._download(_file.name())
                self._list_after_cd = False

    def _download(self, _filename):
        _file = QtCore.QFile(_filename)
        _file.open(QtCore.QIODevice.WriteOnly)
        self._files[self.ftp.get(_filename, _file)] = _file


    def commandFinished(self, command, error):
        if error:
            self._clear()
            self.ftp.close()

        elif self.ftp.currentCommand() == QtNetwork.QFtp.Get:
            _file = self._files[command]
            crc = CRC32_RE.match(_file.fileName()).group(1).toLower()[1:9]
            self.fileDownloaded.emit(crc)
            _file.close()

            if self._items is None and not self.ftp.hasPendingCommands:
                self.allDownloadsDone.emit()
                self.ftp.close()
                return

            self.ftp.cd("../..")
            self._find_next_file()

        elif self.ftp.currentCommand() == QtNetwork.QFtp.List:
            if self._current_item is not None:
                crc = self._current_item[0]
                if not crc in self._files:
                    self.notFound.emit(crc)
            self._list_after_cd = False
            self.ftp.cd("../..")
            self._find_next_file()

        elif self.ftp.currentCommand() == QtNetwork.QFtp.Cd:
            if self._list_after_cd:
                self.ftp.list()
