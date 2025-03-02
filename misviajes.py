from PyQt6 import QtWidgets, uic
import sys
from PyQt6.QtWidgets import * 
import sqlite3
import BD.basedatos as baseLocal
from datetime import datetime

class MisViajes(QtWidgets.QMainWindow):
    def __init__(self, manager):
        super().__init__()
        uic.loadUi("misviajes.ui", self) 
        self.manager = manager
        if self.manager.usuario is not None:
            self.email = self.manager.usuario.email
            self.boton_actualizar.clicked.connect(self.actualizar_viaje)
            self.boton_eliminar.clicked.connect(self.eliminar_viaje)
            self.boton_volver_menu.clicked.connect(self.volverMenu)
            self.cargar_viajes()

    def cargar_viajes(self):
        self.viajes = baseLocal.getMisViajes(self.email)
        print(f"Viajes encontrados: {self.viajes}") 

        # La fuckin tabla
        self.tabla_viajes.setColumnCount(4)
        self.tabla_viajes.setHorizontalHeaderLabels(["Destino", "Fecha de Salida", "Fecha de Regreso", "Precio"])
        self.tabla_viajes.setRowCount(0) 

        for viaje in self.viajes:
            destino = viaje[2]
            fecha_salida = viaje[3]  
            fecha_regreso = viaje[4]  
            precio = viaje[5]  

            row_position = self.tabla_viajes.rowCount()
            self.tabla_viajes.insertRow(row_position)

            self.tabla_viajes.setItem(row_position, 0, QtWidgets.QTableWidgetItem(destino))
            self.tabla_viajes.setItem(row_position, 1, QtWidgets.QTableWidgetItem(fecha_salida))
            self.tabla_viajes.setItem(row_position, 2, QtWidgets.QTableWidgetItem(fecha_regreso))
            self.tabla_viajes.setItem(row_position, 3, QtWidgets.QTableWidgetItem(str(precio)))
         
       
        

    def actualizar_viaje(self):
        selected = self.tabla_viajes.currentRow()
        if selected < 0:
            QtWidgets.QMessageBox.warning(self, "Error", "Selecciona un viaje para actualizar")
            return

        viaje_id = int(self.viajes[selected][0])

        fila = self.tabla_viajes.currentRow()
        columna = self.tabla_viajes.currentColumn()

        print(fila)
        print(columna)

        nueva_fecha_salida = self.tabla_viajes.item(selected, 1).text() 
        nueva_fecha_regreso = self.tabla_viajes.item(selected, 2).text()

        formato_fecha = "%Y-%m-%d"
        try:
            fecha_salida = datetime.strptime(nueva_fecha_salida, formato_fecha)
            fecha_regreso = datetime.strptime(nueva_fecha_regreso, formato_fecha)
            fecha_actual = datetime.today()

            if fecha_salida < fecha_actual:
                QtWidgets.QMessageBox.warning(self, "Error", "La fecha de salida no puede ser en el pasado.")
                return

            if fecha_regreso < fecha_salida:
                QtWidgets.QMessageBox.warning(self, "Error", "La fecha de regreso no puede ser anterior a la de salida.")
                return

        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Error", "Formato de fecha inválido. Use YYYY-MM-DD.")
            return

        baseLocal.putMisViajes(nueva_fecha_salida, nueva_fecha_regreso,viaje_id)

        self.cargar_viajes()

    def eliminar_viaje(self):

        selected = self.tabla_viajes.currentRow()
        if selected < 0:
            QtWidgets.QMessageBox.warning(self, "Error", "Selecciona un viaje para eliminar")
            return
        
        viaje_id = int(self.viajes[selected][0])

        respuesta = QtWidgets.QMessageBox.question(
            self, "Confirmar Eliminación", "¿Estás seguro de eliminar este viaje?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
        )
        if respuesta == QtWidgets.QMessageBox.StandardButton.Yes:
            baseLocal.delMisViajes(viaje_id)
            self.cargar_viajes()
    
    
    def volverMenu(self):
        self.manager.mostrarVentana("menu")