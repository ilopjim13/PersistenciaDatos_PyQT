from PyQt6 import QtWidgets, uic
import sys
from PyQt6.QtWidgets import * # Librerías de los componentes
import sqlite3

class MisViajes(QtWidgets.QMainWindow):
    def __init__(self, email):
        super().__init__()
        uic.loadUi("misviajes.ui", self) 
        self.email = email
        self.boton_actualizar.clicked.connect(self.actualizar_viaje)
        self.boton_eliminar.clicked.connect(self.eliminar_viaje)
        self.cargar_viajes()

    def cargar_viajes(self):
        conn = sqlite3.connect("viajes.db") 
        cursor = conn.cursor()

        cursor.execute("""
            SELECT viaje.id,cliente.nombre, destino.nombre, viaje.fecha_salida, viaje.fecha_regreso, viaje.precio
            FROM viaje
            JOIN cliente ON viaje.cliente_id = cliente.id
            JOIN destino ON viaje.destino_id = destino.id
            WHERE cliente.email = ?
        """, (self.email,))

        # Porquee cojoneeees no sale nadaaaaaaaaa
        viajes = cursor.fetchall()
        print(f"Viajes encontrados: {viajes}") 

        # La fuckin tabla
        self.tabla_viajes.setColumnCount(5) 
        self.tabla_viajes.setHorizontalHeaderLabels(["ID", "Destino", "Fecha de Salida", "Fecha de Regreso", "Precio"])

        self.tabla_viajes.setRowCount(0)  
        for row_idx, row_data in enumerate(viajes):
            self.tabla_viajes.insertRow(row_idx) 
            for col_idx, data in enumerate(row_data):
               
                self.tabla_viajes.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(data)))

        conn.close()


    def actualizar_viaje(self):

        selected = self.tabla_viajes.currentRow()
        if selected < 0:
            QtWidgets.QMessageBox.warning(self, "Error", "Selecciona un viaje para actualizar")
            return
        
        viaje_id = int(self.tabla_viajes.item(selected, 0).text())
        nueva_fecha_salida = self.input_fecha_salida.text()
        nueva_fecha_regreso = self.input_fecha_regreso.text()

        conn = sqlite3.connect("viajes.db")  
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE viaje SET fecha_salida = ?, fecha_regreso = ? WHERE id = ?
        """, (nueva_fecha_salida, nueva_fecha_regreso, viaje_id))
        conn.commit()
        conn.close()
        
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
            conn = sqlite3.connect("viajes.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM viaje WHERE id = ?", (viaje_id,))
            conn.commit()
            conn.close()
            
            self.cargar_viajes()


if __name__ == '__main__':
    # se crea la instancia de la aplicación
    app = QApplication(sys.argv)
    # se crea la instancia de la ventana
    window = MisViajes("paco@gmail.com")

    # se muestra la ventana 
    window.show()
    # se entrega el control al sistema operativo
    app.exec() 