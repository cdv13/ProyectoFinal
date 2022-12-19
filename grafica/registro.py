import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox, StringVar, IntVar


#importacion de modulos propios de otra carpeta
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from clases.cliente import Cliente
from clases.usuario import Usuario


class Registro(tk.Toplevel):
    def __init__(self, root, textFrame, text, textTitulo):
        #setting title
        self.root=root
        self.root.title(text)
        
        width=450
        height=360

        #________________frame1___________________
        font_f1=("Helvetica", 14, "bold")

        self.frame1=tk.LabelFrame(self.root, width=350, height=100, bg="bisque3" )
        self.frame1.pack()

        self.titulo=tk.Label(self.frame1, text=textTitulo)
        self.titulo.config(font=font_f1)
        self.titulo.place(rely=0.5, relx=0.5, anchor="center")
        
        #________________frame2______________________
        font_f2=("Helvetica", 10)

        self.frame2=tk.LabelFrame(self.root, text=textFrame,width=350, height=350, bg="bisque3" )
        self.frame2.config(font=font_f2)
        self.frame2.pack()

        
        #Creo Variables de control para administrar las entry
        self.sNombre=tk.StringVar()
        self.sApellido=tk.StringVar()
        self.sDNI=tk.IntVar()
        self.sCorreo=tk.StringVar()
        self.sPass=tk.StringVar()
        
        
        #Creo los Widgets
        self.nombre=tk.Label(self.frame2, text="Nombre")
        self.nombre.config(font=font_f2)
        self.nombre.place(x=10,y=10,width=70,height=25)

        self.nombreEntry=tk.Entry(self.frame2, textvariable=self.sNombre)
        self.nombreEntry.config(font=font_f2)
        self.nombreEntry.place(x=100,y=10,width=171,height=25)

        self.apellido=tk.Label(self.frame2, text="Apellido")
        self.apellido.config(font=font_f2)
        self.apellido.place(x=10,y=50,width=70,height=25)

        self.apellidoEntry=tk.Entry(self.frame2, textvariable=self.sApellido)
        self.apellidoEntry.config(font=font_f2)
        self.apellidoEntry.place(x=100,y=50,width=171,height=25)

        self.dni=tk.Label(self.frame2, text="DNI")
        self.dni.config(font=font_f2)
        self.dni.place(x=10,y=100,width=70,height=25)

        self.dniEntry=tk.Entry(self.frame2, textvariable=self.sDNI)
        self.dniEntry.config(font=font_f2)
        self.dniEntry.place(x=100,y=100,width=171,height=25)

        self.correo=tk.Label(self.frame2, text="Correo")
        self.correo.config(font=font_f2)
        self.correo.place(x=10,y=150,width=70,height=25)

        self.correoEntry=tk.Entry(self.frame2, textvariable=self.sCorreo)
        self.correoEntry.config(font=font_f2)
        self.correoEntry.place(x=100,y=150,width=171,height=25)

        self.contrasena=tk.Label(self.frame2, text="Contraseña")
        self.contrasena.config(font=font_f2)
        self.contrasena.place(x=10,y=200,width=70,height=25)

        self.contrasenaEntry=tk.Entry(self.frame2, textvariable=self.sPass)
        self.contrasenaEntry.config(font=font_f2)
        self.contrasenaEntry.place(x=100,y=200,width=171,height=25)

        self.Cancel=tk.Button(self.frame2, text="Cancelar")
        self.Cancel.config(font=font_f2)
        self.Cancel.place(x=110,y=250,width=70,height=25)
        self.Cancel["command"] = self.Cancel_command

        self.Crear=tk.Button(self.frame2, text="Guardar")
        self.Crear.config(font=font_f2)
        self.Crear.place(x=200,y=250,width=70,height=25)
        self.Crear["command"] = self.Crear_command

        

    def Cancel_command(self):
        self.root.destroy()


    def Crear_command(self):
        try:
            self.c=Cliente("NULL", self.sNombre.get(),self.sApellido.get(),self.sDNI.get(),self.sCorreo.get())
            self.c.insertar_CL()
            self.u=Usuario(self.sCorreo.get(),self.sPass.get())
            self.u.insertar_US()
            
            messagebox.showinfo("BBDD", "Registro insertado con exito")
            self.root.destroy()
        except:
            messagebox.showwarning("BBDD", "Usuario no Registrado, intente nuevamente")
            self.root.destroy()
        

'''
if __name__ == "__main__":
    root = tk.Tk()
    app = Registro(root)
    root.mainloop()
'''