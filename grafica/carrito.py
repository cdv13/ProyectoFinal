from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont

from cuenta import Cuenta
from cargaproducto import Carga


import sys
sys.path.append('d:\\00_CURSOS\\2022_Curso_Python_SALTA\\ProyectoFinal\\clases')
from producto import Producto
from classCarrito import CarritoCompra


class Carrito(tk.Frame):
    def __init__(self, root, tituloFrame,titulo ):
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

        
        font_f1=("Helvetica", 14, "bold")
        font_f2=("Helvetica",10)
        font_f3=("Helvetica",10, "bold")
        
        #____Frame 0______________________________
        #puedo agregar un buscador
        self.frame=tk.LabelFrame(self.root, width=600, height=50, bg="bisque3")
        self.frame.pack()

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
        
        #de Prueba
        #self.tree.insert("", "end", text="1", values=("arroz", "1kg largo fino",34,123))
        
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
        self.vaciar=tk.Button(self.frame2,text="Vaciar Carrito",command=self.vaciarCarrito)
        self.total=tk.Label(self.frame2, text=f"Total : $ {self.totalCompra()}", font=font_f3, bg="bisque3")
        self.confirmar=tk.Button(self.frame2,text="Confirmar Compra",command=self.confirmarCompra)
        self.retornar.place(relx=0.05, rely=0, width=135, height=30)
        self.vaciar.place(relx=0.3, rely=0, width=135, height=30)
        self.total.place(relx=0.55, rely=0, width=100, height=30)
        self.confirmar.place(relx=0.75, rely=0, width=135, height=30)

        #Funcion para q se llenen las filas de la tabla
        self.mostrarProd()

    #Para q se muestren en la tabla
    def mostrarProd(self):
        #Obtener datos de la tabla y limpiar
        record=self.tree.get_children()
        for element in record:
            self.tree.delete(element)
        #Realizo la consulta en la tabla        
        self.c=CarritoCompra(0,0,0,0)
        filas=self.c.consutaCruzada()
        #Corro la tuplas
        for fila in filas:
            self.tree.insert("",tk.END,text=fila[0], values= (fila[1], fila[2], fila[3], fila[4], fila[5]) )


    #s uso la misma ventana de carga.... tendria q ir un UPDATE.......
    def vaciarCarrito(self):
        self.c=CarritoCompra(0, 0, 0, 0)
        self.c.vaciarCarrito()
        self.mostrarProd()

    def confirmarCompra(self):
        #Al confirmar hacer control stock

        #self.c=CarritoCompra(0, 0, stock, 0)
        #self.c.modificarStock()
        pass
    '''
    venta['fecha'] = datetime.now()
    ventas.append(venta)
        cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    # escribir los datos en un archivo de texto
    with open('productos.txt', 'w') as archivo:
        for producto in productos:
            archivo.write(f"{producto[0]}, {producto[1]}, {producto[2]}\n")
    '''          
        
    def returnCompra(self):
        self.root.destroy()
    
    #Para calcular el total en la tabla
    def totalCompra(self):
        self.c=CarritoCompra(0,0,0,0)
        total=self.c.precioCarrito()
        return total
    


if __name__ == "__main__":
    root = tk.Tk()
    app=Carrito(root)
    root.mainloop()