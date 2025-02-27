# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1163, 660)
        MainWindow.setMinimumSize(QSize(775, 485))
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet(u"")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
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
        self.principal = QWidget(MainWindow)
        self.principal.setObjectName(u"principal")
        self.principal.setAcceptDrops(False)
        self.principal.setAutoFillBackground(False)
        self.principal.setStyleSheet(u"#principal{\n"
"background-image: url(:/icons/recursos/media/fondo.jpg);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-attachment: fixed;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.principal)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.QWGridCabecera = QWidget(self.principal)
        self.QWGridCabecera.setObjectName(u"QWGridCabecera")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.QWGridCabecera.sizePolicy().hasHeightForWidth())
        self.QWGridCabecera.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.QWGridCabecera)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.QLabelUsuario = QLabel(self.QWGridCabecera)
        self.QLabelUsuario.setObjectName(u"QLabelUsuario")
        self.QLabelUsuario.setMaximumSize(QSize(85, 85))
        self.QLabelUsuario.setPixmap(QPixmap(u":/icons/recursos/iconos/usuario.png"))
        self.QLabelUsuario.setScaledContents(True)
        self.QLabelUsuario.setWordWrap(False)

        self.horizontalLayout.addWidget(self.QLabelUsuario)

        self.QWGirdDatosUsuarios = QWidget(self.QWGridCabecera)
        self.QWGirdDatosUsuarios.setObjectName(u"QWGirdDatosUsuarios")
        self.verticalLayout_2 = QVBoxLayout(self.QWGirdDatosUsuarios)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.QLNombre = QLabel(self.QWGirdDatosUsuarios)
        self.QLNombre.setObjectName(u"QLNombre")
        font = QFont()
        font.setPointSize(20)
        font.setWeight(QFont.ExtraBold)
        self.QLNombre.setFont(font)

        self.verticalLayout_2.addWidget(self.QLNombre)

        self.QLCorreo = QLabel(self.QWGirdDatosUsuarios)
        self.QLCorreo.setObjectName(u"QLCorreo")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setWeight(QFont.ExtraBold)
        self.QLCorreo.setFont(font1)

        self.verticalLayout_2.addWidget(self.QLCorreo)


        self.horizontalLayout.addWidget(self.QWGirdDatosUsuarios)

        self.QLNombreApp = QLabel(self.QWGridCabecera)
        self.QLNombreApp.setObjectName(u"QLNombreApp")
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.QLNombreApp.setPalette(palette)
        font2 = QFont()
        font2.setPointSize(24)
        font2.setWeight(QFont.Black)
        font2.setUnderline(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        font2.setHintingPreference(QFont.PreferDefaultHinting)
        self.QLNombreApp.setFont(font2)

        self.horizontalLayout.addWidget(self.QLNombreApp)

        self.QLabelConfiguracion = QLabel(self.QWGridCabecera)
        self.QLabelConfiguracion.setObjectName(u"QLabelConfiguracion")
        self.QLabelConfiguracion.setMaximumSize(QSize(80, 80))
        self.QLabelConfiguracion.setPixmap(QPixmap(u":/icons/recursos/iconos/engranaje.png"))
        self.QLabelConfiguracion.setScaledContents(True)
        self.QLabelConfiguracion.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.QLabelConfiguracion)


        self.verticalLayout.addWidget(self.QWGridCabecera)

        self.QWGridMenus = QWidget(self.principal)
        self.QWGridMenus.setObjectName(u"QWGridMenus")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(90)
        sizePolicy1.setHeightForWidth(self.QWGridMenus.sizePolicy().hasHeightForWidth())
        self.QWGridMenus.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.QWGridMenus)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.QWMenus = QWidget(self.QWGridMenus)
        self.QWMenus.setObjectName(u"QWMenus")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.QWMenus.sizePolicy().hasHeightForWidth())
        self.QWMenus.setSizePolicy(sizePolicy2)
        self.QWMenus.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.QWMenus)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.QFMisViajes = QWidget(self.QWMenus)
        self.QFMisViajes.setObjectName(u"QFMisViajes")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.QFMisViajes.sizePolicy().hasHeightForWidth())
        self.QFMisViajes.setSizePolicy(sizePolicy3)
        self.verticalLayout_4 = QVBoxLayout(self.QFMisViajes)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.QLMisViajes = QLabel(self.QFMisViajes)
        self.QLMisViajes.setObjectName(u"QLMisViajes")
        self.QLMisViajes.setMaximumSize(QSize(16777215, 22))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setWeight(QFont.ExtraBold)
        self.QLMisViajes.setFont(font3)
        self.QLMisViajes.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.QLMisViajes)

        self.widget_2 = QWidget(self.QFMisViajes)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.QTredingTopics = QListWidget(self.widget_2)
        QListWidgetItem(self.QTredingTopics)
        QListWidgetItem(self.QTredingTopics)
        QListWidgetItem(self.QTredingTopics)
        self.QTredingTopics.setObjectName(u"QTredingTopics")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.QTredingTopics.sizePolicy().hasHeightForWidth())
        self.QTredingTopics.setSizePolicy(sizePolicy4)
        self.QTredingTopics.setMaximumSize(QSize(350, 16777215))

        self.horizontalLayout_4.addWidget(self.QTredingTopics)


        self.verticalLayout_4.addWidget(self.widget_2)

        self.BMisViajes = QPushButton(self.QFMisViajes)
        self.BMisViajes.setObjectName(u"BMisViajes")

        self.verticalLayout_4.addWidget(self.BMisViajes)


        self.horizontalLayout_2.addWidget(self.QFMisViajes)

        self.QFTredingTopics = QWidget(self.QWMenus)
        self.QFTredingTopics.setObjectName(u"QFTredingTopics")
        sizePolicy3.setHeightForWidth(self.QFTredingTopics.sizePolicy().hasHeightForWidth())
        self.QFTredingTopics.setSizePolicy(sizePolicy3)
        self.QFTredingTopics.setAcceptDrops(False)
        self.verticalLayout_5 = QVBoxLayout(self.QFTredingTopics)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.QLTredingTopics = QLabel(self.QFTredingTopics)
        self.QLTredingTopics.setObjectName(u"QLTredingTopics")
        self.QLTredingTopics.setMaximumSize(QSize(16777215, 22))
        self.QLTredingTopics.setFont(font3)
        self.QLTredingTopics.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.QLTredingTopics.setIndent(-1)

        self.verticalLayout_5.addWidget(self.QLTredingTopics)

        self.widget = QWidget(self.QFTredingTopics)
        self.widget.setObjectName(u"widget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy5)
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tableWidget = QTableWidget(self.widget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy6)
        self.tableWidget.setMinimumSize(QSize(0, 0))
        self.tableWidget.setMaximumSize(QSize(350, 16777215))
        self.tableWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.tableWidget.setAcceptDrops(False)
        self.tableWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tableWidget.setFrameShadow(QFrame.Shadow.Sunken)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget.setAutoScrollMargin(1)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(24)

        self.horizontalLayout_3.addWidget(self.tableWidget)


        self.verticalLayout_5.addWidget(self.widget)

        self.BViajes = QPushButton(self.QFTredingTopics)
        self.BViajes.setObjectName(u"BViajes")

        self.verticalLayout_5.addWidget(self.BViajes)


        self.horizontalLayout_2.addWidget(self.QFTredingTopics)


        self.verticalLayout_3.addWidget(self.QWMenus)


        self.verticalLayout.addWidget(self.QWGridMenus)

        MainWindow.setCentralWidget(self.principal)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.actionCerrar_sesion.setText(QCoreApplication.translate("MainWindow", u"Cerrar sesion", None))
        self.actionSalir_del_programa.setText(QCoreApplication.translate("MainWindow", u"Salir del programa", None))
        self.actionver_viajes.setText(QCoreApplication.translate("MainWindow", u"ver viajes", None))
        self.actioncomprar_viaje.setText(QCoreApplication.translate("MainWindow", u"comprar viaje", None))
        self.actionconfiguracion.setText(QCoreApplication.translate("MainWindow", u"configuracion", None))
        self.actionacerca_de_mi.setText(QCoreApplication.translate("MainWindow", u"acerca de mi", None))
#if QT_CONFIG(tooltip)
        self.principal.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.QLabelUsuario.setText("")
        self.QLNombre.setText(QCoreApplication.translate("MainWindow", u"usuario", None))
        self.QLCorreo.setText(QCoreApplication.translate("MainWindow", u"usuario@gmail.com", None))
        self.QLNombreApp.setText(QCoreApplication.translate("MainWindow", u"Skyberia", None))
        self.QLabelConfiguracion.setText("")
        self.QLMisViajes.setText(QCoreApplication.translate("MainWindow", u"Mis viajes", None))

        __sortingEnabled = self.QTredingTopics.isSortingEnabled()
        self.QTredingTopics.setSortingEnabled(False)
        ___qlistwidgetitem = self.QTredingTopics.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Grecia", None));
        ___qlistwidgetitem1 = self.QTredingTopics.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Francia", None));
        ___qlistwidgetitem2 = self.QTredingTopics.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Alemania", None));
        self.QTredingTopics.setSortingEnabled(__sortingEnabled)

        self.BMisViajes.setText(QCoreApplication.translate("MainWindow", u"Mis Viajes", None))
        self.QLTredingTopics.setText(QCoreApplication.translate("MainWindow", u"Treding topics", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Origen", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Destino", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Precio", None));

        __sortingEnabled1 = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem3 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"espa\u00f1a", None));
        ___qtablewidgetitem4 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Francia", None));
        ___qtablewidgetitem5 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"23\u20ac", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled1)

        self.BViajes.setText(QCoreApplication.translate("MainWindow", u"Viajes", None))
    # retranslateUi

