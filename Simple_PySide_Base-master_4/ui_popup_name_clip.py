# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popup_name_clip.ui'
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
        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 440, 921, 41))
        self.frame_2.setStyleSheet(u"background-color: rgba(27,29,35,200);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
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
        self.minimize_nameclip = QPushButton(self.frame_btns_right)
        self.minimize_nameclip.setObjectName(u"minimize_nameclip")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.minimize_nameclip.sizePolicy().hasHeightForWidth())
        self.minimize_nameclip.setSizePolicy(sizePolicy1)
        self.minimize_nameclip.setMinimumSize(QSize(40, 0))
        self.minimize_nameclip.setMaximumSize(QSize(40, 16777215))
        self.minimize_nameclip.setStyleSheet(u"QPushButton {	\n"
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
        self.minimize_nameclip.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.minimize_nameclip)

        self.maximize_nameclip = QPushButton(self.frame_btns_right)
        self.maximize_nameclip.setObjectName(u"maximize_nameclip")
        sizePolicy1.setHeightForWidth(self.maximize_nameclip.sizePolicy().hasHeightForWidth())
        self.maximize_nameclip.setSizePolicy(sizePolicy1)
        self.maximize_nameclip.setMinimumSize(QSize(40, 0))
        self.maximize_nameclip.setMaximumSize(QSize(40, 16777215))
        self.maximize_nameclip.setStyleSheet(u"QPushButton {	\n"
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
        self.maximize_nameclip.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.maximize_nameclip)

        self.close_nameclip = QPushButton(self.frame_btns_right)
        self.close_nameclip.setObjectName(u"close_nameclip")
        sizePolicy1.setHeightForWidth(self.close_nameclip.sizePolicy().hasHeightForWidth())
        self.close_nameclip.setSizePolicy(sizePolicy1)
        self.close_nameclip.setMinimumSize(QSize(40, 0))
        self.close_nameclip.setMaximumSize(QSize(40, 16777215))
        self.close_nameclip.setStyleSheet(u"QPushButton {	\n"
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
        self.close_nameclip.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.close_nameclip)

        self.frame_6 = QFrame(Dialog)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(350, 390, 571, 51))
        self.frame_6.setStyleSheet(u"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 2px;\n"
"	background-color: rgba(40,40,40,200);\n"
"	border: 2px solid rgba(200,200,200,200);  /* Borde blanco con transparencia */")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.nameclip_delete = QPushButton(self.frame_6)
        self.nameclip_delete.setObjectName(u"nameclip_delete")
        self.nameclip_delete.setGeometry(QRect(2, 0, 291, 51))
        self.nameclip_delete.setStyleSheet(u"QPushButton {\n"
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
        self.nameclip_confirm = QPushButton(self.frame_6)
        self.nameclip_confirm.setObjectName(u"nameclip_confirm")
        self.nameclip_confirm.setGeometry(QRect(290, 0, 281, 51))
        self.nameclip_confirm.setStyleSheet(u"QPushButton {\n"
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
        self.frame_5 = QFrame(Dialog)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(350, 40, 571, 351))
        self.frame_5.setStyleSheet(u"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 2px;\n"
"	background-color: rgba(40,40,40,200);\n"
"	border: 2px solid rgba(200,200,200,200); ")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.nameclip_1 = QPushButton(self.frame_5)
        self.nameclip_1.setObjectName(u"nameclip_1")
        self.nameclip_1.setGeometry(QRect(50, 60, 51, 61))
        self.nameclip_1.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_2 = QPushButton(self.frame_5)
        self.nameclip_2.setObjectName(u"nameclip_2")
        self.nameclip_2.setGeometry(QRect(100, 60, 51, 61))
        self.nameclip_2.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_3 = QPushButton(self.frame_5)
        self.nameclip_3.setObjectName(u"nameclip_3")
        self.nameclip_3.setGeometry(QRect(150, 60, 51, 61))
        self.nameclip_3.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_5 = QPushButton(self.frame_5)
        self.nameclip_5.setObjectName(u"nameclip_5")
        self.nameclip_5.setGeometry(QRect(250, 60, 41, 61))
        self.nameclip_5.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_6 = QPushButton(self.frame_5)
        self.nameclip_6.setObjectName(u"nameclip_6")
        self.nameclip_6.setGeometry(QRect(290, 60, 51, 61))
        self.nameclip_6.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_4 = QPushButton(self.frame_5)
        self.nameclip_4.setObjectName(u"nameclip_4")
        self.nameclip_4.setGeometry(QRect(200, 60, 51, 61))
        self.nameclip_4.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_8 = QPushButton(self.frame_5)
        self.nameclip_8.setObjectName(u"nameclip_8")
        self.nameclip_8.setGeometry(QRect(390, 60, 51, 61))
        self.nameclip_8.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_9 = QPushButton(self.frame_5)
        self.nameclip_9.setObjectName(u"nameclip_9")
        self.nameclip_9.setGeometry(QRect(440, 60, 51, 61))
        self.nameclip_9.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_7 = QPushButton(self.frame_5)
        self.nameclip_7.setObjectName(u"nameclip_7")
        self.nameclip_7.setGeometry(QRect(340, 60, 51, 61))
        self.nameclip_7.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_0 = QPushButton(self.frame_5)
        self.nameclip_0.setObjectName(u"nameclip_0")
        self.nameclip_0.setGeometry(QRect(490, 60, 41, 61))
        self.nameclip_0.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_punt = QPushButton(self.frame_5)
        self.nameclip_punt.setObjectName(u"nameclip_punt")
        self.nameclip_punt.setGeometry(QRect(440, 240, 51, 61))
        self.nameclip_punt.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_dospunts = QPushButton(self.frame_5)
        self.nameclip_dospunts.setObjectName(u"nameclip_dospunts")
        self.nameclip_dospunts.setGeometry(QRect(490, 240, 41, 61))
        self.nameclip_dospunts.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_E = QPushButton(self.frame_5)
        self.nameclip_E.setObjectName(u"nameclip_E")
        self.nameclip_E.setGeometry(QRect(150, 120, 51, 61))
        self.nameclip_E.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_R = QPushButton(self.frame_5)
        self.nameclip_R.setObjectName(u"nameclip_R")
        self.nameclip_R.setGeometry(QRect(200, 120, 51, 61))
        self.nameclip_R.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_Y = QPushButton(self.frame_5)
        self.nameclip_Y.setObjectName(u"nameclip_Y")
        self.nameclip_Y.setGeometry(QRect(290, 120, 51, 61))
        self.nameclip_Y.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_U = QPushButton(self.frame_5)
        self.nameclip_U.setObjectName(u"nameclip_U")
        self.nameclip_U.setGeometry(QRect(340, 120, 51, 61))
        self.nameclip_U.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_I = QPushButton(self.frame_5)
        self.nameclip_I.setObjectName(u"nameclip_I")
        self.nameclip_I.setGeometry(QRect(390, 120, 51, 61))
        self.nameclip_I.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_Q = QPushButton(self.frame_5)
        self.nameclip_Q.setObjectName(u"nameclip_Q")
        self.nameclip_Q.setGeometry(QRect(50, 120, 51, 61))
        self.nameclip_Q.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_W = QPushButton(self.frame_5)
        self.nameclip_W.setObjectName(u"nameclip_W")
        self.nameclip_W.setGeometry(QRect(100, 120, 51, 61))
        self.nameclip_W.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_O = QPushButton(self.frame_5)
        self.nameclip_O.setObjectName(u"nameclip_O")
        self.nameclip_O.setGeometry(QRect(440, 120, 51, 61))
        self.nameclip_O.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_T = QPushButton(self.frame_5)
        self.nameclip_T.setObjectName(u"nameclip_T")
        self.nameclip_T.setGeometry(QRect(250, 120, 41, 61))
        self.nameclip_T.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_P = QPushButton(self.frame_5)
        self.nameclip_P.setObjectName(u"nameclip_P")
        self.nameclip_P.setGeometry(QRect(490, 120, 41, 61))
        self.nameclip_P.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_barra = QPushButton(self.frame_5)
        self.nameclip_barra.setObjectName(u"nameclip_barra")
        self.nameclip_barra.setGeometry(QRect(490, 180, 41, 61))
        self.nameclip_barra.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_F = QPushButton(self.frame_5)
        self.nameclip_F.setObjectName(u"nameclip_F")
        self.nameclip_F.setGeometry(QRect(200, 180, 51, 61))
        self.nameclip_F.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_L = QPushButton(self.frame_5)
        self.nameclip_L.setObjectName(u"nameclip_L")
        self.nameclip_L.setGeometry(QRect(440, 180, 51, 61))
        self.nameclip_L.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_H = QPushButton(self.frame_5)
        self.nameclip_H.setObjectName(u"nameclip_H")
        self.nameclip_H.setGeometry(QRect(290, 180, 51, 61))
        self.nameclip_H.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_J = QPushButton(self.frame_5)
        self.nameclip_J.setObjectName(u"nameclip_J")
        self.nameclip_J.setGeometry(QRect(340, 180, 51, 61))
        self.nameclip_J.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_D = QPushButton(self.frame_5)
        self.nameclip_D.setObjectName(u"nameclip_D")
        self.nameclip_D.setGeometry(QRect(150, 180, 51, 61))
        self.nameclip_D.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_G = QPushButton(self.frame_5)
        self.nameclip_G.setObjectName(u"nameclip_G")
        self.nameclip_G.setGeometry(QRect(250, 180, 41, 61))
        self.nameclip_G.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_K = QPushButton(self.frame_5)
        self.nameclip_K.setObjectName(u"nameclip_K")
        self.nameclip_K.setGeometry(QRect(390, 180, 51, 61))
        self.nameclip_K.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_A = QPushButton(self.frame_5)
        self.nameclip_A.setObjectName(u"nameclip_A")
        self.nameclip_A.setGeometry(QRect(50, 180, 51, 61))
        self.nameclip_A.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_S = QPushButton(self.frame_5)
        self.nameclip_S.setObjectName(u"nameclip_S")
        self.nameclip_S.setGeometry(QRect(100, 180, 51, 61))
        self.nameclip_S.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_V = QPushButton(self.frame_5)
        self.nameclip_V.setObjectName(u"nameclip_V")
        self.nameclip_V.setGeometry(QRect(200, 240, 51, 61))
        self.nameclip_V.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_Z = QPushButton(self.frame_5)
        self.nameclip_Z.setObjectName(u"nameclip_Z")
        self.nameclip_Z.setGeometry(QRect(50, 240, 51, 61))
        self.nameclip_Z.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_B = QPushButton(self.frame_5)
        self.nameclip_B.setObjectName(u"nameclip_B")
        self.nameclip_B.setGeometry(QRect(250, 240, 41, 61))
        self.nameclip_B.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_M = QPushButton(self.frame_5)
        self.nameclip_M.setObjectName(u"nameclip_M")
        self.nameclip_M.setGeometry(QRect(340, 240, 51, 61))
        self.nameclip_M.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_barra_baixa = QPushButton(self.frame_5)
        self.nameclip_barra_baixa.setObjectName(u"nameclip_barra_baixa")
        self.nameclip_barra_baixa.setGeometry(QRect(390, 240, 51, 61))
        self.nameclip_barra_baixa.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_X = QPushButton(self.frame_5)
        self.nameclip_X.setObjectName(u"nameclip_X")
        self.nameclip_X.setGeometry(QRect(100, 240, 51, 61))
        self.nameclip_X.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_N = QPushButton(self.frame_5)
        self.nameclip_N.setObjectName(u"nameclip_N")
        self.nameclip_N.setGeometry(QRect(290, 240, 51, 61))
        self.nameclip_N.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.nameclip_C = QPushButton(self.frame_5)
        self.nameclip_C.setObjectName(u"nameclip_C")
        self.nameclip_C.setGeometry(QRect(150, 240, 51, 61))
        self.nameclip_C.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.textedit_clipname_name = QTextEdit(Dialog)
        self.textedit_clipname_name.setObjectName(u"textedit_clipname_name")
        self.textedit_clipname_name.setGeometry(QRect(40, 210, 271, 61))
        self.textedit_clipname_name.setStyleSheet(u"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 22px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	background-color: transparent;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */")
        self.label_name = QLabel(Dialog)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(120, 160, 131, 41))
        self.label_name.setStyleSheet(u"QLabel {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 24px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	background-color: transparent;\n"
"}\n"
"")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.minimize_nameclip.setToolTip(QCoreApplication.translate("Dialog", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimize_nameclip.setText("")
#if QT_CONFIG(tooltip)
        self.maximize_nameclip.setToolTip(QCoreApplication.translate("Dialog", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximize_nameclip.setText("")
#if QT_CONFIG(tooltip)
        self.close_nameclip.setToolTip(QCoreApplication.translate("Dialog", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.close_nameclip.setText("")
        self.nameclip_delete.setText(QCoreApplication.translate("Dialog", u"Delete", None))
        self.nameclip_confirm.setText(QCoreApplication.translate("Dialog", u"Confirm", None))
        self.nameclip_1.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.nameclip_2.setText(QCoreApplication.translate("Dialog", u"2", None))
        self.nameclip_3.setText(QCoreApplication.translate("Dialog", u"3", None))
        self.nameclip_5.setText(QCoreApplication.translate("Dialog", u"5", None))
        self.nameclip_6.setText(QCoreApplication.translate("Dialog", u"6", None))
        self.nameclip_4.setText(QCoreApplication.translate("Dialog", u"4", None))
        self.nameclip_8.setText(QCoreApplication.translate("Dialog", u"8", None))
        self.nameclip_9.setText(QCoreApplication.translate("Dialog", u"9", None))
        self.nameclip_7.setText(QCoreApplication.translate("Dialog", u"7", None))
        self.nameclip_0.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.nameclip_punt.setText(QCoreApplication.translate("Dialog", u".", None))
        self.nameclip_dospunts.setText(QCoreApplication.translate("Dialog", u":", None))
        self.nameclip_E.setText(QCoreApplication.translate("Dialog", u"E", None))
        self.nameclip_R.setText(QCoreApplication.translate("Dialog", u"R", None))
        self.nameclip_Y.setText(QCoreApplication.translate("Dialog", u"Y", None))
        self.nameclip_U.setText(QCoreApplication.translate("Dialog", u"U", None))
        self.nameclip_I.setText(QCoreApplication.translate("Dialog", u"I", None))
        self.nameclip_Q.setText(QCoreApplication.translate("Dialog", u"Q", None))
        self.nameclip_W.setText(QCoreApplication.translate("Dialog", u"W", None))
        self.nameclip_O.setText(QCoreApplication.translate("Dialog", u"O", None))
        self.nameclip_T.setText(QCoreApplication.translate("Dialog", u"T", None))
        self.nameclip_P.setText(QCoreApplication.translate("Dialog", u"P", None))
        self.nameclip_barra.setText(QCoreApplication.translate("Dialog", u"-", None))
        self.nameclip_F.setText(QCoreApplication.translate("Dialog", u"F", None))
        self.nameclip_L.setText(QCoreApplication.translate("Dialog", u"L", None))
        self.nameclip_H.setText(QCoreApplication.translate("Dialog", u"H", None))
        self.nameclip_J.setText(QCoreApplication.translate("Dialog", u"J", None))
        self.nameclip_D.setText(QCoreApplication.translate("Dialog", u"D", None))
        self.nameclip_G.setText(QCoreApplication.translate("Dialog", u"G", None))
        self.nameclip_K.setText(QCoreApplication.translate("Dialog", u"K", None))
        self.nameclip_A.setText(QCoreApplication.translate("Dialog", u"A", None))
        self.nameclip_S.setText(QCoreApplication.translate("Dialog", u"S", None))
        self.nameclip_V.setText(QCoreApplication.translate("Dialog", u"V", None))
        self.nameclip_Z.setText(QCoreApplication.translate("Dialog", u"Z", None))
        self.nameclip_B.setText(QCoreApplication.translate("Dialog", u"B", None))
        self.nameclip_M.setText(QCoreApplication.translate("Dialog", u"M", None))
        self.nameclip_barra_baixa.setText(QCoreApplication.translate("Dialog", u"_", None))
        self.nameclip_X.setText(QCoreApplication.translate("Dialog", u"X", None))
        self.nameclip_N.setText(QCoreApplication.translate("Dialog", u"N", None))
        self.nameclip_C.setText(QCoreApplication.translate("Dialog", u"C", None))
        self.label_name.setText(QCoreApplication.translate("Dialog", u"Clip Name", None))
    # retranslateUi

