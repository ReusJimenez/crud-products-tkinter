from controller import *
from entity import *

class Prueba:
    prod = Producto("mouse", "14/12/2023", "tecnologia", 99.99, 1)
    obj = ProductoController()
    
    msg = obj.procesarProducto(prod, 1)
    print(msg)
    lista = obj.listaProductos()
    print(lista)
    producto = obj.buscarProducto(prod.codigo)
    print(producto)

# prueba de la clase prueba
p = Prueba()
