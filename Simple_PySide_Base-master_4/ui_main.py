# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_BASE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 600)
        MainWindow.setMinimumSize(QSize(1000, 600))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.label_page = QLabel(self.frame_label_top_btns)
        self.label_page.setObjectName(u"label_page")
        self.label_page.setGeometry(QRect(5, 0, 67, 41))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_page.setFont(font1)
        self.label_page.setStyleSheet(u"background-color: transparent;")
        self.label_bank = QLabel(self.frame_label_top_btns)
        self.label_bank.setObjectName(u"label_bank")
        self.label_bank.setGeometry(QRect(72, 0, 71, 41))
        self.label_bank.setFont(font1)
        self.label_bank.setStyleSheet(u"background-color: transparent;")
        self.label_bank.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_pgm = QLabel(self.frame_label_top_btns)
        self.label_pgm.setObjectName(u"label_pgm")
        self.label_pgm.setGeometry(QRect(250, 0, 351, 41))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_pgm.setFont(font2)
        self.label_pgm.setStyleSheet(u"background: transparent;\n"
"")
        self.label_pgm.setAlignment(Qt.AlignCenter)
        self.label_vmixconn = QLabel(self.frame_label_top_btns)
        self.label_vmixconn.setObjectName(u"label_vmixconn")
        self.label_vmixconn.setGeometry(QRect(640, 0, 99, 41))
        self.label_vmixconn.setStyleSheet(u"background: transparent;")
        self.label_vmixconn.setAlignment(Qt.AlignCenter)
        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        self.label_title_bar_top.setGeometry(QRect(720, 0, 16, 23))
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")
        self.vmix_conn_no = QFrame(self.frame_label_top_btns)
        self.vmix_conn_no.setObjectName(u"vmix_conn_no")
        self.vmix_conn_no.setGeometry(QRect(748, 0, 28, 42))
        self.vmix_conn_no.setStyleSheet(u"background-color: rgb(255,0,0);\n"
"border-radius: 5px;\n"
"border: 1px solid rgb(0,0,0);")
        self.vmix_conn_no.setFrameShape(QFrame.StyledPanel)
        self.vmix_conn_no.setFrameShadow(QFrame.Raised)
        self.vmix_conn_ok = QFrame(self.frame_label_top_btns)
        self.vmix_conn_ok.setObjectName(u"vmix_conn_ok")
        self.vmix_conn_ok.setGeometry(QRect(776, 0, 28, 42))
        self.vmix_conn_ok.setStyleSheet(u"background-color: rgb(0,255,0);\n"
"border-radius: 5px;\n"
"border: 1px solid rgb(0,0,0);\n"
"")
        self.vmix_conn_ok.setFrameShape(QFrame.StyledPanel)
        self.vmix_conn_ok.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
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
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
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
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
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
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        self.label_top_info_1.setFont(font3)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setBold(True)
        font4.setWeight(75)
        self.label_top_info_2.setFont(font4)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy4)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(12)
        self.label_user_icon.setFont(font5)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(44, 49, 60);\n"
"	border: 5px solid rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.clip_addtoplaylist = QPushButton(self.page_home)
        self.clip_addtoplaylist.setObjectName(u"clip_addtoplaylist")
        self.clip_addtoplaylist.setGeometry(QRect(710, 30, 175, 70))
        self.clip_addtoplaylist.setLayoutDirection(Qt.RightToLeft)
        self.clip_addtoplaylist.setAutoFillBackground(False)
        self.clip_addtoplaylist.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"    qproperty-iconAlignment: right;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-chevron-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clip_addtoplaylist.setIcon(icon3)
        self.clip_widget_estrelles3 = QWidget(self.page_home)
        self.clip_widget_estrelles3.setObjectName(u"clip_widget_estrelles3")
        self.clip_widget_estrelles3.setGeometry(QRect(490, 30, 175, 70))
        self.clip_widget_estrelles3.setStyleSheet(u"background-color: rgba(255,255,255,0);\n"
"border-radius: 15px;\n"
"border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"\n"
"")
        self.clip_star_widget_estrelles3_1 = QLabel(self.clip_widget_estrelles3)
        self.clip_star_widget_estrelles3_1.setObjectName(u"clip_star_widget_estrelles3_1")
        self.clip_star_widget_estrelles3_1.setGeometry(QRect(45, 10, 21, 51))
        self.clip_star_widget_estrelles3_1.setStyleSheet(u"background-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.clip_star_widget_estrelles3_1.setPixmap(QPixmap(u":/20x20/icons/20x20/cil-star.png"))
        self.clip_star_widget_estrelles3_2 = QLabel(self.clip_widget_estrelles3)
        self.clip_star_widget_estrelles3_2.setObjectName(u"clip_star_widget_estrelles3_2")
        self.clip_star_widget_estrelles3_2.setGeometry(QRect(72, 10, 21, 51))
        self.clip_star_widget_estrelles3_2.setStyleSheet(u"background-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.clip_star_widget_estrelles3_2.setPixmap(QPixmap(u":/20x20/icons/20x20/cil-star.png"))
        self.clip_star_widget_estrelles3_3 = QLabel(self.clip_widget_estrelles3)
        self.clip_star_widget_estrelles3_3.setObjectName(u"clip_star_widget_estrelles3_3")
        self.clip_star_widget_estrelles3_3.setGeometry(QRect(99, 10, 21, 51))
        self.clip_star_widget_estrelles3_3.setStyleSheet(u"background-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.clip_star_widget_estrelles3_3.setPixmap(QPixmap(u":/20x20/icons/20x20/cil-star.png"))
        self.clip_button_onwidget_estrelles3 = QPushButton(self.clip_widget_estrelles3)
        self.clip_button_onwidget_estrelles3.setObjectName(u"clip_button_onwidget_estrelles3")
        self.clip_button_onwidget_estrelles3.setGeometry(QRect(0, 0, 175, 70))
        font6 = QFont()
        font6.setFamily(u"Arial")
        font6.setBold(True)
        font6.setWeight(75)
        self.clip_button_onwidget_estrelles3.setFont(font6)
        self.clip_button_onwidget_estrelles3.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"	\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"")
        self.clip_button_onwidget_estrelles3.setIconSize(QSize(20, 20))
        self.clip_gotoestrella3 = QPushButton(self.clip_widget_estrelles3)
        self.clip_gotoestrella3.setObjectName(u"clip_gotoestrella3")
        self.clip_gotoestrella3.setGeometry(QRect(139, 0, 34, 68))
        self.clip_gotoestrella3.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 9px;\n"
"	border: 1px solid rgba(255,255,255,100);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"	\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"")
        self.clip_gotoestrella3.setIcon(icon3)
        self.clip_estrella1 = QPushButton(self.page_home)
        self.clip_estrella1.setObjectName(u"clip_estrella1")
        self.clip_estrella1.setGeometry(QRect(50, 30, 175, 70))
        self.clip_estrella1.setFont(font6)
        self.clip_estrella1.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"	\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/20x20/icons/20x20/cil-star.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clip_estrella1.setIcon(icon4)
        self.clip_estrella1.setIconSize(QSize(20, 20))
        self.clip_widget_estrelles2 = QWidget(self.page_home)
        self.clip_widget_estrelles2.setObjectName(u"clip_widget_estrelles2")
        self.clip_widget_estrelles2.setGeometry(QRect(270, 30, 175, 70))
        self.clip_widget_estrelles2.setStyleSheet(u"background-color: rgba(255,255,255,0);\n"
"border-radius: 15px;\n"
"border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"\n"
"")
        self.clip_star_widget_estrelles2_1 = QLabel(self.clip_widget_estrelles2)
        self.clip_star_widget_estrelles2_1.setObjectName(u"clip_star_widget_estrelles2_1")
        self.clip_star_widget_estrelles2_1.setGeometry(QRect(55, 10, 21, 51))
        self.clip_star_widget_estrelles2_1.setStyleSheet(u"background-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.clip_star_widget_estrelles2_1.setPixmap(QPixmap(u":/20x20/icons/20x20/cil-star.png"))
        self.clip_star_widget_estrelles2_2 = QLabel(self.clip_widget_estrelles2)
        self.clip_star_widget_estrelles2_2.setObjectName(u"clip_star_widget_estrelles2_2")
        self.clip_star_widget_estrelles2_2.setGeometry(QRect(85, 10, 21, 51))
        self.clip_star_widget_estrelles2_2.setStyleSheet(u"background-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);\n"
"border")
        self.clip_star_widget_estrelles2_2.setPixmap(QPixmap(u":/20x20/icons/20x20/cil-star.png"))
        self.clip_button_onwidget_estrelles2 = QPushButton(self.clip_widget_estrelles2)
        self.clip_button_onwidget_estrelles2.setObjectName(u"clip_button_onwidget_estrelles2")
        self.clip_button_onwidget_estrelles2.setGeometry(QRect(0, 0, 175, 70))
        self.clip_button_onwidget_estrelles2.setFont(font6)
        self.clip_button_onwidget_estrelles2.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"	\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.clip_button_onwidget_estrelles2.setIconSize(QSize(20, 20))
        self.clip_gotoestrella2 = QPushButton(self.clip_widget_estrelles2)
        self.clip_gotoestrella2.setObjectName(u"clip_gotoestrella2")
        self.clip_gotoestrella2.setGeometry(QRect(139, 0, 34, 68))
        self.clip_gotoestrella2.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 9px;\n"
"	border: 1px solid rgba(255,255,255,100);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"	\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"")
        self.clip_gotoestrella2.setIcon(icon3)
        self.clip_gotoestrella1 = QPushButton(self.page_home)
        self.clip_gotoestrella1.setObjectName(u"clip_gotoestrella1")
        self.clip_gotoestrella1.setGeometry(QRect(189, 31, 34, 68))
        self.clip_gotoestrella1.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 9px;\n"
"	border: 1px solid rgba(255,255,255,100);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"	\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"")
        self.clip_gotoestrella1.setIcon(icon3)
        self.clip_nameclip = QPushButton(self.page_home)
        self.clip_nameclip.setObjectName(u"clip_nameclip")
        self.clip_nameclip.setGeometry(QRect(50, 140, 175, 70))
        self.clip_nameclip.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.stackedWidget.addWidget(self.page_home)
        self.page_estrella1 = QWidget()
        self.page_estrella1.setObjectName(u"page_estrella1")
        self.list_estrella1 = QListWidget(self.page_estrella1)
        self.list_estrella1.setObjectName(u"list_estrella1")
        self.list_estrella1.setGeometry(QRect(120, 70, 661, 371))
        self.list_estrella1.setStyleSheet(u"QListWidget {\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_estrella1 = QLabel(self.page_estrella1)
        self.label_estrella1.setObjectName(u"label_estrella1")
        self.label_estrella1.setGeometry(QRect(120, 20, 661, 51))
        self.label_estrella1.setStyleSheet(u"QLabel {\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_estrella1.setPixmap(QPixmap(u":/20x20/icons/20x20/cil-star.png"))
        self.label_estrella1.setAlignment(Qt.AlignCenter)
        self.estrella1_delete = QPushButton(self.page_estrella1)
        self.estrella1_delete.setObjectName(u"estrella1_delete")
        self.estrella1_delete.setGeometry(QRect(710, 20, 71, 51))
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
        icon5 = QIcon()
        icon5.addFile(u":/20x20/icons/20x20/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.estrella1_delete.setIcon(icon5)
        self.estrella1_add = QPushButton(self.page_estrella1)
        self.estrella1_add.setObjectName(u"estrella1_add")
        self.estrella1_add.setGeometry(QRect(120, 20, 71, 51))
        self.estrella1_add.setStyleSheet(u"QPushButton {\n"
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
        icon6 = QIcon()
        icon6.addFile(u":/20x20/icons/20x20/cil-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.estrella1_add.setIcon(icon6)
        self.stackedWidget.addWidget(self.page_estrella1)
        self.page_pl11 = QWidget()
        self.page_pl11.setObjectName(u"page_pl11")
        self.pl11_add = QPushButton(self.page_pl11)
        self.pl11_add.setObjectName(u"pl11_add")
        self.pl11_add.setGeometry(QRect(150, 30, 71, 51))
        self.pl11_add.setStyleSheet(u"QPushButton {\n"
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
        self.pl11_add.setIcon(icon6)
        self.pl11_delete = QPushButton(self.page_pl11)
        self.pl11_delete.setObjectName(u"pl11_delete")
        self.pl11_delete.setGeometry(QRect(680, 30, 71, 51))
        self.pl11_delete.setStyleSheet(u"QPushButton {\n"
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
        self.pl11_delete.setIcon(icon5)
        self.label_nclips_11 = QLabel(self.page_pl11)
        self.label_nclips_11.setObjectName(u"label_nclips_11")
        self.label_nclips_11.setGeometry(QRect(620, 60, 61, 20))
        font7 = QFont()
        font7.setPointSize(9)
        self.label_nclips_11.setFont(font7)
        self.label_nclips_11.setAlignment(Qt.AlignCenter)
        self.list_pl11 = QListWidget(self.page_pl11)
        self.list_pl11.setObjectName(u"list_pl11")
        self.list_pl11.setGeometry(QRect(150, 80, 601, 351))
        self.list_pl11.setStyleSheet(u"QListWidget {\n"
"    font-weight: bold;\n"
"    background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_dur_11 = QLabel(self.page_pl11)
        self.label_dur_11.setObjectName(u"label_dur_11")
        self.label_dur_11.setGeometry(QRect(220, 60, 101, 20))
        self.label_dur_11.setFont(font7)
        self.label_dur_11.setAlignment(Qt.AlignCenter)
        self.label_pl11 = QLabel(self.page_pl11)
        self.label_pl11.setObjectName(u"label_pl11")
        self.label_pl11.setGeometry(QRect(150, 30, 601, 51))
        font8 = QFont()
        font8.setBold(True)
        font8.setWeight(75)
        self.label_pl11.setFont(font8)
        self.label_pl11.setStyleSheet(u"QLabel {\n"
"	font \"arial\"\n"
"    font-weight: bold;\n"
"	font-size: 20px;\n"
"	background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_pl11.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_pl11)
        self.label_pl11.raise_()
        self.pl11_add.raise_()
        self.pl11_delete.raise_()
        self.label_nclips_11.raise_()
        self.list_pl11.raise_()
        self.label_dur_11.raise_()
        self.page_pl13 = QWidget()
        self.page_pl13.setObjectName(u"page_pl13")
        self.pl13_add = QPushButton(self.page_pl13)
        self.pl13_add.setObjectName(u"pl13_add")
        self.pl13_add.setGeometry(QRect(150, 30, 71, 51))
        self.pl13_add.setStyleSheet(u"QPushButton {\n"
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
        self.pl13_add.setIcon(icon6)
        self.pl13_delete = QPushButton(self.page_pl13)
        self.pl13_delete.setObjectName(u"pl13_delete")
        self.pl13_delete.setGeometry(QRect(680, 30, 71, 51))
        self.pl13_delete.setStyleSheet(u"QPushButton {\n"
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
        self.pl13_delete.setIcon(icon5)
        self.label_nclips_13 = QLabel(self.page_pl13)
        self.label_nclips_13.setObjectName(u"label_nclips_13")
        self.label_nclips_13.setGeometry(QRect(620, 60, 61, 20))
        self.label_nclips_13.setFont(font7)
        self.label_nclips_13.setAlignment(Qt.AlignCenter)
        self.list_pl13 = QListWidget(self.page_pl13)
        self.list_pl13.setObjectName(u"list_pl13")
        self.list_pl13.setGeometry(QRect(150, 80, 601, 351))
        self.list_pl13.setStyleSheet(u"QListWidget {\n"
"    font-weight: bold;\n"
"    background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_dur_13 = QLabel(self.page_pl13)
        self.label_dur_13.setObjectName(u"label_dur_13")
        self.label_dur_13.setGeometry(QRect(220, 60, 101, 20))
        self.label_dur_13.setFont(font7)
        self.label_dur_13.setAlignment(Qt.AlignCenter)
        self.label_pl13 = QLabel(self.page_pl13)
        self.label_pl13.setObjectName(u"label_pl13")
        self.label_pl13.setGeometry(QRect(150, 30, 601, 51))
        self.label_pl13.setFont(font8)
        self.label_pl13.setStyleSheet(u"QLabel {\n"
"	font \"arial\"\n"
"    font-weight: bold;\n"
"	font-size: 20px;\n"
"	background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_pl13.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_pl13)
        self.label_pl13.raise_()
        self.pl13_add.raise_()
        self.pl13_delete.raise_()
        self.label_nclips_13.raise_()
        self.list_pl13.raise_()
        self.label_dur_13.raise_()
        self.page_pl18 = QWidget()
        self.page_pl18.setObjectName(u"page_pl18")
        self.pl18_add = QPushButton(self.page_pl18)
        self.pl18_add.setObjectName(u"pl18_add")
        self.pl18_add.setGeometry(QRect(150, 30, 71, 51))
        self.pl18_add.setStyleSheet(u"QPushButton {\n"
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
        self.pl18_add.setIcon(icon6)
        self.pl18_delete = QPushButton(self.page_pl18)
        self.pl18_delete.setObjectName(u"pl18_delete")
        self.pl18_delete.setGeometry(QRect(680, 30, 71, 51))
        self.pl18_delete.setStyleSheet(u"QPushButton {\n"
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
        self.pl18_delete.setIcon(icon5)
        self.label_nclips_18 = QLabel(self.page_pl18)
        self.label_nclips_18.setObjectName(u"label_nclips_18")
        self.label_nclips_18.setGeometry(QRect(620, 60, 61, 20))
        self.label_nclips_18.setFont(font7)
        self.label_nclips_18.setAlignment(Qt.AlignCenter)
        self.list_pl18 = QListWidget(self.page_pl18)
        self.list_pl18.setObjectName(u"list_pl18")
        self.list_pl18.setGeometry(QRect(150, 80, 601, 351))
        self.list_pl18.setStyleSheet(u"QListWidget {\n"
"    font-weight: bold;\n"
"    background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_dur_18 = QLabel(self.page_pl18)
        self.label_dur_18.setObjectName(u"label_dur_18")
        self.label_dur_18.setGeometry(QRect(220, 60, 101, 20))
        self.label_dur_18.setFont(font7)
        self.label_dur_18.setAlignment(Qt.AlignCenter)
        self.label_pl18 = QLabel(self.page_pl18)
        self.label_pl18.setObjectName(u"label_pl18")
        self.label_pl18.setGeometry(QRect(150, 30, 601, 51))
        self.label_pl18.setFont(font8)
        self.label_pl18.setStyleSheet(u"QLabel {\n"
"	font \"arial\"\n"
"    font-weight: bold;\n"
"	font-size: 20px;\n"
"	background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_pl18.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_pl18)
        self.label_pl18.raise_()
        self.pl18_add.raise_()
        self.pl18_delete.raise_()
        self.label_nclips_18.raise_()
        self.list_pl18.raise_()
        self.label_dur_18.raise_()
        self.page_pl17 = QWidget()
        self.page_pl17.setObjectName(u"page_pl17")
        self.pl17_add = QPushButton(self.page_pl17)
        self.pl17_add.setObjectName(u"pl17_add")
        self.pl17_add.setGeometry(QRect(150, 30, 71, 51))
        self.pl17_add.setStyleSheet(u"QPushButton {\n"
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
        self.pl17_add.setIcon(icon6)
        self.pl17_delete = QPushButton(self.page_pl17)
        self.pl17_delete.setObjectName(u"pl17_delete")
        self.pl17_delete.setGeometry(QRect(680, 30, 71, 51))
        self.pl17_delete.setStyleSheet(u"QPushButton {\n"
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
        self.pl17_delete.setIcon(icon5)
        self.label_nclips_17 = QLabel(self.page_pl17)
        self.label_nclips_17.setObjectName(u"label_nclips_17")
        self.label_nclips_17.setGeometry(QRect(620, 60, 61, 20))
        self.label_nclips_17.setFont(font7)
        self.label_nclips_17.setAlignment(Qt.AlignCenter)
        self.list_pl17 = QListWidget(self.page_pl17)
        self.list_pl17.setObjectName(u"list_pl17")
        self.list_pl17.setGeometry(QRect(150, 80, 601, 351))
        self.list_pl17.setStyleSheet(u"QListWidget {\n"
"    font-weight: bold;\n"
"    background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_dur_17 = QLabel(self.page_pl17)
        self.label_dur_17.setObjectName(u"label_dur_17")
        self.label_dur_17.setGeometry(QRect(220, 60, 101, 20))
        self.label_dur_17.setFont(font7)
        self.label_dur_17.setAlignment(Qt.AlignCenter)
        self.label_pl17 = QLabel(self.page_pl17)
        self.label_pl17.setObjectName(u"label_pl17")
        self.label_pl17.setGeometry(QRect(150, 30, 601, 51))
        self.label_pl17.setFont(font8)
        self.label_pl17.setStyleSheet(u"QLabel {\n"
"	font \"arial\"\n"
"    font-weight: bold;\n"
"	font-size: 20px;\n"
"	background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_pl17.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_pl17)
        self.label_pl17.raise_()
        self.pl17_add.raise_()
        self.pl17_delete.raise_()
        self.label_nclips_17.raise_()
        self.list_pl17.raise_()
        self.label_dur_17.raise_()
        self.page_pl16 = QWidget()
        self.page_pl16.setObjectName(u"page_pl16")
        self.pl16_add = QPushButton(self.page_pl16)
        self.pl16_add.setObjectName(u"pl16_add")
        self.pl16_add.setGeometry(QRect(150, 30, 71, 51))
        self.pl16_add.setStyleSheet(u"QPushButton {\n"
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
        self.pl16_add.setIcon(icon6)
        self.pl16_delete = QPushButton(self.page_pl16)
        self.pl16_delete.setObjectName(u"pl16_delete")
        self.pl16_delete.setGeometry(QRect(680, 30, 71, 51))
        self.pl16_delete.setStyleSheet(u"QPushButton {\n"
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
        self.pl16_delete.setIcon(icon5)
        self.label_nclips_16 = QLabel(self.page_pl16)
        self.label_nclips_16.setObjectName(u"label_nclips_16")
        self.label_nclips_16.setGeometry(QRect(620, 60, 61, 20))
        self.label_nclips_16.setFont(font7)
        self.label_nclips_16.setAlignment(Qt.AlignCenter)
        self.list_pl16 = QListWidget(self.page_pl16)
        self.list_pl16.setObjectName(u"list_pl16")
        self.list_pl16.setGeometry(QRect(150, 80, 601, 351))
        self.list_pl16.setStyleSheet(u"QListWidget {\n"
"    font-weight: bold;\n"
"    background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_dur_16 = QLabel(self.page_pl16)
        self.label_dur_16.setObjectName(u"label_dur_16")
        self.label_dur_16.setGeometry(QRect(220, 60, 101, 20))
        self.label_dur_16.setFont(font7)
        self.label_dur_16.setAlignment(Qt.AlignCenter)
        self.label_pl16 = QLabel(self.page_pl16)
        self.label_pl16.setObjectName(u"label_pl16")
        self.label_pl16.setGeometry(QRect(150, 30, 601, 51))
        self.label_pl16.setFont(font8)
        self.label_pl16.setStyleSheet(u"QLabel {\n"
"	font \"arial\"\n"
"    font-weight: bold;\n"
"	font-size: 20px;\n"
"	background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_pl16.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_pl16)
        self.label_pl16.raise_()
        self.pl16_add.raise_()
        self.pl16_delete.raise_()
        self.label_nclips_16.raise_()
        self.list_pl16.raise_()
        self.label_dur_16.raise_()
        self.page_pl15 = QWidget()
        self.page_pl15.setObjectName(u"page_pl15")
        self.pl15_add = QPushButton(self.page_pl15)
        self.pl15_add.setObjectName(u"pl15_add")
        self.pl15_add.setGeometry(QRect(150, 30, 71, 51))
        self.pl15_add.setStyleSheet(u"QPushButton {\n"
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
        self.pl15_add.setIcon(icon6)
        self.pl15_delete = QPushButton(self.page_pl15)
        self.pl15_delete.setObjectName(u"pl15_delete")
        self.pl15_delete.setGeometry(QRect(680, 30, 71, 51))
        self.pl15_delete.setStyleSheet(u"QPushButton {\n"
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
        self.pl15_delete.setIcon(icon5)
        self.label_nclips_15 = QLabel(self.page_pl15)
        self.label_nclips_15.setObjectName(u"label_nclips_15")
        self.label_nclips_15.setGeometry(QRect(620, 60, 61, 20))
        self.label_nclips_15.setFont(font7)
        self.label_nclips_15.setAlignment(Qt.AlignCenter)
        self.list_pl15 = QListWidget(self.page_pl15)
        self.list_pl15.setObjectName(u"list_pl15")
        self.list_pl15.setGeometry(QRect(150, 80, 601, 351))
        self.list_pl15.setStyleSheet(u"QListWidget {\n"
"    font-weight: bold;\n"
"    background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_dur_15 = QLabel(self.page_pl15)
        self.label_dur_15.setObjectName(u"label_dur_15")
        self.label_dur_15.setGeometry(QRect(220, 60, 101, 20))
        self.label_dur_15.setFont(font7)
        self.label_dur_15.setAlignment(Qt.AlignCenter)
        self.label_pl15 = QLabel(self.page_pl15)
        self.label_pl15.setObjectName(u"label_pl15")
        self.label_pl15.setGeometry(QRect(150, 30, 601, 51))
        self.label_pl15.setFont(font8)
        self.label_pl15.setStyleSheet(u"QLabel {\n"
"	font \"arial\"\n"
"    font-weight: bold;\n"
"	font-size: 20px;\n"
"	background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_pl15.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_pl15)
        self.label_pl15.raise_()
        self.pl15_add.raise_()
        self.pl15_delete.raise_()
        self.label_nclips_15.raise_()
        self.list_pl15.raise_()
        self.label_dur_15.raise_()
        self.page_pl14 = QWidget()
        self.page_pl14.setObjectName(u"page_pl14")
        self.pl14_add = QPushButton(self.page_pl14)
        self.pl14_add.setObjectName(u"pl14_add")
        self.pl14_add.setGeometry(QRect(150, 30, 71, 51))
        self.pl14_add.setStyleSheet(u"QPushButton {\n"
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
        self.pl14_add.setIcon(icon6)
        self.pl14_delete = QPushButton(self.page_pl14)
        self.pl14_delete.setObjectName(u"pl14_delete")
        self.pl14_delete.setGeometry(QRect(680, 30, 71, 51))
        self.pl14_delete.setStyleSheet(u"QPushButton {\n"
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
        self.pl14_delete.setIcon(icon5)
        self.label_nclips_14 = QLabel(self.page_pl14)
        self.label_nclips_14.setObjectName(u"label_nclips_14")
        self.label_nclips_14.setGeometry(QRect(620, 60, 61, 20))
        self.label_nclips_14.setFont(font7)
        self.label_nclips_14.setAlignment(Qt.AlignCenter)
        self.list_pl14 = QListWidget(self.page_pl14)
        self.list_pl14.setObjectName(u"list_pl14")
        self.list_pl14.setGeometry(QRect(150, 80, 601, 351))
        self.list_pl14.setStyleSheet(u"QListWidget {\n"
"    font-weight: bold;\n"
"    background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_dur_14 = QLabel(self.page_pl14)
        self.label_dur_14.setObjectName(u"label_dur_14")
        self.label_dur_14.setGeometry(QRect(220, 60, 101, 20))
        self.label_dur_14.setFont(font7)
        self.label_dur_14.setAlignment(Qt.AlignCenter)
        self.label_pl14 = QLabel(self.page_pl14)
        self.label_pl14.setObjectName(u"label_pl14")
        self.label_pl14.setGeometry(QRect(150, 30, 601, 51))
        self.label_pl14.setFont(font8)
        self.label_pl14.setStyleSheet(u"QLabel {\n"
"	font \"arial\"\n"
"    font-weight: bold;\n"
"	font-size: 20px;\n"
"	background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_pl14.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_pl14)
        self.label_pl14.raise_()
        self.pl14_add.raise_()
        self.pl14_delete.raise_()
        self.label_nclips_14.raise_()
        self.list_pl14.raise_()
        self.label_dur_14.raise_()
        self.page_pl12 = QWidget()
        self.page_pl12.setObjectName(u"page_pl12")
        self.pl12_add = QPushButton(self.page_pl12)
        self.pl12_add.setObjectName(u"pl12_add")
        self.pl12_add.setGeometry(QRect(150, 30, 71, 51))
        self.pl12_add.setStyleSheet(u"QPushButton {\n"
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
        self.pl12_add.setIcon(icon6)
        self.pl12_delete = QPushButton(self.page_pl12)
        self.pl12_delete.setObjectName(u"pl12_delete")
        self.pl12_delete.setGeometry(QRect(680, 30, 71, 51))
        self.pl12_delete.setStyleSheet(u"QPushButton {\n"
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
        self.pl12_delete.setIcon(icon5)
        self.label_nclips_12 = QLabel(self.page_pl12)
        self.label_nclips_12.setObjectName(u"label_nclips_12")
        self.label_nclips_12.setGeometry(QRect(620, 60, 61, 20))
        self.label_nclips_12.setFont(font7)
        self.label_nclips_12.setAlignment(Qt.AlignCenter)
        self.list_pl12 = QListWidget(self.page_pl12)
        self.list_pl12.setObjectName(u"list_pl12")
        self.list_pl12.setGeometry(QRect(150, 80, 601, 351))
        self.list_pl12.setStyleSheet(u"QListWidget {\n"
"    font-weight: bold;\n"
"    background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_dur_12 = QLabel(self.page_pl12)
        self.label_dur_12.setObjectName(u"label_dur_12")
        self.label_dur_12.setGeometry(QRect(220, 60, 101, 20))
        self.label_dur_12.setFont(font7)
        self.label_dur_12.setAlignment(Qt.AlignCenter)
        self.label_pl12 = QLabel(self.page_pl12)
        self.label_pl12.setObjectName(u"label_pl12")
        self.label_pl12.setGeometry(QRect(150, 30, 601, 51))
        self.label_pl12.setFont(font8)
        self.label_pl12.setStyleSheet(u"QLabel {\n"
"	font \"arial\"\n"
"    font-weight: bold;\n"
"	font-size: 20px;\n"
"	background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_pl12.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_pl12)
        self.label_pl12.raise_()
        self.pl12_add.raise_()
        self.pl12_delete.raise_()
        self.label_nclips_12.raise_()
        self.list_pl12.raise_()
        self.label_dur_12.raise_()
        self.page_pl9 = QWidget()
        self.page_pl9.setObjectName(u"page_pl9")
        self.pl9_add = QPushButton(self.page_pl9)
        self.pl9_add.setObjectName(u"pl9_add")
        self.pl9_add.setGeometry(QRect(150, 30, 71, 51))
        self.pl9_add.setStyleSheet(u"QPushButton {\n"
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
        self.pl9_add.setIcon(icon6)
        self.pl9_delete = QPushButton(self.page_pl9)
        self.pl9_delete.setObjectName(u"pl9_delete")
        self.pl9_delete.setGeometry(QRect(680, 30, 71, 51))
        self.pl9_delete.setStyleSheet(u"QPushButton {\n"
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
        self.pl9_delete.setIcon(icon5)
        self.label_nclips_9 = QLabel(self.page_pl9)
        self.label_nclips_9.setObjectName(u"label_nclips_9")
        self.label_nclips_9.setGeometry(QRect(620, 60, 61, 20))
        self.label_nclips_9.setFont(font7)
        self.label_nclips_9.setAlignment(Qt.AlignCenter)
        self.list_pl9 = QListWidget(self.page_pl9)
        self.list_pl9.setObjectName(u"list_pl9")
        self.list_pl9.setGeometry(QRect(150, 80, 601, 351))
        self.list_pl9.setStyleSheet(u"QListWidget {\n"
"    font-weight: bold;\n"
"    background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_dur_9 = QLabel(self.page_pl9)
        self.label_dur_9.setObjectName(u"label_dur_9")
        self.label_dur_9.setGeometry(QRect(220, 60, 101, 20))
        self.label_dur_9.setFont(font7)
        self.label_dur_9.setAlignment(Qt.AlignCenter)
        self.label_pl9 = QLabel(self.page_pl9)
        self.label_pl9.setObjectName(u"label_pl9")
        self.label_pl9.setGeometry(QRect(150, 30, 601, 51))
        self.label_pl9.setFont(font8)
        self.label_pl9.setStyleSheet(u"QLabel {\n"
"	font \"arial\"\n"
"    font-weight: bold;\n"
"	font-size: 20px;\n"
"	background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_pl9.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_pl9)
        self.label_pl9.raise_()
        self.pl9_add.raise_()
        self.pl9_delete.raise_()
        self.label_nclips_9.raise_()
        self.list_pl9.raise_()
        self.label_dur_9.raise_()
        self.page_pl10 = QWidget()
        self.page_pl10.setObjectName(u"page_pl10")
        self.pl10_add = QPushButton(self.page_pl10)
        self.pl10_add.setObjectName(u"pl10_add")
        self.pl10_add.setGeometry(QRect(150, 30, 71, 51))
        self.pl10_add.setStyleSheet(u"QPushButton {\n"
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
        self.pl10_add.setIcon(icon6)
        self.pl10_delete = QPushButton(self.page_pl10)
        self.pl10_delete.setObjectName(u"pl10_delete")
        self.pl10_delete.setGeometry(QRect(680, 30, 71, 51))
        self.pl10_delete.setStyleSheet(u"QPushButton {\n"
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
        self.pl10_delete.setIcon(icon5)
        self.label_nclips_10 = QLabel(self.page_pl10)
        self.label_nclips_10.setObjectName(u"label_nclips_10")
        self.label_nclips_10.setGeometry(QRect(620, 60, 61, 20))
        self.label_nclips_10.setFont(font7)
        self.label_nclips_10.setAlignment(Qt.AlignCenter)
        self.list_pl10 = QListWidget(self.page_pl10)
        self.list_pl10.setObjectName(u"list_pl10")
        self.list_pl10.setGeometry(QRect(150, 80, 601, 351))
        self.list_pl10.setStyleSheet(u"QListWidget {\n"
"    font-weight: bold;\n"
"    background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_dur_10 = QLabel(self.page_pl10)
        self.label_dur_10.setObjectName(u"label_dur_10")
        self.label_dur_10.setGeometry(QRect(220, 60, 101, 20))
        self.label_dur_10.setFont(font7)
        self.label_dur_10.setAlignment(Qt.AlignCenter)
        self.label_pl10 = QLabel(self.page_pl10)
        self.label_pl10.setObjectName(u"label_pl10")
        self.label_pl10.setGeometry(QRect(150, 30, 601, 51))
        self.label_pl10.setFont(font8)
        self.label_pl10.setStyleSheet(u"QLabel {\n"
"	font \"arial\"\n"
"    font-weight: bold;\n"
"	font-size: 20px;\n"
"	background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_pl10.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_pl10)
        self.label_pl10.raise_()
        self.pl10_add.raise_()
        self.pl10_delete.raise_()
        self.label_nclips_10.raise_()
        self.list_pl10.raise_()
        self.label_dur_10.raise_()
        self.page_pl8 = QWidget()
        self.page_pl8.setObjectName(u"page_pl8")
        self.pl8_add = QPushButton(self.page_pl8)
        self.pl8_add.setObjectName(u"pl8_add")
        self.pl8_add.setGeometry(QRect(150, 30, 71, 51))
        self.pl8_add.setStyleSheet(u"QPushButton {\n"
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
        self.pl8_add.setIcon(icon6)
        self.pl8_delete = QPushButton(self.page_pl8)
        self.pl8_delete.setObjectName(u"pl8_delete")
        self.pl8_delete.setGeometry(QRect(680, 30, 71, 51))
        self.pl8_delete.setStyleSheet(u"QPushButton {\n"
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
        self.pl8_delete.setIcon(icon5)
        self.label_nclips_8 = QLabel(self.page_pl8)
        self.label_nclips_8.setObjectName(u"label_nclips_8")
        self.label_nclips_8.setGeometry(QRect(620, 60, 61, 20))
        self.label_nclips_8.setFont(font7)
        self.label_nclips_8.setAlignment(Qt.AlignCenter)
        self.list_pl8 = QListWidget(self.page_pl8)
        self.list_pl8.setObjectName(u"list_pl8")
        self.list_pl8.setGeometry(QRect(150, 80, 601, 351))
        self.list_pl8.setStyleSheet(u"QListWidget {\n"
"    font-weight: bold;\n"
"    background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_dur_8 = QLabel(self.page_pl8)
        self.label_dur_8.setObjectName(u"label_dur_8")
        self.label_dur_8.setGeometry(QRect(220, 60, 101, 20))
        self.label_dur_8.setFont(font7)
        self.label_dur_8.setAlignment(Qt.AlignCenter)
        self.label_pl8 = QLabel(self.page_pl8)
        self.label_pl8.setObjectName(u"label_pl8")
        self.label_pl8.setGeometry(QRect(150, 30, 601, 51))
        self.label_pl8.setFont(font8)
        self.label_pl8.setStyleSheet(u"QLabel {\n"
"	font \"arial\"\n"
"    font-weight: bold;\n"
"	font-size: 20px;\n"
"	background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_pl8.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_pl8)
        self.label_pl8.raise_()
        self.pl8_add.raise_()
        self.pl8_delete.raise_()
        self.label_nclips_8.raise_()
        self.list_pl8.raise_()
        self.label_dur_8.raise_()
        self.page_pl3 = QWidget()
        self.page_pl3.setObjectName(u"page_pl3")
        self.pl3_add = QPushButton(self.page_pl3)
        self.pl3_add.setObjectName(u"pl3_add")
        self.pl3_add.setGeometry(QRect(150, 30, 71, 51))
        self.pl3_add.setStyleSheet(u"QPushButton {\n"
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
        self.pl3_add.setIcon(icon6)
        self.pl3_delete = QPushButton(self.page_pl3)
        self.pl3_delete.setObjectName(u"pl3_delete")
        self.pl3_delete.setGeometry(QRect(680, 30, 71, 51))
        self.pl3_delete.setStyleSheet(u"QPushButton {\n"
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
        self.pl3_delete.setIcon(icon5)
        self.label_nclips_3 = QLabel(self.page_pl3)
        self.label_nclips_3.setObjectName(u"label_nclips_3")
        self.label_nclips_3.setGeometry(QRect(620, 60, 61, 20))
        self.label_nclips_3.setFont(font7)
        self.label_nclips_3.setAlignment(Qt.AlignCenter)
        self.list_pl3 = QListWidget(self.page_pl3)
        self.list_pl3.setObjectName(u"list_pl3")
        self.list_pl3.setGeometry(QRect(150, 80, 601, 351))
        self.list_pl3.setStyleSheet(u"QListWidget {\n"
"    font-weight: bold;\n"
"    background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_dur_3 = QLabel(self.page_pl3)
        self.label_dur_3.setObjectName(u"label_dur_3")
        self.label_dur_3.setGeometry(QRect(220, 60, 101, 20))
        self.label_dur_3.setFont(font7)
        self.label_dur_3.setAlignment(Qt.AlignCenter)
        self.label_pl3 = QLabel(self.page_pl3)
        self.label_pl3.setObjectName(u"label_pl3")
        self.label_pl3.setGeometry(QRect(150, 30, 601, 51))
        self.label_pl3.setFont(font8)
        self.label_pl3.setStyleSheet(u"QLabel {\n"
"	font \"arial\"\n"
"    font-weight: bold;\n"
"	font-size: 20px;\n"
"	background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_pl3.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_pl3)
        self.label_pl3.raise_()
        self.pl3_add.raise_()
        self.pl3_delete.raise_()
        self.label_nclips_3.raise_()
        self.list_pl3.raise_()
        self.label_dur_3.raise_()
        self.page_pl4 = QWidget()
        self.page_pl4.setObjectName(u"page_pl4")
        self.pl4_add = QPushButton(self.page_pl4)
        self.pl4_add.setObjectName(u"pl4_add")
        self.pl4_add.setGeometry(QRect(150, 30, 71, 51))
        self.pl4_add.setStyleSheet(u"QPushButton {\n"
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
        self.pl4_add.setIcon(icon6)
        self.pl4_delete = QPushButton(self.page_pl4)
        self.pl4_delete.setObjectName(u"pl4_delete")
        self.pl4_delete.setGeometry(QRect(680, 30, 71, 51))
        self.pl4_delete.setStyleSheet(u"QPushButton {\n"
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
        self.pl4_delete.setIcon(icon5)
        self.label_nclips_4 = QLabel(self.page_pl4)
        self.label_nclips_4.setObjectName(u"label_nclips_4")
        self.label_nclips_4.setGeometry(QRect(620, 60, 61, 20))
        self.label_nclips_4.setFont(font7)
        self.label_nclips_4.setAlignment(Qt.AlignCenter)
        self.list_pl4 = QListWidget(self.page_pl4)
        self.list_pl4.setObjectName(u"list_pl4")
        self.list_pl4.setGeometry(QRect(150, 80, 601, 351))
        self.list_pl4.setStyleSheet(u"QListWidget {\n"
"    font-weight: bold;\n"
"    background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_dur_4 = QLabel(self.page_pl4)
        self.label_dur_4.setObjectName(u"label_dur_4")
        self.label_dur_4.setGeometry(QRect(220, 60, 101, 20))
        self.label_dur_4.setFont(font7)
        self.label_dur_4.setAlignment(Qt.AlignCenter)
        self.label_pl4 = QLabel(self.page_pl4)
        self.label_pl4.setObjectName(u"label_pl4")
        self.label_pl4.setGeometry(QRect(150, 30, 601, 51))
        self.label_pl4.setFont(font8)
        self.label_pl4.setStyleSheet(u"QLabel {\n"
"	font \"arial\"\n"
"    font-weight: bold;\n"
"	font-size: 20px;\n"
"	background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_pl4.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_pl4)
        self.label_pl4.raise_()
        self.pl4_add.raise_()
        self.pl4_delete.raise_()
        self.label_nclips_4.raise_()
        self.list_pl4.raise_()
        self.label_dur_4.raise_()
        self.page_pl7 = QWidget()
        self.page_pl7.setObjectName(u"page_pl7")
        self.pl7_add = QPushButton(self.page_pl7)
        self.pl7_add.setObjectName(u"pl7_add")
        self.pl7_add.setGeometry(QRect(150, 30, 71, 51))
        self.pl7_add.setStyleSheet(u"QPushButton {\n"
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
        self.pl7_add.setIcon(icon6)
        self.pl7_delete = QPushButton(self.page_pl7)
        self.pl7_delete.setObjectName(u"pl7_delete")
        self.pl7_delete.setGeometry(QRect(680, 30, 71, 51))
        self.pl7_delete.setStyleSheet(u"QPushButton {\n"
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
        self.pl7_delete.setIcon(icon5)
        self.label_nclips_7 = QLabel(self.page_pl7)
        self.label_nclips_7.setObjectName(u"label_nclips_7")
        self.label_nclips_7.setGeometry(QRect(620, 60, 61, 20))
        self.label_nclips_7.setFont(font7)
        self.label_nclips_7.setAlignment(Qt.AlignCenter)
        self.list_pl7 = QListWidget(self.page_pl7)
        self.list_pl7.setObjectName(u"list_pl7")
        self.list_pl7.setGeometry(QRect(150, 80, 601, 351))
        self.list_pl7.setStyleSheet(u"QListWidget {\n"
"    font-weight: bold;\n"
"    background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_dur_7 = QLabel(self.page_pl7)
        self.label_dur_7.setObjectName(u"label_dur_7")
        self.label_dur_7.setGeometry(QRect(220, 60, 101, 20))
        self.label_dur_7.setFont(font7)
        self.label_dur_7.setAlignment(Qt.AlignCenter)
        self.label_pl7 = QLabel(self.page_pl7)
        self.label_pl7.setObjectName(u"label_pl7")
        self.label_pl7.setGeometry(QRect(150, 30, 601, 51))
        self.label_pl7.setFont(font8)
        self.label_pl7.setStyleSheet(u"QLabel {\n"
"	font \"arial\"\n"
"    font-weight: bold;\n"
"	font-size: 20px;\n"
"	background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_pl7.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_pl7)
        self.label_pl7.raise_()
        self.pl7_add.raise_()
        self.pl7_delete.raise_()
        self.label_nclips_7.raise_()
        self.list_pl7.raise_()
        self.label_dur_7.raise_()
        self.page_pl6 = QWidget()
        self.page_pl6.setObjectName(u"page_pl6")
        self.pl6_add = QPushButton(self.page_pl6)
        self.pl6_add.setObjectName(u"pl6_add")
        self.pl6_add.setGeometry(QRect(150, 30, 71, 51))
        self.pl6_add.setStyleSheet(u"QPushButton {\n"
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
        self.pl6_add.setIcon(icon6)
        self.pl6_delete = QPushButton(self.page_pl6)
        self.pl6_delete.setObjectName(u"pl6_delete")
        self.pl6_delete.setGeometry(QRect(680, 30, 71, 51))
        self.pl6_delete.setStyleSheet(u"QPushButton {\n"
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
        self.pl6_delete.setIcon(icon5)
        self.label_nclips_6 = QLabel(self.page_pl6)
        self.label_nclips_6.setObjectName(u"label_nclips_6")
        self.label_nclips_6.setGeometry(QRect(620, 60, 61, 20))
        self.label_nclips_6.setFont(font7)
        self.label_nclips_6.setAlignment(Qt.AlignCenter)
        self.list_pl6 = QListWidget(self.page_pl6)
        self.list_pl6.setObjectName(u"list_pl6")
        self.list_pl6.setGeometry(QRect(150, 80, 601, 351))
        self.list_pl6.setStyleSheet(u"QListWidget {\n"
"    font-weight: bold;\n"
"    background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_dur_6 = QLabel(self.page_pl6)
        self.label_dur_6.setObjectName(u"label_dur_6")
        self.label_dur_6.setGeometry(QRect(220, 60, 101, 20))
        self.label_dur_6.setFont(font7)
        self.label_dur_6.setAlignment(Qt.AlignCenter)
        self.label_pl6 = QLabel(self.page_pl6)
        self.label_pl6.setObjectName(u"label_pl6")
        self.label_pl6.setGeometry(QRect(150, 30, 601, 51))
        self.label_pl6.setFont(font8)
        self.label_pl6.setStyleSheet(u"QLabel {\n"
"	font \"arial\"\n"
"    font-weight: bold;\n"
"	font-size: 20px;\n"
"	background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_pl6.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_pl6)
        self.label_pl6.raise_()
        self.pl6_add.raise_()
        self.pl6_delete.raise_()
        self.label_nclips_6.raise_()
        self.list_pl6.raise_()
        self.label_dur_6.raise_()
        self.page_pl5 = QWidget()
        self.page_pl5.setObjectName(u"page_pl5")
        self.pl5_add = QPushButton(self.page_pl5)
        self.pl5_add.setObjectName(u"pl5_add")
        self.pl5_add.setGeometry(QRect(150, 30, 71, 51))
        self.pl5_add.setStyleSheet(u"QPushButton {\n"
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
        self.pl5_add.setIcon(icon6)
        self.pl5_delete = QPushButton(self.page_pl5)
        self.pl5_delete.setObjectName(u"pl5_delete")
        self.pl5_delete.setGeometry(QRect(680, 30, 71, 51))
        self.pl5_delete.setStyleSheet(u"QPushButton {\n"
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
        self.pl5_delete.setIcon(icon5)
        self.label_nclips_5 = QLabel(self.page_pl5)
        self.label_nclips_5.setObjectName(u"label_nclips_5")
        self.label_nclips_5.setGeometry(QRect(620, 60, 61, 20))
        self.label_nclips_5.setFont(font7)
        self.label_nclips_5.setAlignment(Qt.AlignCenter)
        self.list_pl5 = QListWidget(self.page_pl5)
        self.list_pl5.setObjectName(u"list_pl5")
        self.list_pl5.setGeometry(QRect(150, 80, 601, 351))
        self.list_pl5.setStyleSheet(u"QListWidget {\n"
"    font-weight: bold;\n"
"    background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_dur_5 = QLabel(self.page_pl5)
        self.label_dur_5.setObjectName(u"label_dur_5")
        self.label_dur_5.setGeometry(QRect(220, 60, 101, 20))
        self.label_dur_5.setFont(font7)
        self.label_dur_5.setAlignment(Qt.AlignCenter)
        self.label_pl5 = QLabel(self.page_pl5)
        self.label_pl5.setObjectName(u"label_pl5")
        self.label_pl5.setGeometry(QRect(150, 30, 601, 51))
        self.label_pl5.setFont(font8)
        self.label_pl5.setStyleSheet(u"QLabel {\n"
"	font \"arial\"\n"
"    font-weight: bold;\n"
"	font-size: 20px;\n"
"	background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_pl5.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_pl5)
        self.label_pl5.raise_()
        self.pl5_add.raise_()
        self.pl5_delete.raise_()
        self.label_nclips_5.raise_()
        self.list_pl5.raise_()
        self.label_dur_5.raise_()
        self.page_pl2 = QWidget()
        self.page_pl2.setObjectName(u"page_pl2")
        self.pl2_add = QPushButton(self.page_pl2)
        self.pl2_add.setObjectName(u"pl2_add")
        self.pl2_add.setGeometry(QRect(150, 30, 71, 51))
        self.pl2_add.setStyleSheet(u"QPushButton {\n"
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
        self.pl2_add.setIcon(icon6)
        self.pl2_delete = QPushButton(self.page_pl2)
        self.pl2_delete.setObjectName(u"pl2_delete")
        self.pl2_delete.setGeometry(QRect(680, 30, 71, 51))
        self.pl2_delete.setStyleSheet(u"QPushButton {\n"
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
        self.pl2_delete.setIcon(icon5)
        self.label_nclips_2 = QLabel(self.page_pl2)
        self.label_nclips_2.setObjectName(u"label_nclips_2")
        self.label_nclips_2.setGeometry(QRect(620, 60, 61, 20))
        self.label_nclips_2.setFont(font7)
        self.label_nclips_2.setAlignment(Qt.AlignCenter)
        self.list_pl2 = QListWidget(self.page_pl2)
        self.list_pl2.setObjectName(u"list_pl2")
        self.list_pl2.setGeometry(QRect(150, 80, 601, 351))
        self.list_pl2.setStyleSheet(u"QListWidget {\n"
"    font-weight: bold;\n"
"    background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_dur_2 = QLabel(self.page_pl2)
        self.label_dur_2.setObjectName(u"label_dur_2")
        self.label_dur_2.setGeometry(QRect(220, 60, 101, 20))
        self.label_dur_2.setFont(font7)
        self.label_dur_2.setAlignment(Qt.AlignCenter)
        self.label_pl2 = QLabel(self.page_pl2)
        self.label_pl2.setObjectName(u"label_pl2")
        self.label_pl2.setGeometry(QRect(150, 30, 601, 51))
        self.label_pl2.setFont(font8)
        self.label_pl2.setStyleSheet(u"QLabel {\n"
"	font \"arial\"\n"
"    font-weight: bold;\n"
"	font-size: 20px;\n"
"	background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_pl2.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_pl2)
        self.label_pl2.raise_()
        self.pl2_add.raise_()
        self.pl2_delete.raise_()
        self.label_nclips_2.raise_()
        self.list_pl2.raise_()
        self.label_dur_2.raise_()
        self.page_pl1 = QWidget()
        self.page_pl1.setObjectName(u"page_pl1")
        self.list_pl1 = QListWidget(self.page_pl1)
        self.list_pl1.setObjectName(u"list_pl1")
        self.list_pl1.setGeometry(QRect(150, 80, 601, 351))
        self.list_pl1.setStyleSheet(u"QListWidget {\n"
"    font-weight: bold;\n"
"    background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.pl1_delete = QPushButton(self.page_pl1)
        self.pl1_delete.setObjectName(u"pl1_delete")
        self.pl1_delete.setGeometry(QRect(680, 30, 71, 51))
        self.pl1_delete.setStyleSheet(u"QPushButton {\n"
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
        self.pl1_delete.setIcon(icon5)
        self.label_pl1 = QLabel(self.page_pl1)
        self.label_pl1.setObjectName(u"label_pl1")
        self.label_pl1.setGeometry(QRect(150, 30, 601, 51))
        self.label_pl1.setFont(font8)
        self.label_pl1.setStyleSheet(u"QLabel {\n"
"	font \"arial\"\n"
"    font-weight: bold;\n"
"	font-size: 20px;\n"
"	background-color: transparent;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_pl1.setAlignment(Qt.AlignCenter)
        self.pl1_add = QPushButton(self.page_pl1)
        self.pl1_add.setObjectName(u"pl1_add")
        self.pl1_add.setGeometry(QRect(150, 30, 71, 51))
        self.pl1_add.setStyleSheet(u"QPushButton {\n"
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
        self.pl1_add.setIcon(icon6)
        self.label_dur_1 = QLabel(self.page_pl1)
        self.label_dur_1.setObjectName(u"label_dur_1")
        self.label_dur_1.setGeometry(QRect(220, 60, 101, 20))
        self.label_dur_1.setFont(font7)
        self.label_dur_1.setAlignment(Qt.AlignCenter)
        self.label_nclips_1 = QLabel(self.page_pl1)
        self.label_nclips_1.setObjectName(u"label_nclips_1")
        self.label_nclips_1.setGeometry(QRect(620, 60, 61, 20))
        self.label_nclips_1.setFont(font7)
        self.label_nclips_1.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_pl1)
        self.label_pl1.raise_()
        self.list_pl1.raise_()
        self.pl1_delete.raise_()
        self.pl1_add.raise_()
        self.label_dur_1.raise_()
        self.label_nclips_1.raise_()
        self.page_estrella2 = QWidget()
        self.page_estrella2.setObjectName(u"page_estrella2")
        self.label_estrella2 = QLabel(self.page_estrella2)
        self.label_estrella2.setObjectName(u"label_estrella2")
        self.label_estrella2.setGeometry(QRect(120, 20, 661, 51))
        self.label_estrella2.setStyleSheet(u"QLabel {\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_estrella2.setPixmap(QPixmap(u":/20x20/icons/20x20/cil-star.png"))
        self.label_estrella2.setAlignment(Qt.AlignCenter)
        self.list_estrella2 = QListWidget(self.page_estrella2)
        self.list_estrella2.setObjectName(u"list_estrella2")
        self.list_estrella2.setGeometry(QRect(120, 70, 661, 371))
        self.list_estrella2.setStyleSheet(u"QListWidget {\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_estrella2_2 = QLabel(self.page_estrella2)
        self.label_estrella2_2.setObjectName(u"label_estrella2_2")
        self.label_estrella2_2.setGeometry(QRect(465, 20, 21, 51))
        self.label_estrella2_2.setStyleSheet(u"background-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.label_estrella2_2.setPixmap(QPixmap(u":/20x20/icons/20x20/cil-star.png"))
        self.estrella2_delete = QPushButton(self.page_estrella2)
        self.estrella2_delete.setObjectName(u"estrella2_delete")
        self.estrella2_delete.setGeometry(QRect(710, 20, 71, 51))
        self.estrella2_delete.setStyleSheet(u"QPushButton {\n"
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
        self.estrella2_delete.setIcon(icon5)
        self.estrella2_add = QPushButton(self.page_estrella2)
        self.estrella2_add.setObjectName(u"estrella2_add")
        self.estrella2_add.setGeometry(QRect(120, 20, 71, 51))
        self.estrella2_add.setStyleSheet(u"QPushButton {\n"
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
        self.estrella2_add.setIcon(icon6)
        self.stackedWidget.addWidget(self.page_estrella2)
        self.page_estrella3 = QWidget()
        self.page_estrella3.setObjectName(u"page_estrella3")
        self.label_estrella3 = QLabel(self.page_estrella3)
        self.label_estrella3.setObjectName(u"label_estrella3")
        self.label_estrella3.setGeometry(QRect(120, 20, 661, 51))
        self.label_estrella3.setStyleSheet(u"QLabel {\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_estrella3.setPixmap(QPixmap(u":/20x20/icons/20x20/cil-star.png"))
        self.label_estrella3.setAlignment(Qt.AlignCenter)
        self.label_estrella3_2 = QLabel(self.page_estrella3)
        self.label_estrella3_2.setObjectName(u"label_estrella3_2")
        self.label_estrella3_2.setGeometry(QRect(470, 20, 21, 51))
        self.label_estrella3_2.setStyleSheet(u"background-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.label_estrella3_2.setPixmap(QPixmap(u":/20x20/icons/20x20/cil-star.png"))
        self.list_estrella3 = QListWidget(self.page_estrella3)
        self.list_estrella3.setObjectName(u"list_estrella3")
        self.list_estrella3.setGeometry(QRect(120, 70, 661, 371))
        self.list_estrella3.setStyleSheet(u"QListWidget {\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}")
        self.label_estrella3_3 = QLabel(self.page_estrella3)
        self.label_estrella3_3.setObjectName(u"label_estrella3_3")
        self.label_estrella3_3.setGeometry(QRect(410, 20, 21, 51))
        self.label_estrella3_3.setStyleSheet(u"background-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.label_estrella3_3.setPixmap(QPixmap(u":/20x20/icons/20x20/cil-star.png"))
        self.estrella3_delete = QPushButton(self.page_estrella3)
        self.estrella3_delete.setObjectName(u"estrella3_delete")
        self.estrella3_delete.setGeometry(QRect(710, 20, 71, 51))
        self.estrella3_delete.setStyleSheet(u"QPushButton {\n"
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
        self.estrella3_delete.setIcon(icon5)
        self.estrella3_add = QPushButton(self.page_estrella3)
        self.estrella3_add.setObjectName(u"estrella3_add")
        self.estrella3_add.setGeometry(QRect(120, 20, 71, 51))
        self.estrella3_add.setStyleSheet(u"QPushButton {\n"
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
        self.estrella3_add.setIcon(icon6)
        self.stackedWidget.addWidget(self.page_estrella3)
        self.page_simulator = QWidget()
        self.page_simulator.setObjectName(u"page_simulator")
        self.sim_menu = QPushButton(self.page_simulator)
        self.sim_menu.setObjectName(u"sim_menu")
        self.sim_menu.setGeometry(QRect(40, 20, 51, 51))
        self.sim_menu.setFont(font6)
        self.sim_menu.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 8px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.sim_take = QPushButton(self.page_simulator)
        self.sim_take.setObjectName(u"sim_take")
        self.sim_take.setGeometry(QRect(370, 360, 101, 81))
        self.sim_take.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.sim_shift = QPushButton(self.page_simulator)
        self.sim_shift.setObjectName(u"sim_shift")
        self.sim_shift.setGeometry(QRect(100, 20, 51, 51))
        self.sim_shift.setFont(font6)
        self.sim_shift.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 8px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.sim_f1 = QPushButton(self.page_simulator)
        self.sim_f1.setObjectName(u"sim_f1")
        self.sim_f1.setGeometry(QRect(170, 20, 51, 51))
        self.sim_f1.setFont(font6)
        self.sim_f1.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 10px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.sim_f2 = QPushButton(self.page_simulator)
        self.sim_f2.setObjectName(u"sim_f2")
        self.sim_f2.setGeometry(QRect(230, 20, 51, 51))
        self.sim_f2.setFont(font6)
        self.sim_f2.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 10px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.sim_f3 = QPushButton(self.page_simulator)
        self.sim_f3.setObjectName(u"sim_f3")
        self.sim_f3.setGeometry(QRect(290, 20, 51, 51))
        self.sim_f3.setFont(font6)
        self.sim_f3.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 10px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.sim_f4 = QPushButton(self.page_simulator)
        self.sim_f4.setObjectName(u"sim_f4")
        self.sim_f4.setGeometry(QRect(350, 20, 51, 51))
        self.sim_f4.setFont(font6)
        self.sim_f4.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 10px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.sim_f5 = QPushButton(self.page_simulator)
        self.sim_f5.setObjectName(u"sim_f5")
        self.sim_f5.setGeometry(QRect(410, 20, 51, 51))
        self.sim_f5.setFont(font6)
        self.sim_f5.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 10px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.sim_f6 = QPushButton(self.page_simulator)
        self.sim_f6.setObjectName(u"sim_f6")
        self.sim_f6.setGeometry(QRect(470, 20, 51, 51))
        self.sim_f6.setFont(font6)
        self.sim_f6.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 10px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.sim_f7 = QPushButton(self.page_simulator)
        self.sim_f7.setObjectName(u"sim_f7")
        self.sim_f7.setGeometry(QRect(530, 20, 51, 51))
        self.sim_f7.setFont(font6)
        self.sim_f7.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 10px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.sim_f8 = QPushButton(self.page_simulator)
        self.sim_f8.setObjectName(u"sim_f8")
        self.sim_f8.setGeometry(QRect(590, 20, 51, 51))
        self.sim_f8.setFont(font6)
        self.sim_f8.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 10px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.sim_f9 = QPushButton(self.page_simulator)
        self.sim_f9.setObjectName(u"sim_f9")
        self.sim_f9.setGeometry(QRect(650, 20, 51, 51))
        self.sim_f9.setFont(font6)
        self.sim_f9.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 10px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.sim_f10 = QPushButton(self.page_simulator)
        self.sim_f10.setObjectName(u"sim_f10")
        self.sim_f10.setGeometry(QRect(710, 20, 51, 51))
        self.sim_f10.setFont(font6)
        self.sim_f10.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 10px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.sim_clear = QPushButton(self.page_simulator)
        self.sim_clear.setObjectName(u"sim_clear")
        self.sim_clear.setGeometry(QRect(780, 20, 51, 51))
        self.sim_clear.setFont(font6)
        self.sim_clear.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 8px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.sim_enter = QPushButton(self.page_simulator)
        self.sim_enter.setObjectName(u"sim_enter")
        self.sim_enter.setGeometry(QRect(840, 20, 51, 51))
        self.sim_enter.setFont(font6)
        self.sim_enter.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 8px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.sim_A = QPushButton(self.page_simulator)
        self.sim_A.setObjectName(u"sim_A")
        self.sim_A.setGeometry(QRect(10, 100, 91, 81))
        self.sim_A.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.sim_B = QPushButton(self.page_simulator)
        self.sim_B.setObjectName(u"sim_B")
        self.sim_B.setGeometry(QRect(110, 100, 91, 81))
        self.sim_B.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.sim_C = QPushButton(self.page_simulator)
        self.sim_C.setObjectName(u"sim_C")
        self.sim_C.setGeometry(QRect(210, 100, 91, 81))
        self.sim_C.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.sim_D = QPushButton(self.page_simulator)
        self.sim_D.setObjectName(u"sim_D")
        self.sim_D.setGeometry(QRect(310, 100, 91, 81))
        self.sim_D.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.sim_play = QPushButton(self.page_simulator)
        self.sim_play.setObjectName(u"sim_play")
        self.sim_play.setGeometry(QRect(490, 100, 101, 81))
        self.sim_play.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.sim_fastjog = QPushButton(self.page_simulator)
        self.sim_fastjog.setObjectName(u"sim_fastjog")
        self.sim_fastjog.setGeometry(QRect(810, 100, 101, 81))
        self.sim_fastjog.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.sim_record = QPushButton(self.page_simulator)
        self.sim_record.setObjectName(u"sim_record")
        self.sim_record.setGeometry(QRect(570, 190, 101, 81))
        self.sim_record.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.sim_prvctl = QPushButton(self.page_simulator)
        self.sim_prvctl.setObjectName(u"sim_prvctl")
        self.sim_prvctl.setGeometry(QRect(730, 190, 101, 81))
        self.sim_prvctl.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.sim_out = QPushButton(self.page_simulator)
        self.sim_out.setObjectName(u"sim_out")
        self.sim_out.setGeometry(QRect(210, 360, 101, 81))
        self.sim_out.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.sim_insert = QPushButton(self.page_simulator)
        self.sim_insert.setObjectName(u"sim_insert")
        self.sim_insert.setGeometry(QRect(280, 260, 101, 81))
        self.sim_insert.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.sim_in = QPushButton(self.page_simulator)
        self.sim_in.setObjectName(u"sim_in")
        self.sim_in.setGeometry(QRect(410, 260, 101, 81))
        self.sim_in.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.sim_loop = QPushButton(self.page_simulator)
        self.sim_loop.setObjectName(u"sim_loop")
        self.sim_loop.setGeometry(QRect(150, 260, 101, 81))
        self.sim_loop.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.sim_palanqueta = QSlider(self.page_simulator)
        self.sim_palanqueta.setObjectName(u"sim_palanqueta")
        self.sim_palanqueta.setGeometry(QRect(50, 220, 71, 221))
        self.sim_palanqueta.setOrientation(Qt.Vertical)
        self.sim_rodeta = QDial(self.page_simulator)
        self.sim_rodeta.setObjectName(u"sim_rodeta")
        self.sim_rodeta.setGeometry(QRect(720, 300, 171, 171))
        self.sim_gototc = QPushButton(self.page_simulator)
        self.sim_gototc.setObjectName(u"sim_gototc")
        self.sim_gototc.setGeometry(QRect(650, 100, 101, 81))
        self.sim_gototc.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.stackedWidget.addWidget(self.page_simulator)
        self.page_configuration = QWidget()
        self.page_configuration.setObjectName(u"page_configuration")
        self.config_ipconfig = QPushButton(self.page_configuration)
        self.config_ipconfig.setObjectName(u"config_ipconfig")
        self.config_ipconfig.setGeometry(QRect(50, 30, 251, 71))
        self.config_ipconfig.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.config_fastjogconfig = QPushButton(self.page_configuration)
        self.config_fastjogconfig.setObjectName(u"config_fastjogconfig")
        self.config_fastjogconfig.setGeometry(QRect(330, 30, 251, 71))
        self.config_fastjogconfig.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.config_deleteclipdict = QPushButton(self.page_configuration)
        self.config_deleteclipdict.setObjectName(u"config_deleteclipdict")
        self.config_deleteclipdict.setGeometry(QRect(610, 30, 251, 71))
        self.config_deleteclipdict.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.config_resetmarks = QPushButton(self.page_configuration)
        self.config_resetmarks.setObjectName(u"config_resetmarks")
        self.config_resetmarks.setGeometry(QRect(50, 140, 251, 71))
        self.config_resetmarks.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.stackedWidget.addWidget(self.page_configuration)
        self.page_export = QWidget()
        self.page_export.setObjectName(u"page_export")
        self.export_playlist = QPushButton(self.page_export)
        self.export_playlist.setObjectName(u"export_playlist")
        self.export_playlist.setGeometry(QRect(270, 30, 175, 70))
        self.export_playlist.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.export_export_clip = QPushButton(self.page_export)
        self.export_export_clip.setObjectName(u"export_export_clip")
        self.export_export_clip.setGeometry(QRect(50, 30, 175, 70))
        self.export_export_clip.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.stackedWidget.addWidget(self.page_export)
        self.page_generic = QWidget()
        self.page_generic.setObjectName(u"page_generic")
        self.generic_none = QPushButton(self.page_generic)
        self.generic_none.setObjectName(u"generic_none")
        self.generic_none.setGeometry(QRect(50, 30, 175, 70))
        self.generic_none.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.generic_lockremote = QPushButton(self.page_generic)
        self.generic_lockremote.setObjectName(u"generic_lockremote")
        self.generic_lockremote.setGeometry(QRect(270, 30, 175, 70))
        self.generic_lockremote.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.stackedWidget.addWidget(self.page_generic)
        self.page_playlist = QWidget()
        self.page_playlist.setObjectName(u"page_playlist")
        self.playlist_btnadd_1 = QPushButton(self.page_playlist)
        self.playlist_btnadd_1.setObjectName(u"playlist_btnadd_1")
        self.playlist_btnadd_1.setGeometry(QRect(10, 0, 93, 51))
        self.playlist_btnadd_1.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_btnadd_1.setIcon(icon6)
        self.playlist_numclip_pl1 = QLabel(self.page_playlist)
        self.playlist_numclip_pl1.setObjectName(u"playlist_numclip_pl1")
        self.playlist_numclip_pl1.setGeometry(QRect(220, 30, 51, 16))
        self.playlist_numclip_pl1.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_dur_pl1 = QLabel(self.page_playlist)
        self.playlist_dur_pl1.setObjectName(u"playlist_dur_pl1")
        self.playlist_dur_pl1.setGeometry(QRect(120, 30, 81, 16))
        self.playlist_dur_pl1.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_codi_pl1 = QLabel(self.page_playlist)
        self.playlist_codi_pl1.setObjectName(u"playlist_codi_pl1")
        self.playlist_codi_pl1.setGeometry(QRect(120, 10, 21, 16))
        font9 = QFont()
        font9.setFamily(u"Arial")
        font9.setPointSize(10)
        font9.setBold(True)
        font9.setWeight(75)
        self.playlist_codi_pl1.setFont(font9)
        self.playlist_codi_pl1.setStyleSheet(u"")
        self.playlist_btnadd_2 = QPushButton(self.page_playlist)
        self.playlist_btnadd_2.setObjectName(u"playlist_btnadd_2")
        self.playlist_btnadd_2.setGeometry(QRect(10, 80, 93, 51))
        self.playlist_btnadd_2.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_btnadd_2.setIcon(icon6)
        self.playlist_dur_pl2 = QLabel(self.page_playlist)
        self.playlist_dur_pl2.setObjectName(u"playlist_dur_pl2")
        self.playlist_dur_pl2.setGeometry(QRect(120, 110, 81, 16))
        self.playlist_dur_pl2.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_numclip_pl2 = QLabel(self.page_playlist)
        self.playlist_numclip_pl2.setObjectName(u"playlist_numclip_pl2")
        self.playlist_numclip_pl2.setGeometry(QRect(220, 110, 51, 16))
        self.playlist_numclip_pl2.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_codi_pl2 = QLabel(self.page_playlist)
        self.playlist_codi_pl2.setObjectName(u"playlist_codi_pl2")
        self.playlist_codi_pl2.setGeometry(QRect(120, 90, 21, 16))
        self.playlist_codi_pl2.setFont(font9)
        self.playlist_codi_pl2.setStyleSheet(u"")
        self.playlist_btnadd_3 = QPushButton(self.page_playlist)
        self.playlist_btnadd_3.setObjectName(u"playlist_btnadd_3")
        self.playlist_btnadd_3.setGeometry(QRect(10, 160, 93, 51))
        self.playlist_btnadd_3.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_btnadd_3.setIcon(icon6)
        self.playlist_dur_pl3 = QLabel(self.page_playlist)
        self.playlist_dur_pl3.setObjectName(u"playlist_dur_pl3")
        self.playlist_dur_pl3.setGeometry(QRect(120, 190, 81, 16))
        self.playlist_dur_pl3.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_numclip_pl3 = QLabel(self.page_playlist)
        self.playlist_numclip_pl3.setObjectName(u"playlist_numclip_pl3")
        self.playlist_numclip_pl3.setGeometry(QRect(220, 190, 51, 16))
        self.playlist_numclip_pl3.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_codi_pl3 = QLabel(self.page_playlist)
        self.playlist_codi_pl3.setObjectName(u"playlist_codi_pl3")
        self.playlist_codi_pl3.setGeometry(QRect(120, 170, 21, 16))
        self.playlist_codi_pl3.setFont(font9)
        self.playlist_codi_pl3.setStyleSheet(u"")
        self.playlist_btnadd_4 = QPushButton(self.page_playlist)
        self.playlist_btnadd_4.setObjectName(u"playlist_btnadd_4")
        self.playlist_btnadd_4.setGeometry(QRect(10, 240, 93, 51))
        self.playlist_btnadd_4.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_btnadd_4.setIcon(icon6)
        self.playlist_dur_pl4 = QLabel(self.page_playlist)
        self.playlist_dur_pl4.setObjectName(u"playlist_dur_pl4")
        self.playlist_dur_pl4.setGeometry(QRect(120, 270, 81, 16))
        self.playlist_dur_pl4.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_numclip_pl4 = QLabel(self.page_playlist)
        self.playlist_numclip_pl4.setObjectName(u"playlist_numclip_pl4")
        self.playlist_numclip_pl4.setGeometry(QRect(220, 270, 51, 16))
        self.playlist_numclip_pl4.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_codi_pl4 = QLabel(self.page_playlist)
        self.playlist_codi_pl4.setObjectName(u"playlist_codi_pl4")
        self.playlist_codi_pl4.setGeometry(QRect(120, 250, 21, 16))
        self.playlist_codi_pl4.setFont(font9)
        self.playlist_codi_pl4.setStyleSheet(u"")
        self.playlist_btnadd_5 = QPushButton(self.page_playlist)
        self.playlist_btnadd_5.setObjectName(u"playlist_btnadd_5")
        self.playlist_btnadd_5.setGeometry(QRect(10, 320, 93, 51))
        self.playlist_btnadd_5.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_btnadd_5.setIcon(icon6)
        self.playlist_dur_pl5 = QLabel(self.page_playlist)
        self.playlist_dur_pl5.setObjectName(u"playlist_dur_pl5")
        self.playlist_dur_pl5.setGeometry(QRect(120, 350, 81, 16))
        self.playlist_dur_pl5.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_numclip_pl5 = QLabel(self.page_playlist)
        self.playlist_numclip_pl5.setObjectName(u"playlist_numclip_pl5")
        self.playlist_numclip_pl5.setGeometry(QRect(220, 350, 51, 16))
        self.playlist_numclip_pl5.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_codi_pl5 = QLabel(self.page_playlist)
        self.playlist_codi_pl5.setObjectName(u"playlist_codi_pl5")
        self.playlist_codi_pl5.setGeometry(QRect(120, 330, 21, 16))
        self.playlist_codi_pl5.setFont(font9)
        self.playlist_codi_pl5.setStyleSheet(u"")
        self.playlist_btnadd_6 = QPushButton(self.page_playlist)
        self.playlist_btnadd_6.setObjectName(u"playlist_btnadd_6")
        self.playlist_btnadd_6.setGeometry(QRect(10, 400, 93, 51))
        self.playlist_btnadd_6.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_btnadd_6.setIcon(icon6)
        self.playlist_dur_pl6 = QLabel(self.page_playlist)
        self.playlist_dur_pl6.setObjectName(u"playlist_dur_pl6")
        self.playlist_dur_pl6.setGeometry(QRect(120, 430, 81, 16))
        self.playlist_dur_pl6.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_numclip_pl6 = QLabel(self.page_playlist)
        self.playlist_numclip_pl6.setObjectName(u"playlist_numclip_pl6")
        self.playlist_numclip_pl6.setGeometry(QRect(220, 430, 51, 16))
        self.playlist_numclip_pl6.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_codi_pl6 = QLabel(self.page_playlist)
        self.playlist_codi_pl6.setObjectName(u"playlist_codi_pl6")
        self.playlist_codi_pl6.setGeometry(QRect(120, 410, 21, 16))
        self.playlist_codi_pl6.setFont(font9)
        self.playlist_codi_pl6.setStyleSheet(u"")
        self.playlist_button_pl1 = QPushButton(self.page_playlist)
        self.playlist_button_pl1.setObjectName(u"playlist_button_pl1")
        self.playlist_button_pl1.setGeometry(QRect(110, 0, 171, 51))
        self.playlist_button_pl1.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_button_pl2 = QPushButton(self.page_playlist)
        self.playlist_button_pl2.setObjectName(u"playlist_button_pl2")
        self.playlist_button_pl2.setGeometry(QRect(110, 80, 171, 51))
        self.playlist_button_pl2.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_button_pl3 = QPushButton(self.page_playlist)
        self.playlist_button_pl3.setObjectName(u"playlist_button_pl3")
        self.playlist_button_pl3.setGeometry(QRect(110, 160, 171, 51))
        self.playlist_button_pl3.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_button_pl4 = QPushButton(self.page_playlist)
        self.playlist_button_pl4.setObjectName(u"playlist_button_pl4")
        self.playlist_button_pl4.setGeometry(QRect(110, 240, 171, 51))
        self.playlist_button_pl4.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_button_pl5 = QPushButton(self.page_playlist)
        self.playlist_button_pl5.setObjectName(u"playlist_button_pl5")
        self.playlist_button_pl5.setGeometry(QRect(110, 320, 171, 51))
        self.playlist_button_pl5.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_button_pl6 = QPushButton(self.page_playlist)
        self.playlist_button_pl6.setObjectName(u"playlist_button_pl6")
        self.playlist_button_pl6.setGeometry(QRect(110, 400, 171, 51))
        self.playlist_button_pl6.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_dur_pl8 = QLabel(self.page_playlist)
        self.playlist_dur_pl8.setObjectName(u"playlist_dur_pl8")
        self.playlist_dur_pl8.setGeometry(QRect(430, 110, 81, 16))
        self.playlist_dur_pl8.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_numclip_pl12 = QLabel(self.page_playlist)
        self.playlist_numclip_pl12.setObjectName(u"playlist_numclip_pl12")
        self.playlist_numclip_pl12.setGeometry(QRect(530, 430, 51, 16))
        self.playlist_numclip_pl12.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_codi_pl10 = QLabel(self.page_playlist)
        self.playlist_codi_pl10.setObjectName(u"playlist_codi_pl10")
        self.playlist_codi_pl10.setGeometry(QRect(430, 250, 21, 16))
        self.playlist_codi_pl10.setFont(font9)
        self.playlist_codi_pl10.setStyleSheet(u"")
        self.playlist_dur_pl9 = QLabel(self.page_playlist)
        self.playlist_dur_pl9.setObjectName(u"playlist_dur_pl9")
        self.playlist_dur_pl9.setGeometry(QRect(430, 190, 81, 16))
        self.playlist_dur_pl9.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_numclip_pl10 = QLabel(self.page_playlist)
        self.playlist_numclip_pl10.setObjectName(u"playlist_numclip_pl10")
        self.playlist_numclip_pl10.setGeometry(QRect(530, 270, 51, 16))
        self.playlist_numclip_pl10.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_dur_pl10 = QLabel(self.page_playlist)
        self.playlist_dur_pl10.setObjectName(u"playlist_dur_pl10")
        self.playlist_dur_pl10.setGeometry(QRect(430, 270, 81, 16))
        self.playlist_dur_pl10.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_codi_pl9 = QLabel(self.page_playlist)
        self.playlist_codi_pl9.setObjectName(u"playlist_codi_pl9")
        self.playlist_codi_pl9.setGeometry(QRect(430, 170, 21, 16))
        self.playlist_codi_pl9.setFont(font9)
        self.playlist_codi_pl9.setStyleSheet(u"")
        self.playlist_codi_pl8 = QLabel(self.page_playlist)
        self.playlist_codi_pl8.setObjectName(u"playlist_codi_pl8")
        self.playlist_codi_pl8.setGeometry(QRect(430, 90, 21, 16))
        self.playlist_codi_pl8.setFont(font9)
        self.playlist_codi_pl8.setStyleSheet(u"")
        self.playlist_codi_pl11 = QLabel(self.page_playlist)
        self.playlist_codi_pl11.setObjectName(u"playlist_codi_pl11")
        self.playlist_codi_pl11.setGeometry(QRect(430, 330, 21, 16))
        self.playlist_codi_pl11.setFont(font9)
        self.playlist_codi_pl11.setStyleSheet(u"")
        self.playlist_dur_pl11 = QLabel(self.page_playlist)
        self.playlist_dur_pl11.setObjectName(u"playlist_dur_pl11")
        self.playlist_dur_pl11.setGeometry(QRect(430, 350, 81, 16))
        self.playlist_dur_pl11.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_codi_pl7 = QLabel(self.page_playlist)
        self.playlist_codi_pl7.setObjectName(u"playlist_codi_pl7")
        self.playlist_codi_pl7.setGeometry(QRect(430, 10, 21, 16))
        self.playlist_codi_pl7.setFont(font9)
        self.playlist_codi_pl7.setStyleSheet(u"")
        self.playlist_btnadd_10 = QPushButton(self.page_playlist)
        self.playlist_btnadd_10.setObjectName(u"playlist_btnadd_10")
        self.playlist_btnadd_10.setGeometry(QRect(320, 240, 93, 51))
        self.playlist_btnadd_10.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_btnadd_10.setIcon(icon6)
        self.playlist_button_pl10 = QPushButton(self.page_playlist)
        self.playlist_button_pl10.setObjectName(u"playlist_button_pl10")
        self.playlist_button_pl10.setGeometry(QRect(420, 240, 171, 51))
        self.playlist_button_pl10.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_button_pl12 = QPushButton(self.page_playlist)
        self.playlist_button_pl12.setObjectName(u"playlist_button_pl12")
        self.playlist_button_pl12.setGeometry(QRect(420, 400, 171, 51))
        self.playlist_button_pl12.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_button_pl9 = QPushButton(self.page_playlist)
        self.playlist_button_pl9.setObjectName(u"playlist_button_pl9")
        self.playlist_button_pl9.setGeometry(QRect(420, 160, 171, 51))
        self.playlist_button_pl9.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_numclip_pl11 = QLabel(self.page_playlist)
        self.playlist_numclip_pl11.setObjectName(u"playlist_numclip_pl11")
        self.playlist_numclip_pl11.setGeometry(QRect(530, 350, 51, 16))
        self.playlist_numclip_pl11.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_btnadd_7 = QPushButton(self.page_playlist)
        self.playlist_btnadd_7.setObjectName(u"playlist_btnadd_7")
        self.playlist_btnadd_7.setGeometry(QRect(320, 0, 93, 51))
        self.playlist_btnadd_7.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_btnadd_7.setIcon(icon6)
        self.playlist_btnadd_8 = QPushButton(self.page_playlist)
        self.playlist_btnadd_8.setObjectName(u"playlist_btnadd_8")
        self.playlist_btnadd_8.setGeometry(QRect(320, 80, 93, 51))
        self.playlist_btnadd_8.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_btnadd_8.setIcon(icon6)
        self.playlist_numclip_pl8 = QLabel(self.page_playlist)
        self.playlist_numclip_pl8.setObjectName(u"playlist_numclip_pl8")
        self.playlist_numclip_pl8.setGeometry(QRect(530, 110, 51, 16))
        self.playlist_numclip_pl8.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_button_pl8 = QPushButton(self.page_playlist)
        self.playlist_button_pl8.setObjectName(u"playlist_button_pl8")
        self.playlist_button_pl8.setGeometry(QRect(420, 80, 171, 51))
        self.playlist_button_pl8.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_numclip_pl9 = QLabel(self.page_playlist)
        self.playlist_numclip_pl9.setObjectName(u"playlist_numclip_pl9")
        self.playlist_numclip_pl9.setGeometry(QRect(530, 190, 51, 16))
        self.playlist_numclip_pl9.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_dur_pl12 = QLabel(self.page_playlist)
        self.playlist_dur_pl12.setObjectName(u"playlist_dur_pl12")
        self.playlist_dur_pl12.setGeometry(QRect(430, 430, 81, 16))
        self.playlist_dur_pl12.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_codi_pl12 = QLabel(self.page_playlist)
        self.playlist_codi_pl12.setObjectName(u"playlist_codi_pl12")
        self.playlist_codi_pl12.setGeometry(QRect(430, 410, 21, 16))
        self.playlist_codi_pl12.setFont(font9)
        self.playlist_codi_pl12.setStyleSheet(u"")
        self.playlist_numclip_pl7 = QLabel(self.page_playlist)
        self.playlist_numclip_pl7.setObjectName(u"playlist_numclip_pl7")
        self.playlist_numclip_pl7.setGeometry(QRect(530, 30, 51, 16))
        self.playlist_numclip_pl7.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_button_pl11 = QPushButton(self.page_playlist)
        self.playlist_button_pl11.setObjectName(u"playlist_button_pl11")
        self.playlist_button_pl11.setGeometry(QRect(420, 320, 171, 51))
        self.playlist_button_pl11.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_btnadd_11 = QPushButton(self.page_playlist)
        self.playlist_btnadd_11.setObjectName(u"playlist_btnadd_11")
        self.playlist_btnadd_11.setGeometry(QRect(320, 320, 93, 51))
        self.playlist_btnadd_11.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_btnadd_11.setIcon(icon6)
        self.playlist_dur_pl7 = QLabel(self.page_playlist)
        self.playlist_dur_pl7.setObjectName(u"playlist_dur_pl7")
        self.playlist_dur_pl7.setGeometry(QRect(430, 30, 81, 16))
        self.playlist_dur_pl7.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_button_pl7 = QPushButton(self.page_playlist)
        self.playlist_button_pl7.setObjectName(u"playlist_button_pl7")
        self.playlist_button_pl7.setGeometry(QRect(420, 0, 171, 51))
        self.playlist_button_pl7.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_btnadd_9 = QPushButton(self.page_playlist)
        self.playlist_btnadd_9.setObjectName(u"playlist_btnadd_9")
        self.playlist_btnadd_9.setGeometry(QRect(320, 160, 93, 51))
        self.playlist_btnadd_9.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_btnadd_9.setIcon(icon6)
        self.playlist_btnadd_12 = QPushButton(self.page_playlist)
        self.playlist_btnadd_12.setObjectName(u"playlist_btnadd_12")
        self.playlist_btnadd_12.setGeometry(QRect(320, 400, 93, 51))
        self.playlist_btnadd_12.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_btnadd_12.setIcon(icon6)
        self.playlist_dur_pl14 = QLabel(self.page_playlist)
        self.playlist_dur_pl14.setObjectName(u"playlist_dur_pl14")
        self.playlist_dur_pl14.setGeometry(QRect(750, 110, 81, 16))
        self.playlist_dur_pl14.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_numclip_pl18 = QLabel(self.page_playlist)
        self.playlist_numclip_pl18.setObjectName(u"playlist_numclip_pl18")
        self.playlist_numclip_pl18.setGeometry(QRect(850, 430, 51, 16))
        self.playlist_numclip_pl18.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_codi_pl16 = QLabel(self.page_playlist)
        self.playlist_codi_pl16.setObjectName(u"playlist_codi_pl16")
        self.playlist_codi_pl16.setGeometry(QRect(750, 250, 21, 16))
        self.playlist_codi_pl16.setFont(font9)
        self.playlist_codi_pl16.setStyleSheet(u"")
        self.playlist_dur_pl15 = QLabel(self.page_playlist)
        self.playlist_dur_pl15.setObjectName(u"playlist_dur_pl15")
        self.playlist_dur_pl15.setGeometry(QRect(750, 190, 81, 16))
        self.playlist_dur_pl15.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_numclip_pl16 = QLabel(self.page_playlist)
        self.playlist_numclip_pl16.setObjectName(u"playlist_numclip_pl16")
        self.playlist_numclip_pl16.setGeometry(QRect(850, 270, 51, 16))
        self.playlist_numclip_pl16.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_dur_pl16 = QLabel(self.page_playlist)
        self.playlist_dur_pl16.setObjectName(u"playlist_dur_pl16")
        self.playlist_dur_pl16.setGeometry(QRect(750, 270, 81, 16))
        self.playlist_dur_pl16.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_codi_pl15 = QLabel(self.page_playlist)
        self.playlist_codi_pl15.setObjectName(u"playlist_codi_pl15")
        self.playlist_codi_pl15.setGeometry(QRect(750, 170, 21, 16))
        self.playlist_codi_pl15.setFont(font9)
        self.playlist_codi_pl15.setStyleSheet(u"")
        self.playlist_codi_pl14 = QLabel(self.page_playlist)
        self.playlist_codi_pl14.setObjectName(u"playlist_codi_pl14")
        self.playlist_codi_pl14.setGeometry(QRect(750, 90, 21, 16))
        self.playlist_codi_pl14.setFont(font9)
        self.playlist_codi_pl14.setStyleSheet(u"")
        self.playlist_codi_pl17 = QLabel(self.page_playlist)
        self.playlist_codi_pl17.setObjectName(u"playlist_codi_pl17")
        self.playlist_codi_pl17.setGeometry(QRect(750, 330, 21, 16))
        self.playlist_codi_pl17.setFont(font9)
        self.playlist_codi_pl17.setStyleSheet(u"")
        self.playlist_dur_pl17 = QLabel(self.page_playlist)
        self.playlist_dur_pl17.setObjectName(u"playlist_dur_pl17")
        self.playlist_dur_pl17.setGeometry(QRect(750, 350, 81, 16))
        self.playlist_dur_pl17.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_codi_pl13 = QLabel(self.page_playlist)
        self.playlist_codi_pl13.setObjectName(u"playlist_codi_pl13")
        self.playlist_codi_pl13.setGeometry(QRect(750, 10, 21, 16))
        self.playlist_codi_pl13.setFont(font9)
        self.playlist_codi_pl13.setStyleSheet(u"")
        self.playlist_btnadd_16 = QPushButton(self.page_playlist)
        self.playlist_btnadd_16.setObjectName(u"playlist_btnadd_16")
        self.playlist_btnadd_16.setGeometry(QRect(640, 240, 93, 51))
        self.playlist_btnadd_16.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_btnadd_16.setIcon(icon6)
        self.playlist_button_pl16 = QPushButton(self.page_playlist)
        self.playlist_button_pl16.setObjectName(u"playlist_button_pl16")
        self.playlist_button_pl16.setGeometry(QRect(740, 240, 171, 51))
        self.playlist_button_pl16.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_button_pl18 = QPushButton(self.page_playlist)
        self.playlist_button_pl18.setObjectName(u"playlist_button_pl18")
        self.playlist_button_pl18.setGeometry(QRect(740, 400, 171, 51))
        self.playlist_button_pl18.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_button_pl15 = QPushButton(self.page_playlist)
        self.playlist_button_pl15.setObjectName(u"playlist_button_pl15")
        self.playlist_button_pl15.setGeometry(QRect(740, 160, 171, 51))
        self.playlist_button_pl15.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_numclip_pl17 = QLabel(self.page_playlist)
        self.playlist_numclip_pl17.setObjectName(u"playlist_numclip_pl17")
        self.playlist_numclip_pl17.setGeometry(QRect(850, 350, 51, 16))
        self.playlist_numclip_pl17.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_btnadd_13 = QPushButton(self.page_playlist)
        self.playlist_btnadd_13.setObjectName(u"playlist_btnadd_13")
        self.playlist_btnadd_13.setGeometry(QRect(640, 0, 93, 51))
        self.playlist_btnadd_13.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_btnadd_13.setIcon(icon6)
        self.playlist_btnadd_14 = QPushButton(self.page_playlist)
        self.playlist_btnadd_14.setObjectName(u"playlist_btnadd_14")
        self.playlist_btnadd_14.setGeometry(QRect(640, 80, 93, 51))
        self.playlist_btnadd_14.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_btnadd_14.setIcon(icon6)
        self.playlist_numclip_pl14 = QLabel(self.page_playlist)
        self.playlist_numclip_pl14.setObjectName(u"playlist_numclip_pl14")
        self.playlist_numclip_pl14.setGeometry(QRect(850, 110, 51, 16))
        self.playlist_numclip_pl14.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_button_pl14 = QPushButton(self.page_playlist)
        self.playlist_button_pl14.setObjectName(u"playlist_button_pl14")
        self.playlist_button_pl14.setGeometry(QRect(740, 80, 171, 51))
        self.playlist_button_pl14.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_numclip_pl15 = QLabel(self.page_playlist)
        self.playlist_numclip_pl15.setObjectName(u"playlist_numclip_pl15")
        self.playlist_numclip_pl15.setGeometry(QRect(850, 190, 51, 16))
        self.playlist_numclip_pl15.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_dur_pl18 = QLabel(self.page_playlist)
        self.playlist_dur_pl18.setObjectName(u"playlist_dur_pl18")
        self.playlist_dur_pl18.setGeometry(QRect(750, 430, 81, 16))
        self.playlist_dur_pl18.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_codi_pl18 = QLabel(self.page_playlist)
        self.playlist_codi_pl18.setObjectName(u"playlist_codi_pl18")
        self.playlist_codi_pl18.setGeometry(QRect(750, 410, 21, 16))
        self.playlist_codi_pl18.setFont(font9)
        self.playlist_codi_pl18.setStyleSheet(u"")
        self.playlist_numclip_pl13 = QLabel(self.page_playlist)
        self.playlist_numclip_pl13.setObjectName(u"playlist_numclip_pl13")
        self.playlist_numclip_pl13.setGeometry(QRect(850, 30, 51, 16))
        self.playlist_numclip_pl13.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_button_pl17 = QPushButton(self.page_playlist)
        self.playlist_button_pl17.setObjectName(u"playlist_button_pl17")
        self.playlist_button_pl17.setGeometry(QRect(740, 320, 171, 51))
        self.playlist_button_pl17.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_btnadd_17 = QPushButton(self.page_playlist)
        self.playlist_btnadd_17.setObjectName(u"playlist_btnadd_17")
        self.playlist_btnadd_17.setGeometry(QRect(640, 320, 93, 51))
        self.playlist_btnadd_17.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_btnadd_17.setIcon(icon6)
        self.playlist_dur_pl13 = QLabel(self.page_playlist)
        self.playlist_dur_pl13.setObjectName(u"playlist_dur_pl13")
        self.playlist_dur_pl13.setGeometry(QRect(750, 30, 81, 16))
        self.playlist_dur_pl13.setStyleSheet(u"backgound-color: rgba(255,255,255,0);\n"
"border: rgba(255,255,255,0);")
        self.playlist_button_pl13 = QPushButton(self.page_playlist)
        self.playlist_button_pl13.setObjectName(u"playlist_button_pl13")
        self.playlist_button_pl13.setGeometry(QRect(740, 0, 171, 51))
        self.playlist_button_pl13.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_btnadd_15 = QPushButton(self.page_playlist)
        self.playlist_btnadd_15.setObjectName(u"playlist_btnadd_15")
        self.playlist_btnadd_15.setGeometry(QRect(640, 160, 93, 51))
        self.playlist_btnadd_15.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_btnadd_15.setIcon(icon6)
        self.playlist_btnadd_18 = QPushButton(self.page_playlist)
        self.playlist_btnadd_18.setObjectName(u"playlist_btnadd_18")
        self.playlist_btnadd_18.setGeometry(QRect(640, 400, 93, 51))
        self.playlist_btnadd_18.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}")
        self.playlist_btnadd_18.setIcon(icon6)
        self.stackedWidget.addWidget(self.page_playlist)
        self.playlist_btnadd_1.raise_()
        self.playlist_numclip_pl1.raise_()
        self.playlist_dur_pl1.raise_()
        self.playlist_codi_pl1.raise_()
        self.playlist_btnadd_2.raise_()
        self.playlist_dur_pl2.raise_()
        self.playlist_numclip_pl2.raise_()
        self.playlist_codi_pl2.raise_()
        self.playlist_btnadd_3.raise_()
        self.playlist_dur_pl3.raise_()
        self.playlist_numclip_pl3.raise_()
        self.playlist_codi_pl3.raise_()
        self.playlist_btnadd_4.raise_()
        self.playlist_dur_pl4.raise_()
        self.playlist_numclip_pl4.raise_()
        self.playlist_codi_pl4.raise_()
        self.playlist_btnadd_5.raise_()
        self.playlist_dur_pl5.raise_()
        self.playlist_numclip_pl5.raise_()
        self.playlist_codi_pl5.raise_()
        self.playlist_btnadd_6.raise_()
        self.playlist_dur_pl6.raise_()
        self.playlist_numclip_pl6.raise_()
        self.playlist_codi_pl6.raise_()
        self.playlist_dur_pl8.raise_()
        self.playlist_numclip_pl12.raise_()
        self.playlist_codi_pl10.raise_()
        self.playlist_dur_pl9.raise_()
        self.playlist_numclip_pl10.raise_()
        self.playlist_dur_pl10.raise_()
        self.playlist_codi_pl9.raise_()
        self.playlist_codi_pl8.raise_()
        self.playlist_codi_pl11.raise_()
        self.playlist_dur_pl11.raise_()
        self.playlist_codi_pl7.raise_()
        self.playlist_btnadd_10.raise_()
        self.playlist_numclip_pl11.raise_()
        self.playlist_btnadd_7.raise_()
        self.playlist_btnadd_8.raise_()
        self.playlist_numclip_pl8.raise_()
        self.playlist_numclip_pl9.raise_()
        self.playlist_dur_pl12.raise_()
        self.playlist_codi_pl12.raise_()
        self.playlist_numclip_pl7.raise_()
        self.playlist_btnadd_11.raise_()
        self.playlist_dur_pl7.raise_()
        self.playlist_btnadd_9.raise_()
        self.playlist_btnadd_12.raise_()
        self.playlist_dur_pl14.raise_()
        self.playlist_numclip_pl18.raise_()
        self.playlist_codi_pl16.raise_()
        self.playlist_dur_pl15.raise_()
        self.playlist_numclip_pl16.raise_()
        self.playlist_dur_pl16.raise_()
        self.playlist_codi_pl15.raise_()
        self.playlist_codi_pl14.raise_()
        self.playlist_codi_pl17.raise_()
        self.playlist_dur_pl17.raise_()
        self.playlist_codi_pl13.raise_()
        self.playlist_btnadd_16.raise_()
        self.playlist_numclip_pl17.raise_()
        self.playlist_btnadd_13.raise_()
        self.playlist_btnadd_14.raise_()
        self.playlist_numclip_pl14.raise_()
        self.playlist_numclip_pl15.raise_()
        self.playlist_dur_pl18.raise_()
        self.playlist_codi_pl18.raise_()
        self.playlist_numclip_pl13.raise_()
        self.playlist_btnadd_17.raise_()
        self.playlist_dur_pl13.raise_()
        self.playlist_btnadd_15.raise_()
        self.playlist_btnadd_18.raise_()
        self.playlist_button_pl1.raise_()
        self.playlist_button_pl2.raise_()
        self.playlist_button_pl3.raise_()
        self.playlist_button_pl4.raise_()
        self.playlist_button_pl5.raise_()
        self.playlist_button_pl6.raise_()
        self.playlist_button_pl7.raise_()
        self.playlist_button_pl8.raise_()
        self.playlist_button_pl9.raise_()
        self.playlist_button_pl10.raise_()
        self.playlist_button_pl11.raise_()
        self.playlist_button_pl12.raise_()
        self.playlist_button_pl13.raise_()
        self.playlist_button_pl14.raise_()
        self.playlist_button_pl15.raise_()
        self.playlist_button_pl16.raise_()
        self.playlist_button_pl17.raise_()
        self.playlist_button_pl18.raise_()
        self.page_clipmanagement = QWidget()
        self.page_clipmanagement.setObjectName(u"page_clipmanagement")
        self.clip_manag_name_clip = QPushButton(self.page_clipmanagement)
        self.clip_manag_name_clip.setObjectName(u"clip_manag_name_clip")
        self.clip_manag_name_clip.setGeometry(QRect(50, 30, 175, 70))
        self.clip_manag_name_clip.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.stackedWidget.addWidget(self.page_clipmanagement)
        self.page_control = QWidget()
        self.page_control.setObjectName(u"page_control")
        self.control_loop = QPushButton(self.page_control)
        self.control_loop.setObjectName(u"control_loop")
        self.control_loop.setGeometry(QRect(710, 140, 175, 70))
        self.control_loop.setLayoutDirection(Qt.RightToLeft)
        self.control_loop.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.control_prv_ctl = QPushButton(self.page_control)
        self.control_prv_ctl.setObjectName(u"control_prv_ctl")
        self.control_prv_ctl.setGeometry(QRect(710, 30, 175, 70))
        self.control_prv_ctl.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.control_syncprv = QPushButton(self.page_control)
        self.control_syncprv.setObjectName(u"control_syncprv")
        self.control_syncprv.setGeometry(QRect(490, 30, 175, 70))
        self.control_syncprv.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.control_fast_jog = QPushButton(self.page_control)
        self.control_fast_jog.setObjectName(u"control_fast_jog")
        self.control_fast_jog.setGeometry(QRect(270, 30, 175, 70))
        self.control_fast_jog.setLayoutDirection(Qt.RightToLeft)
        self.control_fast_jog.setAutoFillBackground(False)
        self.control_fast_jog.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"    qproperty-iconAlignment: right;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.control_gotoout = QPushButton(self.page_control)
        self.control_gotoout.setObjectName(u"control_gotoout")
        self.control_gotoout.setGeometry(QRect(270, 140, 175, 70))
        self.control_gotoout.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.control_gotoin = QPushButton(self.page_control)
        self.control_gotoin.setObjectName(u"control_gotoin")
        self.control_gotoin.setGeometry(QRect(50, 140, 175, 70))
        self.control_gotoin.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.control_gototc = QPushButton(self.page_control)
        self.control_gototc.setObjectName(u"control_gototc")
        self.control_gototc.setGeometry(QRect(490, 140, 175, 70))
        self.control_gototc.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.control_2ndfastjog = QPushButton(self.page_control)
        self.control_2ndfastjog.setObjectName(u"control_2ndfastjog")
        self.control_2ndfastjog.setGeometry(QRect(50, 30, 175, 70))
        self.control_2ndfastjog.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.stackedWidget.addWidget(self.page_control)
        self.page_contentacc = QWidget()
        self.page_contentacc.setObjectName(u"page_contentacc")
        self.cont_acc_lastmark = QPushButton(self.page_contentacc)
        self.cont_acc_lastmark.setObjectName(u"cont_acc_lastmark")
        self.cont_acc_lastmark.setGeometry(QRect(50, 140, 175, 70))
        self.cont_acc_lastmark.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.cont_acc_mark = QPushButton(self.page_contentacc)
        self.cont_acc_mark.setObjectName(u"cont_acc_mark")
        self.cont_acc_mark.setGeometry(QRect(270, 140, 175, 70))
        self.cont_acc_mark.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.cont_acc_lasttc = QPushButton(self.page_contentacc)
        self.cont_acc_lasttc.setObjectName(u"cont_acc_lasttc")
        self.cont_acc_lasttc.setGeometry(QRect(710, 30, 175, 70))
        self.cont_acc_lasttc.setLayoutDirection(Qt.RightToLeft)
        self.cont_acc_lasttc.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.cont_acc_page = QPushButton(self.page_contentacc)
        self.cont_acc_page.setObjectName(u"cont_acc_page")
        self.cont_acc_page.setGeometry(QRect(490, 30, 175, 70))
        self.cont_acc_page.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.contec_acc_actualclip = QLabel(self.page_contentacc)
        self.contec_acc_actualclip.setObjectName(u"contec_acc_actualclip")
        self.contec_acc_actualclip.setGeometry(QRect(50, 30, 175, 70))
        self.contec_acc_actualclip.setStyleSheet(u"QLabel {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QLabel:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"")
        self.contec_acc_actualclip.setAlignment(Qt.AlignCenter)
        self.cont_acc_actualplaylist = QPushButton(self.page_contentacc)
        self.cont_acc_actualplaylist.setObjectName(u"cont_acc_actualplaylist")
        self.cont_acc_actualplaylist.setGeometry(QRect(270, 30, 175, 70))
        self.cont_acc_actualplaylist.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";    /* Cambia la fuente */\n"
"    font-size: 16px;         /* Tama\u00f1o del texto */\n"
"    font-weight: bold;       /* Negrita */    \n"
"    color: white;				 /* Color del texto */\n"
"	padding: 10px;           \n"
"    border-radius: 15px;\n"
"	border: 2px solid rgba(255,255,255,255);  /* Borde blanco con transparencia */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0,150,250,50);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.stackedWidget.addWidget(self.page_contentacc)
        self.page_widgets = QWidget()
        self.page_widgets.setObjectName(u"page_widgets")
        self.verticalLayout_6 = QVBoxLayout(self.page_widgets)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.page_widgets)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.frame)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font1)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_7.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        font10 = QFont()
        font10.setFamily(u"Segoe UI")
        font10.setPointSize(9)
        self.pushButton.setFont(font10)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/16x16/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon7)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)

        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_7.addWidget(self.frame_content_wid_1)


        self.verticalLayout_15.addWidget(self.frame_div_content_1)


        self.verticalLayout_6.addWidget(self.frame)

        self.frame_2 = QFrame(self.page_widgets)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 150))
        self.frame_2.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.frame_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.frame_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.frame_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.frame_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 222, 222))
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"}\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font10)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.frame_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy5)
        self.horizontalScrollBar.setStyleSheet(u"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.frame_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setStyleSheet(u"QCommandLinkButton {	\n"
"	color: rgb(85, 170, 255);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(52, 58, 71);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/16x16/icons/16x16/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon8)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.frame_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_11.addLayout(self.gridLayout_2)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.page_widgets)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 150))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.frame_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font3);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush15 = QBrush(QColor(39, 44, 54, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush15)
        brush16 = QBrush(QColor(210, 210, 210, 128))
        brush16.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        brush17 = QBrush(QColor(210, 210, 210, 128))
        brush17.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        brush18 = QBrush(QColor(210, 210, 210, 128))
        brush18.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.tableWidget.setPalette(palette1)
        self.tableWidget.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_widgets)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font3)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font3)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)
        QWidget.setTabOrder(self.btn_toggle_menu, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.radioButton)
        QWidget.setTabOrder(self.radioButton, self.horizontalSlider)
        QWidget.setTabOrder(self.horizontalSlider, self.verticalSlider)
        QWidget.setTabOrder(self.verticalSlider, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.plainTextEdit)
        QWidget.setTabOrder(self.plainTextEdit, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.commandLinkButton)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(22)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_page.setText(QCoreApplication.translate("MainWindow", u"PAGE 0  ", None))
        self.label_bank.setText(QCoreApplication.translate("MainWindow", u" 1 BANK", None))
        self.label_pgm.setText(QCoreApplication.translate("MainWindow", u"PGM  A", None))
        self.label_vmixconn.setText(QCoreApplication.translate("MainWindow", u"vMix connection: ", None))
        self.label_title_bar_top.setText("")
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText("")
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| CLIP", None))
        self.label_user_icon.setText(QCoreApplication.translate("MainWindow", u"WM", None))
        self.clip_addtoplaylist.setText(QCoreApplication.translate("MainWindow", u"Add to Playlist   ", None))
        self.clip_star_widget_estrelles3_1.setText("")
        self.clip_star_widget_estrelles3_2.setText("")
        self.clip_star_widget_estrelles3_3.setText("")
        self.clip_button_onwidget_estrelles3.setText("")
        self.clip_gotoestrella3.setText("")
        self.clip_estrella1.setText("")
        self.clip_star_widget_estrelles2_1.setText("")
        self.clip_star_widget_estrelles2_2.setText("")
        self.clip_button_onwidget_estrelles2.setText("")
        self.clip_gotoestrella2.setText("")
        self.clip_gotoestrella1.setText("")
        self.clip_nameclip.setText(QCoreApplication.translate("MainWindow", u"Name Clip", None))
        self.label_estrella1.setText("")
        self.estrella1_delete.setText("")
        self.estrella1_add.setText("")
        self.pl11_add.setText("")
        self.pl11_delete.setText("")
        self.label_nclips_11.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.label_dur_11.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.label_pl11.setText(QCoreApplication.translate("MainWindow", u"PLAYLIST 11", None))
        self.pl13_add.setText("")
        self.pl13_delete.setText("")
        self.label_nclips_13.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.label_dur_13.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.label_pl13.setText(QCoreApplication.translate("MainWindow", u"PLAYLIST 13", None))
        self.pl18_add.setText("")
        self.pl18_delete.setText("")
        self.label_nclips_18.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.label_dur_18.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.label_pl18.setText(QCoreApplication.translate("MainWindow", u"PLAYLIST 18", None))
        self.pl17_add.setText("")
        self.pl17_delete.setText("")
        self.label_nclips_17.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.label_dur_17.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.label_pl17.setText(QCoreApplication.translate("MainWindow", u"PLAYLIST 17", None))
        self.pl16_add.setText("")
        self.pl16_delete.setText("")
        self.label_nclips_16.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.label_dur_16.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.label_pl16.setText(QCoreApplication.translate("MainWindow", u"PLAYLIST 16", None))
        self.pl15_add.setText("")
        self.pl15_delete.setText("")
        self.label_nclips_15.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.label_dur_15.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.label_pl15.setText(QCoreApplication.translate("MainWindow", u"PLAYLIST 15", None))
        self.pl14_add.setText("")
        self.pl14_delete.setText("")
        self.label_nclips_14.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.label_dur_14.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.label_pl14.setText(QCoreApplication.translate("MainWindow", u"PLAYLIST 14", None))
        self.pl12_add.setText("")
        self.pl12_delete.setText("")
        self.label_nclips_12.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.label_dur_12.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.label_pl12.setText(QCoreApplication.translate("MainWindow", u"PLAYLIST 12", None))
        self.pl9_add.setText("")
        self.pl9_delete.setText("")
        self.label_nclips_9.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.label_dur_9.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.label_pl9.setText(QCoreApplication.translate("MainWindow", u"PLAYLIST 9", None))
        self.pl10_add.setText("")
        self.pl10_delete.setText("")
        self.label_nclips_10.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.label_dur_10.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.label_pl10.setText(QCoreApplication.translate("MainWindow", u"PLAYLIST 10", None))
        self.pl8_add.setText("")
        self.pl8_delete.setText("")
        self.label_nclips_8.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.label_dur_8.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.label_pl8.setText(QCoreApplication.translate("MainWindow", u"PLAYLIST 8", None))
        self.pl3_add.setText("")
        self.pl3_delete.setText("")
        self.label_nclips_3.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.label_dur_3.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.label_pl3.setText(QCoreApplication.translate("MainWindow", u"PLAYLIST 3", None))
        self.pl4_add.setText("")
        self.pl4_delete.setText("")
        self.label_nclips_4.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.label_dur_4.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.label_pl4.setText(QCoreApplication.translate("MainWindow", u"PLAYLIST 4", None))
        self.pl7_add.setText("")
        self.pl7_delete.setText("")
        self.label_nclips_7.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.label_dur_7.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.label_pl7.setText(QCoreApplication.translate("MainWindow", u"PLAYLIST 7", None))
        self.pl6_add.setText("")
        self.pl6_delete.setText("")
        self.label_nclips_6.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.label_dur_6.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.label_pl6.setText(QCoreApplication.translate("MainWindow", u"PLAYLIST 6", None))
        self.pl5_add.setText("")
        self.pl5_delete.setText("")
        self.label_nclips_5.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.label_dur_5.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.label_pl5.setText(QCoreApplication.translate("MainWindow", u"PLAYLIST 5", None))
        self.pl2_add.setText("")
        self.pl2_delete.setText("")
        self.label_nclips_2.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.label_dur_2.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.label_pl2.setText(QCoreApplication.translate("MainWindow", u"PLAYLIST 2", None))
        self.pl1_delete.setText("")
        self.label_pl1.setText(QCoreApplication.translate("MainWindow", u"PLAYLIST 1", None))
        self.pl1_add.setText("")
        self.label_dur_1.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.label_nclips_1.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.label_estrella2.setText("")
        self.label_estrella2_2.setText("")
        self.estrella2_delete.setText("")
        self.estrella2_add.setText("")
        self.label_estrella3.setText("")
        self.label_estrella3_2.setText("")
        self.label_estrella3_3.setText("")
        self.estrella3_delete.setText("")
        self.estrella3_add.setText("")
        self.sim_menu.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.sim_take.setText(QCoreApplication.translate("MainWindow", u"TAKE", None))
        self.sim_shift.setText(QCoreApplication.translate("MainWindow", u"SHIFT", None))
        self.sim_f1.setText(QCoreApplication.translate("MainWindow", u"F1", None))
        self.sim_f2.setText(QCoreApplication.translate("MainWindow", u"F2", None))
        self.sim_f3.setText(QCoreApplication.translate("MainWindow", u"F3", None))
        self.sim_f4.setText(QCoreApplication.translate("MainWindow", u"F4", None))
        self.sim_f5.setText(QCoreApplication.translate("MainWindow", u"F5", None))
        self.sim_f6.setText(QCoreApplication.translate("MainWindow", u"F6", None))
        self.sim_f7.setText(QCoreApplication.translate("MainWindow", u"F7", None))
        self.sim_f8.setText(QCoreApplication.translate("MainWindow", u"F8", None))
        self.sim_f9.setText(QCoreApplication.translate("MainWindow", u"F9", None))
        self.sim_f10.setText(QCoreApplication.translate("MainWindow", u"F10", None))
        self.sim_clear.setText(QCoreApplication.translate("MainWindow", u"CLEAR", None))
        self.sim_enter.setText(QCoreApplication.translate("MainWindow", u"ENTER", None))
        self.sim_A.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.sim_B.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.sim_C.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.sim_D.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.sim_play.setText(QCoreApplication.translate("MainWindow", u"PLAY", None))
        self.sim_fastjog.setText(QCoreApplication.translate("MainWindow", u"Fast Jog\n"
" ---------------------\n"
" Mark", None))
        self.sim_record.setText(QCoreApplication.translate("MainWindow", u"Return\n"
" ------------------------ \n"
"Record", None))
        self.sim_prvctl.setText(QCoreApplication.translate("MainWindow", u"Page\n"
" ------------------\n"
"PRV CTL", None))
        self.sim_out.setText(QCoreApplication.translate("MainWindow", u"Goto OUT \n"
" ------------------------- \n"
" OUT", None))
        self.sim_insert.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.sim_in.setText(QCoreApplication.translate("MainWindow", u"Goto IN\n"
" --------------------------\n"
"IN", None))
        self.sim_loop.setText(QCoreApplication.translate("MainWindow", u"Loop\n"
" ------------------------- \n"
" PLST", None))
        self.sim_gototc.setText(QCoreApplication.translate("MainWindow", u"Goto TC \n"
" --------------------\n"
" Last Mark", None))
        self.config_ipconfig.setText(QCoreApplication.translate("MainWindow", u"vMix IP Configuration", None))
        self.config_fastjogconfig.setText(QCoreApplication.translate("MainWindow", u"Fast Jog Configuration", None))
        self.config_deleteclipdict.setText(QCoreApplication.translate("MainWindow", u"Delete Clip Dictionary", None))
        self.config_resetmarks.setText(QCoreApplication.translate("MainWindow", u"Reset Marks", None))
        self.export_playlist.setText(QCoreApplication.translate("MainWindow", u"Export Playlist", None))
        self.export_export_clip.setText(QCoreApplication.translate("MainWindow", u"Export Clip", None))
        self.generic_none.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.generic_lockremote.setText(QCoreApplication.translate("MainWindow", u"Lock Remote", None))
        self.playlist_btnadd_1.setText("")
        self.playlist_numclip_pl1.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.playlist_dur_pl1.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.playlist_codi_pl1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.playlist_btnadd_2.setText("")
        self.playlist_dur_pl2.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.playlist_numclip_pl2.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.playlist_codi_pl2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.playlist_btnadd_3.setText("")
        self.playlist_dur_pl3.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.playlist_numclip_pl3.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.playlist_codi_pl3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.playlist_btnadd_4.setText("")
        self.playlist_dur_pl4.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.playlist_numclip_pl4.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.playlist_codi_pl4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.playlist_btnadd_5.setText("")
        self.playlist_dur_pl5.setText(QCoreApplication.translate("MainWindow", u"00.00:00:000", None))
        self.playlist_numclip_pl5.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.playlist_codi_pl5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.playlist_btnadd_6.setText("")
        self.playlist_dur_pl6.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.playlist_numclip_pl6.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.playlist_codi_pl6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.playlist_button_pl1.setText("")
        self.playlist_button_pl2.setText("")
        self.playlist_button_pl3.setText("")
        self.playlist_button_pl4.setText("")
        self.playlist_button_pl5.setText("")
        self.playlist_button_pl6.setText("")
        self.playlist_dur_pl8.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.playlist_numclip_pl12.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.playlist_codi_pl10.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.playlist_dur_pl9.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.playlist_numclip_pl10.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.playlist_dur_pl10.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.playlist_codi_pl9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.playlist_codi_pl8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.playlist_codi_pl11.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.playlist_dur_pl11.setText(QCoreApplication.translate("MainWindow", u"00.00:00:000", None))
        self.playlist_codi_pl7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.playlist_btnadd_10.setText("")
        self.playlist_button_pl10.setText("")
        self.playlist_button_pl12.setText("")
        self.playlist_button_pl9.setText("")
        self.playlist_numclip_pl11.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.playlist_btnadd_7.setText("")
        self.playlist_btnadd_8.setText("")
        self.playlist_numclip_pl8.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.playlist_button_pl8.setText("")
        self.playlist_numclip_pl9.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.playlist_dur_pl12.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.playlist_codi_pl12.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.playlist_numclip_pl7.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.playlist_button_pl11.setText("")
        self.playlist_btnadd_11.setText("")
        self.playlist_dur_pl7.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.playlist_button_pl7.setText("")
        self.playlist_btnadd_9.setText("")
        self.playlist_btnadd_12.setText("")
        self.playlist_dur_pl14.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.playlist_numclip_pl18.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.playlist_codi_pl16.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.playlist_dur_pl15.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.playlist_numclip_pl16.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.playlist_dur_pl16.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.playlist_codi_pl15.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.playlist_codi_pl14.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.playlist_codi_pl17.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.playlist_dur_pl17.setText(QCoreApplication.translate("MainWindow", u"00.00:00:000", None))
        self.playlist_codi_pl13.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.playlist_btnadd_16.setText("")
        self.playlist_button_pl16.setText("")
        self.playlist_button_pl18.setText("")
        self.playlist_button_pl15.setText("")
        self.playlist_numclip_pl17.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.playlist_btnadd_13.setText("")
        self.playlist_btnadd_14.setText("")
        self.playlist_numclip_pl14.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.playlist_button_pl14.setText("")
        self.playlist_numclip_pl15.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.playlist_dur_pl18.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.playlist_codi_pl18.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.playlist_numclip_pl13.setText(QCoreApplication.translate("MainWindow", u"0 clips", None))
        self.playlist_button_pl17.setText("")
        self.playlist_btnadd_17.setText("")
        self.playlist_dur_pl13.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.playlist_button_pl13.setText("")
        self.playlist_btnadd_15.setText("")
        self.playlist_btnadd_18.setText("")
        self.clip_manag_name_clip.setText(QCoreApplication.translate("MainWindow", u"Name Clip", None))
        self.control_loop.setText(QCoreApplication.translate("MainWindow", u"Loop", None))
        self.control_prv_ctl.setText(QCoreApplication.translate("MainWindow", u"PRV CTL", None))
        self.control_syncprv.setText(QCoreApplication.translate("MainWindow", u"Sync PRV", None))
        self.control_fast_jog.setText(QCoreApplication.translate("MainWindow", u"Fast Jog", None))
        self.control_gotoout.setText(QCoreApplication.translate("MainWindow", u"Go to OUT", None))
        self.control_gotoin.setText(QCoreApplication.translate("MainWindow", u"Go to IN", None))
        self.control_gototc.setText(QCoreApplication.translate("MainWindow", u"Go to TC", None))
        self.control_2ndfastjog.setText(QCoreApplication.translate("MainWindow", u"2nd FastJog Speed", None))
        self.cont_acc_lastmark.setText(QCoreApplication.translate("MainWindow", u"Last Mark", None))
        self.cont_acc_mark.setText(QCoreApplication.translate("MainWindow", u"Mark", None))
        self.cont_acc_lasttc.setText(QCoreApplication.translate("MainWindow", u"Last TC", None))
        self.cont_acc_page.setText(QCoreApplication.translate("MainWindow", u"Page", None))
        self.contec_acc_actualclip.setText(QCoreApplication.translate("MainWindow", u"Actual Clip", None))
        self.cont_acc_actualplaylist.setText(QCoreApplication.translate("MainWindow", u"Actual Playlist", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"BLENDER INSTALLATION", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open Blender", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Ex: C:Program FilesBlender FoundationBlender 2.82 blender.exe", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your Password", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"CommandLinkButton", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Open External Link", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_credits.setText("")
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

