from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox, StringVar, DoubleVar
from datetime import date,datetime
from io import open

from cuenta2 import Cuenta
from cargaproducto import Carga

#Importacio de modulos propios de otra carpeta
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from clases.producto import Producto
from clases.detalleVenta import DetalleVenta
from clases.venta import Venta
from clases.cliente import Cliente


class Factura(tk.Toplevel):
    def __init__(self, root, cliente, venta):
        self.root=root
        self.root.title("Comprobante Compra")
        #setting window size
        width=600
        height=450
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=True, height=True)
        self.cliente=cliente
        self.venta=venta
        
        
        #Formato Texto
        font_f1=("Helvetica", 14, "bold")
        font_f2=("Helvetica",10)
        font_f3=("Helvetica",10, "bold")
        
        #____Frame 0____________________ENCABEZADO
        self.frame=tk.LabelFrame(self.root, width=600, height=100)
        self.frame.pack(fill=tk.X)

        self.l1=tk.Label(self.frame, text="Super market", bg="bisque3")
        self.l1.config(font=font_f1)
        self.l1.place(relx=0.5,rely=0.1, anchor="center")

        self.sNombre=StringVar(self.frame)
        self.sIdVenta=StringVar(self.frame)
        self.sFecha=StringVar(self.frame)

        self.l2=tk.Label(self.frame, text="Cliente: ", font=font_f2 )
        self.e2=tk.Entry(self.frame, textvariable=self.sNombre)
        self.l3=tk.Label(self.frame, text="Factura N°: ",font=font_f2)
        self.e3=tk.Entry(self.frame, textvariable=self.sIdVenta)
        self.l4=tk.Label(self.frame, text="Fecha: ", font=font_f2)
        self.e4=tk.Entry(self.frame, textvariable=self.sFecha)
        self.l2.place(relx=0, rely=0.3)
        self.e2.place(relx=0.15, rely=0.3)
        self.l3.place(relx=0, rely=0.7)
        self.e3.place(relx=0.15, rely=0.7)
        self.l4.place(relx=0.6, rely=0.7)
        self.e4.place(relx=0.7, rely=0.7)

        #___ Frame 1__________________DETALLE
        self.frame1=tk.LabelFrame(self.root, width=600, height=300)
        self.frame1.pack(fill=tk.X)

        self.tree = ttk.Treeview(self.frame1, height=10, columns= ("#1", "#2", "#3"))
        self.tree.place(x=0,y=0,width=575, height=280)
        self.tree.column("#0", width=50)
        self.tree.column("#1", width=90)
        self.tree.column("#2", width=150)
        self.tree.column("#3", width=80)
        
        
        self.tree.heading("#0", text = "Descripcion", anchor = "center")
        self.tree.heading("#1", text = "Cantidad", anchor = "center")
        self.tree.heading("#2", text = "Precio", anchor = "center")
        self.tree.heading("#3", text = "SubTotal", anchor = "center")
        
        
        # Agregamos dos scrollbars 
        self.vscrol=ttk.Scrollbar(self.frame1, orient="vertical", command=self.tree.yview)
        self.vscrol.place(in_=self.tree, relx=1, relheight=1, bordermode="outside")
        self.hscrol=ttk.Scrollbar(self.frame1, orient="horizontal", command=self.tree.xview)
        self.hscrol.place(in_=self.tree, rely=1, relwidth=1, bordermode="outside")
        

        self.tree.configure(xscrollcommand=self.hscrol.set, yscrollcommand=self.vscrol.set)
        
        #___________________Frame2______________TOTAL

        self.frame2=tk.LabelFrame(self.root, width=600, height=100)
        self.frame2.pack(fill=tk.X)
        
        self.sTotal=DoubleVar(self.frame2)
        self.total=tk.Label(self.frame2, text="Total : ", font=font_f3,)
        self.pesos=tk.Label(self.frame2, text="Pesos $ ")
        self.totalEntry=tk.Entry(self.frame2, textvariable=self.sTotal)
        self.generar=tk.Button(self.frame2,text="Generar",command=self.generar)
        self.total.place(relx=0.1, rely=0)
        self.pesos.place(relx=0.7, rely=0)
        self.totalEntry.place(relx=0.8, rely=0)
        self.generar.place(relx=0.4, rely=0.3)
        

        #Funcion para q se llenen las filas de la tabla
        self.mostrarProd()
        self.sTotal.set(self.mostrarTotal())
        

    #Para q se muestren en la tabla
    def mostrarProd(self):
        #Obtener datos de la tabla y limpiar
        record=self.tree.get_children()
        for element in record:
            self.tree.delete(element)              
        #---Probando de cargar de la lista detalleVenta
        filas=self.venta.consutaFactura()
        
        self.carro=[]
        for fila in filas[:]:
            self.tree.insert("",tk.END,text=fila[0], values= (fila[1], fila[2], fila[3]))
            producto=[fila[0],fila[1], fila[2], fila[3]]
            self.carro.append(producto)
            

        self.sFecha.set(filas[0][5])
        self.sNombre.set(filas[0][6])
        self.sIdVenta.set(filas[0][4])

    def mostrarTotal(self):
        total=self.venta.calculoTotal()
        return total

    def generar(self):
        respuesta=messagebox.askyesno(message="¿Desea imprimir su comprobante?")
        if respuesta:
            self.imprimir()
        else:
            v=Cuenta(tk.Tk(),self.cliente)

    def imprimir(self):        
        numeroFactura=self.sIdVenta.get()
        nombre=self.sNombre.get()
        fecha=self.sFecha.get()
        total=self.sTotal.get()
        
        
        #Estructura Impresion
        titulo="               SumerMarket \n               Cracias por su compra\n\n"
        datos="N de Factura: {:2s}    Cliente: {:2s}    Fecha {:2s}\n\n".format(numeroFactura,nombre,fecha)
        
        estructura="""\
        +------------------------------------------------------------+
        | Descripcion        Cantidad  Precio    SubTotal  Total     |
        +------------------------------------------------------------+
        {}                                                           
        +------------------------------------------------------------+\
        """

        Tabla=(estructura.format('\n'.join("| {:16}{:10}{:10}{:10}             |".format(*fila) for fila in self.carro)))

        total="\n|{:>55}     |\n+------------------------------------------------------------+".format(total)    


        factura ="{:}{:}{:}{:}".format(titulo,datos,Tabla,total)
        
        nombreArchivo= 'comprobante_' + nombre+'_'+ str(date.today())

        #Creo el archivo
        with open(f"comprobantes\\{nombreArchivo}.txt", "w") as fichero:
            fichero.write(factura)

'''
if __name__ == "__main__":
    root = tk.Tk()
    venta=Venta(0,"",0)
    cliente=Cliente(0,"","",0,"")
    app=Factura(root, cliente, venta)
    root.mainloop()
'''