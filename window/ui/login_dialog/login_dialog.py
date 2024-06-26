# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(900, 550)
        LoginDialog.setMinimumSize(QtCore.QSize(750, 530))
        LoginDialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginDialog.setWindowIcon(icon)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(LoginDialog)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(LoginDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/leftimg.png"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.frame = QtWidgets.QFrame(LoginDialog)
        self.frame.setMinimumSize(QtCore.QSize(360, 0))
        self.frame.setMaximumSize(QtCore.QSize(360, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 79, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.icon = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon.sizePolicy().hasHeightForWidth())
        self.icon.setSizePolicy(sizePolicy)
        self.icon.setMinimumSize(QtCore.QSize(100, 100))
        self.icon.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.icon.setFont(font)
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap(":/icon/icon.png"))
        self.icon.setScaledContents(True)
        self.icon.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.icon.setObjectName("icon")
        self.horizontalLayout.addWidget(self.icon)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.BodyLabel = BodyLabel(self.frame)
        self.BodyLabel.setObjectName("BodyLabel")
        self.verticalLayout.addWidget(self.BodyLabel)
        self.account = LineEdit(self.frame)
        self.account.setObjectName("account")
        self.verticalLayout.addWidget(self.account)
        self.BodyLabel_2 = BodyLabel(self.frame)
        self.BodyLabel_2.setObjectName("BodyLabel_2")
        self.verticalLayout.addWidget(self.BodyLabel_2)
        self.password = PasswordLineEdit(self.frame)
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password)
        spacerItem2 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.login_btn = PrimaryPushButton(self.frame)
        self.login_btn.setObjectName("login_btn")
        self.verticalLayout.addWidget(self.login_btn)
        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.register_btn = HyperlinkButton(self.frame)
        self.register_btn.setObjectName("register_btn")
        self.verticalLayout.addWidget(self.register_btn)
        spacerItem4 = QtWidgets.QSpacerItem(20, 64, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_2.addWidget(self.frame)

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "登录 - 西瓜聊天"))
        self.BodyLabel.setText(_translate("LoginDialog", "账号"))
        self.BodyLabel_2.setText(_translate("LoginDialog", "密码"))
        self.login_btn.setText(_translate("LoginDialog", "登录"))
        self.register_btn.setText(_translate("LoginDialog", "没有账号？立即注册"))
from qfluentwidgets import BodyLabel, HyperlinkButton, LineEdit, PasswordLineEdit, PrimaryPushButton
from . import res_rc
