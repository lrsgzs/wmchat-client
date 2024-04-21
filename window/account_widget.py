from PyQt5.QtWidgets import *

try:
    from .ui import account_widget
except ImportError:
    from ui import account_widget


class AccountWidget(QWidget, account_widget.AccountWidgetUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.info.hide()
        self.avatar.hide()
