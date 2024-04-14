from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from qfluentwidgets import *
import sys

try:
    from .ui import login_dialog
    from .utils import isWin11
except ImportError:
    from ui import login_dialog
    from utils import isWin11

if isWin11():
    from qframelesswindow import AcrylicWindow as Window
else:
    from qframelesswindow import FramelessWindow as Window


class LoginDialog(Window, login_dialog.LoginDialogUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setTitleBar(SplitTitleBar(self))
        self.titleBar.raise_()

        self.windowEffect.setMicaEffect(self.winId(), isDarkMode=isDarkTheme())
        if not isWin11():
            color = QColor(25, 33, 42) if isDarkTheme() else QColor(240, 244, 249)
            self.setStyleSheet(f"LoginWindow{{background: {color.name()}}}")

        self.titleBar.titleLabel.setStyleSheet("""
                    QLabel{
                        background: transparent;
                        font: 13px 'Microsoft YaHei UI';
                        padding: 0 4px;
                        color: white
                    }
                """)

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

        self.setWindowTitle("登录 - 西瓜聊天")
        self.setWindowIcon(QIcon(":/images/leftimg.png"))

    def setWindowTitle(self, a0):
        super().setWindowTitle(a0)
        try:
            self.titleBar.titleLabel.setText(a0)
        except AttributeError:
            pass

    def resizeEvent(self, e):
        super().resizeEvent(e)
        pixmap = QPixmap(":/images/leftimg.png").scaled(
            self.label.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.label.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    window = LoginDialog()
    window.show()
    sys.exit(app.exec())
