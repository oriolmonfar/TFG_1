# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popup_confirm_no_connection.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 297)
        Dialog.setStyleSheet(u"background-color: rgb(44,49,60);")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-1, -1, 401, 31))
        self.frame.setStyleSheet(u"background-color: rgba(27,29,35,200);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.minimize_noconn = QPushButton(self.frame)
        self.minimize_noconn.setObjectName(u"minimize_noconn")
        self.minimize_noconn.setGeometry(QRect(280, 0, 40, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minimize_noconn.sizePolicy().hasHeightForWidth())
        self.minimize_noconn.setSizePolicy(sizePolicy)
        self.minimize_noconn.setMinimumSize(QSize(40, 0))
        self.minimize_noconn.setMaximumSize(QSize(40, 16777215))
        self.minimize_noconn.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_noconn.setIcon(icon)
        self.close_noconn = QPushButton(self.frame)
        self.close_noconn.setObjectName(u"close_noconn")
        self.close_noconn.setGeometry(QRect(360, 0, 40, 31))
        sizePolicy.setHeightForWidth(self.close_noconn.sizePolicy().hasHeightForWidth())
        self.close_noconn.setSizePolicy(sizePolicy)
        self.close_noconn.setMinimumSize(QSize(40, 0))
        self.close_noconn.setMaximumSize(QSize(40, 16777215))
        self.close_noconn.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_noconn.setIcon(icon1)
        self.maximize_noconn = QPushButton(self.frame)
        self.maximize_noconn.setObjectName(u"maximize_noconn")
        self.maximize_noconn.setGeometry(QRect(320, 0, 40, 31))
        sizePolicy.setHeightForWidth(self.maximize_noconn.sizePolicy().hasHeightForWidth())
        self.maximize_noconn.setSizePolicy(sizePolicy)
        self.maximize_noconn.setMinimumSize(QSize(40, 0))
        self.maximize_noconn.setMaximumSize(QSize(40, 16777215))
        self.maximize_noconn.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_noconn.setIcon(icon2)
        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 270, 401, 31))
        self.frame_2.setStyleSheet(u"background-color: rgba(27,29,35,200);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 120, 401, 51))
        self.label.setStyleSheet(u"QLabel {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 20px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;     \n"
"	background-color: transparent;      \n"
"\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.minimize_noconn.setToolTip(QCoreApplication.translate("Dialog", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimize_noconn.setText("")
#if QT_CONFIG(tooltip)
        self.close_noconn.setToolTip(QCoreApplication.translate("Dialog", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.close_noconn.setText("")
#if QT_CONFIG(tooltip)
        self.maximize_noconn.setToolTip(QCoreApplication.translate("Dialog", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximize_noconn.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"There is no connection with this vMix!", None))
    # retranslateUi

