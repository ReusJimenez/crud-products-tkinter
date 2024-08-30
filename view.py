import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox
from datetime import date
from controller import *
from entity import *
from tkinter import PhotoImage
import os

class Application:
    def __init__(self):
        self.ventana = tk.Tk()
        self.obj = ProductoController()

        # Variables
        self.vCodigo = tk.StringVar()
        self.vNombre = tk.StringVar()
        self.vFecha = tk.StringVar()
        self.vCategoria = tk.StringVar()
        self.vPrecio = tk.StringVar()
        self.vCantidad = tk.StringVar()
        self.vFecha.set(date.today().strftime("%d/%m/%Y"))

        # VENTANA
        self.ventana.title(":: MANTENIMIENTO DE PRODUCTOS ::")
        self.ventana.geometry("525x625")
        self.ventana.iconbitmap("logo.ico")
        self.ventana.configure(background="white")
        self.ventana.resizable(False, False)

        # TITULO
        self.label1 = tk.Label(text="CRUD DE PRODUCTOS", bg="white", fg="orange", font=("Arial", 16, "bold")).place(x=160, y=5)

        # ETIQUETA Y TEXBOX
        self.label2 = tk.Label(text="Código", bg="white", fg="orange", font=("Arial", 12, "bold")).place(x=110, y=50)
        self.txtbox1 = tk.Entry(self.ventana, textvariable=self.vCodigo, width=10, borderwidth=2)
        self.txtbox1.place(x=215, y=50)
        self.txtbox1.focus_set()

        self.label3 = tk.Label(text="Nombre", bg="white", fg="orange", font=("Arial", 12, "bold")).place(x=110, y=80)
        self.txtbox2 = tk.Entry(textvariable=self.vNombre, width=30, borderwidth=2).place(x=215, y=80)

        self.label4 = tk.Label(text="Fecha", bg="white", fg="orange", font=("Arial", 12, "bold")).place(x=110, y=110)
        self.txtbox3 = tk.Entry(textvariable=self.vFecha, state="disable", width=10, borderwidth=2).place(x=215, y=110)

        self.label5 = tk.Label(text="Categoría", bg="white", fg="orange", font=("Arial", 12, "bold")).place(x=110, y=140)
        self.txtbox4 = tk.Entry(textvariable=self.vCategoria, width=30, borderwidth=2).place(x=215, y=140)

        self.label6 = tk.Label(text="Precio", bg="white", fg="orange", font=("Arial", 12, "bold")).place(x=110, y=170)
        self.txtbox5 = tk.Entry(textvariable=self.vPrecio, width=10, borderwidth=2).place(x=215, y=170)

        self.label7 = tk.Label(text="Cantidad", bg="white", fg="orange", font=("Arial", 12, "bold")).place(x=110, y=200)
        self.txtbox6 = tk.Entry(textvariable=self.vCantidad, width=10, borderwidth=2).place(x=215, y=200)     
        
        # BOTONES
        img_path = os.path.abspath("lupa_buscar.png")
        photo = PhotoImage(file=img_path)
        self.btn6 = tk.Button(image=photo,command=self.buscar,width=30,height=30).place(x=300,y=40) #boton Buscar
        self.btn1 = tk.Button(text="GUARDAR",command=self.insertardatos,width=10, font=("Arial", 10, "bold")).place(x=40,y=240) #boton Guardar
        self.btn2 = tk.Button(text="ACTUALIZAR", command=self.actualizar,width=10, font=("Arial", 10, "bold")).place(x=130,y=240) #boton Actualizar
        self.btn3 = tk.Button(text="ELIMINAR", command=self.eliminar,width=10, font=("Arial", 10, "bold")).place(x=220,y=240) #boton Eliminar
        self.btn4 = tk.Button(text="LISTAR", command=self.listardatos,width=10, font=("Arial", 10, "bold")).place(x=310,y=240) #boton Listar
        self.btn5 = tk.Button(text="LIMPIAR", command=self.limpiardatos,width=10, font=("Arial", 10, "bold")).place(x=400,y=240) #boton Limpiar

        # Frame
        self.tree_frame = tk.Frame(self.ventana)
        self.tree_frame.config(height=5)
        self.tree_frame.pack(side=BOTTOM, pady=10)
        
        # TABLA
        self.tv = ttk.Treeview(self.tree_frame, selectmode='browse')
        self.tv['columns'] = ('Codigo', 'Nombre', 'Fecha', 'Categoria', 'Precio', 'Cantidad')
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.column('Codigo', anchor=CENTER, width=60, minwidth=60)
        self.tv.column('Nombre', anchor=tk.W, width=100, minwidth=100)
        self.tv.column('Fecha', anchor=tk.W, width=70, minwidth=70)
        self.tv.column('Categoria', anchor=tk.W, width=110, minwidth=110)
        self.tv.column('Precio', anchor=tk.W, width=60, minwidth=60)
        self.tv.column('Cantidad', anchor=tk.W, width=60, minwidth=60)
        
        vsb = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tv.yview)
        vsb.pack(side='right', fill='y')
        self.tv.configure(yscrollcommand=vsb.set)
        self.tv.config(height=15) 

        self.tv.heading('#0', text='', anchor=CENTER)
        self.tv.heading('Codigo', text='Código', anchor=CENTER)
        self.tv.heading('Nombre', text='Nombre', anchor=CENTER)
        self.tv.heading('Fecha', text='Fecha', anchor=CENTER)
        self.tv.heading('Categoria', text='Categoría', anchor=CENTER)
        self.tv.heading('Precio', text='Precio', anchor=CENTER)
        self.tv.heading('Cantidad', text='Cantidad', anchor=CENTER)
        self.tv.pack(side=BOTTOM)

        self.listardatos()
        self.ventana.mainloop()

    # Metodos
    def insertardatos(self):
        prod = Producto(self.vNombre.get(), self.vFecha.get(), self.vCategoria.get(), float(self.vPrecio.get()), int(self.vCantidad.get()))
        msg = self.obj.procesarProducto(prod, 1)
        tkinter.messagebox.showinfo("INFORMACION", msg)
        self.limpiardatos()
        self.listardatos()

    def listardatos(self):
        self.limpiartabla()
        productos = self.obj.listaProductos()
        for p in productos:
            self.tv.insert('', 'end', values=(p['codigo'], p['nombre'], p['fecha'], p['categoria'], p['precio'], p['cantidad']))
    
    def actualizar(self):
        id = self.vCodigo.get()
        prod = Producto(self.vNombre.get(), self.vFecha.get(), self.vCategoria.get(), float(self.vPrecio.get()), int(self.vCantidad.get()))
        msg = self.obj.procesarProducto(prod, 2, id)
        tkinter.messagebox.showinfo("INFORMACION", msg)
        self.limpiardatos()
        self.listardatos()

    def limpiardatos(self):
        self.vCodigo.set("")
        self.vNombre.set("")
        self.vCategoria.set("")
        self.vPrecio.set("")
        self.vCantidad.set("")
        self.limpiartabla()
    
    def limpiartabla(self): 
        for i in self.tv.get_children():
            self.tv.delete(i)
    
    def eliminar(self):
        id = self.vCodigo.get()
        prod = Producto("", "", "", "", "")
        msg = self.obj.procesarProducto(prod, 3, id)
        tkinter.messagebox.showinfo("INFORMACION", msg)
        self.limpiardatos()
        self.listardatos()
    
    def buscar(self):
        id = self.vCodigo.get()
        producto = self.obj.buscarProducto(id)
        if producto != None:
            self.vCodigo.set(producto[0])
            self.vNombre.set(producto[1])
            self.vFecha.set(producto[2])
            self.vCategoria.set(producto[3])
            self.vPrecio.set(producto[4])
            self.vCantidad.set(producto[5])
        else:
            tkinter.messagebox.showwarning("ALERTA", "El producto que está buscando no existe!")
            self.limpiardatos()

# prueba de ventana
x = Application()
