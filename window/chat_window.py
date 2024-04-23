from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from qfluentwidgets import *
from qfluentwidgets import FluentIcon as Icon
import sys

setThemeColor("#0078d4")
try:
    from .message_box import *
    from . import account_widget
    from . import res
except ImportError:
    from message_box import *
    import account_widget
    import res


class TrayIcon(QSystemTrayIcon):
    show_event = pyqtSignal()
    exit_event = pyqtSignal()

    def __init__(self, parent: MSFluentWindow):
        super().__init__()
        self.setIcon(parent.windowIcon())

        self.menu = SystemTrayMenu(parent=parent)
        self.menu.addActions([
            Action(text='显示主窗口', triggered=lambda: self.show_event.emit()),
            Action(text='退出', triggered=lambda: self.exit_event.emit()),
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
        self.init_tray_icon()
        self.init_interface()
        self.init_navigation()
        self.splashScreen.finish()

    def init_window(self):
        self.resize(900, 700)
        self.setWindowTitle("西瓜聊天")
        self.setWindowIcon(QIcon(":/icon/icon.png"))

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

    def init_tray_icon(self):
        self.tray_icon = TrayIcon(self)
        self.tray_icon.show_event.connect(self.show)
        self.tray_icon.exit_event.connect(QCoreApplication.instance().quit)
        self.tray_icon.show()

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
            onClick=self.be_friend,
            selectable=False,
            position=NavigationItemPosition.SCROLL,
        )
        self.navigationInterface.addItem(
            routeKey='create_room',
            icon=Icon.ALBUM,
            text='创建房间',
            onClick=self.create_room,
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

    def be_friend(self):
        w = InfoMessageBox("提示", "添加成功", self)
        w.exec()

    def create_room(self):
        w = InfoMessageBox("提示", "创建成功", self)
        w.exec()

    def closeEvent(self, a0):
        a0.ignore()
        self.hide()


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec())
