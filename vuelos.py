import sys
import os
from PyQt6.QtWidgets import * # Librerías de los componentes
from PyQt6 import uic  # Librería para trabajar con el archivo de la interfaz
import BD.basedatos
import sqlite3

class Vuelos(QMainWindow):
    def __init__(self, destino):
        super().__init__()
        uic.loadUi("vuelos.ui", self)
        self.destino = destino
        self.orden = 2
        self.cargar_vuelos()
        self.comboBox.currentIndexChanged.connect(self.update_tabla_vuelos)

    def cargar_vuelos(self, orden=2):
        conn = sqlite3.connect("viajes.db")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT v.id, a.modelo, a.categoria, v.precio, (v.cantidad_asientos - a.capacidad_total) AS cantidad_total
            FROM avion a
            JOIN vuelo v ON a.id = v.avion_id
            JOIN destino d ON v.destino_id = d.id
            WHERE d.nombre = ?
            ORDER BY ?
        """, (self.destino, orden))

        aviones = cursor.fetchall()

        self.tabla_vuelos.setColumnCount(4)
        self.tabla_vuelos.setHorizontalHeaderLabels(["Modelo", "Categoria", "Precio", "Cantidad de Asientos"])

        self.tabla_vuelos.setRowCount(0)
        for row_idx, row_data in enumerate(aviones):
            self.tabla_vuelos.insertRow(row_idx)
            for col_idx, data in enumerate(row_data):
                self.tabla_vuelos.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))

        conn.close()

    def update_tabla_vuelos(self):
        if self.comboBox.currentText() == "Modelo":
            self.orden = 2
        elif self.comboBox.currentText() == "Categoria":
            self.orden = 3
        elif self.comboBox.currentText() == "Precio":
            self.orden = 4
        self.cargar_vuelos(self.orden)

if __name__ == "__main__":
    # se crea la instancia de la aplicación
    app = QApplication(sys.argv)
    # se crea la instancia de la ventana
    window = Vuelos("japon")
    # se muestra la ventana 
    window.show()
    # se entrega el control al sistema operativo
    app.exec() 
