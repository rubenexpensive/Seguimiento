import pydicom 
import matplotlib.pyplot as plt
import numpy as np
import os
import cv2

class basededatos():
    def __init__(self) :
        self.__login = ' ' #medicoAnalitico
        self.__password = ' ' #bio12345
    
    def validaruser(self,l,p):
        return(self.__login == l) and (self.__password == p)
    
class img():
    def __init__(self):
        self.__archivos = []
    
    def verarchivos(self):
        return self.__archivos

    # def loadDCMI(self,file,ruta):
    #     for i in range(len(file)):
    #         corte = pydicom.read_file(f'{ruta}/{file[i]}')
    #         self.__archivos.append(corte)

    def picture_creator(self, imagen):
        ds = pydicom.dcmread(self.carpeta+'/'+imagen)
        pixel_data = ds.pixel_array
        if (len(pixel_data.shape))==3:
            slice_index = pixel_data.shape[0] // 2
            selected_slice = pixel_data[slice_index, :, :]
            plt.imshow(selected_slice, cmap=plt.cm.bone)
        else:
            plt.imshow(imagen, cmap = plt.cm.bone)
        plt.axis('off')
        plt.savefig("temp_image.png")

