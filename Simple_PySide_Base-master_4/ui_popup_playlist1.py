# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popup_playlist_1.ui'
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
        Dialog.resize(924, 480)
        Dialog.setStyleSheet(u"background-color: rgb(44,49,60);")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 921, 41))
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
        self.minimize_myvmix = QPushButton(self.frame_btns_right)
        self.minimize_myvmix.setObjectName(u"minimize_myvmix")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.minimize_myvmix.sizePolicy().hasHeightForWidth())
        self.minimize_myvmix.setSizePolicy(sizePolicy1)
        self.minimize_myvmix.setMinimumSize(QSize(40, 0))
        self.minimize_myvmix.setMaximumSize(QSize(40, 16777215))
        self.minimize_myvmix.setStyleSheet(u"QPushButton {	\n"
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
        self.minimize_myvmix.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.minimize_myvmix)

        self.maximize_myvmix = QPushButton(self.frame_btns_right)
        self.maximize_myvmix.setObjectName(u"maximize_myvmix")
        sizePolicy1.setHeightForWidth(self.maximize_myvmix.sizePolicy().hasHeightForWidth())
        self.maximize_myvmix.setSizePolicy(sizePolicy1)
        self.maximize_myvmix.setMinimumSize(QSize(40, 0))
        self.maximize_myvmix.setMaximumSize(QSize(40, 16777215))
        self.maximize_myvmix.setStyleSheet(u"QPushButton {	\n"
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
        self.maximize_myvmix.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.maximize_myvmix)

        self.close_myvmix = QPushButton(self.frame_btns_right)
        self.close_myvmix.setObjectName(u"close_myvmix")
        sizePolicy1.setHeightForWidth(self.close_myvmix.sizePolicy().hasHeightForWidth())
        self.close_myvmix.setSizePolicy(sizePolicy1)
        self.close_myvmix.setMinimumSize(QSize(40, 0))
        self.close_myvmix.setMaximumSize(QSize(40, 16777215))
        self.close_myvmix.setStyleSheet(u"QPushButton {	\n"
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
        self.close_myvmix.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.close_myvmix)

        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 440, 921, 41))
        self.frame_3.setStyleSheet(u"background-color: rgba(27,29,35,200);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.estrella1_delete = QPushButton(Dialog)
        self.estrella1_delete.setObjectName(u"estrella1_delete")
        self.estrella1_delete.setGeometry(QRect(670, 40, 71, 51))
        self.estrella1_delete.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;   \n"
"	background-color: rgba(250,50,50,10);        \n"
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
        icon3 = QIcon()
        icon3.addFile(u":/20x20/icons/20x20/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.estrella1_delete.setIcon(icon3)
        self.estrella1_refresh = QPushButton(Dialog)
        self.estrella1_refresh.setObjectName(u"estrella1_refresh")
        self.estrella1_refresh.setGeometry(QRect(140, 40, 71, 51))
        self.estrella1_refresh.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 20px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;  \n"
"	background-color: rgba(75,175,250,10);         \n"
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
        icon4 = QIcon()
        icon4.addFile(u":/20x20/icons/20x20/cil-loop-circular.png", QSize(), QIcon.Normal, QIcon.Off)
        self.estrella1_refresh.setIcon(icon4)
        self.label_estrella1 = QLabel(Dialog)
        self.label_estrella1.setObjectName(u"label_estrella1")
        self.label_estrella1.setGeometry(QRect(140, 40, 601, 51))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_estrella1.setFont(font)
        self.label_estrella1.setStyleSheet(u"QLabel {\n"
"	font \"arial\"\n"
"    font-weight: bold;\n"
"	font-size: 20px;\n"
"	background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_estrella1.setAlignment(Qt.AlignCenter)
        self.list_estrella1 = QListWidget(Dialog)
        self.list_estrella1.setObjectName(u"list_estrella1")
        self.list_estrella1.setGeometry(QRect(140, 90, 601, 351))
        self.list_estrella1.setStyleSheet(u"QListWidget {\n"
"    font-weight: bold;\n"
"    background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_estrella1.raise_()
        self.list_estrella1.raise_()
        self.frame.raise_()
        self.frame_3.raise_()
        self.estrella1_delete.raise_()
        self.estrella1_refresh.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.minimize_myvmix.setToolTip(QCoreApplication.translate("Dialog", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimize_myvmix.setText("")
#if QT_CONFIG(tooltip)
        self.maximize_myvmix.setToolTip(QCoreApplication.translate("Dialog", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximize_myvmix.setText("")
#if QT_CONFIG(tooltip)
        self.close_myvmix.setToolTip(QCoreApplication.translate("Dialog", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.close_myvmix.setText("")
        self.estrella1_delete.setText("")
        self.estrella1_refresh.setText("")
        self.label_estrella1.setText(QCoreApplication.translate("Dialog", u"PLAYLIST 1", None))
    # retranslateUi

