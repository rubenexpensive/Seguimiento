import sys
import os
from modelo import basededatos
from PyQt5.QtWidgets import QApplication,QMainWindow, QDialog,QMessageBox, QFileDialog, QSlider
from PyQt5.QtGui import QDoubleValidator, QRegExpValidator,QIntValidator
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Ventanainicio(QMainWindow):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("inicio.ui",self)
        self.setup()
    
    def setup(self):
        self.campo_user.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.campo_password.setValidator(QRegExpValidator(QRegExp("[a-zA-Z0-9 ]+")))
        self.ingresar.clicked.connect(self.validardatos)

    def setCoordinador(self,c):
        self.__coordinador = c
    
    def validardatos(self):
        username = self.campo_user.text()
        password = self.campo_password.text()
        verificar = self.__coordinador.validarusuario(username,password)

        if verificar:
            
            self.hide()
            nueva_ventana = Vista()
            nueva_ventana.show()

        else:
            QMessageBox.warning(self, "Error de inicio de sesión", "Usuario o contraseña incorrectos.")
    


# class MyGraphCanvas(FigureCanvas):
#     def __init__(self, parent= None,width=5, height=4, dpi=100):
        
#         self.fig = Figure(figsize=(width, height), dpi=dpi)
#         self.axes = self.fig.add_subplot(111)        
#         FigureCanvas.__init__(self,self.fig)
    
#     def graficar_imagen(self, datos):
#         self.axes.clear()
#         self.axes.imshow(datos)
#         self.axes.figure.canvas.draw()

class Vista(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('ventana_img.ui', self)
        self.setup()
    
    def setup(self):
        self.comboBox.currentIndexChanged.connect(self.load)
        self.abrir.clicked.connect(self.load)
        self.carpeta = 'imagenes'
        lista_archivos = os.listdir(self.carpeta)   
        # self.verticalSlider = QSlider(self)
        # self.verticalSlider.valueChanged.connect(self.load)
        # self.current_index = self.slider.value() - 1
        # for archivo in lista_archivos:
        #     self.comboBox.addItem(archivo)

    def setCoordinador(self,c):
        self.__coordinador2 = c
    
    def load(self):
        archivo_cargado, _ = QFileDialog.getOpenFileName(self, "Abrir señal", "", "Todos los archivos (*);;Archivos mat (*.dcm)")
        if archivo_cargado != '':
            imagen = self.comboBox.currentText()
            imagen_cargada = self._Vista__coordinador2.img_conextion(imagen)

            # Update the slider's maximum value
            self.verticalSlider.setMaximum(len(os.listdir(self.carpeta)))

            # Display the selected image
            pixmap = QPixmap("temp_image.png")
            pixmap.fromImage(imagen_cargada)
            pixmap = pixmap.scaledToWidth(self.img.width())
            self.img.setPixmap(pixmap)
            os.remove('temp_image.png')

            # Update the slider's value based on the selected image index
            image_index = os.listdir(self.carpeta).index(imagen)
            self.verticalSlider.setValue(image_index + 1)
        else:
            QMessageBox.warning(self, "No exites el archivo")