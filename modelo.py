import pydicom 
from PyQt5.QtCore import QObject
import matplotlib.pyplot as plt
import numpy as np
import os
import cv2

class basededatos(QObject):
    def __init__(self):
        super().__init__()
        self.__login = 'medicoAnalitico' 
        self.__password = 'bio12345'  
        self.__carpeta = ""

    def validaruser(self, l, p):
        return self.__login == l and self.__password == p

    def get_path(self, f):
        self.__carpeta = f

    def picture_creator(self, imagen):
        ds = pydicom.dcmread(self.__carpeta+'/'+imagen)
        pixel_data = ds.pixel_array

        if len(pixel_data.shape) == 3:
            slice_index = pixel_data.shape[0] // 2
            selected_slice = pixel_data[slice_index, :, :]
            plt.imshow(selected_slice, cmap=plt.cm.bone)
        else:

            plt.imshow(pixel_data, cmap=plt.cm.bone)

        plt.axis('off')
        plt.savefig("temp_image.png")
    
