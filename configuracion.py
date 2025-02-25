# -*- coding: utf-8 -*-

import os
from PyQt6.QtWidgets import * # Librerías de los componentes
from PyQt6 import QtWidgets, uic  # Librería para trabajar con el archivo de la interfaz
import BD
import BD.basedatos

#configuracion
#eliminar la cuenta del usuario
#actualizar la cuneta del usuario
#si se actualiza la contraseña del mismo debemos actualizarloen el firebase,como se hace esto?
#si se elimina la cuenta del usuario debemos eliminarlo del firebase,como se hace esto?
#si se actualiza la cuenta del usuario debemos actualizarlo en el firebase,como se hace esto?
#contraseña y email estan dentro del firebase, 
#el usuario preguntar sobre el usuario una vez que se haya accedido 
# en firebase trabajar directamente con usuario y cuenta, todo lo demas puede ser en bd local??

class Configuracion(QtWidgets.QMainWindow):
    def __init__(self,manager):
        super(Configuracion, self).__init__()
        file_log = "configuracion.ui"
        full_path_lo = os.path.join(os.path.dirname(__file__), file_log)
        login = uic.loadUi(full_path_lo, self)  # Cargar la UI de QtDesigner
        self.manager = manager
        self.QPBVolver.clicked.connect(self.irAMenu)
    
    def irAMenu(self):
        self.manager.mostrarVentana("menu")