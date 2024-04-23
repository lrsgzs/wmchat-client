from qfluentwidgets import *


class InfoMessageBox(object):
    def __new__(cls, title: str, message: str, parent=None):
        obj = MessageBox(title, message, parent)
        obj.yesButton.setText("好的")
        obj.cancelButton.hide()
        return obj


__all__ = ['InfoMessageBox']
