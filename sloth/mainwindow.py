# coding: utf-8
from ui.mainwindow import Ui_MainWindow
from feedreader import FeedReader
from PyQt4 import QtGui, QtCore
from . import model
from .settings import SettingsDialog

class MainWindow(Ui_MainWindow):
    def setupUi(self, window):
        Ui_MainWindow.setupUi(self, window)
        header = QtGui.QHeaderView(QtCore.Qt.Horizontal)
        header.setResizeMode(QtGui.QHeaderView.Stretch)
        self.episodeTable.setHorizontalHeader(header)
        self.fetchFeedButton.clicked.connect(self._load_feed)
        self.downloadButton.clicked.connect(self._download)
        self.deleteButton.clicked.connect(self._delete_row)
        self.saveQueueButton.clicked.connect(self._save_queue)
        self.settings = SettingsDialog()
        self.settingsButton.clicked.connect(self.settings.show)

        QtGui.qApp.queuehandler.finishedLoading.connect(self._set_model)
        QtGui.qApp.queuehandler.load()

        QtGui.qApp.downloader.fileDownloaded.connect(self._downloaded)
        QtGui.qApp.downloader.notFound.connect(self._notfound)

    def _download(self):
        rows = sorted(set([item.row() for item in
            self.episodeTable.selectedIndexes()]))
        l_model = self.episodeTable.model()

        items = {}

        if len(rows) > 0:
            for row in rows:
                items[l_model.item(row, model.COLUMN_CRC).text()] = \
                        l_model.item(row, model.COLUMN_ANIME).text()
        else:
            for i in xrange(0, l_model.rowCount()):
                items[l_model.item(i, model.COLUMN_CRC).text()] = \
                        l_model.item(i, model.COLUMN_ANIME).text()

        self.downloader.enqueue(items)

    def _downloaded(self, crc):
        l_model = self.episodeTable.model()
        for i in xrange(0, l_model.rowCount()):
                if crc == l_model.data(l_model.index(i, model.COLUMN_CRC)).toString():
                    l_model.removeRows(i, 1)

    def _notfound(self, crc):
        l_model = self.episodeTable.model()
        for i in xrange(0, l_model.rowCount()):
            if crc == l_model.data(l_model.index(i, model.COLUMN_CRC)).toString():
                for k in xrange(0, model.COLUMNS):
                    l_model.setData(l_model.index(i,k),
                            QtCore.QVariant(QtGui.QBrush(QtCore.Qt.red)),
                            QtCore.Qt.BackgroundRole)

    def _load_feed(self):
        loader = FeedReader()
        loader.finishedLoading.connect(self._dicts_to_tree)
        loader.load()

    def _dicts_to_tree(self, dicts):
    # TODO move into the feedreader
        d_model = model.make_model(len(dicts))
        for index, item in enumerate(dicts):
            d_model.setData(d_model.index(index, 0), QtCore.QVariant(item["anime"]))
            if "episode" in item:
                d_model.setData(d_model.index(index, 1),
                        QtCore.QVariant(item["episode"]))
            if "group" in item:
                d_model.setData(d_model.index(index, 3),
                        QtCore.QVariant(item["group"]))
            d_model.setData(d_model.index(index, 2), QtCore.QVariant(item["crc"]))
        self._set_model(d_model)

    def _set_model(self, new_model):
        new_model.sort(model.COLUMN_ANIME)
        self.episodeTable.setModel(new_model)
        self.episodeTable.resizeColumnsToContents()

    def _delete_row(self):
        rows = sorted(set([item.row() for item in
            self.episodeTable.selectedIndexes()]))
        model = self.episodeTable.model()
        for index, row in enumerate(rows):
            model.removeRows(row - index, 1)

    def _save_queue(self):
        model = self.episodeTable.model()
        self.queuehandler.save(model)
