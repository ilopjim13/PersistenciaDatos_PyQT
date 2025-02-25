import os
from PyQt6 import QtWidgets, uic
import sys
from PyQt6.QtWidgets import *


class Menu(QtWidgets.QMainWindow):
    def __init__(self,manager):
        super(Menu, self).__init__()
        file_log = "menu.ui"
        full_path_lo = os.path.join(os.path.dirname(__file__), file_log)
        uic.loadUi(full_path_lo,self)
        self.manager = manager
        self.BMisViajes.clicked.connect(self.cargar_viajes)
        self.BViajes.clicked.connect(self.cargar_viajes)
        self.QLabelConfiguracion.mousePressEvent= self.mousePressEventLabel

    def cargar_viajes(self):
        conn = 3
        print("emmanuel")

    def mousePressEventLabel(self, event):
        self.irAConfiguracion()

    def irAConfiguracion(self):
        self.manager.mostrarVentana("configuracion")