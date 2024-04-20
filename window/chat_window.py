from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from qfluentwidgets import *
from qfluentwidgets import FluentIcon as Icon
import sys

setThemeColor("#0078d4")


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

        self.init_window()
        self.init_navigation()

    def init_window(self):
        self.resize(900, 700)
        self.setWindowTitle("西瓜聊天")

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

    def init_navigation(self):
        self.chat_interface = Widget("Chat Frame", self)
        self.friend_interface = Widget("Friend Frame", self)
        self.settings_interface = Widget("Settings Frame", self)
        self.account_interface = Widget("Account Frame", self)

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

        # self.navigationInterface.addWidget(
        #     routeKey='account',
        #     widget=NavigationAvatarWidget("abc", "ui/login_dialog/res/leftimg.png"),
        #     onClick=lambda: ...,
        #     position=NavigationItemPosition.BOTTOM,
        # )
        self.addSubInterface(
            self.account_interface,
            QIcon("ui/login_dialog/res/leftimg.png"),
            'zhiyiYo',
            position=NavigationItemPosition.BOTTOM
        )
        self.addSubInterface(
            self.settings_interface,
            Icon.SETTING,
            '设置',
            position=NavigationItemPosition.BOTTOM
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    window = ChatWindow()
    window.show()

    sys.exit(app.exec())
