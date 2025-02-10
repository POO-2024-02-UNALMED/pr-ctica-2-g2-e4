import os
import pickle

class Persistencia:
    DIRECTORIO_TEMP = "temp/"

    @staticmethod
    def crear_directorio():
        if not os.path.exists(Persistencia.DIRECTORIO_TEMP):
            os.makedirs(Persistencia.DIRECTORIO_TEMP)

    @staticmethod
    def guardar_objeto(objeto, nombre_archivo):
        Persistencia.crear_directorio()
        with open(Persistencia.DIRECTORIO_TEMP + nombre_archivo, 'wb') as f:
            pickle.dump(objeto, f)

    @staticmethod
    def cargar_objeto(nombre_archivo):
        with open(Persistencia.DIRECTORIO_TEMP + nombre_archivo, 'rb') as f:
            return pickle.load(f)

    @staticmethod
    def guardar_lista(lista, nombre_archivo):
        Persistencia.guardar_objeto(lista, nombre_archivo)

    @staticmethod
    def cargar_lista(nombre_archivo):
        return Persistencia.cargar_objeto(nombre_archivo)
    