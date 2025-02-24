# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(799, 623)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.actionCerrar_sesion = QAction(MainWindow)
        self.actionCerrar_sesion.setObjectName(u"actionCerrar_sesion")
        self.actionSalir_del_programa = QAction(MainWindow)
        self.actionSalir_del_programa.setObjectName(u"actionSalir_del_programa")
        self.actionver_viajes = QAction(MainWindow)
        self.actionver_viajes.setObjectName(u"actionver_viajes")
        self.actioncomprar_viaje = QAction(MainWindow)
        self.actioncomprar_viaje.setObjectName(u"actioncomprar_viaje")
        self.actionconfiguracion = QAction(MainWindow)
        self.actionconfiguracion.setObjectName(u"actionconfiguracion")
        self.actionacerca_de_mi = QAction(MainWindow)
        self.actionacerca_de_mi.setObjectName(u"actionacerca_de_mi")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(99, 119, 18, 28))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 799, 33))
        self.mis_viajes = QMenu(self.menubar)
        self.mis_viajes.setObjectName(u"mis_viajes")
        self.menuMi_zona = QMenu(self.menubar)
        self.menuMi_zona.setObjectName(u"menuMi_zona")
        self.menuCerrar_sesion = QMenu(self.menubar)
        self.menuCerrar_sesion.setObjectName(u"menuCerrar_sesion")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.mis_viajes.menuAction())
        self.menubar.addAction(self.menuMi_zona.menuAction())
        self.menubar.addAction(self.menuCerrar_sesion.menuAction())
        self.mis_viajes.addAction(self.actionver_viajes)
        self.mis_viajes.addAction(self.actioncomprar_viaje)
        self.menuMi_zona.addAction(self.actionconfiguracion)
        self.menuMi_zona.addAction(self.actionacerca_de_mi)
        self.menuCerrar_sesion.addAction(self.actionCerrar_sesion)
        self.menuCerrar_sesion.addAction(self.actionSalir_del_programa)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionCerrar_sesion.setText(QCoreApplication.translate("MainWindow", u"Cerrar sesion", None))
        self.actionSalir_del_programa.setText(QCoreApplication.translate("MainWindow", u"Salir del programa", None))
        self.actionver_viajes.setText(QCoreApplication.translate("MainWindow", u"ver viajes", None))
        self.actioncomprar_viaje.setText(QCoreApplication.translate("MainWindow", u"comprar viaje", None))
        self.actionconfiguracion.setText(QCoreApplication.translate("MainWindow", u"configuracion", None))
        self.actionacerca_de_mi.setText(QCoreApplication.translate("MainWindow", u"acerca de mi", None))
        self.mis_viajes.setTitle(QCoreApplication.translate("MainWindow", u"Mis viajes", None))
        self.menuMi_zona.setTitle(QCoreApplication.translate("MainWindow", u"Mi zona", None))
        self.menuCerrar_sesion.setTitle(QCoreApplication.translate("MainWindow", u"Salir", None))
    # retranslateUi

