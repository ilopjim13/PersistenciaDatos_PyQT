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

rutaUi = os.path.join(os.path.dirname(__file__), 'calculadora.ui')
diractual = os.getcwd()
path = diractual + "/8-login/"


#Carga la interfaz gráfica y conecta los botones
class AcceptWindow(QMainWindow):

    def __init__(self):
    #Inicializa la ventana
        super().__init__() # Reservamos un espacio en memoria para la clase

        file_accept = "accept.ui"
        full_path_accept =  os.path.join(os.path.dirname(__file__), file_accept)
        accept = uic.loadUi(full_path_accept) 
        uic.loadUi(full_path_accept,self) #Lee el archivo de QtDesigner
        self.bu_volver_a.clicked.connect(self.show_new_window2)

    def show_new_window2(self, checked):
        window.show()
        w3.hide()  


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


    def __init__(self):        #Inicializa la ventana
        super(Ventana, self).__init__() # Reservamos un espacio en memoria para la clase
        file_log = "login.ui"
        full_path_lo = os.path.join(os.path.dirname(__file__), file_log)

        login = uic.loadUi(full_path_lo, self) #Lee el archivo de QtDesigner

        self.firebaseConfig = {
            "apiKey": "AIzaSyBcKaidBnSBRdPIBmFoVJsgW9Qc0PcK9xo",
            "authDomain": "login-new-17939.firebaseapp.com",
            "databaseURL": "https://login-new-17939.firebaseio.com",
            "projectId": "login-new-17939",
            "storageBucket": "login-new-17939.firebasestorage.app",
            "messagingSenderId": "884933777222",
            "appId": "1:884933777222:web:93cffbbc6a878632a3b747"
        }   
        


        self.firebase = pyrebase.initialize_app(self.firebaseConfig) #Inicializa la app. 
        self.auth = self.firebase.auth()
     

        self.bu_login.clicked.connect(self.gui_login)
        self.bu_reg.clicked.connect(self.gui_reg)


    def correcto(self, estatus):
        if estatus=="l":
            QMessageBox.information(self,'¡Login correcto!', "Acceso garantizado") 
        else:
            QMessageBox.information(self,'¡Usuario creado correctamente!', "Creación de usuario") 
        self.msg = QMessageBox(self)
        self.msg.show
        window.hide()
        w3.show() 

    def error():
        window.hide()
        w2.show() 

    def gui_reg(self):
        name = self.li_usuario.text()
        passw = self.li_contra.text()  #hashlib
        if len(name)== 0 or len(passw) == 0:
            self.la_res.setText("Ingrese todos los datos")
        else:
            # user = self.auth.create_user_with_email_and_password(name, passw)
            try:
                user = self.auth.create_user_with_email_and_password(name, passw)
                self.correcto("r")
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
            self.la_res.setText("Ingrese todos los datos")
        else:
            try:
                user = self.auth.sign_in_with_email_and_password(name, passw)
                self.correcto("l")
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
            self.la_res.setText("Ingrese todos los datos")
            
        else:
            try:
                user = self.auth.sign_in_with_email_and_password(name, passw)
                self.correcto()
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
    w3 = AcceptWindow()
    # se muestra la ventana 
    window.show()
    # se entrega el control al sistema operativo
    app.exec() 

   

    