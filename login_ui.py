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
        MainWindow.setStyleSheet(u"\n"
"    MainWindow {\n"
"        background-image: url(\"imagenes/fondo.jpg\") background-position: center;\n"
"    }\n"
"   ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Titulo = QLabel(self.centralwidget)
        self.Titulo.setObjectName(u"Titulo")
        self.Titulo.setGeometry(QRect(0, 50, 800, 60))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(20)
        font.setBold(True)
        self.Titulo.setFont(font)
        self.Titulo.setStyleSheet(u"color: white;")
        self.Titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(215, 200, 370, 200))
        self.frame.setStyleSheet(u"\n"
"        QFrame {\n"
"            background-color: rgba(255, 255, 255, 0.8);\n"
"            border-radius: 15px;\n"
"            border: 2px solid #3498db;\n"
"        }\n"
"     ")
        self.frame.setFrameShape(QFrame.Shape.Box)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.la_usu = QLabel(self.frame)
        self.la_usu.setObjectName(u"la_usu")
        self.la_usu.setGeometry(QRect(50, 40, 80, 25))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.la_usu.setFont(font1)
        self.la_usu.setStyleSheet(u"color: black;")
        self.li_usuario = QLineEdit(self.frame)
        self.li_usuario.setObjectName(u"li_usuario")
        self.li_usuario.setGeometry(QRect(140, 40, 180, 25))
        self.li_usuario.setStyleSheet(u"background-color: white; border-radius: 5px;")
        self.la_contra = QLabel(self.frame)
        self.la_contra.setObjectName(u"la_contra")
        self.la_contra.setGeometry(QRect(30, 90, 100, 25))
        self.la_contra.setFont(font1)
        self.la_contra.setStyleSheet(u"color: black;")
        self.li_contra = QLineEdit(self.frame)
        self.li_contra.setObjectName(u"li_contra")
        self.li_contra.setGeometry(QRect(140, 90, 180, 25))
        self.li_contra.setStyleSheet(u"background-color: white; border-radius: 5px;")
        self.li_contra.setEchoMode(QLineEdit.EchoMode.Password)
        self.bu_login = QPushButton(self.frame)
        self.bu_login.setObjectName(u"bu_login")
        self.bu_login.setGeometry(QRect(50, 140, 100, 30))
        self.bu_login.setStyleSheet(u"\n"
"        QPushButton {\n"
"            background-color: #3498db;\n"
"            color: white;\n"
"            border-radius: 5px;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #2980b9;\n"
"        }\n"
"      ")
        self.bu_reg = QPushButton(self.frame)
        self.bu_reg.setObjectName(u"bu_reg")
        self.bu_reg.setGeometry(QRect(210, 140, 100, 30))
        self.bu_reg.setStyleSheet(u"\n"
"        QPushButton {\n"
"            background-color: #2ecc71;\n"
"            color: white;\n"
"            border-radius: 5px;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #27ae60;\n"
"        }\n"
"      ")
        self.bu_salir = QPushButton(self.centralwidget)
        self.bu_salir.setObjectName(u"bu_salir")
        self.bu_salir.setGeometry(QRect(350, 450, 100, 30))
        self.bu_salir.setStyleSheet(u"\n"
"        QPushButton {\n"
"            background-color: red;\n"
"            color: white;\n"
"            border-radius: 5px;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: darkred;\n"
"        }\n"
"      ")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Vuelos App", None))
        self.Titulo.setText(QCoreApplication.translate("MainWindow", u"Bienvenido a Vuelos App", None))
        self.la_usu.setText(QCoreApplication.translate("MainWindow", u"Usuario:", None))
        self.li_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Introduce tu usuario", None))
        self.la_contra.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a:", None))
        self.li_contra.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Introduce tu contrase\u00f1a", None))
        self.bu_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.bu_reg.setText(QCoreApplication.translate("MainWindow", u"Registrarse", None))
        self.bu_salir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
    # retranslateUi

