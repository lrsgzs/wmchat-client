from qfluentwidgets import *


class InfoMessageBox(object):
    def __new__(cls, title: str, message: str, parent):
        return MessageBox(title, message, parent)
