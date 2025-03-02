# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'compras.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(755, 485)
        MainWindow.setMinimumSize(QSize(755, 485))
        MainWindow.setStyleSheet(u"QWidget#principal {\n"
"    background-image: url(recursos/media/fondo.jpg);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    background-size: cover; /* Ajusta la imagen al tama\u00f1o de la ventana */\n"
"}\n"
"   ")
        self.principal = QWidget(MainWindow)
        self.principal.setObjectName(u"principal")
        self.gridLayout = QGridLayout(self.principal)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(17)
        self.gridLayout.setVerticalSpacing(18)
        self.gridLayout.setContentsMargins(16, 16, 16, 16)
        self.te_apellido = QLineEdit(self.principal)
        self.te_apellido.setObjectName(u"te_apellido")

        self.gridLayout.addWidget(self.te_apellido, 9, 0, 1, 1)

        self.label = QLabel(self.principal)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.label_2 = QLabel(self.principal)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.label_2, 7, 0, 1, 1)

        self.te_dni = QLineEdit(self.principal)
        self.te_dni.setObjectName(u"te_dni")

        self.gridLayout.addWidget(self.te_dni, 13, 0, 1, 1)

        self.fc_salida = QDateEdit(self.principal)
        self.fc_salida.setObjectName(u"fc_salida")
        self.fc_salida.setDateTime(QDateTime(QDate(2025, 2, 24), QTime(20, 0, 0)))
        self.fc_salida.setCalendarPopup(True)
        self.fc_salida.setDate(QDate(2025, 2, 24))

        self.gridLayout.addWidget(self.fc_salida, 3, 3, 1, 1)

        self.pt_vuelo = QLineEdit(self.principal)
        self.pt_vuelo.setObjectName(u"pt_vuelo")

        self.gridLayout.addWidget(self.pt_vuelo, 13, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(0, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 16, 2, 1, 1)

        self.label_5 = QLabel(self.principal)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.label_5, 7, 2, 1, 1)

        self.Titulo = QLabel(self.principal)
        self.Titulo.setObjectName(u"Titulo")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(20)
        font.setBold(True)
        self.Titulo.setFont(font)
        self.Titulo.setLayoutDirection(Qt.LeftToRight)
        self.Titulo.setStyleSheet(u"color: black;")
        self.Titulo.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Titulo, 0, 0, 1, 5)

        self.pt_destino = QLineEdit(self.principal)
        self.pt_destino.setObjectName(u"pt_destino")

        self.gridLayout.addWidget(self.pt_destino, 9, 2, 1, 1)

        self.bt_volver = QPushButton(self.principal)
        self.bt_volver.setObjectName(u"bt_volver")
        self.bt_volver.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 180); /* Fondo blanco semi-transparente */\n"
"    border: 1px solid black;  /* Borde negro */\n"
"    border-radius: 5px;  /* Esquinas redondeadas */\n"
"    font-size: 14px;  /* Tama\u00f1o del texto */\n"
"    padding: 5px;  /* Espaciado interno */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(200, 200, 200, 200); /* Cambio de color al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(180, 180, 180, 200); /* Color m\u00e1s oscuro al presionar */\n"
"}")

        self.gridLayout.addWidget(self.bt_volver, 17, 3, 1, 1)

        self.boton_comprar = QPushButton(self.principal)
        self.boton_comprar.setObjectName(u"boton_comprar")
        self.boton_comprar.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 180); /* Fondo blanco semi-transparente */\n"
"    border: 1px solid black;  /* Borde negro */\n"
"    border-radius: 5px;  /* Esquinas redondeadas */\n"
"    font-size: 14px;  /* Tama\u00f1o del texto */\n"
"    padding: 5px;  /* Espaciado interno */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(200, 200, 200, 200); /* Cambio de color al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(180, 180, 180, 200); /* Color m\u00e1s oscuro al presionar */\n"
"}")

        self.gridLayout.addWidget(self.boton_comprar, 17, 2, 1, 1)

        self.label_7 = QLabel(self.principal)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 15, 0, 1, 1)

        self.label_8 = QLabel(self.principal)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 5, 2, 1, 1)

        self.bt_cantidad = QSpinBox(self.principal)
        self.bt_cantidad.setObjectName(u"bt_cantidad")
        self.bt_cantidad.setMinimum(1)

        self.gridLayout.addWidget(self.bt_cantidad, 15, 1, 1, 1)

        self.te_nombre = QLineEdit(self.principal)
        self.te_nombre.setObjectName(u"te_nombre")

        self.gridLayout.addWidget(self.te_nombre, 5, 0, 1, 1)

        self.label_3 = QLabel(self.principal)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.label_3, 11, 0, 1, 1)

        self.label_6 = QLabel(self.principal)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.label_6, 11, 2, 1, 1)

        self.label_4 = QLabel(self.principal)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 2, 1, 1)

        self.fc_vuelta = QDateEdit(self.principal)
        self.fc_vuelta.setObjectName(u"fc_vuelta")
        self.fc_vuelta.setDateTime(QDateTime(QDate(2025, 2, 24), QTime(19, 0, 0)))
        self.fc_vuelta.setCalendarPopup(True)
        self.fc_vuelta.setDate(QDate(2025, 2, 24))

        self.gridLayout.addWidget(self.fc_vuelta, 5, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(2, 2)
        self.gridLayout.setColumnStretch(3, 1)
        MainWindow.setCentralWidget(self.principal)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Vuelos App", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nombre del pasajero:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Apellidos:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Destino:", None))
        self.Titulo.setText(QCoreApplication.translate("MainWindow", u"COMPRAR VUELO", None))
        self.bt_volver.setText(QCoreApplication.translate("MainWindow", u"Volver", None))
        self.boton_comprar.setText(QCoreApplication.translate("MainWindow", u"Comprar", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Cantidad de asientos:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Fecha de regreso:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"NIF/Pasaporte:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Avi\u00f3n:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Fecha de salida:", None))
    # retranslateUi

