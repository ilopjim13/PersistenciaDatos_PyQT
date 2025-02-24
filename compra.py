import sys
import os
from PyQt6.QtWidgets import * # Librerías de los componentes
from PyQt6 import uic  # Librería para trabajar con el archivo de la interfaz
import BD.basedatos
import sqlite3

class Compra(QMainWindow):
    def __init__(self, vuelo, pasajero):
        super().__init__()
        uic.loadUi("compras.ui", self)
        self.vuelo = vuelo
        self.pasajero = pasajero
        self.cargar_datos()
        self.boton_comprar.clicked.connect(self.comprar)


    def cargar_datos(self):
        self.te_nombre.setText(self.pasajero[0])
        self.te_apellido.setText(self.pasajero[1])
        self.te_dni.setText(self.pasajero[2])
        self.pt_destino.setPlainText(self.vuelo[0])
        self.pt_vuelo.setPlainText(self.vuelo[1])

if __name__ == "__main__":
    # se crea la instancia de la aplicación
    app = QApplication(sys.argv)
    # se crea la instancia de la ventana
    window = Compra(["España", "Avion 1"], ["Juan", "Perez", "12345678"])
    # se muestra la ventana 
    window.show()
    # se entrega el control al sistema operativo
    app.exec() 
