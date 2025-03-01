# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'billete.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFormLayout, QFrame,
    QHBoxLayout, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)
import recursos_rc

class Ui_GestionViajes(object):
    def setupUi(self, GestionViajes):
        if not GestionViajes.objectName():
            GestionViajes.setObjectName(u"GestionViajes")
        GestionViajes.resize(755, 485)
        GestionViajes.setMinimumSize(QSize(755, 485))
        self.principal = QWidget(GestionViajes)
        self.principal.setObjectName(u"principal")
        self.principal.setStyleSheet(u"#principal{\n"
"background-image: url(:/icons/recursos/media/fondo.jpg);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-attachment: fixed;\n"
"}\n"
"QTableWidget {\n"
"background-color: rgba(255, 255, 255, 150); /* Fondo blanco con 150 de opacidad (0-255) */\n"
"color: black; \n"
"border: 1px solid #555; /* Borde gris */\n"
"padding: 5px; /* Espaciado interno */\n"
"}\n"
"QTableWidget::item {\n"
"padding: 5px; /* Espaciado interno en cada item */\n"
"color: black; \n"
"margin: 5px; /* Espaciado externo en cada item */\n"
"}\n"
"QTableWidget::item:selected {\n"
"background-color: rgba(100, 100, 255, 200); /* Fondo azul al seleccionar un item */\n"
"color: black; /* Color del texto al seleccionar */\n"
"}\n"
"QTableWidget QTableCornerButton::section {\n"
"background-color: rgba(255, 255, 255, 50); /* Fondo semitransparente para las cabeceras */\n"
"color: black; /* Color del texto en las cabeceras */\n"
"border: 1px solid black; /* Borde negro */\n"
"}\n"
"QTableWidget::horizon"
                        "talHeader {\n"
"background-color: rgba(255, 255, 255, 50); /* Fondo semitransparente para las cabeceras horizontales */\n"
"color: black; /* Color del texto en las cabeceras */\n"
"border: 1px solid black; /* Borde negro */\n"
"}\n"
"QPushButton {\n"
"background-color: rgba(255, 255, 255, 150); /* Fondo semitransparente para los botones */\n"
"color: black; /* Color del texto en los botones */\n"
"border: 1px solid black; /* Borde negro */\n"
"padding: 5px; /* Espaciado interno */\n"
"border-radius: 5px; /* Bordes redondeados */\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(200, 200, 200, 200); /* Fondo m\u00e1s oscuro al pasar el rat\u00f3n */\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(150, 150, 150, 200); /* Fondo a\u00fan m\u00e1s oscuro al presionar */\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.principal)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(self.principal)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout.addWidget(self.widget1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"QTextEdit {\n"
"    background-color: transparent;  /* Fondo negro suave */\n"
"    font-size: 24px;  /* Tama\u00f1o del texto */\n"
"    font-family: \"Arial\", sans-serif;  /* Fuente elegante */\n"
"    padding: 10px;  /* Espaciado interno */\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 2px solid #555555;  /* Cambio de borde al enfocar */\n"
"}\n"
"\n"
"\n"
"")
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.textEdit)

        self.textEdit_2 = QTextEdit(self.widget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setStyleSheet(u"QTextEdit {\n"
"    background-color: transparent;  /* Fondo negro suave */\n"
"    font-size: 24px;  /* Tama\u00f1o del texto */\n"
"    font-family: \"Arial\", sans-serif;  /* Fuente elegante */\n"
"    padding: 10px;  /* Espaciado interno */\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 2px solid #555555;  /* Cambio de borde al enfocar */\n"
"}")
        self.textEdit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_2.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.textEdit_2)

        self.te_nombre = QTextEdit(self.widget)
        self.te_nombre.setObjectName(u"te_nombre")
        self.te_nombre.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.te_nombre)

        self.textEdit_4 = QTextEdit(self.widget)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setEnabled(True)
        self.textEdit_4.setAutoFillBackground(False)
        self.textEdit_4.setFrameShape(QFrame.StyledPanel)
        self.textEdit_4.setFrameShadow(QFrame.Sunken)
        self.textEdit_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_4.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.textEdit_4.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.textEdit_4)

        self.textEdit_5 = QTextEdit(self.widget)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setStyleSheet(u"QTextEdit {\n"
"    background-color: transparent;  /* Fondo negro suave */\n"
"    font-size: 24px;  /* Tama\u00f1o del texto */\n"
"    font-family: \"Arial\", sans-serif;  /* Fuente elegante */\n"
"    padding: 10px;  /* Espaciado interno */\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 2px solid #555555;  /* Cambio de borde al enfocar */\n"
"}")
        self.textEdit_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_5.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.textEdit_5)

        self.textEdit_6 = QTextEdit(self.widget)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setStyleSheet(u"QTextEdit {\n"
"    background-color: transparent;  /* Fondo negro suave */\n"
"    font-size: 24px;  /* Tama\u00f1o del texto */\n"
"    font-family: \"Arial\", sans-serif;  /* Fuente elegante */\n"
"    padding: 10px;  /* Espaciado interno */\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 2px solid #555555;  /* Cambio de borde al enfocar */\n"
"}")
        self.textEdit_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_6.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.textEdit_6)

        self.te_apellido = QTextEdit(self.widget)
        self.te_apellido.setObjectName(u"te_apellido")
        self.te_apellido.setReadOnly(True)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.te_apellido)

        self.textEdit_16 = QTextEdit(self.widget)
        self.textEdit_16.setObjectName(u"textEdit_16")
        self.textEdit_16.setReadOnly(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.textEdit_16)

        self.textEdit_14 = QTextEdit(self.widget)
        self.textEdit_14.setObjectName(u"textEdit_14")
        self.textEdit_14.setStyleSheet(u"QTextEdit {\n"
"    background-color: transparent;  /* Fondo negro suave */\n"
"    font-size: 24px;  /* Tama\u00f1o del texto */\n"
"    font-family: \"Arial\", sans-serif;  /* Fuente elegante */\n"
"    padding: 10px;  /* Espaciado interno */\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 2px solid #555555;  /* Cambio de borde al enfocar */\n"
"}")
        self.textEdit_14.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_14.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_14.setReadOnly(True)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.textEdit_14)

        self.textEdit_15 = QTextEdit(self.widget)
        self.textEdit_15.setObjectName(u"textEdit_15")
        self.textEdit_15.setStyleSheet(u"QTextEdit {\n"
"    background-color: transparent;  /* Fondo negro suave */\n"
"    font-size: 24px;  /* Tama\u00f1o del texto */\n"
"    font-family: \"Arial\", sans-serif;  /* Fuente elegante */\n"
"    padding: 10px;  /* Espaciado interno */\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 2px solid #555555;  /* Cambio de borde al enfocar */\n"
"}")
        self.textEdit_15.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_15.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_15.setReadOnly(True)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.textEdit_15)

        self.te_dni = QTextEdit(self.widget)
        self.te_dni.setObjectName(u"te_dni")
        self.te_dni.setReadOnly(True)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.te_dni)

        self.textEdit_12 = QTextEdit(self.widget)
        self.textEdit_12.setObjectName(u"textEdit_12")
        self.textEdit_12.setReadOnly(True)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.textEdit_12)

        self.textEdit_9 = QTextEdit(self.widget)
        self.textEdit_9.setObjectName(u"textEdit_9")
        self.textEdit_9.setStyleSheet(u"QTextEdit {\n"
"    background-color: transparent;  /* Fondo negro suave */\n"
"    font-size: 24px;  /* Tama\u00f1o del texto */\n"
"    font-family: \"Arial\", sans-serif;  /* Fuente elegante */\n"
"    padding: 10px;  /* Espaciado interno */\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 2px solid #555555;  /* Cambio de borde al enfocar */\n"
"}")
        self.textEdit_9.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_9.setReadOnly(True)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.textEdit_9)

        self.textEdit_10 = QTextEdit(self.widget)
        self.textEdit_10.setObjectName(u"textEdit_10")
        self.textEdit_10.setStyleSheet(u"QTextEdit {\n"
"    background-color: transparent;  /* Fondo negro suave */\n"
"    font-size: 24px;  /* Tama\u00f1o del texto */\n"
"    font-family: \"Arial\", sans-serif;  /* Fuente elegante */\n"
"    padding: 10px;  /* Espaciado interno */\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 2px solid #555555;  /* Cambio de borde al enfocar */\n"
"}")
        self.textEdit_10.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_10.setReadOnly(True)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.textEdit_10)

        self.te_asientos = QTextEdit(self.widget)
        self.te_asientos.setObjectName(u"te_asientos")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.te_asientos)

        self.textEdit_8 = QTextEdit(self.widget)
        self.textEdit_8.setObjectName(u"textEdit_8")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.textEdit_8)


        self.verticalLayout.addLayout(self.formLayout)

        self.widget2 = QWidget(self.widget)
        self.widget2.setObjectName(u"widget2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.boton_actualizar = QPushButton(self.widget2)
        self.boton_actualizar.setObjectName(u"boton_actualizar")

        self.horizontalLayout_2.addWidget(self.boton_actualizar)

        self.pushButton = QPushButton(self.widget2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.widget2)


        self.verticalLayout_3.addWidget(self.widget)

        GestionViajes.setCentralWidget(self.principal)

        self.retranslateUi(GestionViajes)

        QMetaObject.connectSlotsByName(GestionViajes)
    # setupUi

    def retranslateUi(self, GestionViajes):
        GestionViajes.setWindowTitle(QCoreApplication.translate("GestionViajes", u"Gesti\u00f3n de Viajes", None))
        self.textEdit.setHtml(QCoreApplication.translate("GestionViajes", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Arial','sans-serif'; font-size:24px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:9pt;\">Nombre del pasajero:</span></p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("GestionViajes", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Arial','sans-serif'; font-size:24px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:9pt;\">Origen:</span></p></body></html>", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("GestionViajes", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Espa\u00f1a</p></body></html>", None))
        self.textEdit_5.setHtml(QCoreApplication.translate("GestionViajes", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Arial','sans-serif'; font-size:24px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:9pt;\">Apellido del pasajero:</span></p></body></html>", None))
        self.textEdit_6.setHtml(QCoreApplication.translate("GestionViajes", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Arial','sans-serif'; font-size:24px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:9pt;\">Destino:</span></p></body></html>", None))
        self.textEdit_14.setHtml(QCoreApplication.translate("GestionViajes", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Arial','sans-serif'; font-size:24px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:9pt;\">DNI Del pasajero:</span></p></body></html>", None))
        self.textEdit_15.setHtml(QCoreApplication.translate("GestionViajes", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Arial','sans-serif'; font-size:24px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:9pt;\">Fecha de salida:</span></p></body></html>", None))
        self.textEdit_9.setHtml(QCoreApplication.translate("GestionViajes", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Arial','sans-serif'; font-size:24px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:9pt;\">Asientos:</span></p></body></html>", None))
        self.textEdit_10.setHtml(QCoreApplication.translate("GestionViajes", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Arial','sans-serif'; font-size:24px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:9pt;\">Fecha de vuelta:</span></p></body></html>", None))
        self.boton_actualizar.setText(QCoreApplication.translate("GestionViajes", u"Aceptar", None))
        self.pushButton.setText(QCoreApplication.translate("GestionViajes", u"Descargar PDF", None))
    # retranslateUi

