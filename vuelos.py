import sys
import os
from PyQt6.QtWidgets import * # Librerías de los componentes
from PyQt6 import uic  # Librería para trabajar con el archivo de la interfaz
import BD.basedatos as baseLocal
import sqlite3
from compra import Compra

# Clase que muestra los vuelos disponibles
class Vuelos(QMainWindow):
    def __init__(self, manager):
        super().__init__()
        uic.loadUi("vuelos.ui", self)
        # Cargamos las variables de la clase y los componente de la interfaz
        self.manager = manager
        self.destino = self.manager.destino
        self.Titulo.setText(f"Vuelos a {self.destino}")
        self.pasajero = self.manager.usuario
        self.orden = 0
        self.cargar_vuelos()
        self.comboBox.currentIndexChanged.connect(self.update_tabla_vuelos)
        self.tabla_vuelos.cellClicked.connect(self.ir_a_comprar)
        self.bt_volver.clicked.connect(self.volver)

    # Método que carga los vuelos disponibles
    def cargar_vuelos(self):
        aviones = baseLocal.obtener_vuelos(self.destino, self.orden)
        aviones.sort(key=lambda x: x[self.orden])
        self.cargar_tabla(aviones)

    # Método que carga la tabla con los vuelos disponibles
    def cargar_tabla(self, aviones):
        #Definimos las columnas de la tabla
        self.tabla_vuelos.setColumnCount(5)
        self.tabla_vuelos.setHorizontalHeaderLabels(["Modelo", "Categoria", "Precio", "Asientos", "ID"])
        self.tabla_vuelos.setRowCount(0)

        #Añadimos los datos a la tabla
        for row_idx, row_data in enumerate(aviones):
            self.tabla_vuelos.insertRow(row_idx)
            for col_idx, data in enumerate(row_data):
                self.tabla_vuelos.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))
        #Ajustamos el tamaño de las columnas
        self.tabla_vuelos.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    # Método que actualiza el orden de la tabla de vuelos
    def update_tabla_vuelos(self):
        # Obtenemos el orden seleccionado
        if self.comboBox.currentText() == "Modelo":
            self.orden = 0
        elif self.comboBox.currentText() == "Categoria":
            self.orden = 1
        elif self.comboBox.currentText() == "Precio":
            self.orden = 2
        # Limpiamos la tabla y cargamos los vuelos ordenados
        self.tabla_vuelos.setRowCount(0)
        # Cargamos los vuelos ordenados
        self.cargar_vuelos()

    # Método que lleva a la ventana de compra
    def ir_a_comprar(self, row):
        # Obtenemos los datos del vuelo seleccionado
        modelo = self.tabla_vuelos.item(row, 0).text()
        precio = self.tabla_vuelos.item(row, 2).text()
        asientos = self.tabla_vuelos.item(row, 3).text()
        id_vuelo = self.tabla_vuelos.item(row, 4).text()
        # Guardamos los datos del vuelo seleccionado
        self.manager.vuelo = [modelo, precio, asientos, id_vuelo, self.destino]
        # Mostramos la ventana de compra
        self.manager.mostrarVentana("compra")

    # Método que lleva a la ventana de menu
    def volver(self):
        self.manager.mostrarVentana("menu")