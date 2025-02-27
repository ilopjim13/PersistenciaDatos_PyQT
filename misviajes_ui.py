# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'misviajes.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QMainWindow,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_GestionViajes(object):
    def setupUi(self, GestionViajes):
        if not GestionViajes.objectName():
            GestionViajes.setObjectName(u"GestionViajes")
        GestionViajes.resize(653, 420)
        self.centralwidget = QWidget(GestionViajes)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.boton_volver_menu = QPushButton(self.widget1)
        self.boton_volver_menu.setObjectName(u"boton_volver_menu")

        self.horizontalLayout.addWidget(self.boton_volver_menu)


        self.verticalLayout.addWidget(self.widget1)

        self.tabla_viajes = QTableWidget(self.widget)
        self.tabla_viajes.setObjectName(u"tabla_viajes")

        self.verticalLayout.addWidget(self.tabla_viajes)

        self.widget2 = QWidget(self.widget)
        self.widget2.setObjectName(u"widget2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.boton_actualizar = QPushButton(self.widget2)
        self.boton_actualizar.setObjectName(u"boton_actualizar")

        self.horizontalLayout_2.addWidget(self.boton_actualizar)

        self.boton_eliminar = QPushButton(self.widget2)
        self.boton_eliminar.setObjectName(u"boton_eliminar")

        self.horizontalLayout_2.addWidget(self.boton_eliminar)


        self.verticalLayout.addWidget(self.widget2)


        self.verticalLayout_3.addWidget(self.widget)

        GestionViajes.setCentralWidget(self.centralwidget)

        self.retranslateUi(GestionViajes)

        QMetaObject.connectSlotsByName(GestionViajes)
    # setupUi

    def retranslateUi(self, GestionViajes):
        GestionViajes.setWindowTitle(QCoreApplication.translate("GestionViajes", u"Gesti\u00f3n de Viajes", None))
        self.boton_volver_menu.setText(QCoreApplication.translate("GestionViajes", u"< Volver al menu", None))
        self.boton_actualizar.setText(QCoreApplication.translate("GestionViajes", u"Actualizar Viaje", None))
        self.boton_eliminar.setText(QCoreApplication.translate("GestionViajes", u"Eliminar Viaje", None))
    # retranslateUi

