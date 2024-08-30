from entity import *
from io import open
from os.path import exists
from os import remove, rename

class ProductoFile:
    def __init__(self):
        self.__archivo = "productos.txt"
        self.__temporal = "Temporal.txt"
        if not exists(self.__archivo):
            fichero = open(self.__archivo, "w")
            fichero.close()
            print("Archivo creado con exito!")

    # Métodos para la persistencia de datos
    def adicionar(self, prod):
        fichero = None
        ok = False # Bandera
        try:
            fichero = open(self.__archivo, "a")
            codigo_generado = self.generarcodigo()  # Implementa la lógica para generar el código automáticamente
            prod.generarcodigo(codigo_generado)  # Actualizar el objeto producto con el código generado
            datos = prod.codigo + "#" + prod.nombre + "#" + prod.fecha + "#" + prod.categoria + "#" + str(prod.precio) + "#" + str(prod.cantidad) + "\n"
            prod = self.buscar(prod.codigo)
            if prod == None:
                fichero.write(datos)
            else:
                ok = True
        except IOError as e:
            print("Error:", e)
        finally:
            fichero.close()
        return ok

    # Método para generar código automáticamente
    codigo_actual = 0
    def generarcodigo(self):
        productos = self.listar()
        if productos:
            codigos = [int(producto['codigo'][1:]) for producto in productos if producto['codigo'][1:].isdigit()]
            codigo_actual = max(codigos) if codigos else 0
        else:
            codigo_actual = 0
        return f"P{codigo_actual + 1:03d}"  # Formato P001, P002, P003, ...

    def actualizar(self, prod, id):
        fuente = None
        destino = None
        try:
            fuente = open(self.__archivo, "r", encoding="utf8")
            destino = open(self.__temporal, "w", encoding="utf8")
            lineas = fuente.readlines()
            separador = "#"
            for linea in lineas:
                dato = linea.split(separador)
                if dato[0] == id:
                    datos = id + "#" + prod.nombre + "#" + prod.fecha + "#" + prod.categoria + "#" + str(prod.precio) + "#" + str(prod.cantidad) + "\n"
                    destino.write(datos)
                else:
                    destino.write(linea)
        except IOError as e:
            print("Error: ", e)
        finally:
            fuente.close()
            destino.close()
        remove(self.__archivo)
        rename(self.__temporal, self.__archivo)

    def actualizar(self, prod, id):
        fuente = None
        destino = None
        ok = 'F'  # Bandera para verificar si se actualizó algún producto
        try:
            fuente = open(self.__archivo, "r", encoding="utf8")
            destino = open(self.__temporal, "w", encoding="utf8")
            lineas = fuente.readlines()
            separador = "#"
            for linea in lineas:
                dato = linea.split(separador)
                if dato[0] == id:
                    datos = id + "#" + prod.nombre + "#" + prod.fecha + "#" + prod.categoria + "#" + str(prod.precio) + "#" + str(prod.cantidad) + "\n"
                    if linea == datos:
                        destino.write(linea)
                        ok = 'S' # Si no se ha encontrado algun cambio
                    else:
                        destino.write(datos)
                        ok = 'T'  # Si existe algun cambio
                else:
                    destino.write(linea)
        except IOError as e:
            print("Error: ", e)
        finally:
            fuente.close()
            destino.close()
        remove(self.__archivo)
        rename(self.__temporal, self.__archivo)
        return ok  # Devuelve T si se actualizó, S si no hubo cambios, F si no existe
                 
    def eliminar(self, id):
        fuente = None
        destino = None
        ok = False  # Bandera para verificar si se eliminó algún producto
        try:
            fuente = open(self.__archivo, "r", encoding="utf8")
            destino = open(self.__temporal, "w", encoding="utf8")
            lineas = fuente.readlines()
            separador = "#"
            for linea in lineas:
                dato = linea.split(separador)
                if dato[0] == id:
                    ok = True  # Se encontró el id, se marca como eliminado
                else:
                    destino.write(linea)
        except IOError as e:
            print("Error: ", e)
        finally:
            fuente.close()
            destino.close()
        remove(self.__archivo)
        rename(self.__temporal, self.__archivo)
        return ok  # Devuelve True si se eliminó, False si no se encontró el id

    def listar(self):
        fichero = None
        productos = []
        try:
            fichero = open(self.__archivo, "r", encoding="utf8")
            lineas = fichero.readlines()
            for linea in lineas:
                dato = linea.replace("\n", "").split("#")
                producto = {"codigo": dato[0], "nombre": dato[1], "fecha": dato[2], "categoria": dato[3], "precio": dato[4], "cantidad": dato[5]}
                productos.append(producto)
        except IOError as e:
            print("Error: ", e)
        finally:
            fichero.close()
        return productos

    def buscar(self, id):
        fichero = None
        producto = None
        try:
            fichero = open(self.__archivo, "r", encoding="utf8")
            lineas = fichero.readlines()
            separador = "#"
            for linea in lineas:
                dato = linea.split(separador)
                cod = dato[0]
                if cod == id:
                    producto = dato
                    break
        except IOError as e:
            print("Error: ", e)
        finally:
            fichero.close()
        return producto
