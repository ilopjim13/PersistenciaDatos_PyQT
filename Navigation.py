from PyQt6.QtWidgets import *
import sys
from configuracion import Configuracion
from menu import Menu
from models.cliente import Cliente


class WindowManager:
    def __init__(self):
        self.current_window = None  # Almacena la ventana actual dd

        self.ventanas = {  #aqui estara todos las ventanas que necesitaremos
            "menu": Menu(self), 
            "configuracion": Configuracion(self)
        }

        self.token = None # paco aqui quiero que me des el token y lo pases aqui

        self.usuario:Cliente = None # paco o ivan aqui teneis el usuario actual lo guardamos

    def mostrarVentana(self, nombre:str):
        if nombre not in self.ventanas:
            print(f"❌ ERROR: La ventana '{nombre}' no está registrada.")
            return

        if self.current_window:
            self.full_screen_state = self.current_window.isFullScreen()
            self.current_window.close()
        self.current_window = self.ventanas[nombre]
        if self.full_screen_state:
            self.current_window.showFullScreen()
        else:
            self.current_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    manager = WindowManager()
    manager.mostrarVentana("menu")
    sys.exit(app.exec())