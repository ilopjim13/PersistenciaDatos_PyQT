# -*- coding: utf-8 -*-
import sqlite3

import os
from PyQt6.QtWidgets import * # Librerías de los componentes
from PyQt6 import QtWidgets, uic
import BD.basedatos as baseLocal
from models.cliente import Cliente  # Librería para trabajar con el archivo de la interfaz

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
        uic.loadUi(full_path_lo, self)  # Cargar la UI de QtDesigner
        self.manager = manager
        self.QPBVolver.clicked.connect(lambda: self.irAMenu())
        self.buttonBox_2.button(self.buttonBox_2.StandardButton.Apply).clicked.connect(lambda: self.eliminarusuario())
        self.BBActualizarUsuario.clicked.connect(lambda :self.actualizarUsuario())
        if self.manager.usuario is not None:
            self.QTENombre.setPlainText(self.manager.usuario.nombre)  # Para QLineEdit
            self.QTEApellido.setPlainText(self.manager.usuario.apellido)  # Para QLineEdit
            self.QTEDni.setPlainText(self.manager.usuario.dni)  # Para QLineEdit
        self.BcerrarSesion.clicked.connect(self.cerrarSesion)
    def irAMenu(self):
        self.manager.mostrarVentana("menu")

    def cerrarSesion(self):
        self.manager.usuario = None
        self.manager.mostrarVentana("login")
    def actualizarUsuario(self):
        # Obtener el texto del QTextEdit para el nombre
        nuevo_nombre = self.QTENombre.toPlainText()
        nuevo_email = self.QTEApellido.toPlainText()
        dni = self.QTEDni.toPlainText()
        correo = self.manager.usuario.email
        respuesta = QMessageBox.question(
        self,
        "Confirmar actualización",
        f"¿Seguro que quieres actualizar estos datos?\n\n"
        f"Nombre: {nuevo_nombre}\n"
        f"Email: {nuevo_email}\n"
        f"DNI: {dni}",
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        # Si el usuario confirma, actualizar en la base de datos
        if respuesta == QMessageBox.StandardButton.Yes:
            baseLocal.update_cliente(nuevo_nombre, nuevo_email, dni, correo,)
            usuario_actualizado = baseLocal.obtenerUsuarioPorCorreo(correo)
            id, nombre, email, apellido, dni = usuario_actualizado
            self.manager.usuario = Cliente(id, nombre, email, apellido, dni)
            QMessageBox.information(self, "Actualización", "Datos actualizados con éxito.")
        #si no informa que el propio usuario lo ha cancelado
        else:
            QMessageBox.information(self, "Cancelado", "No se han actualizado los datos.")

    def eliminarusuario(self):
        import pyrebase
        import requests
        respuesta = QMessageBox.question(
        self,
        "Confirmar eliminacion PERMANENTE",
        f"¿Seguro que quiere eliminar tu cuenta de la plataforma?\n\n",
        QMessageBox.StandardButton.No | QMessageBox.StandardButton.Yes)
        # Si el usuario confirma, actualizar en la base de datos
        if respuesta == QMessageBox.StandardButton.Yes:
            self.firebaseConfig = {
            "apiKey": "AIzaSyDtWlIUbITDQtvTI6pi4k0WxxOlimBIXxY",
            "authDomain": "prueba1-79b1f.firebaseapp.com",
            "databaseURL": "https://prueba1-79b1f-default-rtdb.firebaseio.com/", 
            "projectId": "prueba1-79b1f",
            "storageBucket": "prueba1-79b1f.appspot.com",
            "messagingSenderId": "827606316467",
            "appId": "1:827606316467:web:7cd3fcc0d0d4af6edec7c6"
            }

            # Inicializar Firebase
            self.firebase = pyrebase.initialize_app(self.firebaseConfig)
            auth = self.firebase.auth()

            try:

                # Hacer la solicitud a la API de Firebase para eliminar la cuenta
                url = f"https://identitytoolkit.googleapis.com/v1/accounts:delete?key={self.firebaseConfig['apiKey']}"
                response = requests.post(url, json={"idToken": self.manager.token})

                if response.status_code == 200:
                    baseLocal.eliminarClientePorCorreo(self.manager.usuario.email)
                    print("✅ Usuario eliminado correctamente de Firebase")
                    # una vez elminado de firebase, podemos irno de la base de datos y lo regresamos al login
                    self.cerrarSesion()
                else:
                    print("❌ Error al eliminar el usuario:", response.json())

            except requests.exceptions.RequestException as e:
                print("❌ Error de conexión:", e)

            except Exception as e:
                print("❌ Error general:", e)
        else:
            QMessageBox.information(self, "Cancelado", "No se ha eliminado la cuenta.")