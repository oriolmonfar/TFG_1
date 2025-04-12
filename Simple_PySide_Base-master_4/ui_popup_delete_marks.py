# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popup_delete_marks.ui'
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
        Dialog.resize(400, 300)
        Dialog.setStyleSheet(u"background-color: rgb(44,49,60);\n"
"")
        self.confirm_deletemarks_no = QPushButton(Dialog)
        self.confirm_deletemarks_no.setObjectName(u"confirm_deletemarks_no")
        self.confirm_deletemarks_no.setGeometry(QRect(110, 180, 93, 41))
        self.confirm_deletemarks_no.setStyleSheet(u"QPushButton {\n"
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
        self.confirm_deletemarks_yes = QPushButton(Dialog)
        self.confirm_deletemarks_yes.setObjectName(u"confirm_deletemarks_yes")
        self.confirm_deletemarks_yes.setGeometry(QRect(200, 180, 93, 41))
        self.confirm_deletemarks_yes.setStyleSheet(u"QPushButton {\n"
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
        self.frame_6 = QFrame(Dialog)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 0, 401, 31))
        self.frame_6.setStyleSheet(u"background-color: rgba(27,29,35,200);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.close_confirm_deletemarks = QPushButton(self.frame_6)
        self.close_confirm_deletemarks.setObjectName(u"close_confirm_deletemarks")
        self.close_confirm_deletemarks.setGeometry(QRect(360, 0, 40, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_confirm_deletemarks.sizePolicy().hasHeightForWidth())
        self.close_confirm_deletemarks.setSizePolicy(sizePolicy)
        self.close_confirm_deletemarks.setMinimumSize(QSize(40, 0))
        self.close_confirm_deletemarks.setMaximumSize(QSize(40, 16777215))
        self.close_confirm_deletemarks.setStyleSheet(u"QPushButton {	\n"
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
        icon.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_confirm_deletemarks.setIcon(icon)
        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 270, 401, 31))
        self.frame_3.setStyleSheet(u"background-color: rgba(27,29,35,200);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.overwrite_label_2 = QLabel(Dialog)
        self.overwrite_label_2.setObjectName(u"overwrite_label_2")
        self.overwrite_label_2.setGeometry(QRect(50, 60, 311, 81))
        self.overwrite_label_2.setStyleSheet(u"QLabel {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 20px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;     \n"
"	background-color: transparent;      \n"
"\n"
"}")
        self.frame_8 = QFrame(Dialog)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(380, 30, 21, 251))
        self.frame_8.setStyleSheet(u"background-color: rgba(27,29,35,200);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(Dialog)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(0, 20, 21, 251))
        self.frame_7.setStyleSheet(u"background-color: rgba(27,29,35,200);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.confirm_deletemarks_no.setText(QCoreApplication.translate("Dialog", u"NO", None))
        self.confirm_deletemarks_yes.setText(QCoreApplication.translate("Dialog", u"YES", None))
#if QT_CONFIG(tooltip)
        self.close_confirm_deletemarks.setToolTip(QCoreApplication.translate("Dialog", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.close_confirm_deletemarks.setText("")
        self.overwrite_label_2.setText(QCoreApplication.translate("Dialog", u"Do you want to delete marks?", None))
    # retranslateUi

