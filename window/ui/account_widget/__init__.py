from PyQt5 import QtWidgets
from .account_widget import Ui_Account as AccountWidgetUI


class AccountWidget(QtWidgets.QWidget, AccountWidgetUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.info.hide()
        self.avatar.hide()
