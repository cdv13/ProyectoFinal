from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox, StringVar, DoubleVar
from datetime import date,datetime
from io import open

from cuenta2 import Cuenta
from cargaproducto import Carga
from factura import Factura
#Importacio de modulos propios de otra carpeta
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from clases.producto import Producto
from clases.detalleVenta import DetalleVenta
from clases.venta import Venta


class Carrito(tk.Frame):
    def __init__(self, root, tituloFrame,titulo, seleccionCarrito, listaProductos, cliente,correo):
        self.root=root
        self.root.title(titulo)
        #setting window size
        width=600
        height=500
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)
        self.seleccionCarrito=seleccionCarrito
        self.listaProductos=listaProductos
        self.cliente=cliente
        self.correo=correo
        

        
        font_f1=("Helvetica", 14, "bold")
        font_f2=("Helvetica",10)
        font_f3=("Helvetica",10, "bold")
        
        #____Frame 0______________________________
        self.frame=tk.LabelFrame(self.root, width=600, height=50, bg="bisque3")
        self.frame.pack(fill=tk.X)

        self.l2=tk.Label(self.frame, text=f"{self.correo}", bg="bisque3")
        self.l2.place(relx=0.1,rely=0.1)

        self.l1=tk.Label(self.frame, text="Super market", bg="bisque3")
        self.l1.config(font=font_f1)
        self.l1.place(rely=0.5, relx=0.5, anchor="center")

        #___ Frame 1__________________ para la tabla
        self.frame1=tk.LabelFrame(self.root, text=tituloFrame, width=600, height=400, bg="bisque3")
        self.frame1.pack()

        self.tree = ttk.Treeview(self.frame1, height=10, columns= ("#1", "#2", "#3","#4", "#5"))
        self.tree.place(x=0,y=0,width=575, height=365)
        self.tree.column("#0", width=50)
        self.tree.column("#1", width=90)
        self.tree.column("#2", width=150)
        self.tree.column("#3", width=80)
        self.tree.column("#4", width=80)
        self.tree.column("#5", width=80)


        self.tree.heading("#0", text = "ID", anchor = "center")
        self.tree.heading("#1", text = "Nombre", anchor = "center")
        self.tree.heading("#2", text = "Descripcion", anchor = "center")
        self.tree.heading("#3", text = "Precio", anchor = "center")
        self.tree.heading("#4", text = "Unidades", anchor = "center")
        self.tree.heading("#5", text = "SubTotal", anchor = "center")
        
        # Agregamos dos scrollbars 
        self.vscrol=ttk.Scrollbar(self.frame1, orient="vertical", command=self.tree.yview)
        self.vscrol.place(in_=self.tree, relx=1, relheight=1, bordermode="outside")
        self.hscrol=ttk.Scrollbar(self.frame1, orient="horizontal", command=self.tree.xview)
        self.hscrol.place(in_=self.tree, rely=1, relwidth=1, bordermode="outside")
        

        self.tree.configure(xscrollcommand=self.hscrol.set, yscrollcommand=self.vscrol.set)
        
        #___________________Frame2___________ para las operaciones

        self.frame2=tk.LabelFrame(self.root, text="Operaciones", width=600, height=50, bg="bisque3")
        self.frame2.pack()
        
        self.retornar=tk.Button(self.frame2,text="Continuar Comprando",command=self.returnCompra)
        self.elminar=tk.Button(self.frame2,text="Elimnar \nProducto",command=self.eliminarProducto)
        self.vaciar=tk.Button(self.frame2,text="Vaciar \nCarrito",command=self.vaciarCarrito)
        
        self.sTotal=DoubleVar(self.frame2)
        self.total=tk.Label(self.frame2, textvariable=self.sTotal, font=font_f3, bg="bisque3")
        #self.total=tk.Label(self.frame2, text=f"Total : $ {self.totalCompra()}", font=font_f3,bg="bisque3")
        
        self.confirmar=tk.Button(self.frame2,text="Confirmar Compra",command=self.confirmarCompra)
        self.retornar.place(relx=0, rely=0, width=135, height=30)
        self.elminar.place(relx=0.25, rely=0, width=70, height=30)
        self.vaciar.place(relx=0.40, rely=0, width=70, height=30)
        self.total.place(relx=0.55, rely=0, width=100, height=30)
        self.confirmar.place(relx=0.75, rely=0, width=135, height=30)

        #Funcion para q se llenen las filas de la tabla
        self.mostrarProd()
        self.sTotal.set(self.totalCompra())


    #Para q se muestren en la tabla
    def mostrarProd(self):
        #Obtener datos de la tabla y limpiar
        record=self.tree.get_children()
        for element in record:
            self.tree.delete(element)              
        
        #---Probando de cargar de la lista carrito
        filas=self.listaProductos
        for fila in filas:
            self.tree.insert("",tk.END,text=fila[0], values= (fila[1], fila[2], fila[3], fila[4],fila[5]) )
        
        
    
    def vaciarCarrito(self):
        self.listaProductos.clear()
        self.seleccionCarrito.clear()
        
        self.mostrarProd()
        #reseteo total
        self.sTotal.set(0.0)
    
    def eliminarProducto(self):
        #item=self.tree.focus()
        item=self.tree.selection()[0]
        item_id=self.tree.item(item, "text")
        #print(item_id)
        
        if item_id !="":
            indice=self.buscarIndice(item_id)
            del self.listaProductos[indice]
            del self.seleccionCarrito[indice]
            messagebox.showinfo(message= "Registro eliminado con exito")
            self.mostrarProd()
        else:
            messagebox.showinfo(message= "Debe seleccionar un Registro")
        self.mostrarProd()
        self.sTotal.set(self.totalCompra())

    def buscarIndice(self, item_id):
        id=0
        for producto in self.listaProductos:
            if producto[0]==item_id:
                return id
            id+=1

    def confirmarCompra(self):
        respuesta=messagebox.askyesno(message="¿Seguro que desea Confirmar?")
        
        if respuesta:
            #Agrego en BD VENTA
            fecha=date.today()
            fecha_str=fecha.strftime("%Y/%m/%d")
            id_cliente=self.cliente
            venta=Venta(0,fecha_str,id_cliente)
            venta.insertarVenta()
            
            #Agrego en BD DETALLE
            for fila in self.seleccionCarrito:
                detalle=DetalleVenta(0, fila.venta, fila.producto, fila.cantidad, fila.precioVenta)
                detalle.insertarDV()

            #Modifico el Stock en BD producto
            for fila in self.seleccionCarrito:
                producto=Producto(fila.producto,"","",0,fila.cantidad,"")
                producto.modificarStock()
            
            v=Factura(tk.Tk(), self.cliente,venta)


    def returnCompra(self):
        self.root.destroy()
    
    #Para calcular el total en la tabla
    def totalCompra(self):
        total=0
        for producto in self.seleccionCarrito:
            subTotal=producto.cantidad*producto.precioVenta
            total+=subTotal
        return total
        
    

'''
if __name__ == "__main__":
    root = tk.Tk()
    app=Carrito(root)
    root.mainloop()
'''