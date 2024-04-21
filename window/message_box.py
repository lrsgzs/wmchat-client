from qfluentwidgets import *


class InfoMessageBox(MessageBox):
    def __init__(self, title: str, message: str, parent):
        super().__init__(title, message, parent)
        self.yesButton.setText("好的")
        self.cancelButton.hide()
