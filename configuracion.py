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
        self.BBActualizarUsuario.clicked.connect(lambda: self.actualizarUsuario())
        self.eliminarusuario()
        if self.manager.usuario is not None:
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
        correo = self.manager.usuario.email
        # Conectar a la base de datos
        baseLocal.update_cliente(nuevo_nombre, nuevo_email, dni,correo,)
        usuario_actualizado = baseLocal.obtenerUsuarioPorCorreo(correo)
        QMessageBox.information(self, "Actualización", usuario_actualizado)
        
        id, nombre, email, apellido, dni = usuario_actualizado
        self.manager.usuario = Cliente(nombre, email, apellido, dni)
    
    def eliminarusuario(self):
        import pyrebase
        self.firebaseConfig ={
            "apiKey": "AIzaSyDtWlIUbITDQtvTI6pi4k0WxxOlimBIXxY",
            "authDomain": "prueba1-79b1f.firebaseapp.com",
            "databaseURL": "https://prueba1-79b1f-default-rtdb.firebaseio.com/", 
            "projectId": "prueba1-79b1f",
            "storageBucket": "prueba1-79b1f.appspot.com",
            "messagingSenderId": "827606316467",
            "appId": "1:827606316467:web:7cd3fcc0d0d4af6edec7c6"
        }
        self.firebase = pyrebase.initialize_app(self.firebaseConfig)
        self.firebase.auth().delete_user_account(self.manager.token)
      
        #eliminar de manera local