# -*- coding: utf-8 -*-
"""
Ejemplo de ventana básico de Login

"""
#importamos las librerías necesarias
import sys
import os
from PyQt6.QtWidgets import * # Librerías de los componentes
from PyQt6 import uic  # Librería para trabajar con el archivo de la interfaz
import pyrebase
import requests
import json
import BD.basedatos
import menu
from misviajes import MisViajes 

#TODO hacer register bien y devolver el cliente

class VentanaPrincipal(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Principal")




class ErrorWindow(QMainWindow):

    def __init__(self):
    #Inicializa la ventana
        super().__init__() # Reservamos un espacio en memoria para la clase

        file_err = "error.ui"
        full_path_err =  os.path.join(os.path.dirname(__file__), file_err)
        error = uic.loadUi(full_path_err) 
        uic.loadUi(full_path_err,self) #Lee el archivo de QtDesigner
        self.bu_volver.clicked.connect(self.show_new_window1)

    def show_new_window1(self, checked):
        window.show()
        w2.hide()  

class Ventana(QMainWindow):
    '''Esta es la clase principal'''

    email = ""


    def __init__(self):        #Inicializa la ventana
        super(Ventana, self).__init__() # Reservamos un espacio en memoria para la clase
        file_log = "login.ui"
        full_path_lo = os.path.join(os.path.dirname(__file__), file_log)

        login = uic.loadUi(full_path_lo, self) #Lee el archivo de QtDesigner

        self.firebaseConfig ={
            "apiKey": "AIzaSyDtWlIUbITDQtvTI6pi4k0WxxOlimBIXxY",
            "authDomain": "prueba1-79b1f.firebaseapp.com",
            "databaseURL": "https://prueba1-79b1f-default-rtdb.firebaseio.com/", 
            "projectId": "prueba1-79b1f",
            "storageBucket": "prueba1-79b1f.appspot.com",
            "messagingSenderId": "827606316467",
            "appId": "1:827606316467:web:7cd3fcc0d0d4af6edec7c6"
        }

        


        self.firebase = pyrebase.initialize_app(self.firebaseConfig) #Inicializa la app. 
        self.auth = self.firebase.auth()
     

        self.bu_login.clicked.connect(self.gui_login)
        self.bu_reg.clicked.connect(self.gui_reg)


    def correcto(self, estatus,email):
        if estatus=="l":
            QMessageBox.information(self,'¡Login correcto!', "Acceso garantizado")
            self.cliente = BD.basedatos.get_cliente(email)
        else:
            QMessageBox.information(self,'¡Usuario creado correctamente!', "Creación de usuario")
            self.cliente #TODO hacer data class del cliente y consegir los datos

        
        self.msg = QMessageBox(self)
        self.msg.show
        window.hide()
        self.menu = menu(self.cliente) 

    def error():
        window.hide()
        w2.show()

    def gui_reg(self):
        name = self.li_usuario.text()
        passw = self.li_contra.text()  #hashlib
        if len(name)== 0 or len(passw) == 0:
            QMessageBox.critical(self,'Error', "Ingrese todos los datos") 
        else:
            # user = self.auth.create_user_with_email_and_password(name, passw)
            try:
                user = self.auth.create_user_with_email_and_password(name, passw)
                self.correcto("r",email=user["email"])
            except requests.exceptions.HTTPError as e:
                error_json = e.args[1]
                error = json.loads(error_json)['error']['message']
                self.delete_line()
                print("e: ", error)
                if error == "EMAIL_EXISTS":              
                  QMessageBox.critical(self,'Error', 'EMAIL Existente') 
                elif "INVALID" in error:              
                    QMessageBox.critical(self,'Error', 'EMAIL No válido') 
                elif "WEAK" in error:      
                    QMessageBox.critical(self,'Error', 'Password debe tener al menos 6 caracteres') 
                else:   
                    QMessageBox.critical(self,'Error', 'Error desconocido') 


    def delete_line(self):
        self.li_usuario.setText("")
        self.li_contra.setText("")
        self.li_usuario.setFocus()


    def gui_login(self):
        name = self.li_usuario.text()
        passw = self.li_contra.text()  #hashlib
        if len(name)== 0 or len(passw) == 0:
            QMessageBox.critical(self,'Error', "Ingrese todos los datos") 
        else:
            try:
                user = self.auth.sign_in_with_email_and_password(name, passw)
                self.correcto("l",user["email"])
            except requests.exceptions.HTTPError as e:
                error_json = e.args[1]
                error = json.loads(error_json)['error']['message']
                self.delete_line()
                if  error == "INVALID_EMAIL":        
                      QMessageBox.critical(self,'Error', 'EMAIL NO VÁLIDO') 
                else:     
                      QMessageBox.critical(self,'Error', 'Error') 

    def gui_loginp(self):
        name = self.li_usuario.text()
        passw = self.li_contra.text()  #hashlib
        if len(name)== 0 or len(passw) == 0:
            QMessageBox.critical(self,'Error', "Ingrese todos los datos") 
            
        else:
            try:
                user = self.auth.sign_in_with_email_and_password(name, passw)
                self.correcto(email=user["email"])
            except requests.exceptions.HTTPError as e:
                error_json = e.args[1]
                error = json.loads(error_json)['error']['message']
                self.delete_line()
                if error == "EMAIL_EXISTS":              
                  QMessageBox.critical(self,'Error', 'EMAIL EXISTS') 
                else:
                    if error == "INVALID_EMAIL":        
                      QMessageBox.critical(self,'Error', 'INVALID EMAIL') 
                
        





if __name__ == '__main__':
    # se crea la instancia de la aplicación
    app = QApplication(sys.argv)
    # se crea la instancia de la ventana
    window = Ventana()
    w2 = ErrorWindow()

    window.show()
    # se entrega el control al sistema operativo
    app.exec() 

   

    