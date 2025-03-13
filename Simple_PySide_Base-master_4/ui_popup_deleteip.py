# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popup_deleteip.ui'
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
        Dialog.resize(452, 319)
        Dialog.setStyleSheet(u"background-color: rgb(44,49,60);")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 60, 331, 51))
        self.label.setStyleSheet(u"QLabel {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 20px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;     \n"
"	background-color: transparent;    \n"
"\n"
"}")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 110, 231, 41))
        self.label_2.setStyleSheet(u"QLabel {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 20px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;     \n"
"	background-color: transparent;    \n"
"\n"
"}")
        self.deleteip_no = QPushButton(Dialog)
        self.deleteip_no.setObjectName(u"deleteip_no")
        self.deleteip_no.setGeometry(QRect(130, 190, 93, 41))
        self.deleteip_no.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;  \n"
"	background-color: rgba(75,150,250,200);         \n"
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
        self.deleteip_yes = QPushButton(Dialog)
        self.deleteip_yes.setObjectName(u"deleteip_yes")
        self.deleteip_yes.setGeometry(QRect(220, 190, 93, 41))
        self.deleteip_yes.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
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
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-1, 0, 451, 41))
        self.frame.setStyleSheet(u"background-color: rgba(27,29,35,200);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.minimize_deleteip = QPushButton(self.frame)
        self.minimize_deleteip.setObjectName(u"minimize_deleteip")
        self.minimize_deleteip.setGeometry(QRect(330, 0, 40, 41))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minimize_deleteip.sizePolicy().hasHeightForWidth())
        self.minimize_deleteip.setSizePolicy(sizePolicy)
        self.minimize_deleteip.setMinimumSize(QSize(40, 0))
        self.minimize_deleteip.setMaximumSize(QSize(40, 16777215))
        self.minimize_deleteip.setStyleSheet(u"QPushButton {	\n"
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
        self.minimize_deleteip.setIcon(icon)
        self.maximize_deleteip = QPushButton(self.frame)
        self.maximize_deleteip.setObjectName(u"maximize_deleteip")
        self.maximize_deleteip.setGeometry(QRect(370, 0, 40, 41))
        sizePolicy.setHeightForWidth(self.maximize_deleteip.sizePolicy().hasHeightForWidth())
        self.maximize_deleteip.setSizePolicy(sizePolicy)
        self.maximize_deleteip.setMinimumSize(QSize(40, 0))
        self.maximize_deleteip.setMaximumSize(QSize(40, 16777215))
        self.maximize_deleteip.setStyleSheet(u"QPushButton {	\n"
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
        self.maximize_deleteip.setIcon(icon1)
        self.close_deleteip = QPushButton(self.frame)
        self.close_deleteip.setObjectName(u"close_deleteip")
        self.close_deleteip.setGeometry(QRect(410, 0, 40, 41))
        sizePolicy.setHeightForWidth(self.close_deleteip.sizePolicy().hasHeightForWidth())
        self.close_deleteip.setSizePolicy(sizePolicy)
        self.close_deleteip.setMinimumSize(QSize(40, 0))
        self.close_deleteip.setMaximumSize(QSize(40, 16777215))
        self.close_deleteip.setStyleSheet(u"QPushButton {	\n"
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
        self.close_deleteip.setIcon(icon2)
        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 280, 451, 31))
        self.frame_2.setStyleSheet(u"background-color: rgba(27,29,35,200);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 30, 21, 251))
        self.frame_3.setStyleSheet(u"background-color: rgba(27,29,35,200);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(Dialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(430, 30, 21, 251))
        self.frame_4.setStyleSheet(u"background-color: rgba(27,29,35,200);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Are you sure you want to delete", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"the vMix connection?", None))
        self.deleteip_no.setText(QCoreApplication.translate("Dialog", u"NO", None))
        self.deleteip_yes.setText(QCoreApplication.translate("Dialog", u"YES", None))
#if QT_CONFIG(tooltip)
        self.minimize_deleteip.setToolTip(QCoreApplication.translate("Dialog", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimize_deleteip.setText("")
#if QT_CONFIG(tooltip)
        self.maximize_deleteip.setToolTip(QCoreApplication.translate("Dialog", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximize_deleteip.setText("")
#if QT_CONFIG(tooltip)
        self.close_deleteip.setToolTip(QCoreApplication.translate("Dialog", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.close_deleteip.setText("")
    # retranslateUi

