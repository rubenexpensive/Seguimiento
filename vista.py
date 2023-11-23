import sys
import os
from PyQt5.QtWidgets import QApplication,QMainWindow, QDialog,QMessageBox, QFileDialog, QLineEdit
from PyQt5.QtGui import  QRegExpValidator
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.uic import loadUi


class Ventanainicio(QMainWindow):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("inicio.ui",self)
        self.setup()
    
    def setup(self):
        self.campo_user.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.campo_password.setValidator(QRegExpValidator(QRegExp("[a-zA-Z0-9 ]+")))
        self.campo_password.setEchoMode(QLineEdit.Password)
        self.buttonBox.accepted.connect(self.validardatos) 
        self.buttonBox.rejected.connect(self.closeOption)

    def setCoordinador(self,c):
        self.__coordinador = c
    
    def validardatos(self):
        username = self.campo_user.text()
        password = self.campo_password.text()
        verificar = self.__coordinador.validarusuario(username,password)

        if verificar:
            
            self.hide()
            self.newWindow = Vista()
            self.newWindow.setCoordinador(self.__coordinador)
            self.newWindow.show()

        else:
            QMessageBox.warning(self, "Error de inicio de sesión", "Usuario o contraseña incorrectos.")
    
    def closeOption(self):
        self.close()
class Vista(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("ventana_img2.ui", self)
        self.setup()

    def setup(self):
        self.abrir.clicked.connect(self.load)
        self.close.clicked.connect(self.closeWindow)
        self.comboBox.currentIndexChanged.connect(self.cargar)

        self.verticalSlider.valueChanged.connect(self.sliderValueChanged)
        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setSingleStep(1)
        self.verticalSlider.setValue(0)

    def setCoordinador(self, c):
        self.__coordinador2 = c

    def load(self):
        if self.sender() == self.abrir:
            carpeta = QFileDialog.getExistingDirectory(self, "Abrir carpeta", "", options=QFileDialog.ShowDirsOnly)
            if carpeta:
                self.__coordinador2.get_file(carpeta)
                lista_archivos = [archivo for archivo in os.listdir(carpeta) if archivo.lower().endswith(".dcm")]
                self.comboBox.clear()
                self.comboBox.addItems(lista_archivos)
                self.verticalSlider.setMaximum(len(lista_archivos) - 1)

                if lista_archivos:
                    imagen = self.comboBox.currentText()
                    self.__coordinador2.img_conextion(imagen)
                    self.mostrar_imagen_seleccionada()

    def mostrar_imagen_seleccionada(self):
        current_index = self.verticalSlider.value()
        if 0 <= current_index < self.comboBox.count():
            imagen = self.comboBox.itemText(current_index)
            self.__coordinador2.img_conextion(imagen)
            pixmap = QPixmap("temp_image.png").scaled(self.label.size(), Qt.KeepAspectRatio)
            self.label.setPixmap(pixmap)
            os.remove("temp_image.png")

    def cargar(self):
        imagen = self.comboBox.currentText()
        self.__coordinador2.img_conextion(imagen)
        pixmap = QPixmap("temp_image.png")
        self.label.setPixmap(pixmap)
        os.remove("temp_image.png")

    def sliderValueChanged(self, value):
        self.comboBox.setCurrentIndex(value)

    def closeWindow(self):
        self.hide()
        self.lastWindow = Ventanainicio()
        self.lastWindow.setCoordinador(self.__coordinador2)
        self.lastWindow.show()


