from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import IntVar, messagebox, StringVar

from cuenta2 import Cuenta
from carrito import Carrito
from cargaproducto import Carga

#Importacio de modulos propios
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from clases.producto import Producto
from clases.detalleVenta import DetalleVenta
from clases.venta import Venta
from clases.cliente import Cliente

class Compra(tk.Frame):
    def __init__(self, root,cliente,correo):
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
        self.cliente=cliente
        self.correo=correo
        

        #___________fuentes_____________________________
        font_f1=("Helvetica", 14, "bold")
        font_f2=("Helvetica",10)
        

        #____________Frame 0______________________________________
        #Crear una funcion para filtrar/Para Buscar
        #cromebook 
        
        self.frame=tk.LabelFrame(self.root, width=600, height=100, bg="bisque3")
        self.frame.pack(fill=tk.X)

        self.l2=tk.Label(self.frame, text=f"{self.correo}", bg="bisque3")
        self.l2.grid(column=1, row=0)

        self.l1=tk.Label(self.frame, text="Super market", bg="bisque3")
        self.l1.config(font=font_f1)
        self.l1.grid(column=2, row=0,columnspan=4, sticky="nsew")

        #Filtro
        self.labelFiltro=tk.Label(self.frame, text="Filtro:")
        self.labelFiltro.grid(column=0, row=1,ipadx=2, ipady=2)

        self.textFiltro=StringVar(self.frame)
        self.filtro= ttk.Combobox(self.frame, textvariable=self.textFiltro,state="readonly", values=["Todo","Perfumeria", "Limpieza", "Almacen"])
        self.filtro.grid(column=1, row=1,ipadx=2, ipady=2, padx=5)
        self.filtro.bind("<<ComboboxSelected>>", self.filtroProd)

        #Busqueda x Nombre
        self.textBusqueda=StringVar(self.frame,value="Busqueda por nombre..")
        self.busqueda=tk.Entry(self.frame, textvariable=self.textBusqueda, fg="grey")
        self.busqueda.config(font=("Helvetica",10))
        self.busqueda.grid(column=2, row=1,ipadx=2, ipady=2)

        #self.img=tk.PhotoImage('icons8-búsqueda-40.png')      
        self.botonBusqueda=tk.Button(self.frame, text="Buscar", command=self.buscar)
        self.botonBusqueda.config(font=font_f2)
        self.botonBusqueda.grid(column=3, row=1, ipadx=2, ipady=2, padx=5)

        #Ir Perfil
        self.irPerfil=tk.Button(self.frame, text="Ir a Perfil", justify="center", command=self.irPerfil)
        self.irPerfil.config(font=(font_f2))
        self.irPerfil.grid(column=4, row=1,ipadx=2, ipady=2, padx=5)

        #Ir Carrito
        self.irCarrito=tk.Button(self.frame, text="Ir a Carrito", justify="center", command=self.irCarrito)
        self.irCarrito.config(font=(font_f2))
        self.irCarrito.grid(column=5, row=1,ipadx=2, ipady=2, padx=5)
        
        
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
        self.varContador=IntVar(self.frame2)
        self.contador=tk.Spinbox(self.frame2,from_=1,to=30,textvariable=self.varContador)
        self.contador.place(x=100, y=0, width=70, height=30)

        #boton agregar
        self.addCarrito=tk.Button(self.frame2,text="Agregar al Carrito", command=self.agregarCarrito)
        self.addCarrito.place(x=400, y=0, width=140, height=30)

        #Funcion para q se llenen las filas de la tabla
        self.mostrarProd()
        
        self.datos=[]
        self.seleccionCarrito=[]
        venta=Venta(0,"",0)
        self.id_venta=venta.consultaUltimaVenta()
        self.listaProductos=[]
        
        
        

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

    def buscar(self):
        record=self.tree.get_children()
        for element in record:
            self.tree.delete(element)
        
        producto=self.textBusqueda.get()  
        p=Producto(0, "","",0,0,"")
        filas=p.mostrarbusqueda(producto)  
        for fila in filas:
            self.tree.insert("",tk.END,text=fila[0], values= (fila[1], fila[2], fila[3]))
        
    
    def agregarCarrito(self):
        #Falta Control de STOCK
        item=self.tree.focus()
        valores=self.tree.item(item)["values"]
        producto=self.tree.item(item)["text"] #Para que me ponga el id
        cantidad=self.varContador.get()
        #print(cantidad)
        
        #Valido el stock antes de agregar
        #self.validarstock()

        #crear una lista para mostrar en Carrito....
        self.listaProductos.append([producto,valores[0], valores[1], valores[2], cantidad, cantidad*float(valores[2])])
        
        #Creo un objeto de clase detalle Venta, sin agregar a BD
        self.detalleCarrito=DetalleVenta(0,self.id_venta,producto,cantidad, float(valores[2]))
        self.seleccionCarrito.append(self.detalleCarrito)

        #Calculo de cantidad de productos agregados al carrito
        self.cantidadProductos=0
        for seleccion in self.seleccionCarrito:
            self.cantidadProductos+=seleccion.cantidad
        
        #reseteo contador
        self.varContador.set(1)
        
        #Valido la cantidad de productos
        self.validarcantidad()   

    '''
    def validarstock(self):
        if fila[4]>listaProductos[4]:
            messagebox.showinfo(message="No hay Stock Suficiente, merme la cantidad")
        elif fila[4]==0:
            messagebox.showinfo(message="No Hay Stock Disponible")
    '''    

        
    def validarcantidad(self):
        if self.cantidadProductos>30:
            messagebox.showinfo( message="Supero el Limite de Compra (¡MAX 30 productos!)")
            self.addCarrito.config(state="disabled") #Dehabilito Boton cuando supera los 30
            self.seleccionCarrito.pop() #Elimina el ultimo prod agregado que supera la cantidad en objeto Detalle venta
            self.listaProductos.pop() ##Elimina el ultimo prod agregado que supera la cantidad en lista p mostrar

    def irCarrito(self):
        v=Carrito(tk.Tk(),"Productos Seleccionados","Carrito de Compra", self.seleccionCarrito, self.listaProductos, self.cliente, self.correo)

    def irPerfil(self):
        v=Cuenta(tk.Tk(),self.cliente, self.correo)

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
            if self.selection=="Todo":
                #Realizo la consulta en la tabla        
                p=Producto(0,"","",0,0,"")
                filas=p.mostrar()  
                for fila in filas:
                    self.tree.insert("",tk.END,text=fila[0], values= (fila[1], fila[2], fila[3]) )
        else:
            self.mostrarProd()  

'''
if __name__ == "__main__":
    root = tk.Tk()
    cliente=Cliente(0,"","",0,"")
    app=Compra(root, cliente)
    root.mainloop()
'''