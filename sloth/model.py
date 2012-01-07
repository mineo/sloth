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

def merge_models(old, new):
    """docstring for merge_model"""
    if old.rowCount() == 0:
        return new
    if new.rowCount() == 0:
        return old
    old_crcs = [(old.item(row, COLUMN_CRC).text(), row) for row in
            xrange(old.rowCount())]
    new_crcs = [(new.item(row, COLUMN_CRC).text(), row) for row in
            xrange(new.rowCount())]

    for crc, row in new_crcs:
        for old_crc, _ in old_crcs:
            if crc == old_crc:
                break
        old.appendRow(new.takeRow(row))

    return old
