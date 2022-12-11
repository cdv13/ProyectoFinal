import tkinter as tk
import tkinter.font as tkFont
from tkinter import Scrollbar, messagebox

import sys
sys.path.append('d:\\00_CURSOS\\2022_Curso_Python_SALTA\\ProyectoFinal\\clases')
from producto import Producto 

class Carga(tk.Toplevel):
    def __init__(self, root,tituloFrame, titulo,frame_root,editar=None):
        #setting title
        self.root=root
        self.root.title(titulo)
        self.titulo=titulo
        self.frame_root=frame_root
        
        if(editar is None):
            editar=["","","","","",""]

        #__________________Frame 1______________________

        font_f1=("Helvetica", 14, "bold")

        self.frame=tk.LabelFrame(self.root, width=400, height=50, bg="bisque3")
        self.frame.pack()

        
        self.l1=tk.Label(self.frame, text="Super market")
        self.l1.config(font=font_f1)
        self.l1.place(rely=0.5, relx=0.5, anchor="center")

        #________________________Frame 2_________________

        font_f2=("Helvetica",10)

        self.frame2=tk.LabelFrame(self.root,text=tituloFrame, width=400, height=460, bg="bisque3")
        self.frame2.config(font=font_f2)
        self.frame2.pack()
        
        #Creo los Widgets
        self.id=tk.Label(self.frame2, text="Id")
        self.id.config(font=font_f2)
        self.id.place(x=10,y=10,width=80,height=30)

        self.idEntry=tk.Entry(self.frame2)
        self.idEntry.config(font=font_f2)
        self.idEntry.insert('0', editar[0])
        self.idEntry.place(x=150,y=10, width=200,height=30)

        self.nombre=tk.Label(self.frame2, text="Nombre")
        self.nombre.config(font=font_f2)
        self.nombre.place(x=10,y=50,width=80,height=30)

        self.nombreEntry=tk.Entry(self.frame2)
        self.nombreEntry.config(font=font_f2)
        self.nombreEntry.focus() #para q salga el tilde
        self.nombreEntry.insert('0', editar[1])
        self.nombreEntry.place(x=150,y=50, width=200,height=30)

        self.descripcion=tk.Label(self.frame2, text="Descripccion")
        self.descripcion.config(font=font_f2)
        self.descripcion.place(x=10,y=100,width=80,height=30)

        self.descripcionText=tk.Text(self.frame2,width=20,height=10)
        self.descripcionText.config(font=font_f2)
        self.descripcionText.insert('0.0', editar[2])
        self.descripcionText.place(x=150,y=100,width=200,height=200)

        self.scrollVert=tk.Scrollbar(self.frame2, command=self.descripcionText.yview)
        self.scrollVert.place(in_=self.descripcionText, relx=1, relheight=1, bordermode="outside")
        
        self.descripcionText.config(yscrollcommand=self.scrollVert.set)
        self.scrollVert.config(command=self.descripcionText.yview)

        self.precio=tk.Label(self.frame2, text="Precio")
        self.precio.config(font=font_f2)
        self.precio.place(x=10,y=320,width=80,height=30)
        
        self.precioEntry=tk.Entry(self.frame2)
        self.precioEntry.config(font=font_f2)
        self.precioEntry.insert('0', editar[3])
        self.precioEntry.place(x=150,y=320,width=200,height=30)
        
        self.cantidad=tk.Label(self.frame2, text="Cantidad")
        self.cantidad.config(font=font_f2)
        self.cantidad.place(x=10,y=360,width=80,height=30)
        
        self.cantidadEntry=tk.Entry(self.frame2)
        self.cantidadEntry.config(font=font_f2)
        self.cantidadEntry.insert('0', editar[4])
        self.cantidadEntry.place(x=150,y=360,width=200,height=30)

        self.categoria=tk.Label(self.frame2, text="categoria")
        self.categoria.config(font=font_f2)
        self.categoria.place(x=10,y=400,width=80,height=30)
        
        self.categoriaEntry=tk.Entry(self.frame2)
        self.categoriaEntry.config(font=font_f2)
        self.categoriaEntry.insert('0', editar[5])
        self.categoriaEntry.place(x=150,y=400,width=200,height=30)
        
        #_____________________________Creo Frame 3____________________

        self.frame3=tk.LabelFrame(self.root, text="Operaciones", width=400, height=80, bg="bisque3")
        self.frame3.config(font=font_f2)
        self.frame3.pack()

        self.Cancelar=tk.Button(self.frame3, text="Cancelar", justify="center")
        self.Cancelar.config(font=font_f2)
        self.Cancelar.place(x=25,y=10,width=80,height=40)
        self.Cancelar["command"] = self.cancelar_command
        
        self.Guardar=tk.Button(self.frame3, text= "Guardar \nProducto", justify="center")
        self.Guardar.config(font=font_f2)
        self.Guardar.place(x=155,y=10,width=80,height=40)
        self.Guardar["command"] = self.guardar_command
        
        self.Actualizar=tk.Button(self.frame3, text= "Actualizar \nProducto", justify="center")
        self.Actualizar.config(font=font_f2)
        self.Actualizar.place(x=285,y=10,width=80,height=40)
        self.Actualizar["command"] = self.actualizar_command

        #self.data=[]
    #_________________________Creo las Funciones__________________________________

    def cancelar_command(self):
        self.root.destroy()
        

    def guardar_command(self):
        if len(self.nombreEntry.get())!=0 and len(self.descripcionText.get("1.0", "end"))!=0 and len(self.precioEntry.get())!=0 and len(self.cantidadEntry.get())!=0 and len(self.categoriaEntry.get())!=0:
            p=Producto("NULL",self.nombreEntry.get(),self.descripcionText.get("1.0", "end"),self.precioEntry.get(),self.cantidadEntry.get(), self.categoriaEntry.get())
            p.insertar()
            messagebox.showinfo("BBDD", "Registro insertado con exito")
            self.frame_root.mostrarProd()
            self.root.destroy()
        else:
            messagebox.showerror("BBDD", "No se pudo agregar el Registro, \ndebe completar todos los campos")
        
    
    def actualizar_command(self):
        self.datos=(self.idEntry, self.nombreEntry.get(),self.descripcionText.get("1.0", "end"),self.precioEntry.get(),self.cantidadEntry.get(), self.categoriaEntry.get())
        print("actual",self.datos)
        if self.datos != "":
        #if len(self.nombreEntry.get())!=0 and len(self.descripcionText.get("1.0", "end"))!=0 and len(self.precioEntry.get())!=0 and len(self.cantidadEntry.get())!=0 and len(self.categoriaEntry.get())!=0:
            p=Producto(int(self.idEntry.get()),self.nombreEntry.get(),self.descripcionText.get("1.0", "end"),float(self.precioEntry.get()),int(self.cantidadEntry.get()), self.categoriaEntry.get())
            p.modificar()
            messagebox.showinfo("BBDD", "Registro actualizado con exito")
            self.frame_root.mostrarProd()
            self.root.destroy()
        else:
            messagebox.showinfo("BBDD", "No se actualizo el Registro")
    

if __name__ == "__main__":
    root = tk.Tk()
    app = Carga(root,"","")
    root.mainloop()


'''
Tambien en vez de hacr un popUP, puedo crear un mensaje,q se ejecute en la
el mismo cuerpo de la ventana, (abajo de la tabla x ej), y en las funciones
cambio el texto.

self.mensaje.grid(row=3, column=0, columnspam=2, sticky=WE)

lo q iria en las funciones seria

self.mensaje['text']= "producto {} agregado con exito".format(self.sNombre.get())
'''