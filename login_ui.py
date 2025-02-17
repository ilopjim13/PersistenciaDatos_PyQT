# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 225, 148);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Titulo = QLabel(self.centralwidget)
        self.Titulo.setObjectName(u"Titulo")
        self.Titulo.setGeometry(QRect(0, 80, 791, 61))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(16)
        font.setBold(True)
        self.Titulo.setFont(font)
        self.Titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(160, 220, 371, 181))
        self.frame.setStyleSheet(u"background-color: rgb(85, 255, 255);")
        self.frame.setFrameShape(QFrame.Shape.Box)
        self.frame.setFrameShadow(QFrame.Shadow.Sunken)
        self.li_contra = QLineEdit(self.frame)
        self.li_contra.setObjectName(u"li_contra")
        self.li_contra.setGeometry(QRect(130, 80, 161, 21))
        self.li_contra.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.li_contra.setEchoMode(QLineEdit.EchoMode.Password)
        self.la_usu = QLabel(self.frame)
        self.la_usu.setObjectName(u"la_usu")
        self.la_usu.setGeometry(QRect(50, 30, 71, 21))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.la_usu.setFont(font1)
        self.la_usu.setStyleSheet(u"colo: rgb(255, 255, 255)")
        self.la_usu.setScaledContents(True)
        self.la_usu.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.li_usuario = QLineEdit(self.frame)
        self.li_usuario.setObjectName(u"li_usuario")
        self.li_usuario.setGeometry(QRect(130, 30, 161, 21))
        self.li_usuario.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"\n"
"")
        self.la_contra = QLabel(self.frame)
        self.la_contra.setObjectName(u"la_contra")
        self.la_contra.setGeometry(QRect(30, 80, 91, 21))
        self.la_contra.setFont(font1)
        self.la_contra.setStyleSheet(u"colo: rgb(255, 255, 255)")
        self.la_contra.setScaledContents(True)
        self.la_contra.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.la_res = QLabel(self.frame)
        self.la_res.setObjectName(u"la_res")
        self.la_res.setGeometry(QRect(30, 110, 331, 20))
        font2 = QFont()
        font2.setPointSize(12)
        self.la_res.setFont(font2)
        self.la_res.setStyleSheet(u"color: red;")
        self.bu_login = QPushButton(self.frame)
        self.bu_login.setObjectName(u"bu_login")
        self.bu_login.setGeometry(QRect(50, 130, 75, 25))
        self.bu_login.setStyleSheet(u"QPushButton {\n"
"        background-color: palegoldenrod;\n"
"        border-width: 2px;\n"
"        border-color: darkkhaki;\n"
"        border-style: solid;\n"
"        border-radius: 5;\n"
"        padding: 3px;\n"
"        min-width: 9ex;\n"
"        min-height: 2.5ex;\n"
"    }\n"
"QPushButton:hover {\n"
"        background-color: red;\n"
"        border-width: 2px;\n"
"        border-color: darkkhaki;\n"
"        border-style: solid;\n"
"        border-radius: 5;\n"
"        padding: 3px;\n"
"        min-width: 9ex;\n"
"        min-height: 2.5ex;\n"
"    }\n"
"QPushButton:pressed{\n"
"        background-color: blue;\n"
"        border-width: 2px;\n"
"        border-color: darkkhaki;\n"
"        border-style: solid;\n"
"        border-radius: 10;\n"
"        padding: 3px;\n"
"        min-width: 9ex;\n"
"        min-height: 2.5ex;\n"
"    }")
        self.bu_reg = QPushButton(self.frame)
        self.bu_reg.setObjectName(u"bu_reg")
        self.bu_reg.setGeometry(QRect(240, 130, 75, 25))
        self.bu_reg.setStyleSheet(u"QPushButton {\n"
"        background-color: palegoldenrod;\n"
"        border-width: 2px;\n"
"        border-color: darkkhaki;\n"
"        border-style: solid;\n"
"        border-radius: 5;\n"
"        padding: 3px;\n"
"        min-width: 9ex;\n"
"        min-height: 2.5ex;\n"
"    }\n"
"QPushButton:hover {\n"
"        background-color: red;\n"
"        border-width: 2px;\n"
"        border-color: darkkhaki;\n"
"        border-style: solid;\n"
"        border-radius: 5;\n"
"        padding: 3px;\n"
"        min-width: 9ex;\n"
"        min-height: 2.5ex;\n"
"    }\n"
"QPushButton:pressed{\n"
"        background-color: blue;\n"
"        border-width: 2px;\n"
"        border-color: darkkhaki;\n"
"        border-style: solid;\n"
"        border-radius: 10;\n"
"        padding: 3px;\n"
"        min-width: 9ex;\n"
"        min-height: 2.5ex;\n"
"    }")
        self.bu_salir = QPushButton(self.centralwidget)
        self.bu_salir.setObjectName(u"bu_salir")
        self.bu_salir.setGeometry(QRect(300, 440, 75, 25))
        self.bu_salir.setStyleSheet(u"QPushButton {\n"
"        background-color: palegoldenrod;\n"
"        border-width: 2px;\n"
"        border-color: darkkhaki;\n"
"        border-style: solid;\n"
"        border-radius: 5;\n"
"        padding: 3px;\n"
"        min-width: 9ex;\n"
"        min-height: 2.5ex;\n"
"    }\n"
"QPushButton:hover {\n"
"        background-color: red;\n"
"        border-width: 2px;\n"
"        border-color: darkkhaki;\n"
"        border-style: solid;\n"
"        border-radius: 5;\n"
"        padding: 3px;\n"
"        min-width: 9ex;\n"
"        min-height: 2.5ex;\n"
"    }\n"
"QPushButton:pressed{\n"
"        background-color: blue;\n"
"        border-width: 2px;\n"
"        border-color: darkkhaki;\n"
"        border-style: solid;\n"
"        border-radius: 10;\n"
"        padding: 3px;\n"
"        min-width: 9ex;\n"
"        min-height: 2.5ex;\n"
"    }")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.li_usuario, self.li_contra)
        QWidget.setTabOrder(self.li_contra, self.bu_login)
        QWidget.setTabOrder(self.bu_login, self.bu_reg)
        QWidget.setTabOrder(self.bu_reg, self.bu_salir)

        self.retranslateUi(MainWindow)
        self.bu_salir.clicked.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Titulo.setText(QCoreApplication.translate("MainWindow", u"EJEMPLO LOGIN", None))
        self.li_contra.setPlaceholderText(QCoreApplication.translate("MainWindow", u"introduce una contrase\u00f1a", None))
        self.la_usu.setText(QCoreApplication.translate("MainWindow", u"Usuario:", None))
        self.li_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Introduce un usuario", None))
        self.la_contra.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a:", None))
        self.la_res.setText("")
        self.bu_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.bu_reg.setText(QCoreApplication.translate("MainWindow", u"Registrarse", None))
        self.bu_salir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
    # retranslateUi

