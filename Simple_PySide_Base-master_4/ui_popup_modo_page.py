# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popup_modo_page.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc
import files_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(451, 300)
        Dialog.setStyleSheet(u"background-color: rgb(44,49,60);")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 450, 31))
        self.frame.setStyleSheet(u"background-color: rgba(27,29,35,200);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.minimize_modo_page = QPushButton(self.frame)
        self.minimize_modo_page.setObjectName(u"minimize_modo_page")
        self.minimize_modo_page.setGeometry(QRect(330, 0, 40, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minimize_modo_page.sizePolicy().hasHeightForWidth())
        self.minimize_modo_page.setSizePolicy(sizePolicy)
        self.minimize_modo_page.setMinimumSize(QSize(40, 0))
        self.minimize_modo_page.setMaximumSize(QSize(40, 16777215))
        self.minimize_modo_page.setStyleSheet(u"QPushButton {	\n"
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
        self.minimize_modo_page.setIcon(icon)
        self.maximize_modo_page = QPushButton(self.frame)
        self.maximize_modo_page.setObjectName(u"maximize_modo_page")
        self.maximize_modo_page.setGeometry(QRect(370, 0, 40, 31))
        sizePolicy.setHeightForWidth(self.maximize_modo_page.sizePolicy().hasHeightForWidth())
        self.maximize_modo_page.setSizePolicy(sizePolicy)
        self.maximize_modo_page.setMinimumSize(QSize(40, 0))
        self.maximize_modo_page.setMaximumSize(QSize(40, 16777215))
        self.maximize_modo_page.setStyleSheet(u"QPushButton {	\n"
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
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_modo_page.setIcon(icon1)
        self.close_modo_page = QPushButton(self.frame)
        self.close_modo_page.setObjectName(u"close_modo_page")
        self.close_modo_page.setGeometry(QRect(410, 0, 40, 31))
        sizePolicy.setHeightForWidth(self.close_modo_page.sizePolicy().hasHeightForWidth())
        self.close_modo_page.setSizePolicy(sizePolicy)
        self.close_modo_page.setMinimumSize(QSize(40, 0))
        self.close_modo_page.setMaximumSize(QSize(40, 16777215))
        self.close_modo_page.setStyleSheet(u"QPushButton {	\n"
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
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_modo_page.setIcon(icon2)
        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 270, 450, 31))
        self.frame_2.setStyleSheet(u"background-color: rgba(27,29,35,200);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.overwrite_label = QLabel(Dialog)
        self.overwrite_label.setObjectName(u"overwrite_label")
        self.overwrite_label.setGeometry(QRect(135, 50, 191, 51))
        self.overwrite_label.setStyleSheet(u"QLabel {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 20px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;     \n"
"	background-color: transparent;      \n"
"\n"
"}")
        self.overwrite_label_2 = QLabel(Dialog)
        self.overwrite_label_2.setObjectName(u"overwrite_label_2")
        self.overwrite_label_2.setGeometry(QRect(20, 150, 171, 51))
        self.overwrite_label_2.setStyleSheet(u"QLabel {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 20px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: rgb(250,50,50);				 /* Color del texto */\n"
"	padding: 10px;     \n"
"	background-color: transparent;      \n"
"\n"
"}")
        self.overwrite_label_3 = QLabel(Dialog)
        self.overwrite_label_3.setObjectName(u"overwrite_label_3")
        self.overwrite_label_3.setGeometry(QRect(270, 150, 171, 51))
        self.overwrite_label_3.setStyleSheet(u"QLabel {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 20px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: rgba(75,150,200);				 /* Color del texto */\n"
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
        self.minimize_modo_page.setToolTip(QCoreApplication.translate("Dialog", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimize_modo_page.setText("")
#if QT_CONFIG(tooltip)
        self.maximize_modo_page.setToolTip(QCoreApplication.translate("Dialog", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximize_modo_page.setText("")
#if QT_CONFIG(tooltip)
        self.close_modo_page.setToolTip(QCoreApplication.translate("Dialog", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.close_modo_page.setText("")
        self.overwrite_label.setText(QCoreApplication.translate("Dialog", u"Select new Page:", None))
        self.overwrite_label_2.setText(QCoreApplication.translate("Dialog", u"[Menu]: Cancel", None))
        self.overwrite_label_3.setText(QCoreApplication.translate("Dialog", u"[F1-F10]: Page", None))
    # retranslateUi

