from PyQt4 import QtCore, QtGui

COLUMNS = 4
COLUMN_ANIME = 0
COLUMN_EPISODE = 1
COLUMN_CRC = 2
COLUMN_GROUP = 3

def make_model(rows=0, columns=COLUMNS):
    model = QtGui.QStandardItemModel(rows, columns)
    model.setHeaderData(COLUMN_ANIME,
            QtCore.Qt.Horizontal, QtCore.QString("Anime"))
    model.setHeaderData(COLUMN_EPISODE,
            QtCore.Qt.Horizontal, QtCore.QString("Episode"))
    model.setHeaderData(COLUMN_CRC,
            QtCore.Qt.Horizontal, QtCore.QString("CRC"))
    model.setHeaderData(COLUMN_GROUP,
            QtCore.Qt.Horizontal, QtCore.QString("Group"))
    return model
