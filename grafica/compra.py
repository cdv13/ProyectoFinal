from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont

from cargaproducto import Carga
from cuenta import Cuenta

import sys
sys.path.append('d:\\00_CURSOS\\2022_Curso_Python_SALTA\\ProyectoFinal\\clases')
from producto import Producto

class Compra(tk.Frame):
    def __init__(self, root):
        self.root=root
        self.root.title("Ventana de Compra")
        #__________________________________________________
        #Crear una funcion para filtrar/Para Buscar
        #cromebook 
        
        #__________________________________________________
        #Crear una Boton para ir al carrito/mi Perfil



        #________________________ Frame 1________ para la tabla
        self.frame1=tk.LabelFrame(self.root, text="Productos disponibles", width=480, height=280, bg="bisque3")
        self.frame1.pack()

        self.tree = ttk.Treeview(self.frame1, height=10, columns= ("#1", "#2", "#3","#4"))
        self.tree.place(x=0,y=0 )
        self.tree.column("#0", width=50)
        self.tree.column("#1", width=90)
        self.tree.column("#2", width=150)
        self.tree.column("#3", width=80)
        self.tree.column("#4", width=80)

        self.tree.heading("#0", text = "ID", anchor = "center")
        self.tree.heading("#1", text = "Nombre", anchor = "center")
        self.tree.heading("#2", text = "Descripcion", anchor = "center")
        self.tree.heading("#3", text = "Precio", anchor = "center")
        self.tree.heading("#4", text = "Cantidad", anchor = "center")
        
        
        
        # Agregamos dos scrollbars 
        self.vscrol=ttk.Scrollbar(self.frame1, orient="vertical", command=self.tree.yview)
        self.vscrol.place(in_=self.tree, relx=1, relheight=1, bordermode="outside")
        self.hscrol=ttk.Scrollbar(self.frame1, orient="horizontal", command=self.tree.xview)
        self.hscrol.place(in_=self.tree, rely=1, relwidth=1, bordermode="outside")
        

        self.tree.configure(xscrollcommand=self.hscrol.set, yscrollcommand=self.vscrol.set)
        
        #_____________________Frame2___________________ para las operaciones
        self.frame2=tk.LabelFrame(self.root, text="Operaciones", width=460, height=50, bg="bisque3")
        self.frame2.pack()
        
        #self.editar=tk.Button(self.frame2,text="Categoria",command=self.categoriasProducto)
        self.addCarrito=tk.Button(self.frame2,text="Agregar al Carrito",command=self.agregarCarrito)
        #self.cuenta=tk.Button(self.frame2,text="Mi Cuenta",command=self.irCuenta)
        #self.cuenta.place(x=0, y=0, width=140, height=30)
        #self.editar.place(x=150, y=0, width=140, height=30)
        self.addCarrito.place(x=300, y=0, width=140, height=30)

        #Funcion para q se llenen las filas de la tabla
        self.mostrarProd()


    #s uso la misma ventana de carga.... tendria q ir un UPDATE.......
    def categoriasProducto(self):
        pass
        

    def agregarCarrito(self):
        pass
            
        
    def irCuenta(self):
        '''
        v=Cuenta(tk.Tk(),"Nuevo Producto","Cargar...")
        datos=v.getCampos()
        print(datos)
        '''
        pass
    
    #Para q se muestren en la tabla
    def mostrarProd(self):
        '''
        #Obtener datos de la tabla y limpiar
        record=self.tree.get_children()
        for element in record:
            self.tree.delete(element)
        #Realizo la consulta en la tabla        
        p=Producto()
        filas=p.mostrar()
        #Corro la tuplas
        for fila in filas:
            self.tree.insert("",text=fila[0], values= (fila[1], fila[2], fila[3], fila[4]) )
        '''
        pass
        
        


if __name__ == "__main__":
    root = tk.Tk()
    app=Compra(root)
    root.mainloop()