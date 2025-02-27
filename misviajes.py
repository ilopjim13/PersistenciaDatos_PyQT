from PyQt6 import QtWidgets, uic
import sys
from PyQt6.QtWidgets import * # Librerías de los componentes
import sqlite3
import BD.basedatos as baseLocal

class MisViajes(QtWidgets.QMainWindow):
    def __init__(self, email, manager):
        super().__init__()
        uic.loadUi("misviajes.ui", self) 
        self.email = email
        self.manager = manager
        self.boton_actualizar.clicked.connect(self.actualizar_viaje)
        self.boton_eliminar.clicked.connect(self.eliminar_viaje)
        self.cargar_viajes()

    def cargar_viajes(self):
        viajes = baseLocal.getMisViajes()
        print(f"Viajes encontrados: {viajes}") 

        # La fuckin tabla
        self.tabla_viajes.setColumnCount(5) 
        self.tabla_viajes.setHorizontalHeaderLabels(["ID", "Destino", "Fecha de Salida", "Fecha de Regreso", "Precio"])

        self.tabla_viajes.setRowCount(0)  
        for row_idx, row_data in enumerate(viajes):
            self.tabla_viajes.insertRow(row_idx) 
            for col_idx, data in enumerate(row_data):
               
                self.tabla_viajes.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(data)))
        

    def actualizar_viaje(self):

        selected = self.tabla_viajes.currentRow()
        if selected < 0:
            QtWidgets.QMessageBox.warning(self, "Error", "Selecciona un viaje para actualizar")
            return
        
        viaje_id = int(self.tabla_viajes.item(selected, 0).text())
        nueva_fecha_salida = self.input_fecha_salida.text()
        nueva_fecha_regreso = self.input_fecha_regreso.text()

        baseLocal.putMisViajes(nueva_fecha_salida, nueva_fecha_regreso, viaje_id)
        
        self.cargar_viajes()

    def eliminar_viaje(self):

        selected = self.tabla_viajes.currentRow()
        if selected < 0:
            QtWidgets.QMessageBox.warning(self, "Error", "Selecciona un viaje para eliminar")
            return
        
        viaje_id = int(self.tabla_viajes.item(selected, 0).text())

        respuesta = QtWidgets.QMessageBox.question(
            self, "Confirmar Eliminación", "¿Estás seguro de eliminar este viaje?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
        )
        if respuesta == QtWidgets.QMessageBox.StandardButton.Yes:
            baseLocal.delMisViajes(viaje_id)
            self.cargar_viajes()
    
    
    def volverMenu(self):
        self.manager.mostrarVentana("menu")