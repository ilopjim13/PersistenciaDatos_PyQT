# -*- coding: utf-8 -*-
import sqlite3

import os
from PyQt6.QtWidgets import * # Librerías de los componentes
from PyQt6 import QtWidgets, uic
import pyrebase
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
        login = uic.loadUi(full_path_lo, self)  # Cargar la UI de QtDesigner
        self.manager = manager
        self.BBActualizarUsuario.clicked.connect(lambda: self.actualizarUsuario())
        self.QPBVolver.clicked.connect(lambda: self.irAMenu())
        self.obtenerUsuarioPorId("juan@example.com")
        self.QTENombre.setPlainText(self.manager.usuario.nombre)  # Para QLineEdit
        self.QTEApellido.setPlainText(self.manager.usuario.apellido)  # Para QLineEdit
        self.QTEDni.setPlainText(self.manager.usuario.dni)  # Para QLineEdit
    def irAMenu(self):
        self.manager.mostrarVentana("menu")

    def actualizarUsuario(self):
        # Obtener el texto del QTextEdit para el nombre
        nuevo_nombre = self.QTENombre.toPlainText()
        nuevo_email = self.QTEApellido.toPlainText()
        dni = self.QTEDni.toPlainText()
        print(dni)
        correo = "juan@example.com"
        # Conectar a la base de datos
        conn = sqlite3.connect('viajes.db')
        cursor = conn.cursor()

        # Ejecutar la actualización
        cursor.execute("""
            UPDATE cliente
            SET nombre = ?, apellido = ?, dni = ?
            WHERE email = ? 
        """, (nuevo_nombre, nuevo_email, dni,correo,))
        conn.commit()
        conn.close()
        usuario_actualizado = self.obtenerUsuarioPorId(correo)
        QMessageBox.information(self, "Actualización", usuario_actualizado)
    
    def obtenerUsuarioPorId(self,correo):
        conn = sqlite3.connect('viajes.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM cliente WHERE email = ?""", (correo,))
        usuario_actualizado = cursor.fetchone()
        conn.close()

        id, nombre, email, apellido, dni = usuario_actualizado
        self.manager.usuario = Cliente(id, nombre, email, apellido, dni)
    
    def eliminarusuario(self):
        self.firebaseConfig ={
            "apiKey": "AIzaSyDtWlIUbITDQtvTI6pi4k0WxxOlimBIXxY",
            "authDomain": "prueba1-79b1f.firebaseapp.com",
            "databaseURL": "https://prueba1-79b1f-default-rtdb.firebaseio.com/", 
            "projectId": "prueba1-79b1f",
            "storageBucket": "prueba1-79b1f.appspot.com",
            "messagingSenderId": "827606316467",
            "appId": "1:827606316467:web:7cd3fcc0d0d4af6edec7c6"
        }
        self.firebase = self.pyrebase.initialize_app(self.firebaseConfig)
        self.auth = self.firebase.auth()
        self.auth.delete_user(self.manager.token)
        #eliminar de manera local