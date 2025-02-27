import sys
import os
from PyQt6.QtWidgets import * # Librerías de los componentes
from PyQt6 import uic  # Librería para trabajar con el archivo de la interfaz
from PyQt6.QtCore import QDate
import BD.basedatos
import sqlite3

class Compra(QMainWindow):
    def __init__(self, manager):
        super().__init__()
        uic.loadUi("compras.ui", self)
        self.manager = manager
        self.vuelo = self.manager.selfvuelo
        self.pasajero = self.manager.usuario
        self.fecha_salida = ""
        self.fecha_regreso = ""
        self.cantidad_asientos = 1
        self.cargar_datos()
        self.fc_salida.dateChanged.connect(self.set_fecha_salida)
        self.fc_vuelta.dateChanged.connect(self.set_fecha_regreso)
        self.bt_cantidad.valueChanged.connect(self.set_cantidad_asientos)
        self.boton_comprar.clicked.connect(self.comprar)

    def cargar_datos(self):
        self.te_nombre.setText(self.pasajero.nombre)
        self.te_apellido.setText(self.pasajero.apellido)
        self.te_dni.setText(self.pasajero.dni)
        self.pt_destino.setPlainText(self.vuelo[4])
        self.pt_vuelo.setPlainText(self.vuelo[0])
        self.fc_salida.setDate(QDate.currentDate())
        self.fc_vuelta.setDate(QDate.currentDate())
        self.set_fecha_regreso(QDate.currentDate())
        self.set_fecha_salida(QDate.currentDate())
        self.bt_volver.clicked.connect(self.volver)

    def set_cantidad_asientos(self, cantidad):
        self.cantidad_asientos = cantidad

    def set_fecha_salida(self, fecha):
        self.fecha_salida = fecha.toString("yyyy-MM-dd")

    def set_fecha_regreso(self, fecha):
        self.fecha_regreso = fecha.toString("yyyy-MM-dd")

    def comprar(self):
        if self.cantidad_asientos > int(self.vuelo[3]):
            QMessageBox.critical(self, "Error", "No hay suficientes asientos disponibles")
            return

        if self.comprobar_fechas():
            con = sqlite3.connect("viajes.db")
            cur = con.cursor()
            id = self.obtener_ultimo_id_viaje() + 1 
            cur.execute('''
                INSERT INTO viaje (id, cliente_email, vuelo_id, fecha_salida, fecha_regreso, precio)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (id, self.pasajero.email, self.vuelo[3], self.fecha_salida, self.fecha_regreso, self.vuelo[1])) 
            con.commit()
            con.close()
            self.actualizar_asientos()
            QMessageBox.information(self, "Compra exitosa", "Compra realizada con éxito")
        else:
            QMessageBox.critical(self, "Error", "La fecha de regreso debe ser posterior a la de salida")

    def actualizar_asientos(self):
        con = sqlite3.connect("viajes.db")
        cur = con.cursor()
        cur.execute('''
            UPDATE vuelo
            SET cantidad_asientos = cantidad_asientos - ?
            WHERE id = ?
        ''', (self.cantidad_asientos, self.vuelo[3]))
        con.commit()
        con.close()

    def comprobar_fechas(self):
        if self.fecha_salida <= self.fecha_regreso:
            return True
        return False

    def obtener_ultimo_id_viaje(self):
        con = sqlite3.connect("viajes.db")
        cur = con.cursor()
        cur.execute('''
            SELECT MAX(id) FROM viaje
        ''')
        id = cur.fetchone()
        con.close()
        print(f"ID: {id}")
        if id[0] == None:
            return 0
        else:
            return int(id[0])
        
    def volver(self):
        self.manager.mostrarVentana("vuelos")


class Bilete(QMainWindow):
    def __init__(self, viaje):
        super().__init__()
        uic.loadUi("bilete.ui", self)
        self.viaje = viaje
        self.cargar_datos()

    def cargar_datos(self):
        self.te_nombre.setText(self.viaje.nombre)
        self.te_apellido.setText(self.viaje[1])
        self.te_dni.setText(self.viaje[2])
        self.te_id.setText(self.viaje[3])

if __name__ == "__main__":
    # se crea la instancia de la aplicación
    app = QApplication(sys.argv)
    # se crea la instancia de la ventana
    window = Compra(["España", "Avion 1"], ["Juan", "Perez", "12345678", "1"])
    # se muestra la ventana 
    window.show()
    # se entrega el control al sistema operativo
    app.exec() 
