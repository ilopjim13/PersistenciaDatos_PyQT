import os
from PyQt6 import QtWidgets, uic, QtGui
import sys
from PyQt6.QtWidgets import *
from recursos_rc import *
import BD.basedatos as baseLocal

class Menu(QtWidgets.QMainWindow):
    def __init__(self,manager):
        super(Menu, self).__init__()
        
        #cargamos la interfaz grafica
        file_log = "menu.ui"
        full_path_lo = os.path.join(os.path.dirname(__file__), file_log)
        uic.loadUi(full_path_lo,self)
        
        #cargamos los datos del destino
        self.cargarDatos()
        
        #este es nuestro navigation
        self.manager = manager

        #revisamo si el usuario ya se ha logeado
        if self.manager.usuario is not None:
            #cargamos los viajes del usuario
            self.cargarDatosLista()
            self.QLNombre.setText(self.manager.usuario.nombre)
            self.QLCorreo.setText(self.manager.usuario.email)
        
        #conectamos los diferentes elementos
        self.QLabelUsuario.setPixmap(QtGui.QPixmap(":/icons/recursos/iconos/usuario.png"))
        self.QLabelConfiguracion.setPixmap(QtGui.QPixmap(":/icons/recursos/iconos/engranaje.png"))
        self.QTMisViajes.itemClicked.connect(self.irAMisViajes)
        self.BMisViajes.clicked.connect(self.irAMisViajes)
        self.QTTredingsTopicsTabla.cellClicked.connect(self.irACompras)
        self.QLabelConfiguracion.mousePressEvent= self.mousePressEventLabel

    #cargamos los datos al a tabla del desinger 
    def cargarDatos(self):

        #esta funcion nos regresa todas los nombre de los destinos disponible
        destinos = baseLocal.obtenerSoloElNombreDelDestinoParaLaPantallaMenu()

        # Configurar la tabla con una sola columna llamada "Destinos"
        self.QTTredingsTopicsTabla.setColumnCount(1)
        self.QTTredingsTopicsTabla.setHorizontalHeaderLabels(["Destinos"])

        # Limpiar filas anteriores
        self.QTTredingsTopicsTabla.setRowCount(0)

        # Insertar los datos en la tabla
        for row_idx, row_data in enumerate(destinos):
            self.QTTredingsTopicsTabla.insertRow(row_idx)
            for col_idx, data in enumerate(row_data):
                self.QTTredingsTopicsTabla.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(data)))
    
    #cargamos los viajes que tenga el usuario vigente en la lista
    def cargarDatosLista(self):
        #recuperamos todos los destinos de la base de datos
        viajes = baseLocal.obtenerSoloElNombreDelViajeParaLaPantallaMenu(self.manager.usuario.email)
        if not viajes:
            print("No se encontraron viajes para este email.")

        #limpiamos la lista antes de meter contenido
        self.QTMisViajes.clear()

        #agregamos la informacion en la lista
        for viaje in viajes:
            self.QTMisViajes.addItem(viaje[0]) 

    #navegamos a la pestaña mis viajes
    def irAMisViajes(self):
        self.manager.mostrarVentana("misviajes")

    #navegamos a la pestaña ir a comprar vuelos
    def irACompras(self,row):
        self.manager.destino=self.QTTredingsTopicsTabla.item(row,0).text()
        self.manager.mostrarVentana("vuelos")

    #si le pulsa al engranage viajamos a la pestaña configuracion
    def mousePressEventLabel(self, event):
        self.irAConfiguracion()

    #navegamos a la pestaña configuracion
    def irAConfiguracion(self):
        self.manager.mostrarVentana("configuracion")