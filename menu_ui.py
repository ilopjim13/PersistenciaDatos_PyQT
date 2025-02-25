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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QSizePolicy, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(775, 485)
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
"background-color:#6b6b6b\n"
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
        self.QLabelUsuario.setPixmap(QPixmap(u":/icons/iconos/usuario.png"))
        self.QLabelUsuario.setScaledContents(True)

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
        self.QLabelConfiguracion.setPixmap(QPixmap(u":/icons/iconos/engranaje.png"))
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
        self.QWMenus.setMinimumSize(QSize(0, 484))
        self.horizontalLayout_2 = QHBoxLayout(self.QWMenus)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.QFMisViajes = QFrame(self.QWMenus)
        self.QFMisViajes.setObjectName(u"QFMisViajes")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.QFMisViajes.sizePolicy().hasHeightForWidth())
        self.QFMisViajes.setSizePolicy(sizePolicy2)
        self.QFMisViajes.setFrameShape(QFrame.Shape.StyledPanel)
        self.QFMisViajes.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.QFMisViajes)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.QLMisViajes = QLabel(self.QFMisViajes)
        self.QLMisViajes.setObjectName(u"QLMisViajes")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setWeight(QFont.ExtraBold)
        self.QLMisViajes.setFont(font3)

        self.verticalLayout_4.addWidget(self.QLMisViajes)

        self.QTredingTopics = QListWidget(self.QFMisViajes)
        QListWidgetItem(self.QTredingTopics)
        QListWidgetItem(self.QTredingTopics)
        QListWidgetItem(self.QTredingTopics)
        self.QTredingTopics.setObjectName(u"QTredingTopics")

        self.verticalLayout_4.addWidget(self.QTredingTopics)


        self.horizontalLayout_2.addWidget(self.QFMisViajes)

        self.QFTredingTopics = QFrame(self.QWMenus)
        self.QFTredingTopics.setObjectName(u"QFTredingTopics")
        sizePolicy2.setHeightForWidth(self.QFTredingTopics.sizePolicy().hasHeightForWidth())
        self.QFTredingTopics.setSizePolicy(sizePolicy2)
        self.QFTredingTopics.setFrameShape(QFrame.Shape.StyledPanel)
        self.QFTredingTopics.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.QFTredingTopics)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.QLTredingTopics = QLabel(self.QFTredingTopics)
        self.QLTredingTopics.setObjectName(u"QLTredingTopics")
        self.QLTredingTopics.setMaximumSize(QSize(16777215, 22))
        self.QLTredingTopics.setFont(font3)
        self.QLTredingTopics.setIndent(-1)

        self.verticalLayout_5.addWidget(self.QLTredingTopics)

        self.tableWidget = QTableWidget(self.QFTredingTopics)
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
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)
        self.tableWidget.setMinimumSize(QSize(0, 0))
        self.tableWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.tableWidget.setAcceptDrops(False)
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

        self.verticalLayout_5.addWidget(self.tableWidget)


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

    # retranslateUi

