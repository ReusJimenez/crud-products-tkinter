from model import *
from entity import *
from util import *

class ProductoController:
    def __init__(self):
        self.__obj = ProductoFile()

    def listaProductos(self):
        return self.__obj.listar()

    def buscarProducto(self, id):
        return self.__obj.buscar(id)

    def procesarProducto(self, prod, opcion, id=None):
        self.__msg = None
        
        if opcion == ADD:
            ok = self.__obj.adicionar(prod)
            if ok == False:
                self.__msg = "Producto registrado con éxito!"
            else:
                self.__msg = "Código de Producto ya existe..."
        elif opcion == UPD:
            ok = self.__obj.actualizar(prod, id)
            if ok == 'S':
                self.__msg = f"No ha ingresado cambios para el Producto {id}"
            elif ok == 'T':
                self.__msg = "Producto actualizado con éxito!"            
            else:
                self.__msg = "Código de Producto no existe..."
        elif opcion == DEL:
            if id is None or id.strip() == "":
                self.__msg = "El campo Codigo está vacío..."
            else:
                ok = self.__obj.eliminar(id)
                if ok == True:
                    self.__msg = "Producto eliminado con éxito!"
                else:
                    self.__msg = "Código de Producto no existe..."
        return self.__msg
