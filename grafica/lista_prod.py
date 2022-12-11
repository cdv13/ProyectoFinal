from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox

from cargaproducto import Carga

import sys
sys.path.append('d:\\00_CURSOS\\2022_Curso_Python_SALTA\\ProyectoFinal\\clases')
from producto import Producto

class Lista(tk.Frame):
    def __init__(self, root):
        self.root=root
        self.root.title("Stock de Productos")

        #___ Frame 1________ para la tabla
        self.frame1=tk.LabelFrame(self.root, text="Listado de Productos", width=550, height=280, bg="bisque3")
        self.frame1.pack()

        self.tree= ttk.Treeview(self.frame1, height=10, columns= ("#1", "#2", "#3","#4", "#5"))
        self.tree.place(x=0,y=0 )
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
        self.tree.heading("#4", text = "Cantidad", anchor = "center")
        self.tree.heading("#5", text = "Categoria", anchor = "center")
        
        #self.tree.insert("", tk.END, text=1, values=("arroz", "1kg largo fino",34,123, comestibles))
        
        # Agregamos dos scrollbars 
        self.vscrol=ttk.Scrollbar(self.frame1, orient="vertical", command=self.tree.yview)
        self.vscrol.place(in_=self.tree, relx=1, relheight=1, bordermode="outside")
        self.hscrol=ttk.Scrollbar(self.frame1, orient="horizontal", command=self.tree.xview)
        self.hscrol.place(in_=self.tree, rely=1, relwidth=1, bordermode="outside")
        

        self.tree.configure(xscrollcommand=self.hscrol.set, yscrollcommand=self.vscrol.set)
        
        #___________________Frame2___________ para las operaciones
        self.frame2=tk.LabelFrame(self.root, text="Operaciones", width=460, height=50, bg="bisque3")
        self.frame2.pack()
        
        self.edit=tk.Button(self.frame2,text="Editar",command=self.editarProducto)
        self.eliminar=tk.Button(self.frame2,text="Eliminar",command=self.eliminarProd)
        self.agregar=tk.Button(self.frame2,text="Nuevo",command=self.agregarNuevo)
        self.agregar.place(x=0, y=0, width=140, height=30)
        self.edit.place(x=150, y=0, width=140, height=30)
        self.eliminar.place(x=300, y=0, width=140, height=30)

        #Funcion para q se llenen las filas de la tabla
        self.mostrarProd()

    #Para q se muestren en la tabla
    def mostrarProd(self):
        #Obtener datos de la tabla y limpiar
        record=self.tree.get_children()
        for element in record:
            self.tree.delete(element)
        #Realizo la consulta en la tabla        
        self.prod=Producto(0,"","",0,0,"")
        filas=self.prod.mostrar()
        #Corro la tuplas
        for fila in filas:
            self.tree.insert("",tk.END,text=fila[0], values= (fila[1], fila[2], fila[3], fila[4], fila[5]) )

    #uso la misma ventana de carga.... 
    def editarProducto(self):
        item=self.tree.focus()
        datos=self.tree.item(item)["values"]
        text=self.tree.item(item)["text"] #Para que me ponga el id
        datos.insert(0,text)
        print("viejo",datos)
        
        v=Carga(tk.Tk(),"Producto", "Editar Producto", self, datos)
        v.Guardar.config(state="disable")
        v.idEntry.config(state="disable")
        

    def eliminarProd(self):
        item=self.tree.item(self.tree.selection())['text']
        if item !="":
            self.prod=Producto(item,"","",0,0,"")
            self.prod.eliminar()
            messagebox.showinfo("BBDD", "Registro eliminado con exito")
            self.mostrarProd()
        else:
            messagebox.showinfo("BBDD", "Debe seleccionar un Registro")
        #print(item)
        
    def agregarNuevo(self):
        v=Carga(tk.Tk(), "Nuevo Producto", "Cargar de Producto", self)
        v.Actualizar.config(state="disable")
        v.idEntry.config(state="disable")
        


if __name__ == "__main__":
    root = tk.Tk()
    app=Lista(root)
    root.mainloop()