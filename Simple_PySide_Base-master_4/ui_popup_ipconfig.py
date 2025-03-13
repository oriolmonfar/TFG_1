# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popup_ipconfig.ui'
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
        self.minimize_ipconfig = QPushButton(self.frame_btns_right)
        self.minimize_ipconfig.setObjectName(u"minimize_ipconfig")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.minimize_ipconfig.sizePolicy().hasHeightForWidth())
        self.minimize_ipconfig.setSizePolicy(sizePolicy1)
        self.minimize_ipconfig.setMinimumSize(QSize(40, 0))
        self.minimize_ipconfig.setMaximumSize(QSize(40, 16777215))
        self.minimize_ipconfig.setStyleSheet(u"QPushButton {	\n"
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
        self.minimize_ipconfig.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.minimize_ipconfig)

        self.maximize_ipconfig = QPushButton(self.frame_btns_right)
        self.maximize_ipconfig.setObjectName(u"maximize_ipconfig")
        sizePolicy1.setHeightForWidth(self.maximize_ipconfig.sizePolicy().hasHeightForWidth())
        self.maximize_ipconfig.setSizePolicy(sizePolicy1)
        self.maximize_ipconfig.setMinimumSize(QSize(40, 0))
        self.maximize_ipconfig.setMaximumSize(QSize(40, 16777215))
        self.maximize_ipconfig.setStyleSheet(u"QPushButton {	\n"
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
        self.maximize_ipconfig.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.maximize_ipconfig)

        self.close_ipconfig = QPushButton(self.frame_btns_right)
        self.close_ipconfig.setObjectName(u"close_ipconfig")
        sizePolicy1.setHeightForWidth(self.close_ipconfig.sizePolicy().hasHeightForWidth())
        self.close_ipconfig.setSizePolicy(sizePolicy1)
        self.close_ipconfig.setMinimumSize(QSize(40, 0))
        self.close_ipconfig.setMaximumSize(QSize(40, 16777215))
        self.close_ipconfig.setStyleSheet(u"QPushButton {	\n"
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
        self.close_ipconfig.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.close_ipconfig)

        self.label_IP = QLabel(Dialog)
        self.label_IP.setObjectName(u"label_IP")
        self.label_IP.setGeometry(QRect(70, 100, 191, 20))
        self.label_IP.setStyleSheet(u"QLabel {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 24px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	background-color: transparent;\n"
"}\n"
"")
        self.textedit_ipconfig = QTextEdit(Dialog)
        self.textedit_ipconfig.setObjectName(u"textedit_ipconfig")
        self.textedit_ipconfig.setGeometry(QRect(30, 140, 271, 61))
        self.textedit_ipconfig.setStyleSheet(u"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 22px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	background-color: transparent;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */")
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
        self.ipconfig_delete = QPushButton(self.frame_6)
        self.ipconfig_delete.setObjectName(u"ipconfig_delete")
        self.ipconfig_delete.setGeometry(QRect(2, 0, 291, 51))
        self.ipconfig_delete.setStyleSheet(u"QPushButton {\n"
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
        self.ipconfig_confirm = QPushButton(self.frame_6)
        self.ipconfig_confirm.setObjectName(u"ipconfig_confirm")
        self.ipconfig_confirm.setGeometry(QRect(290, 0, 281, 51))
        self.ipconfig_confirm.setStyleSheet(u"QPushButton {\n"
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
        self.ipconfig_1 = QPushButton(self.frame_5)
        self.ipconfig_1.setObjectName(u"ipconfig_1")
        self.ipconfig_1.setGeometry(QRect(50, 60, 51, 61))
        self.ipconfig_1.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_2 = QPushButton(self.frame_5)
        self.ipconfig_2.setObjectName(u"ipconfig_2")
        self.ipconfig_2.setGeometry(QRect(100, 60, 51, 61))
        self.ipconfig_2.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_3 = QPushButton(self.frame_5)
        self.ipconfig_3.setObjectName(u"ipconfig_3")
        self.ipconfig_3.setGeometry(QRect(150, 60, 51, 61))
        self.ipconfig_3.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_5 = QPushButton(self.frame_5)
        self.ipconfig_5.setObjectName(u"ipconfig_5")
        self.ipconfig_5.setGeometry(QRect(250, 60, 41, 61))
        self.ipconfig_5.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_6 = QPushButton(self.frame_5)
        self.ipconfig_6.setObjectName(u"ipconfig_6")
        self.ipconfig_6.setGeometry(QRect(290, 60, 51, 61))
        self.ipconfig_6.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_4 = QPushButton(self.frame_5)
        self.ipconfig_4.setObjectName(u"ipconfig_4")
        self.ipconfig_4.setGeometry(QRect(200, 60, 51, 61))
        self.ipconfig_4.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_8 = QPushButton(self.frame_5)
        self.ipconfig_8.setObjectName(u"ipconfig_8")
        self.ipconfig_8.setGeometry(QRect(390, 60, 51, 61))
        self.ipconfig_8.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_9 = QPushButton(self.frame_5)
        self.ipconfig_9.setObjectName(u"ipconfig_9")
        self.ipconfig_9.setGeometry(QRect(440, 60, 51, 61))
        self.ipconfig_9.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_7 = QPushButton(self.frame_5)
        self.ipconfig_7.setObjectName(u"ipconfig_7")
        self.ipconfig_7.setGeometry(QRect(340, 60, 51, 61))
        self.ipconfig_7.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_0 = QPushButton(self.frame_5)
        self.ipconfig_0.setObjectName(u"ipconfig_0")
        self.ipconfig_0.setGeometry(QRect(490, 60, 41, 61))
        self.ipconfig_0.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_punt = QPushButton(self.frame_5)
        self.ipconfig_punt.setObjectName(u"ipconfig_punt")
        self.ipconfig_punt.setGeometry(QRect(440, 240, 51, 61))
        self.ipconfig_punt.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_dospunts = QPushButton(self.frame_5)
        self.ipconfig_dospunts.setObjectName(u"ipconfig_dospunts")
        self.ipconfig_dospunts.setGeometry(QRect(490, 240, 41, 61))
        self.ipconfig_dospunts.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_E = QPushButton(self.frame_5)
        self.ipconfig_E.setObjectName(u"ipconfig_E")
        self.ipconfig_E.setGeometry(QRect(150, 120, 51, 61))
        self.ipconfig_E.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_R = QPushButton(self.frame_5)
        self.ipconfig_R.setObjectName(u"ipconfig_R")
        self.ipconfig_R.setGeometry(QRect(200, 120, 51, 61))
        self.ipconfig_R.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_Y = QPushButton(self.frame_5)
        self.ipconfig_Y.setObjectName(u"ipconfig_Y")
        self.ipconfig_Y.setGeometry(QRect(290, 120, 51, 61))
        self.ipconfig_Y.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_U = QPushButton(self.frame_5)
        self.ipconfig_U.setObjectName(u"ipconfig_U")
        self.ipconfig_U.setGeometry(QRect(340, 120, 51, 61))
        self.ipconfig_U.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_I = QPushButton(self.frame_5)
        self.ipconfig_I.setObjectName(u"ipconfig_I")
        self.ipconfig_I.setGeometry(QRect(390, 120, 51, 61))
        self.ipconfig_I.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_Q = QPushButton(self.frame_5)
        self.ipconfig_Q.setObjectName(u"ipconfig_Q")
        self.ipconfig_Q.setGeometry(QRect(50, 120, 51, 61))
        self.ipconfig_Q.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_W = QPushButton(self.frame_5)
        self.ipconfig_W.setObjectName(u"ipconfig_W")
        self.ipconfig_W.setGeometry(QRect(100, 120, 51, 61))
        self.ipconfig_W.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_O = QPushButton(self.frame_5)
        self.ipconfig_O.setObjectName(u"ipconfig_O")
        self.ipconfig_O.setGeometry(QRect(440, 120, 51, 61))
        self.ipconfig_O.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_T = QPushButton(self.frame_5)
        self.ipconfig_T.setObjectName(u"ipconfig_T")
        self.ipconfig_T.setGeometry(QRect(250, 120, 41, 61))
        self.ipconfig_T.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_P = QPushButton(self.frame_5)
        self.ipconfig_P.setObjectName(u"ipconfig_P")
        self.ipconfig_P.setGeometry(QRect(490, 120, 41, 61))
        self.ipconfig_P.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_barra = QPushButton(self.frame_5)
        self.ipconfig_barra.setObjectName(u"ipconfig_barra")
        self.ipconfig_barra.setGeometry(QRect(490, 180, 41, 61))
        self.ipconfig_barra.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_F = QPushButton(self.frame_5)
        self.ipconfig_F.setObjectName(u"ipconfig_F")
        self.ipconfig_F.setGeometry(QRect(200, 180, 51, 61))
        self.ipconfig_F.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_L = QPushButton(self.frame_5)
        self.ipconfig_L.setObjectName(u"ipconfig_L")
        self.ipconfig_L.setGeometry(QRect(440, 180, 51, 61))
        self.ipconfig_L.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_H = QPushButton(self.frame_5)
        self.ipconfig_H.setObjectName(u"ipconfig_H")
        self.ipconfig_H.setGeometry(QRect(290, 180, 51, 61))
        self.ipconfig_H.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_J = QPushButton(self.frame_5)
        self.ipconfig_J.setObjectName(u"ipconfig_J")
        self.ipconfig_J.setGeometry(QRect(340, 180, 51, 61))
        self.ipconfig_J.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_D = QPushButton(self.frame_5)
        self.ipconfig_D.setObjectName(u"ipconfig_D")
        self.ipconfig_D.setGeometry(QRect(150, 180, 51, 61))
        self.ipconfig_D.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_G = QPushButton(self.frame_5)
        self.ipconfig_G.setObjectName(u"ipconfig_G")
        self.ipconfig_G.setGeometry(QRect(250, 180, 41, 61))
        self.ipconfig_G.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_K = QPushButton(self.frame_5)
        self.ipconfig_K.setObjectName(u"ipconfig_K")
        self.ipconfig_K.setGeometry(QRect(390, 180, 51, 61))
        self.ipconfig_K.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_A = QPushButton(self.frame_5)
        self.ipconfig_A.setObjectName(u"ipconfig_A")
        self.ipconfig_A.setGeometry(QRect(50, 180, 51, 61))
        self.ipconfig_A.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_S = QPushButton(self.frame_5)
        self.ipconfig_S.setObjectName(u"ipconfig_S")
        self.ipconfig_S.setGeometry(QRect(100, 180, 51, 61))
        self.ipconfig_S.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_V = QPushButton(self.frame_5)
        self.ipconfig_V.setObjectName(u"ipconfig_V")
        self.ipconfig_V.setGeometry(QRect(200, 240, 51, 61))
        self.ipconfig_V.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_Z = QPushButton(self.frame_5)
        self.ipconfig_Z.setObjectName(u"ipconfig_Z")
        self.ipconfig_Z.setGeometry(QRect(50, 240, 51, 61))
        self.ipconfig_Z.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_B = QPushButton(self.frame_5)
        self.ipconfig_B.setObjectName(u"ipconfig_B")
        self.ipconfig_B.setGeometry(QRect(250, 240, 41, 61))
        self.ipconfig_B.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_M = QPushButton(self.frame_5)
        self.ipconfig_M.setObjectName(u"ipconfig_M")
        self.ipconfig_M.setGeometry(QRect(340, 240, 51, 61))
        self.ipconfig_M.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_barra_baixa = QPushButton(self.frame_5)
        self.ipconfig_barra_baixa.setObjectName(u"ipconfig_barra_baixa")
        self.ipconfig_barra_baixa.setGeometry(QRect(390, 240, 51, 61))
        self.ipconfig_barra_baixa.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_X = QPushButton(self.frame_5)
        self.ipconfig_X.setObjectName(u"ipconfig_X")
        self.ipconfig_X.setGeometry(QRect(100, 240, 51, 61))
        self.ipconfig_X.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_N = QPushButton(self.frame_5)
        self.ipconfig_N.setObjectName(u"ipconfig_N")
        self.ipconfig_N.setGeometry(QRect(290, 240, 51, 61))
        self.ipconfig_N.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.ipconfig_C = QPushButton(self.frame_5)
        self.ipconfig_C.setObjectName(u"ipconfig_C")
        self.ipconfig_C.setGeometry(QRect(150, 240, 51, 61))
        self.ipconfig_C.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 440, 921, 41))
        self.frame_2.setStyleSheet(u"background-color: rgba(27,29,35,200);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_name = QLabel(Dialog)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(100, 270, 131, 20))
        self.label_name.setStyleSheet(u"QLabel {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 24px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	background-color: transparent;\n"
"}\n"
"")
        self.textedit_ipconfig_name = QTextEdit(Dialog)
        self.textedit_ipconfig_name.setObjectName(u"textedit_ipconfig_name")
        self.textedit_ipconfig_name.setGeometry(QRect(30, 310, 271, 61))
        self.textedit_ipconfig_name.setStyleSheet(u"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 22px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	background-color: transparent;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.minimize_ipconfig.setToolTip(QCoreApplication.translate("Dialog", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimize_ipconfig.setText("")
#if QT_CONFIG(tooltip)
        self.maximize_ipconfig.setToolTip(QCoreApplication.translate("Dialog", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximize_ipconfig.setText("")
#if QT_CONFIG(tooltip)
        self.close_ipconfig.setToolTip(QCoreApplication.translate("Dialog", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.close_ipconfig.setText("")
        self.label_IP.setText(QCoreApplication.translate("Dialog", u"vMix IP and Port", None))
        self.ipconfig_delete.setText(QCoreApplication.translate("Dialog", u"Delete", None))
        self.ipconfig_confirm.setText(QCoreApplication.translate("Dialog", u"Confirm", None))
        self.ipconfig_1.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.ipconfig_2.setText(QCoreApplication.translate("Dialog", u"2", None))
        self.ipconfig_3.setText(QCoreApplication.translate("Dialog", u"3", None))
        self.ipconfig_5.setText(QCoreApplication.translate("Dialog", u"5", None))
        self.ipconfig_6.setText(QCoreApplication.translate("Dialog", u"6", None))
        self.ipconfig_4.setText(QCoreApplication.translate("Dialog", u"4", None))
        self.ipconfig_8.setText(QCoreApplication.translate("Dialog", u"8", None))
        self.ipconfig_9.setText(QCoreApplication.translate("Dialog", u"9", None))
        self.ipconfig_7.setText(QCoreApplication.translate("Dialog", u"7", None))
        self.ipconfig_0.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.ipconfig_punt.setText(QCoreApplication.translate("Dialog", u".", None))
        self.ipconfig_dospunts.setText(QCoreApplication.translate("Dialog", u":", None))
        self.ipconfig_E.setText(QCoreApplication.translate("Dialog", u"E", None))
        self.ipconfig_R.setText(QCoreApplication.translate("Dialog", u"R", None))
        self.ipconfig_Y.setText(QCoreApplication.translate("Dialog", u"Y", None))
        self.ipconfig_U.setText(QCoreApplication.translate("Dialog", u"U", None))
        self.ipconfig_I.setText(QCoreApplication.translate("Dialog", u"I", None))
        self.ipconfig_Q.setText(QCoreApplication.translate("Dialog", u"Q", None))
        self.ipconfig_W.setText(QCoreApplication.translate("Dialog", u"W", None))
        self.ipconfig_O.setText(QCoreApplication.translate("Dialog", u"O", None))
        self.ipconfig_T.setText(QCoreApplication.translate("Dialog", u"T", None))
        self.ipconfig_P.setText(QCoreApplication.translate("Dialog", u"P", None))
        self.ipconfig_barra.setText(QCoreApplication.translate("Dialog", u"-", None))
        self.ipconfig_F.setText(QCoreApplication.translate("Dialog", u"F", None))
        self.ipconfig_L.setText(QCoreApplication.translate("Dialog", u"L", None))
        self.ipconfig_H.setText(QCoreApplication.translate("Dialog", u"H", None))
        self.ipconfig_J.setText(QCoreApplication.translate("Dialog", u"J", None))
        self.ipconfig_D.setText(QCoreApplication.translate("Dialog", u"D", None))
        self.ipconfig_G.setText(QCoreApplication.translate("Dialog", u"G", None))
        self.ipconfig_K.setText(QCoreApplication.translate("Dialog", u"K", None))
        self.ipconfig_A.setText(QCoreApplication.translate("Dialog", u"A", None))
        self.ipconfig_S.setText(QCoreApplication.translate("Dialog", u"S", None))
        self.ipconfig_V.setText(QCoreApplication.translate("Dialog", u"V", None))
        self.ipconfig_Z.setText(QCoreApplication.translate("Dialog", u"Z", None))
        self.ipconfig_B.setText(QCoreApplication.translate("Dialog", u"B", None))
        self.ipconfig_M.setText(QCoreApplication.translate("Dialog", u"M", None))
        self.ipconfig_barra_baixa.setText(QCoreApplication.translate("Dialog", u"_", None))
        self.ipconfig_X.setText(QCoreApplication.translate("Dialog", u"X", None))
        self.ipconfig_N.setText(QCoreApplication.translate("Dialog", u"N", None))
        self.ipconfig_C.setText(QCoreApplication.translate("Dialog", u"C", None))
        self.label_name.setText(QCoreApplication.translate("Dialog", u"vMix Name", None))
    # retranslateUi

