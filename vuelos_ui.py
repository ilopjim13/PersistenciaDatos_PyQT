# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vuelos.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFrame, QHeaderView, QLabel, QMainWindow,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
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
        self.Titulo.setGeometry(QRect(0, 40, 800, 60))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(20)
        font.setBold(True)
        self.Titulo.setFont(font)
        self.Titulo.setLayoutDirection(Qt.LeftToRight)
        self.Titulo.setStyleSheet(u"color: white;")
        self.Titulo.setAlignment(Qt.AlignCenter)
        self.tabla_vuelos = QTableWidget(self.centralwidget)
        self.tabla_vuelos.setObjectName(u"tabla_vuelos")
        self.tabla_vuelos.setGeometry(QRect(20, 129, 760, 421))
        self.tabla_vuelos.setLayoutDirection(Qt.LeftToRight)
        self.tabla_vuelos.setAutoFillBackground(False)
        self.tabla_vuelos.setFrameShape(QFrame.NoFrame)
        self.tabla_vuelos.setFrameShadow(QFrame.Sunken)
        self.tabla_vuelos.setLineWidth(1)
        self.tabla_vuelos.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tabla_vuelos.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tabla_vuelos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla_vuelos.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.tabla_vuelos.setAlternatingRowColors(False)
        self.tabla_vuelos.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla_vuelos.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla_vuelos.setTextElideMode(Qt.ElideMiddle)
        self.tabla_vuelos.setShowGrid(False)
        self.tabla_vuelos.setGridStyle(Qt.SolidLine)
        self.tabla_vuelos.setSortingEnabled(False)
        self.tabla_vuelos.setCornerButtonEnabled(True)
        self.tabla_vuelos.setRowCount(0)
        self.tabla_vuelos.setColumnCount(0)
        self.tabla_vuelos.horizontalHeader().setVisible(True)
        self.tabla_vuelos.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_vuelos.horizontalHeader().setDefaultSectionSize(190)
        self.tabla_vuelos.horizontalHeader().setStretchLastSection(False)
        self.tabla_vuelos.verticalHeader().setVisible(False)
        self.tabla_vuelos.verticalHeader().setHighlightSections(True)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(660, 100, 121, 22))
        self.comboBox.setEditable(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Vuelos App", None))
        self.Titulo.setText(QCoreApplication.translate("MainWindow", u"Vuelos para ", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Modelo", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Categoria", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Precio", None))

    # retranslateUi

