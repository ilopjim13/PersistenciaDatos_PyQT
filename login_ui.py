# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)
import recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(775, 485)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(775, 485))
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet(u"\n"
"    MainWindow {\n"
"        background-image: url(\"imagenes/fondo.jpg\") background-position: center;\n"
"    }\n"
"   ")
        self.principal = QWidget(MainWindow)
        self.principal.setObjectName(u"principal")
        sizePolicy.setHeightForWidth(self.principal.sizePolicy().hasHeightForWidth())
        self.principal.setSizePolicy(sizePolicy)
        self.principal.setAutoFillBackground(False)
        self.principal.setStyleSheet(u"#principal{\n"
"background-image: url(:/icons/recursos/media/fondo.jpg);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-attachment: fixed;\n"
"}")
        self.horizontalLayout_11 = QHBoxLayout(self.principal)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.widget_2 = QWidget(self.principal)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(10)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Titulo = QLabel(self.widget_2)
        self.Titulo.setObjectName(u"Titulo")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(20)
        font.setBold(True)
        self.Titulo.setFont(font)
        self.Titulo.setStyleSheet(u"color: white;")
        self.Titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.Titulo)

        self.ContainerLoginYResgister = QWidget(self.widget_2)
        self.ContainerLoginYResgister.setObjectName(u"ContainerLoginYResgister")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(90)
        sizePolicy2.setHeightForWidth(self.ContainerLoginYResgister.sizePolicy().hasHeightForWidth())
        self.ContainerLoginYResgister.setSizePolicy(sizePolicy2)
        self.ContainerLoginYResgister.setStyleSheet(u"#ContainerLoginYResgister{\n"
"min-height: 325;\n"
"min-width: 556px;\n"
"}\n"
"QFrame {\n"
"background-color: rgba(255, 255, 255, 150);\n"
"border-radius: 15px;\n"
"}\n"
"QLabel{ \n"
"min-height: 35px;\n"
"max-height: 35px;\n"
"min-width: 40px;\n"
"max-width: 150px;\n"
"color:black;\n"
"}   \n"
"QLineEdit { \n"
"min-height: 35px;\n"
"max-height: 35px;\n"
"max-width: 150px;\n"
"}\n"
"QLineEdit{\n"
"color:black;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.ContainerLoginYResgister)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.ContainerLoginYResgister)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(50)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy3)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy4)
        self.widget.setMinimumSize(QSize(0, 42))
        self.horizontalLayout_14 = QHBoxLayout(self.widget)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.widget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.la_nombre = QLabel(self.frame_2)
        self.la_nombre.setObjectName(u"la_nombre")
        self.la_nombre.setFont(font1)
        self.la_nombre.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.la_nombre)

        self.li_nombre = QLineEdit(self.frame_2)
        self.li_nombre.setObjectName(u"li_nombre")
        self.li_nombre.setStyleSheet(u"background-color: white; border-radius: 5px;")

        self.horizontalLayout_2.addWidget(self.li_nombre)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.la_nombre_3 = QLabel(self.frame_2)
        self.la_nombre_3.setObjectName(u"la_nombre_3")
        self.la_nombre_3.setFont(font1)
        self.la_nombre_3.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.la_nombre_3)

        self.li_apellido = QLineEdit(self.frame_2)
        self.li_apellido.setObjectName(u"li_apellido")
        self.li_apellido.setStyleSheet(u"background-color: white; border-radius: 5px;")

        self.horizontalLayout_5.addWidget(self.li_apellido)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.la_contra_3 = QLabel(self.frame_2)
        self.la_contra_3.setObjectName(u"la_contra_3")
        self.la_contra_3.setFont(font1)
        self.la_contra_3.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.la_contra_3)

        self.li_contra_2 = QLineEdit(self.frame_2)
        self.li_contra_2.setObjectName(u"li_contra_2")
        self.li_contra_2.setStyleSheet(u"background-color: white; border-radius: 5px;")

        self.horizontalLayout_6.addWidget(self.li_contra_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.la_usu_3 = QLabel(self.frame_2)
        self.la_usu_3.setObjectName(u"la_usu_3")
        self.la_usu_3.setFont(font1)
        self.la_usu_3.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.la_usu_3)

        self.li_usuario_2 = QLineEdit(self.frame_2)
        self.li_usuario_2.setObjectName(u"li_usuario_2")
        self.li_usuario_2.setStyleSheet(u"background-color: white; border-radius: 5px;")

        self.horizontalLayout_7.addWidget(self.li_usuario_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.la_nombre_2 = QLabel(self.frame_2)
        self.la_nombre_2.setObjectName(u"la_nombre_2")
        self.la_nombre_2.setFont(font1)
        self.la_nombre_2.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.la_nombre_2)

        self.li_dni = QLineEdit(self.frame_2)
        self.li_dni.setObjectName(u"li_dni")
        self.li_dni.setStyleSheet(u"background-color: white; border-radius: 5px;")

        self.horizontalLayout_8.addWidget(self.li_dni)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.bu_reg = QPushButton(self.frame_2)
        self.bu_reg.setObjectName(u"bu_reg")
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

        self.verticalLayout_3.addWidget(self.bu_reg)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.ContainerLoginYResgister)
        self.frame.setObjectName(u"frame")
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalWidget_5 = QWidget(self.frame)
        self.horizontalWidget_5.setObjectName(u"horizontalWidget_5")
        sizePolicy4.setHeightForWidth(self.horizontalWidget_5.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_5.setSizePolicy(sizePolicy4)
        self.horizontalLayout_13 = QHBoxLayout(self.horizontalWidget_5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_2 = QLabel(self.horizontalWidget_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_2)


        self.verticalLayout_4.addWidget(self.horizontalWidget_5)

        self.verticalWidget_2 = QWidget(self.frame)
        self.verticalWidget_2.setObjectName(u"verticalWidget_2")
        sizePolicy4.setHeightForWidth(self.verticalWidget_2.sizePolicy().hasHeightForWidth())
        self.verticalWidget_2.setSizePolicy(sizePolicy4)
        self.horizontalLayout_4 = QHBoxLayout(self.verticalWidget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.la_usu = QLabel(self.verticalWidget_2)
        self.la_usu.setObjectName(u"la_usu")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.la_usu.sizePolicy().hasHeightForWidth())
        self.la_usu.setSizePolicy(sizePolicy5)
        self.la_usu.setFont(font1)
        self.la_usu.setStyleSheet(u"")
        self.la_usu.setTextFormat(Qt.TextFormat.AutoText)

        self.horizontalLayout_4.addWidget(self.la_usu)

        self.li_usuario = QLineEdit(self.verticalWidget_2)
        self.li_usuario.setObjectName(u"li_usuario")
        self.li_usuario.setStyleSheet(u"background-color: white; border-radius: 5px;")

        self.horizontalLayout_4.addWidget(self.li_usuario)


        self.verticalLayout_4.addWidget(self.verticalWidget_2)

        self.horizontalWidget = QWidget(self.frame)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        sizePolicy4.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy4)
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.la_contra = QLabel(self.horizontalWidget)
        self.la_contra.setObjectName(u"la_contra")
        self.la_contra.setFont(font1)
        self.la_contra.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.la_contra)

        self.li_contra = QLineEdit(self.horizontalWidget)
        self.li_contra.setObjectName(u"li_contra")
        self.li_contra.setStyleSheet(u"background-color: white; border-radius: 5px;")
        self.li_contra.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_3.addWidget(self.li_contra)


        self.verticalLayout_4.addWidget(self.horizontalWidget)

        self.bu_login = QPushButton(self.frame)
        self.bu_login.setObjectName(u"bu_login")
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

        self.verticalLayout_4.addWidget(self.bu_login)


        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.ContainerLoginYResgister)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.bu_salir = QPushButton(self.widget_3)
        self.bu_salir.setObjectName(u"bu_salir")
        self.bu_salir.setMaximumSize(QSize(150, 16777215))
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

        self.horizontalLayout_12.addWidget(self.bu_salir)


        self.verticalLayout_2.addWidget(self.widget_3)


        self.horizontalLayout_11.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.principal)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Vuelos App", None))
        self.Titulo.setText(QCoreApplication.translate("MainWindow", u"Bienvenido a Vuelos App", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"REGISTRARSE", None))
        self.la_nombre.setText(QCoreApplication.translate("MainWindow", u"Nombre: ", None))
        self.li_nombre.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Introduce tu usuario", None))
        self.la_nombre_3.setText(QCoreApplication.translate("MainWindow", u"Apellido: ", None))
        self.li_apellido.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Introduce tu usuario", None))
        self.la_contra_3.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a:", None))
        self.li_contra_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Introduce tu usuario", None))
        self.la_usu_3.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.li_usuario_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Introduce tu usuario", None))
        self.la_nombre_2.setText(QCoreApplication.translate("MainWindow", u"DNI:", None))
        self.li_dni.setText("")
        self.li_dni.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Introduce tu usuario", None))
        self.bu_reg.setText(QCoreApplication.translate("MainWindow", u"Registrarse", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.la_usu.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.li_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Introduce tu usuario", None))
        self.la_contra.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a:", None))
        self.li_contra.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Introduce tu contrase\u00f1a", None))
        self.bu_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.bu_salir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
    # retranslateUi

