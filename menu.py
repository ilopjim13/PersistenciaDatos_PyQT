import os
from PyQt6 import QtWidgets, uic, QtGui
import sys
from PyQt6.QtWidgets import *
from recursos_rc import *
import BD.basedatos as baseLocal

class Menu(QtWidgets.QMainWindow):
    def __init__(self,manager):
        super(Menu, self).__init__()
        file_log = "menu.ui"
        full_path_lo = os.path.join(os.path.dirname(__file__), file_log)
        uic.loadUi(full_path_lo,self)
        self.cargarDatos()
        self.QLabelUsuario.setPixmap(QtGui.QPixmap(":/icons/recursos/iconos/usuario.png"))
        self.QLabelConfiguracion.setPixmap(QtGui.QPixmap(":/icons/recursos/iconos/engranaje.png"))
        self.manager = manager
        self.BMisViajes.clicked.connect(self.irAMisViajes)
        self.QTTredingsTopicsTabla.cellClicked.connect(self.irACompras)
        self.QLabelConfiguracion.mousePressEvent= self.mousePressEventLabel


    def cargarDatos(self):
        destinos = baseLocal.obtenerSoloElNombreDelDestinoParaLaPantallaMenu()
        
        self.QTTredingsTopicsTabla.setColumnCount(1)
        self.QTTredingsTopicsTabla.setHorizontalHeaderLabels(["Destinos"])
        self.QTTredingsTopicsTabla.setRowCount(0)
        for row_idx, row_data in enumerate(destinos):
            self.QTTredingsTopicsTabla.insertRow(row_idx)
            for col_idx, data in enumerate(row_data):
                self.QTTredingsTopicsTabla.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(data)))
    
    def irAMisViajes(self):
        self.manager.mostrarVentana("misviajes")

    def irACompras(self,row):
        self.manager.destino=self.QTTredingsTopicsTabla.item(row,0).text()
        self.manager.mostrarVentana("vuelos")

    def mousePressEventLabel(self, event):
        self.irAConfiguracion()

    def irAConfiguracion(self):
        self.manager.mostrarVentana("configuracion")