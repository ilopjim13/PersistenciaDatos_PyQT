# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'misviajes.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)
class Ui_GestionViajes(object):
    def setupUi(self, GestionViajes):
        if not GestionViajes.objectName():
            GestionViajes.setObjectName(u"GestionViajes")
        GestionViajes.resize(800, 600)
        self.centralwidget = QWidget(GestionViajes)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabla_viajes = QTableWidget(self.centralwidget)
        self.tabla_viajes.setObjectName(u"tabla_viajes")
        self.tabla_viajes.setGeometry(QRect(20, 20, 760, 400))
        self.boton_actualizar = QPushButton(self.centralwidget)
        self.boton_actualizar.setObjectName(u"boton_actualizar")
        self.boton_actualizar.setGeometry(QRect(200, 450, 150, 40))
        self.boton_eliminar = QPushButton(self.centralwidget)
        self.boton_eliminar.setObjectName(u"boton_eliminar")
        self.boton_eliminar.setGeometry(QRect(450, 450, 150, 40))
        GestionViajes.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(GestionViajes)
        self.statusbar.setObjectName(u"statusbar")
        GestionViajes.setStatusBar(self.statusbar)

        self.retranslateUi(GestionViajes)

        QMetaObject.connectSlotsByName(GestionViajes)
    # setupUi

    def retranslateUi(self, GestionViajes):
        GestionViajes.setWindowTitle(QCoreApplication.translate("GestionViajes", u"Gesti\u00f3n de Viajes", None))
        self.boton_actualizar.setText(QCoreApplication.translate("GestionViajes", u"Actualizar Viaje", None))
        self.boton_eliminar.setText(QCoreApplication.translate("GestionViajes", u"Eliminar Viaje", None))
    # retranslateUi

