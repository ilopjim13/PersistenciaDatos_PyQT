# -*- coding: utf-8 -*-

#importamos las librerías necesarias
import sys
import os
from PyQt6.QtWidgets import * # Librerías de los componentes
from PyQt6 import uic  # Librería para trabajar con el archivo de la interfaz
import pyrebase
import requests
import json
import BD
import BD.basedatos
from misviajes import MisViajes 

#configuracion
#eliminar la cuenta del usuario
#actualizar la cuneta del usuario
#si se actualiza la contraseña del mismo debemos actualizarloen el firebase,como se hace esto?
#si se elimina la cuenta del usuario debemos eliminarlo del firebase,como se hace esto?
#si se actualiza la cuenta del usuario debemos actualizarlo en el firebase,como se hace esto?
#contraseña y email estan dentro del firebase, 
#el usuario preguntar sobre el usuario una vez que se haya accedido 
# en firebase trabajar directamente con usuario y cuenta, todo lo demas puede ser en bd local??

class Ventana(QMainWindow):
    def __init__(self):
        super(Ventana, self).__init__()
        file_log = "login.ui"
        full_path_lo = os.path.join(os.path.dirname(__file__), file_log)
        login = uic.loadUi(full_path_lo, self)  # Cargar la UI de QtDesigner

        # 🔹 Configurar Firebase con pyrebase para autenticación
        self.firebaseConfig = {
            "apiKey": "TU_API_KEY",
            "authDomain": "TU_AUTH_DOMAIN",
            "databaseURL": "TU_DATABASE_URL",
            "storageBucket": "TU_STORAGE_BUCKET",
            "messagingSenderId": "TU_MESSAGING_SENDER_ID",
            "appId": "TU_APP_ID"
        }

        self.firebase = pyrebase.initialize_app(self.firebaseConfig)
        self.auth = self.firebase.auth()  # Servicio de autenticación

        # Conectar botones a funciones
        self.btn_iniciar_sesion.clicked.connect(self.iniciar_sesion)
        self.btn_cambiar_contraseña.clicked.connect(self.cambiar_contraseña)

        self.usuario_actual = self.auth.current_user # Variable para guardar el usuario autenticado

    def cambiar_contraseña(self):
        nueva_contraseña = self.input_nueva_contraseña.text()

        if not self.usuario_actual:
            QMessageBox.warning(self, "Error", "Debes iniciar sesión primero.")
            return

        try:
            # 🔹 Cambiar la contraseña del usuario autenticado
            self.auth.update_user_password(self.usuario_actual['idToken'], nueva_contraseña)
            QMessageBox.information(self, "Éxito", "¡Contraseña actualizada con éxito!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo cambiar la contraseña: {e}")