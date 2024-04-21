from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from qfluentwidgets import *
from qfluentwidgets import FluentIcon as Icon
from qframelesswindow import *
import sys

setThemeColor("#0078d4")
try:
    from . import account_widget
    from . import res
except ImportError:
    import account_widget
    import res


class TrayIcon(QSystemTrayIcon):
    def __init__(self, parent):
        super().__init__()
        self.setIcon(parent.windowIcon())

        self.menu = SystemTrayMenu(parent=parent)
        self.menu.addActions([
            Action('🎤   唱'),
            Action('🕺   跳'),
            Action('🤘🏼   RAP'),
            Action('🎶   Music'),
            Action('🏀   篮球'),
        ])
        self.setContextMenu(self.menu)


class Widget(QFrame):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = SubtitleLabel(text, self)
        self.hBoxLayout = QHBoxLayout(self)

        setFont(self.label, 24)
        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName(text.replace(' ', '-'))


class ChatWindow(MSFluentWindow):
    def __init__(self):
        super().__init__()

        self.chat_interface = None
        self.friend_interface = None
        self.settings_interface = None
        self.account_interface = None
        self.tray_icon = None

        self.init_window()
        self.splashScreen = SplashScreen(self.windowIcon(), self)
        self.splashScreen.setIconSize(QSize(102, 102))

        self.show()
        self.init_interface()
        self.init_navigation()
        self.splashScreen.finish()

    def init_window(self):
        self.resize(900, 700)
        self.setWindowTitle("西瓜聊天")
        self.setWindowIcon(QIcon(":/icon/icon.png"))
        self.tray_icon = TrayIcon(self)
        self.tray_icon.show()

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

    def init_interface(self):
        self.chat_interface = Widget("Chat Frame", self)
        self.friend_interface = Widget("Friend Frame", self)
        self.settings_interface = Widget("Settings Frame", self)
        self.account_interface = account_widget.AccountWidget()

    def init_navigation(self):
        self.addSubInterface(
            self.chat_interface,
            Icon.CHAT,
            '聊天'
        )
        self.addSubInterface(
            self.friend_interface,
            Icon.PEOPLE,
            '好友'
        )

        self.navigationInterface.addItem(
            routeKey='add_friend',
            icon=Icon.ADD_TO,
            text='添加好友',
            onClick=lambda: ...,
            selectable=False,
            position=NavigationItemPosition.SCROLL,
        )
        self.navigationInterface.addItem(
            routeKey='create_room',
            icon=Icon.ALBUM,
            text='创建房间',
            onClick=lambda: ...,
            selectable=False,
            position=NavigationItemPosition.SCROLL,
        )

        self.addSubInterface(
            self.account_interface,
            QIcon("res/icon.png"),
            'user',
            position=NavigationItemPosition.BOTTOM
        )
        self.addSubInterface(
            self.settings_interface,
            Icon.SETTING,
            '设置',
            position=NavigationItemPosition.BOTTOM
        )


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec())
