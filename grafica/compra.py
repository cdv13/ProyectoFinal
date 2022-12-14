from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import IntVar
from tkinter import messagebox

from cargaproducto import Carga
from cuenta2 import Cuenta
from carrito import Carrito


import sys
sys.path.append('d:\\00_CURSOS\\2022_Curso_Python_SALTA\\ProyectoFinal\\clases')
from producto import Producto
from classCarrito import CarritoCompra

class Compra(tk.Frame):
    def __init__(self, root):
        self.root=root
        self.root.title("Ventana de Compra")
        #setting window size
        width=600
        height=520
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)
        
        #___________fuentes_____________________________
        font_f1=("Helvetica", 14, "bold")
        font_f2=("Helvetica",10)
        

        #____________Frame 0______________________________________
        #Crear una funcion para filtrar/Para Buscar
        #cromebook 
        
        self.frame=tk.LabelFrame(self.root, width=600, height=100, bg="bisque3")
        self.frame.pack(fill=tk.X)

        self.l1=tk.Label(self.frame, text="Super market", bg="bisque3")
        self.l1.config(font=font_f1)
        self.l1.grid(column=0, row=0,columnspan=6, sticky="nsew")

        
        #Filtro
        self.labelFiltro=tk.Label(self.frame, text="Filtro:")
        self.labelFiltro.grid(column=1, row=1,ipadx=2, ipady=2)

        self.textFiltro=tk.StringVar()
        self.filtro= ttk.Combobox(self.frame, textvariable=self.textFiltro,state="readonly", values=["None","Perfumeria", "Limpieza", "Almacen"])
        self.filtro.grid(column=2, row=1,ipadx=2, ipady=2, padx=10)
        self.filtro.bind("<<ComboboxSelected>>", self.filtroProd)

        #Busqueda x Nombre
        self.textBusqueda=tk.StringVar()
        self.busqueda=tk.Entry(self.frame, textvariable=self.textBusqueda, fg="grey")
        self.busqueda.config(font=("Helvetica",10))
        self.busqueda.grid(column=3, row=1,ipadx=2, ipady=2)

        #self.img=tk.PhotoImage('icons8-búsqueda-40.png')      
        self.botonBusqueda=tk.Button(self.frame, text="Buscar", command=self.barraBusqueda)
        self.botonBusqueda.config(font=font_f2)
        self.botonBusqueda.grid(column=4, row=1, ipadx=2, ipady=2, padx=5)

        #Ir Perfil
        self.irPerfil=tk.Button(self.frame, text="Ir a Perfil", justify="center", command=self.irPerfil)
        self.irPerfil.config(font=(font_f2))
        self.irPerfil.grid(column=5, row=1,ipadx=2, ipady=2, padx=10)

        #Ir Carrito
        self.irCarrito=tk.Button(self.frame, text="Ir a Carrito", justify="center", command=self.irCarrito)
        self.irCarrito.config(font=(font_f2))
        self.irCarrito.grid(column=6, row=1,ipadx=2, ipady=2, padx=10)
        
        
        #________________________ Frame 1________ para la tabla
        self.frame1=tk.LabelFrame(self.root, text="Productos disponibles", width=600, height=400, bg="bisque3")
        self.frame1.pack()

        self.tree = ttk.Treeview(self.frame1, height=10, columns= ("#1", "#2", "#3"))
        self.tree.place(x=0,y=0,width=575, height=365)
        self.tree.column("#0", width=50)
        self.tree.column("#1", width=90)
        self.tree.column("#2", width=150)
        self.tree.column("#3", width=80)
        #self.tree.column("#4", width=80)

        self.tree.heading("#0", text = "ID", anchor = "center")
        self.tree.heading("#1", text = "Nombre", anchor = "center")
        self.tree.heading("#2", text = "Descripcion", anchor = "center")
        self.tree.heading("#3", text = "Precio", anchor = "center")
        #self.tree.heading("#4", text = "Stock", anchor = "center")       
        
        # Agregamos dos scrollbars 
        self.vscrol=ttk.Scrollbar(self.frame1, orient="vertical", command=self.tree.yview)
        self.vscrol.place(in_=self.tree, relx=1, relheight=1, bordermode="outside")
        self.hscrol=ttk.Scrollbar(self.frame1, orient="horizontal", command=self.tree.xview)
        self.hscrol.place(in_=self.tree, rely=1, relwidth=1, bordermode="outside")
        

        self.tree.configure(xscrollcommand=self.hscrol.set, yscrollcommand=self.vscrol.set)
        
        #_____________________Frame2___________________ para las operaciones
        self.frame2=tk.LabelFrame(self.root, text="Operaciones", width=600, height=50, bg="bisque3")
        self.frame2.pack()
        
        self.contador=tk.Label(self.frame2, text="Cantidad:", font=font_f2, bg="bisque3")
        self.contador.place(x=20, y=0, width=60, height=30)
        
        # Contador productos
        #Variable de control
        self.resultado=IntVar()
        self.numero = tk.Label(self.frame2, textvariable=self.resultado)
        self.numero.place(x=130, y=0, width=20, height=30)

        self.boton_sum = tk.Button(self.frame2, text = "+",command=lambda: self.sumar(self.resultado))
        self.boton_sum.place(x=100, y=0, width=20, height=30)

        self.boton_res = tk.Button(self.frame2, text = " - ",command=lambda: self.restar(self.resultado))
        self.boton_res.place(x=160, y=0, width=20, height=30)

        #boton agregar
        self.addCarrito=tk.Button(self.frame2,text="Agregar al Carrito",command=self.agregarCarrito)
        self.addCarrito.place(x=400, y=0, width=140, height=30)

        #Funcion para q se llenen las filas de la tabla
        self.mostrarProd()
        
        self.datos=[]

    #Para q se muestren en la tabla
    def mostrarProd(self):
        #Obtener datos de la tabla y limpiar
        record=self.tree.get_children()
        for element in record:
            self.tree.delete(element)
        #Realizo la consulta en la tabla        
        p=Producto(0,"","",0,0,"")
        filas=p.mostrar()
        #Corro la tuplas
        for fila in filas:
            self.tree.insert("",tk.END,text=fila[0], values= (fila[1], fila[2], fila[3]) )

    def barraBusqueda(self):
        record=self.tree.get_children()
        for element in record:
            self.tree.delete(element)
        
        producto=self.textBusqueda.get()  
        p=Producto(0, "","",0,0,"")
        filas=p.mostrarbusqueda(producto)  
        for fila in filas:
            self.tree.insert("",tk.END,text=fila[0], values= (fila[1], fila[2], fila[3]))
        

    def agregarCarrito(self):
        #Falta el control de stock
        item=self.tree.focus()
        valores=self.tree.item(item)["values"]
        producto=self.tree.item(item)["text"] #Para que me ponga el id
        cantidad=self.resultado.get()
        subTotal=float(valores[2])*cantidad
        
        c=CarritoCompra(0,producto,cantidad,subTotal)
        c.insertarCarrito()
        cantidadProductos=c.sumaProductos()

        if cantidadProductos>=30:
            messagebox.showinfo("Supero el Limite de Compra")

    def irCarrito(self):
        v=Carrito(tk.Tk(),"Productos Seleccionados","Carrito de Compra")

    def irPerfil(self):
        v=Cuenta(tk.Tk())

    def filtroProd(self,event):
        self.selection=self.textFiltro.get()
        #Obtener datos de la tabla y limpiar
        record=self.tree.get_children()
        for element in record:
            self.tree.delete(element)
        if self.filtro.get():    
            if self.selection=="Almacen":
                #Realizo la consulta en la tabla        
                p=Producto(0,"","",0,0,"Almacen")
                filas=p.mostrarfiltrado()  
                for fila in filas:
                    self.tree.insert("",tk.END,text=fila[0], values= (fila[1], fila[2], fila[3]) )
            if self.selection=="Perfumeria":
                #Realizo la consulta en la tabla        
                p=Producto(0,"","",0,0,"Perfumeria")
                filas=p.mostrarfiltrado()  
                for fila in filas:
                    self.tree.insert("",tk.END,text=fila[0], values= (fila[1], fila[2], fila[3]) )
            if self.selection=="Limpieza":
                #Realizo la consulta en la tabla        
                p=Producto(0,"","",0,0,"Limpieza")
                filas=p.mostrarfiltrado()  
                for fila in filas:
                    self.tree.insert("",tk.END,text=fila[0], values= (fila[1], fila[2], fila[3]) )
            if self.selection=="None":
                #Realizo la consulta en la tabla        
                p=Producto(0,"","",0,0,"")
                filas=p.mostrar()  
                for fila in filas:
                    self.tree.insert("",tk.END,text=fila[0], values= (fila[1], fila[2], fila[3]) )
        else:
            self.mostrarProd()
    #Funciones para el contador
    def sumar(self,resultado):
            suma =self.resultado.get() + 1 # obtenemos el valor de la variable de control y le sumamos 1
            self.resultado.set(suma) # actualizamos la variable de control

    def restar(self,resultado):
        if self.resultado.get()>0:
            resta=self.resultado.get()-1
            self.resultado.set(resta)
        else:
            pass   


if __name__ == "__main__":
    root = tk.Tk()
    app=Compra(root)
    root.mainloop()