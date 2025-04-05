# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popup_fastjog_tabs.ui'
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
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 924, 480))
        self.tabWidget.setStyleSheet(u"QTabWidget::pane {\n"
"    background: #ffffff;  /* Color de fondo de la zona del contenido */\n"
"    border: 2px solid black; /* Opcional: un borde para ver el \u00e1rea afectada */\n"
"}\n"
"\n"
"QWidget#tab_1 {\n"
"    background: rgb(44,49,60);  /* Color de fondo de los widgets de las pesta\u00f1as */\n"
"}\n"
"\n"
"QWidget#tab_2{\n"
"background: rgb(44,49,60);\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    width: 160px;  /* Ancho de cada pesta\u00f1a */\n"
"    height: 17px;  /* Alto de cada pesta\u00f1a */\n"
"    padding: 5px;  /* Espaciado interno */\n"
"	color: white;\n"
"    background: grey; \n"
"    border: 2px solid black;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"	color: black;\n"
"    background: lightgrey;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background: #ddd;\n"
"}")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.textedit_fastjog = QTextEdit(self.tab)
        self.textedit_fastjog.setObjectName(u"textedit_fastjog")
        self.textedit_fastjog.setGeometry(QRect(100, 180, 271, 61))
        self.textedit_fastjog.setStyleSheet(u"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 22px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	background-color: transparent;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */")
        self.frame_4 = QFrame(self.tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(500, 0, 421, 351))
        self.frame_4.setStyleSheet(u"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 2px;\n"
"	background-color: rgba(40,40,40,200);\n"
"	border: 2px solid rgba(200,200,200,200);  /* Borde blanco con transparencia */")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.fastjogconfig_1 = QPushButton(self.frame_4)
        self.fastjogconfig_1.setObjectName(u"fastjogconfig_1")
        self.fastjogconfig_1.setGeometry(QRect(100, 60, 71, 61))
        self.fastjogconfig_1.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;\n"
"")
        self.fastjogconfig_2 = QPushButton(self.frame_4)
        self.fastjogconfig_2.setObjectName(u"fastjogconfig_2")
        self.fastjogconfig_2.setGeometry(QRect(170, 60, 71, 61))
        self.fastjogconfig_2.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.fastjogconfig_3 = QPushButton(self.frame_4)
        self.fastjogconfig_3.setObjectName(u"fastjogconfig_3")
        self.fastjogconfig_3.setGeometry(QRect(240, 60, 71, 61))
        self.fastjogconfig_3.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.fastjogconfig_5 = QPushButton(self.frame_4)
        self.fastjogconfig_5.setObjectName(u"fastjogconfig_5")
        self.fastjogconfig_5.setGeometry(QRect(170, 120, 71, 61))
        self.fastjogconfig_5.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.fastjogconfig_6 = QPushButton(self.frame_4)
        self.fastjogconfig_6.setObjectName(u"fastjogconfig_6")
        self.fastjogconfig_6.setGeometry(QRect(240, 120, 71, 61))
        self.fastjogconfig_6.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.fastjogconfig_4 = QPushButton(self.frame_4)
        self.fastjogconfig_4.setObjectName(u"fastjogconfig_4")
        self.fastjogconfig_4.setGeometry(QRect(100, 120, 71, 61))
        self.fastjogconfig_4.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.fastjogconfig_8 = QPushButton(self.frame_4)
        self.fastjogconfig_8.setObjectName(u"fastjogconfig_8")
        self.fastjogconfig_8.setGeometry(QRect(170, 180, 71, 61))
        self.fastjogconfig_8.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.fastjogconfig_9 = QPushButton(self.frame_4)
        self.fastjogconfig_9.setObjectName(u"fastjogconfig_9")
        self.fastjogconfig_9.setGeometry(QRect(240, 180, 71, 61))
        self.fastjogconfig_9.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.fastjogconfig_7 = QPushButton(self.frame_4)
        self.fastjogconfig_7.setObjectName(u"fastjogconfig_7")
        self.fastjogconfig_7.setGeometry(QRect(100, 180, 71, 61))
        self.fastjogconfig_7.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.fastjogconfig_0 = QPushButton(self.frame_4)
        self.fastjogconfig_0.setObjectName(u"fastjogconfig_0")
        self.fastjogconfig_0.setGeometry(QRect(170, 240, 71, 61))
        self.fastjogconfig_0.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 130, 121, 31))
        self.label.setStyleSheet(u"QLabel {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 24px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	background-color: transparent;\n"
"}\n"
"")
        self.frame_3 = QFrame(self.tab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(500, 350, 421, 51))
        self.frame_3.setStyleSheet(u"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 2px;\n"
"	background-color: transparent;\n"
"	border: 2px solid rgba(200,200,200,200);  /* Borde blanco con transparencia */")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.fastjogconfig_delete = QPushButton(self.frame_3)
        self.fastjogconfig_delete.setObjectName(u"fastjogconfig_delete")
        self.fastjogconfig_delete.setGeometry(QRect(2, 0, 211, 51))
        self.fastjogconfig_delete.setStyleSheet(u"QPushButton {\n"
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
        self.fastjogconfig_confirm = QPushButton(self.frame_3)
        self.fastjogconfig_confirm.setObjectName(u"fastjogconfig_confirm")
        self.fastjogconfig_confirm.setGeometry(QRect(210, 0, 211, 51))
        self.fastjogconfig_confirm.setStyleSheet(u"QPushButton {\n"
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
        self.frame_5 = QFrame(self.tab)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 400, 921, 41))
        self.frame_5.setStyleSheet(u"background-color: rgba(27,29,35,200);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.frame_2 = QFrame(self.tab_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 400, 921, 41))
        self.frame_2.setStyleSheet(u"background-color: rgba(27,29,35,200);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_6 = QFrame(self.tab_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(500, 0, 421, 351))
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
        self.sec_fastjogconfig_1 = QPushButton(self.frame_6)
        self.sec_fastjogconfig_1.setObjectName(u"sec_fastjogconfig_1")
        self.sec_fastjogconfig_1.setGeometry(QRect(100, 60, 71, 61))
        self.sec_fastjogconfig_1.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;\n"
"")
        self.sec_fastjogconfig_2 = QPushButton(self.frame_6)
        self.sec_fastjogconfig_2.setObjectName(u"sec_fastjogconfig_2")
        self.sec_fastjogconfig_2.setGeometry(QRect(170, 60, 71, 61))
        self.sec_fastjogconfig_2.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.sec_fastjogconfig_3 = QPushButton(self.frame_6)
        self.sec_fastjogconfig_3.setObjectName(u"sec_fastjogconfig_3")
        self.sec_fastjogconfig_3.setGeometry(QRect(240, 60, 71, 61))
        self.sec_fastjogconfig_3.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.sec_fastjogconfig_5 = QPushButton(self.frame_6)
        self.sec_fastjogconfig_5.setObjectName(u"sec_fastjogconfig_5")
        self.sec_fastjogconfig_5.setGeometry(QRect(170, 120, 71, 61))
        self.sec_fastjogconfig_5.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.sec_fastjogconfig_6 = QPushButton(self.frame_6)
        self.sec_fastjogconfig_6.setObjectName(u"sec_fastjogconfig_6")
        self.sec_fastjogconfig_6.setGeometry(QRect(240, 120, 71, 61))
        self.sec_fastjogconfig_6.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.sec_fastjogconfig_4 = QPushButton(self.frame_6)
        self.sec_fastjogconfig_4.setObjectName(u"sec_fastjogconfig_4")
        self.sec_fastjogconfig_4.setGeometry(QRect(100, 120, 71, 61))
        self.sec_fastjogconfig_4.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.sec_fastjogconfig_8 = QPushButton(self.frame_6)
        self.sec_fastjogconfig_8.setObjectName(u"sec_fastjogconfig_8")
        self.sec_fastjogconfig_8.setGeometry(QRect(170, 180, 71, 61))
        self.sec_fastjogconfig_8.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.sec_fastjogconfig_9 = QPushButton(self.frame_6)
        self.sec_fastjogconfig_9.setObjectName(u"sec_fastjogconfig_9")
        self.sec_fastjogconfig_9.setGeometry(QRect(240, 180, 71, 61))
        self.sec_fastjogconfig_9.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.sec_fastjogconfig_7 = QPushButton(self.frame_6)
        self.sec_fastjogconfig_7.setObjectName(u"sec_fastjogconfig_7")
        self.sec_fastjogconfig_7.setGeometry(QRect(100, 180, 71, 61))
        self.sec_fastjogconfig_7.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.sec_fastjogconfig_0 = QPushButton(self.frame_6)
        self.sec_fastjogconfig_0.setObjectName(u"sec_fastjogconfig_0")
        self.sec_fastjogconfig_0.setGeometry(QRect(170, 240, 71, 61))
        self.sec_fastjogconfig_0.setStyleSheet(u"border: transparent;\n"
"font-size: 30px;")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(105, 130, 261, 31))
        self.label_2.setStyleSheet(u"QLabel {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 24px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	background-color: transparent;\n"
"}\n"
"")
        self.frame_7 = QFrame(self.tab_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(500, 350, 421, 51))
        self.frame_7.setStyleSheet(u"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 2px;\n"
"	background-color: transparent;\n"
"	border: 2px solid rgba(200,200,200,200);  /* Borde blanco con transparencia */")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.sec_fastjogconfig_delete = QPushButton(self.frame_7)
        self.sec_fastjogconfig_delete.setObjectName(u"sec_fastjogconfig_delete")
        self.sec_fastjogconfig_delete.setGeometry(QRect(2, 0, 211, 51))
        self.sec_fastjogconfig_delete.setStyleSheet(u"QPushButton {\n"
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
        self.sec_fastjogconfig_confirm = QPushButton(self.frame_7)
        self.sec_fastjogconfig_confirm.setObjectName(u"sec_fastjogconfig_confirm")
        self.sec_fastjogconfig_confirm.setGeometry(QRect(210, 0, 211, 51))
        self.sec_fastjogconfig_confirm.setStyleSheet(u"QPushButton {\n"
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
        self.textedit_sec_fastjog = QTextEdit(self.tab_2)
        self.textedit_sec_fastjog.setObjectName(u"textedit_sec_fastjog")
        self.textedit_sec_fastjog.setGeometry(QRect(100, 180, 271, 61))
        self.textedit_sec_fastjog.setStyleSheet(u"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 22px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	background-color: transparent;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */")
        self.tabWidget.addTab(self.tab_2, "")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(370, 0, 560, 41))
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
        self.close_fastjog = QPushButton(self.frame)
        self.close_fastjog.setObjectName(u"close_fastjog")
        self.close_fastjog.setGeometry(QRect(510, 0, 40, 42))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.close_fastjog.sizePolicy().hasHeightForWidth())
        self.close_fastjog.setSizePolicy(sizePolicy1)
        self.close_fastjog.setMinimumSize(QSize(40, 0))
        self.close_fastjog.setMaximumSize(QSize(40, 16777215))
        self.close_fastjog.setStyleSheet(u"QPushButton {	\n"
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
        self.close_fastjog.setIcon(icon)
        self.minimize_fastjog = QPushButton(self.frame)
        self.minimize_fastjog.setObjectName(u"minimize_fastjog")
        self.minimize_fastjog.setGeometry(QRect(430, 0, 40, 42))
        sizePolicy1.setHeightForWidth(self.minimize_fastjog.sizePolicy().hasHeightForWidth())
        self.minimize_fastjog.setSizePolicy(sizePolicy1)
        self.minimize_fastjog.setMinimumSize(QSize(40, 0))
        self.minimize_fastjog.setMaximumSize(QSize(40, 16777215))
        self.minimize_fastjog.setStyleSheet(u"QPushButton {	\n"
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
        icon1.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_fastjog.setIcon(icon1)
        self.maximize_fastjog = QPushButton(self.frame)
        self.maximize_fastjog.setObjectName(u"maximize_fastjog")
        self.maximize_fastjog.setGeometry(QRect(470, 0, 40, 42))
        sizePolicy1.setHeightForWidth(self.maximize_fastjog.sizePolicy().hasHeightForWidth())
        self.maximize_fastjog.setSizePolicy(sizePolicy1)
        self.maximize_fastjog.setMinimumSize(QSize(40, 0))
        self.maximize_fastjog.setMaximumSize(QSize(40, 16777215))
        self.maximize_fastjog.setStyleSheet(u"QPushButton {	\n"
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
        self.maximize_fastjog.setIcon(icon2)

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.fastjogconfig_1.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.fastjogconfig_2.setText(QCoreApplication.translate("Dialog", u"2", None))
        self.fastjogconfig_3.setText(QCoreApplication.translate("Dialog", u"3", None))
        self.fastjogconfig_5.setText(QCoreApplication.translate("Dialog", u"5", None))
        self.fastjogconfig_6.setText(QCoreApplication.translate("Dialog", u"6", None))
        self.fastjogconfig_4.setText(QCoreApplication.translate("Dialog", u"4", None))
        self.fastjogconfig_8.setText(QCoreApplication.translate("Dialog", u"8", None))
        self.fastjogconfig_9.setText(QCoreApplication.translate("Dialog", u"9", None))
        self.fastjogconfig_7.setText(QCoreApplication.translate("Dialog", u"7", None))
        self.fastjogconfig_0.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Fast Jog", None))
        self.fastjogconfig_delete.setText(QCoreApplication.translate("Dialog", u"Delete", None))
        self.fastjogconfig_confirm.setText(QCoreApplication.translate("Dialog", u"Confirm", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"Tab 1", None))
        self.sec_fastjogconfig_1.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.sec_fastjogconfig_2.setText(QCoreApplication.translate("Dialog", u"2", None))
        self.sec_fastjogconfig_3.setText(QCoreApplication.translate("Dialog", u"3", None))
        self.sec_fastjogconfig_5.setText(QCoreApplication.translate("Dialog", u"5", None))
        self.sec_fastjogconfig_6.setText(QCoreApplication.translate("Dialog", u"6", None))
        self.sec_fastjogconfig_4.setText(QCoreApplication.translate("Dialog", u"4", None))
        self.sec_fastjogconfig_8.setText(QCoreApplication.translate("Dialog", u"8", None))
        self.sec_fastjogconfig_9.setText(QCoreApplication.translate("Dialog", u"9", None))
        self.sec_fastjogconfig_7.setText(QCoreApplication.translate("Dialog", u"7", None))
        self.sec_fastjogconfig_0.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"2nd value for Fast Jog", None))
        self.sec_fastjogconfig_delete.setText(QCoreApplication.translate("Dialog", u"Delete", None))
        self.sec_fastjogconfig_confirm.setText(QCoreApplication.translate("Dialog", u"Confirm", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"Tab 2", None))
#if QT_CONFIG(tooltip)
        self.close_fastjog.setToolTip(QCoreApplication.translate("Dialog", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.close_fastjog.setText("")
#if QT_CONFIG(tooltip)
        self.minimize_fastjog.setToolTip(QCoreApplication.translate("Dialog", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimize_fastjog.setText("")
#if QT_CONFIG(tooltip)
        self.maximize_fastjog.setToolTip(QCoreApplication.translate("Dialog", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximize_fastjog.setText("")
    # retranslateUi

