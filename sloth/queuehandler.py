from PyQt4 import QtCore, QtGui
from os import getenv, mkdir
from os.path import expanduser, join, exists, dirname
from sys import platform
from . import model

class QueueHandler(QtCore.QObject):

    finishedLoading = QtCore.pyqtSignal(QtGui.QStandardItemModel)
    finishedSaving = QtCore.pyqtSignal()

    def __init__(self):
        QtCore.QObject.__init__(self)
        if platform.startswith("win"):
            self._file = join(
                getenv("APPDATA", "~\\Application Data"),
                "Aniftp-Qt", "queue")
        else:
            self._file = join(expanduser(
                getenv("XDG_DATA_HOME", "~/.local/share")),
                "Aniftp-Qt", "queue")

        if not exists(dirname(self._file)):
            mkdir(dirname(self._file))

    def load(self):
        infile = QtCore.QFile(self._file)
        infile.open(QtCore.QIODevice.ReadOnly)
        instream = QtCore.QDataStream(infile)

        load_model = model.make_model(instream.readInt(), instream.readInt())

        for i in xrange(load_model.rowCount()):
           for j in xrange(load_model.columnCount()):
                item = QtGui.QStandardItem()
                item.read(instream)
                load_model.setItem(i, j, item)

        infile.close()
        self.finishedLoading.emit(load_model)

    def save(self, model):
        outfile = QtCore.QFile(self._file)
        outfile.open(QtCore.QIODevice.WriteOnly | QtCore.QIODevice.Truncate)
        out = QtCore.QDataStream(outfile)
        out.setVersion(QtCore.QDataStream.Qt_4_6)
        out.writeInt(model.rowCount())
        out.writeInt(model.columnCount())
        for i in xrange(0, model.rowCount()):
            for j in xrange(0, model.columnCount()):
                model.item(i,j).write(out)
        outfile.close()
