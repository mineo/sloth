# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created: Sun Dec  4 21:16:52 2011
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Sloth", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.episodeTable = QtGui.QTableView(self.centralwidget)
        self.episodeTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.episodeTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.episodeTable.setSortingEnabled(False)
        self.episodeTable.setObjectName(_fromUtf8("episodeTable"))
        self.episodeTable.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.episodeTable)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.fetchFeedButton = QtGui.QPushButton(self.centralwidget)
        self.fetchFeedButton.setText(QtGui.QApplication.translate("MainWindow", "Fetch feed", None, QtGui.QApplication.UnicodeUTF8))
        self.fetchFeedButton.setObjectName(_fromUtf8("fetchFeedButton"))
        self.horizontalLayout.addWidget(self.fetchFeedButton)
        self.downloadButton = QtGui.QPushButton(self.centralwidget)
        self.downloadButton.setText(QtGui.QApplication.translate("MainWindow", "Download", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadButton.setObjectName(_fromUtf8("downloadButton"))
        self.horizontalLayout.addWidget(self.downloadButton)
        self.settingsButton = QtGui.QPushButton(self.centralwidget)
        self.settingsButton.setText(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsButton.setObjectName(_fromUtf8("settingsButton"))
        self.horizontalLayout.addWidget(self.settingsButton)
        self.saveQueueButton = QtGui.QPushButton(self.centralwidget)
        self.saveQueueButton.setText(QtGui.QApplication.translate("MainWindow", "Save queue", None, QtGui.QApplication.UnicodeUTF8))
        self.saveQueueButton.setObjectName(_fromUtf8("saveQueueButton"))
        self.horizontalLayout.addWidget(self.saveQueueButton)
        self.deleteButton = QtGui.QPushButton(self.centralwidget)
        self.deleteButton.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.horizontalLayout.addWidget(self.deleteButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

