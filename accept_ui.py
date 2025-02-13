# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'accept.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 602)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 225, 148);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 40, 791, 61))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.la_res = QLabel(self.centralwidget)
        self.la_res.setObjectName(u"la_res")
        self.la_res.setGeometry(QRect(150, 140, 331, 20))
        font1 = QFont()
        font1.setPointSize(12)
        self.la_res.setFont(font1)
        self.la_res.setStyleSheet(u"color: red;")
        self.bu_volver_a = QPushButton(self.centralwidget)
        self.bu_volver_a.setObjectName(u"bu_volver_a")
        self.bu_volver_a.setGeometry(QRect(310, 350, 121, 51))
        self.bu_volver_a.setStyleSheet(u"QPushButton {\n"
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

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"EJEMPLO LOGIN", None))
        self.la_res.setText(QCoreApplication.translate("MainWindow", u"MEN\u00da DE OPCIONES", None))
        self.bu_volver_a.setText(QCoreApplication.translate("MainWindow", u"VOLVER", None))
    # retranslateUi

