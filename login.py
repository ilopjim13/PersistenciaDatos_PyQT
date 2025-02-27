import sys
import os
from PyQt6.QtWidgets import *
from PyQt6 import uic
import pyrebase
import requests
import json
#import Navigation
import models.cliente as model
import BD.basedatos as baseLocal



class Ventana(QMainWindow):
    def __init__(self,manager):
        super(Ventana, self).__init__()
        file_log = "login.ui"
        full_path_lo = os.path.join(os.path.dirname(__file__), file_log)
        uic.loadUi(full_path_lo, self)
        self.manager = manager
        self.firebaseConfig = {
            "apiKey": "AIzaSyDtWlIUbITDQtvTI6pi4k0WxxOlimBIXxY",
            "authDomain": "prueba1-79b1f.firebaseapp.com",
            "databaseURL": "https://prueba1-79b1f-default-rtdb.firebaseio.com/",
            "projectId": "prueba1-79b1f",
            "storageBucket": "prueba1-79b1f.appspot.com",
            "messagingSenderId": "827606316467",
            "appId": "1:827606316467:web:7cd3fcc0d0d4af6edec7c6"
        }

        
        self.firebase = pyrebase.initialize_app(self.firebaseConfig)
        self.auth = self.firebase.auth()
        self.db = self.firebase.database()

        self.bu_login.clicked.connect(self.gui_login)
        self.bu_reg.clicked.connect(self.gui_reg)

    def gui_reg(self):
        nombre = self.li_nombre.text()
        apellido = self.li_apellido.text()
        dni = self.li_dni.text()
        email = self.li_usuario_2.text()
        passw = self.li_contra_2.text()
        
        if not (nombre and apellido and dni and email and passw):
            QMessageBox.critical(self, 'Error', "Ingrese todos los datos")
            return
        
        try:
            cliente = model.Cliente(0,nombre, email, apellido, dni)
            existo = baseLocal.insertar_cliente(cliente)

            if existo is None:
                QMessageBox.critical(self, 'Error', "No se ingresó el usuario en la base de datos")

            user = self.auth.create_user_with_email_and_password(email, passw)
            print(user)
            self.manager.mostrarVentana("menu")
            self.manager.token = user["idToken"]
            print(user["idToken"])
            
            self.manager.usuario = cliente
            

            self.correcto("r")
        except requests.exceptions.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            QMessageBox.critical(self, 'Error', error)
            self.delete_line()

    def gui_login(self):
        email = self.li_usuario.text()
        passw = self.li_contra.text()

        if not (email and passw):
            QMessageBox.critical(self, 'Error', "Ingrese todos los datos")
            return
        
        try:
            user = self.auth.sign_in_with_email_and_password(email, passw)
            cliente = baseLocal.obtener_cliente(email)

            baseLocal.prueba()

            self.manager.mostrarVentana("menu")
            self.manager.token = user["idToken"]
            self.manager.usuario = cliente        

            if cliente is not None:
                self.correcto("l")
            else:
                QMessageBox.critical(self, 'Error', "No se encontró el usuario en la base de datos")
        except requests.exceptions.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            QMessageBox.critical(self, 'Error', error)
            self.delete_line()

    def correcto(self, estatus):
        if estatus == "l":
            QMessageBox.information(self, '¡Login correcto!', "Acceso garantizado")
        else:
            QMessageBox.information(self, '¡Usuario creado correctamente!', "Creación de usuario")
        

    def delete_line(self):
        self.li_usuario.setText("")
        self.li_contra.setText("")
        self.li_usuario.setFocus()