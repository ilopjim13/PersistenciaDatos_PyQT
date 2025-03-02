import sys
import os
from PyQt6.QtWidgets import * # Librerías de los componentes
from PyQt6 import uic  # Librería para trabajar con el archivo de la interfaz
import BD.basedatos
import sqlite3
from compra import Compra

class Vuelos(QMainWindow):
    def __init__(self, manager):
        super().__init__()
        uic.loadUi("vuelos.ui", self)
        self.manager = manager
        self.destino = self.manager.destino
        self.Titulo.setText(f"Vuelos a {self.destino}")
        self.pasajero = self.manager.usuario
        self.orden = 0
        self.cargar_vuelos()
        self.comboBox.currentIndexChanged.connect(self.update_tabla_vuelos)
        self.tabla_vuelos.cellClicked.connect(self.ir_a_comprar)
        self.bt_volver.clicked.connect(self.volver)

    def cargar_vuelos(self):
        conn = sqlite3.connect("viajes.db")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT a.modelo, a.categoria, ROUND(v.precio, 2), v.cantidad_asientos,v.id 
            FROM avion a
            JOIN vuelo v ON a.id = v.avion_id
            JOIN destino d ON v.destino_id = d.id
            WHERE d.nombre = ?
            ORDER BY ?
        """, (self.destino, self.orden))

        aviones = cursor.fetchall()
        aviones.sort(key=lambda x: x[self.orden])
        print(f"Aviones encontrados: {aviones}")

        self.tabla_vuelos.setColumnCount(5)
        self.tabla_vuelos.setHorizontalHeaderLabels(["Modelo", "Categoria", "Precio", "Asientos", "ID"])

        self.tabla_vuelos.setRowCount(0)
        for row_idx, row_data in enumerate(aviones):
            self.tabla_vuelos.insertRow(row_idx)
            for col_idx, data in enumerate(row_data):
                self.tabla_vuelos.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))

        conn.close()

    def update_tabla_vuelos(self):
        if self.comboBox.currentText() == "Modelo":
            self.orden = 0
        elif self.comboBox.currentText() == "Categoria":
            self.orden = 1
        elif self.comboBox.currentText() == "Precio":
            self.orden = 2
        self.tabla_vuelos.setRowCount(0)
        self.cargar_vuelos()

    def ir_a_comprar(self, row):
        modelo = self.tabla_vuelos.item(row, 0).text()
        precio = self.tabla_vuelos.item(row, 2).text()
        asientos = self.tabla_vuelos.item(row, 3).text()
        id_vuelo = self.tabla_vuelos.item(row, 4).text()
        vuelo = [modelo, precio, asientos, id_vuelo, self.destino]
        self.manager.vuelo = vuelo
        self.manager.mostrarVentana("compra")

    def volver(self):
        self.manager.mostrarVentana("menu")

if __name__ == "__main__":
    # se crea la instancia de la aplicación
    app = QApplication(sys.argv)
    # se crea la instancia de la ventana
    window = Vuelos("Francia", ["Pepe", "Perez", "12345678","1"])
    # se muestra la ventana 
    window.show()
    # se entrega el control al sistema operativo
    app.exec() 
