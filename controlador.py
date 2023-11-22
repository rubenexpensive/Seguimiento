from modelo import basededatos
from vista import Ventanainicio
import sys
from PyQt5.QtWidgets import QApplication

class Coordinador(object):
    def __init__(self,vista,modelo):
        self.__mi_vista = vista
        self.__mi_modelo = modelo

    def validarusuario(self,l,p):
        return self.__mi_modelo.validaruser(l,p)
    
    def img_conextion(self, imagen):
        self.modelo.picture_creator(imagen)
    
    # def listfile(self,file):
    #     return self.__mi_modelo.verarchivos(file)

def main():

    app = QApplication(sys.argv)
    mi_vista = Ventanainicio()
    mi_modelo = basededatos()
    mi_coordinador = Coordinador(mi_vista, mi_modelo)
    mi_vista.setCoordinador(mi_coordinador)
    mi_vista.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()