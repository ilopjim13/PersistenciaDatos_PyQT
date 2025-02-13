# -*- coding: utf-8 -*-
"""
Ejemplo de ventana básico de Login

"""
#importamos las librerías necesarias
import sys
from PyQt6.QtWidgets import * # Librerías de los componentes
from PyQt6 import uic  # Librería para trabajar con el archivo de la interfaz

#Carga la interfaz gráfica y conecta los botones
class AcceptWindow(QMainWindow):

    def __init__(self):
    #Inicializa la ventana
        super().__init__() # Reservamos un espacio en memoria para la clase
        path = "C:/Users/usuario/VSPython/8-login/"
        file_accept = "accept.ui"
        full_path_accept = path + file_accept
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
        path = "C:/Users/usuario/VSPython/8-login/"
        file_err = "error.ui"
        full_path_err = path + file_err
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
      
    
        path = "C:/Users/usuario/VSPython/8-login/"
        file_log = "login.ui"
        full_path_lo = path + file_log

        login = uic.loadUi(full_path_lo, self) #Lee el archivo de QtDesigner

     

        self.buaceptar.clicked.connect(self.gui_login)

    def correcto(self):
        QMessageBox.information(self,'¡Login correcto!', "Acceso garantizado") 
        self.msg = QMessageBox(self)
        self.msg.show
        window.hide()
        w3.show() 

    def error():
        window.hide()
        w2.show() 


    def gui_login(self):
        name = self.li_usuario.text()
        passw = self.li_contra.text()
        if len(name)== 0 or len(passw) == 0:
            self.la_res.setText("Ingrese todos los datos")
        elif name =="1234" and passw == "1234":
            self.correcto()
        else:
            self.error()  




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

   

    