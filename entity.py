class Producto:
    def __init__(self, nombre, fecha, categoria, precio, cantidad):
        self.__codigo = None  # El código se generará automáticamente
        self.__nombre = nombre
        self.__fecha = fecha
        self.__categoria = categoria
        self.__precio = precio
        self.__cantidad = cantidad

    # definir propiedades de lectura
    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def fecha(self):
        return self.__fecha

    @property
    def categoria(self):
        return self.__categoria

    @property
    def precio(self):
        return self.__precio
    
    @property
    def cantidad(self):
        return self.__cantidad

    # propiedades de asignacion
    def generarcodigo(self, codigo): # Método para asignar el código automáticamente
        self.__codigo = codigo

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha

    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria
    
    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad
