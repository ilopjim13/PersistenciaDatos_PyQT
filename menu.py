from PyQt6 import QtWidgets, uic
import sys
from PyQt6.QtWidgets import * # Librerías de los componentes
import sqlite3


class Menu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("menu.ui", self) 
        self.BMisViajes.clicked.connect(self.cargar_viajes)
        self.BViajes.clicked.connect(self.cargar_viajes)
        self.QLabelConfiguracion.mousePressEvent= self.mousePressEventLabel

    def cargar_viajes(self):
        conn = 3
        print("emmanuel")
    def mousePressEventLabel(self, event):
        self.cargar_viajes()
if __name__ == '__main__':
    # se crea la instancia de la aplicación
    app = QApplication(sys.argv)
    # se crea la instancia de la ventana
    window = Menu()

    # se muestra la ventana 
    window.show()
    # se entrega el control al sistema operativo
    app.exec() 