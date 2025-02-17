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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 602)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 225, 148);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.la_tit = QLabel(self.centralwidget)
        self.la_tit.setObjectName(u"la_tit")
        self.la_tit.setGeometry(QRect(0, 40, 791, 61))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(16)
        font.setBold(True)
        self.la_tit.setFont(font)
        self.la_tit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bu_volver_a = QPushButton(self.centralwidget)
        self.bu_volver_a.setObjectName(u"bu_volver_a")
        self.bu_volver_a.setGeometry(QRect(190, 530, 121, 51))
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
        self.li_dni = QLineEdit(self.centralwidget)
        self.li_dni.setObjectName(u"li_dni")
        self.li_dni.setGeometry(QRect(150, 140, 211, 21))
        self.li_apel1 = QLineEdit(self.centralwidget)
        self.li_apel1.setObjectName(u"li_apel1")
        self.li_apel1.setGeometry(QRect(150, 170, 211, 21))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(150, 200, 131, 21))
        self.la_nom = QLabel(self.centralwidget)
        self.la_nom.setObjectName(u"la_nom")
        self.la_nom.setGeometry(QRect(70, 140, 71, 16))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.la_nom.setFont(font1)
        self.la_nom.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.la_nom_2 = QLabel(self.centralwidget)
        self.la_nom_2.setObjectName(u"la_nom_2")
        self.la_nom_2.setGeometry(QRect(60, 170, 81, 20))
        self.la_nom_2.setFont(font1)
        self.la_nom_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.la_nom_3 = QLabel(self.centralwidget)
        self.la_nom_3.setObjectName(u"la_nom_3")
        self.la_nom_3.setGeometry(QRect(70, 200, 71, 16))
        self.la_nom_3.setFont(font1)
        self.la_nom_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(90, 260, 331, 192))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.la_tit.setText(QCoreApplication.translate("MainWindow", u"EJEMPLO LOGIN", None))
        self.bu_volver_a.setText(QCoreApplication.translate("MainWindow", u"VOLVER", None))
        self.la_nom.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.la_nom_2.setText(QCoreApplication.translate("MainWindow", u"Apellido 1:", None))
        self.la_nom_3.setText(QCoreApplication.translate("MainWindow", u"DNI:", None))
    # retranslateUi

