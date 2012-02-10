from .ui import settings
from PyQt4 import QtGui, QtCore

class SettingsDialog(QtGui.QDialog, settings.Ui_dialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.accepted.connect(self.update_settings)
        config = QtCore.QSettings()
        self.server.setText(config.value("server").toString())
        self.port.setText(config.value("port", 21).toString())
        self.user.setText(config.value("user").toString())
        self.password.setText(config.value("password").toString())
        self.feed.setText(config.value("feed").toString())
        self.save_files_to_location.setText(config.value("save_files_to").toString())

    def update_settings(self):
        config = QtCore.QSettings()
        config.setValue("server", self.server.text())
        config.setValue("port", self.port.text())
        config.setValue("user", self.user.text())
        config.setValue("password", self.password.text())
        config.setValue("feed", self.feed.text())
        config.setValue("save_files_to", self.save_files_to_location.text())
        config.sync()
