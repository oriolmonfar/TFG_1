# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popup_searchtc.ui'
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
        Dialog.resize(924, 480)
        Dialog.setStyleSheet(u"background-color: rgb(44,49,60);")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 931, 41))
        self.frame.setStyleSheet(u"background-color: rgba(27,29,35,200);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_btns_right = QFrame(self.frame)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        self.frame_btns_right.setGeometry(QRect(800, 0, 120, 42))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.minimize_searchtc = QPushButton(self.frame_btns_right)
        self.minimize_searchtc.setObjectName(u"minimize_searchtc")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.minimize_searchtc.sizePolicy().hasHeightForWidth())
        self.minimize_searchtc.setSizePolicy(sizePolicy1)
        self.minimize_searchtc.setMinimumSize(QSize(40, 0))
        self.minimize_searchtc.setMaximumSize(QSize(40, 16777215))
        self.minimize_searchtc.setStyleSheet(u"QPushButton {	\n"
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
        self.minimize_searchtc.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.minimize_searchtc)

        self.maximize_searchtc = QPushButton(self.frame_btns_right)
        self.maximize_searchtc.setObjectName(u"maximize_searchtc")
        sizePolicy1.setHeightForWidth(self.maximize_searchtc.sizePolicy().hasHeightForWidth())
        self.maximize_searchtc.setSizePolicy(sizePolicy1)
        self.maximize_searchtc.setMinimumSize(QSize(40, 0))
        self.maximize_searchtc.setMaximumSize(QSize(40, 16777215))
        self.maximize_searchtc.setStyleSheet(u"QPushButton {	\n"
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
        self.maximize_searchtc.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.maximize_searchtc)

        self.close_searchtc = QPushButton(self.frame_btns_right)
        self.close_searchtc.setObjectName(u"close_searchtc")
        sizePolicy1.setHeightForWidth(self.close_searchtc.sizePolicy().hasHeightForWidth())
        self.close_searchtc.setSizePolicy(sizePolicy1)
        self.close_searchtc.setMinimumSize(QSize(40, 0))
        self.close_searchtc.setMaximumSize(QSize(40, 16777215))
        self.close_searchtc.setStyleSheet(u"QPushButton {	\n"
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
        self.close_searchtc.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.close_searchtc)

        self.searchtc_textedit = QTextEdit(Dialog)
        self.searchtc_textedit.setObjectName(u"searchtc_textedit")
        self.searchtc_textedit.setGeometry(QRect(120, 220, 271, 61))
        self.searchtc_textedit.setStyleSheet(u"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 22px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	background-color: transparent;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */")
        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(500, 40, 421, 351))
        self.frame_2.setStyleSheet(u"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 2px;\n"
"	background-color: rgba(40,40,40,200);\n"
"	border: 2px solid rgba(200,200,200,200); ")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.searchtc_1 = QPushButton(self.frame_2)
        self.searchtc_1.setObjectName(u"searchtc_1")
        self.searchtc_1.setGeometry(QRect(100, 60, 71, 61))
        self.searchtc_1.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.searchtc_2 = QPushButton(self.frame_2)
        self.searchtc_2.setObjectName(u"searchtc_2")
        self.searchtc_2.setGeometry(QRect(170, 60, 71, 61))
        self.searchtc_2.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.searchtc_3 = QPushButton(self.frame_2)
        self.searchtc_3.setObjectName(u"searchtc_3")
        self.searchtc_3.setGeometry(QRect(240, 60, 71, 61))
        self.searchtc_3.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.searchtc_5 = QPushButton(self.frame_2)
        self.searchtc_5.setObjectName(u"searchtc_5")
        self.searchtc_5.setGeometry(QRect(170, 120, 71, 61))
        self.searchtc_5.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.searchtc_6 = QPushButton(self.frame_2)
        self.searchtc_6.setObjectName(u"searchtc_6")
        self.searchtc_6.setGeometry(QRect(240, 120, 71, 61))
        self.searchtc_6.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.searchtc_4 = QPushButton(self.frame_2)
        self.searchtc_4.setObjectName(u"searchtc_4")
        self.searchtc_4.setGeometry(QRect(100, 120, 71, 61))
        self.searchtc_4.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.searchtc_8 = QPushButton(self.frame_2)
        self.searchtc_8.setObjectName(u"searchtc_8")
        self.searchtc_8.setGeometry(QRect(170, 180, 71, 61))
        self.searchtc_8.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.searchtc_9 = QPushButton(self.frame_2)
        self.searchtc_9.setObjectName(u"searchtc_9")
        self.searchtc_9.setGeometry(QRect(240, 180, 71, 61))
        self.searchtc_9.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.searchtc_7 = QPushButton(self.frame_2)
        self.searchtc_7.setObjectName(u"searchtc_7")
        self.searchtc_7.setGeometry(QRect(100, 180, 71, 61))
        self.searchtc_7.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.searchtc_0 = QPushButton(self.frame_2)
        self.searchtc_0.setObjectName(u"searchtc_0")
        self.searchtc_0.setGeometry(QRect(170, 240, 71, 61))
        self.searchtc_0.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.searchtc_dospunts = QPushButton(self.frame_2)
        self.searchtc_dospunts.setObjectName(u"searchtc_dospunts")
        self.searchtc_dospunts.setGeometry(QRect(110, 240, 71, 61))
        self.searchtc_dospunts.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.searchtc_punt_2 = QPushButton(self.frame_2)
        self.searchtc_punt_2.setObjectName(u"searchtc_punt_2")
        self.searchtc_punt_2.setGeometry(QRect(240, 240, 71, 61))
        self.searchtc_punt_2.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(500, 390, 421, 51))
        self.frame_3.setStyleSheet(u"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 2px;\n"
"	background-color: transparent;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.searchtc_delete = QPushButton(self.frame_3)
        self.searchtc_delete.setObjectName(u"searchtc_delete")
        self.searchtc_delete.setGeometry(QRect(2, 0, 211, 51))
        self.searchtc_delete.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 20px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;   \n"
"	background-color: rgba(250,50,50,150);        \n"
"	border: 2px solid rgba(200,200,200,200);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(250,50,50,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.searchtc_confirm = QPushButton(self.frame_3)
        self.searchtc_confirm.setObjectName(u"searchtc_confirm")
        self.searchtc_confirm.setGeometry(QRect(210, 0, 211, 51))
        self.searchtc_confirm.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 20px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;  \n"
"	background-color: rgba(75,175,250,150);         \n"
"	border: 2px solid rgba(200,200,200,200);   /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 170, 101, 20))
        self.label.setStyleSheet(u"QLabel {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 24px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	background-color: transparent;\n"
"}")
        self.frame_4 = QFrame(Dialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 440, 931, 41))
        self.frame_4.setStyleSheet(u"background-color: rgba(27,29,35,200);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.minimize_searchtc.setToolTip(QCoreApplication.translate("Dialog", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimize_searchtc.setText("")
#if QT_CONFIG(tooltip)
        self.maximize_searchtc.setToolTip(QCoreApplication.translate("Dialog", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximize_searchtc.setText("")
#if QT_CONFIG(tooltip)
        self.close_searchtc.setToolTip(QCoreApplication.translate("Dialog", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.close_searchtc.setText("")
        self.searchtc_1.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.searchtc_2.setText(QCoreApplication.translate("Dialog", u"2", None))
        self.searchtc_3.setText(QCoreApplication.translate("Dialog", u"3", None))
        self.searchtc_5.setText(QCoreApplication.translate("Dialog", u"5", None))
        self.searchtc_6.setText(QCoreApplication.translate("Dialog", u"6", None))
        self.searchtc_4.setText(QCoreApplication.translate("Dialog", u"4", None))
        self.searchtc_8.setText(QCoreApplication.translate("Dialog", u"8", None))
        self.searchtc_9.setText(QCoreApplication.translate("Dialog", u"9", None))
        self.searchtc_7.setText(QCoreApplication.translate("Dialog", u"7", None))
        self.searchtc_0.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.searchtc_dospunts.setText(QCoreApplication.translate("Dialog", u":", None))
        self.searchtc_punt_2.setText(QCoreApplication.translate("Dialog", u".", None))
        self.searchtc_delete.setText(QCoreApplication.translate("Dialog", u"Delete", None))
        self.searchtc_confirm.setText(QCoreApplication.translate("Dialog", u"Confirm", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Go to TC", None))
    # retranslateUi

