from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

try:
    from .ui import account_widget
except ImportError:
    from ui import account_widget


class AccountWidget(QWidget, account_widget.AccountWidgetUI):
    logout_event = pyqtSignal()

    def __init__(self, user_id: int = 0):
        super().__init__()
        self.setupUi(self)

        self.user_id = user_id

        self.info.hide()
        self.avatar.hide()


__all__ = ['AccountWidget']
