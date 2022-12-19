from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox, BooleanVar, IntVar, StringVar

from compra import Compra
from registro import Registro
from lista_prod import Lista

#importacion de modulos propios de otra carpeta
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from clases.usuario import Usuario


class Login:
    def __init__(self, root):
        #setting title
        self.root=root
        self.root.title("Login")
        self.sv=tk.StringVar()
        
        #__________________frame1___________________________________
        font_f1=("Helvetica", 14, "bold")

        self.frame1=tk.LabelFrame(self.root, width=400, height=100, bg="bisque3" )
        self.frame1.pack()

        self.titulo=tk.Label(self.frame1, text="Super Market \nBienvenido")
        self.titulo.config(font=font_f1)
        self.titulo.place(rely=0.5, relx=0.5, anchor="center")
        
        #____________________frame2___________________________________
        font_f2=("Helvetica", 10)

        self.frame2=tk.LabelFrame(self.root, width=400, height=200, bg="bisque3" )
        self.frame2.pack()

        
        #Creo Variables de control para administrar las entry
        self.sUsuario=tk.StringVar()
        self.sPass=tk.IntVar()
                
        #Creo los widgets
        self.usuario=tk.Label(self.frame2, text="Usuario")
        self.usuario.config(font=font_f2)
        self.usuario.place(x=10,y=10,width=70,height=25)
        
        self.usuarioEntry=tk.Entry(self.frame2, textvariable=self.sUsuario)
        self.usuarioEntry.config(font=font_f2)
        self.usuarioEntry.place(x=100,y=10,width=220,height=25)

        self.contrasena=tk.Label(self.frame2, text="Contraseña")
        self.contrasena.config(font=font_f2)
        self.contrasena.place(x=10,y=50,width=70,height=25)

       
        self.contrasenaEntry=tk.Entry(self.frame2, textvariable=self.sPass)
        self.contrasenaEntry.config(font=font_f2,show="*")
        self.contrasenaEntry.place(x=100,y=50,width=220,height=25)

        self.mostrar_pass=IntVar(value=0)        
        
        
        self.check=ttk.Checkbutton(self.frame2, text='Mostrar Contraseña',variable=self.mostrar_pass,
                                    onvalue=1, offvalue=0,command=self.check_click)
        self.check.place(x=100, y=80)
        
                
        self.Ingresar=tk.Button(self.frame2, text="Ingresar")
        self.Ingresar.config(font=font_f2)
        self.Ingresar.place(x=100,y=120,width=90,height=25)
        self.Ingresar["command"] = self.Ingresar_command

        self.Registro=tk.Button(self.frame2, text="Registrarse")
        self.Registro.config(font=font_f2)
        self.Registro.place(x=220,y=120,width=90,height=25)
        self.Registro["command"] = self.Registro_command

    #FUNCIONES

    #Muestra/Oculta la contraseña
    def check_click(self):
        if (self.mostrar_pass.get()==1):
            self.contrasenaEntry.config(show="")
        else:
            self.contrasenaEntry.config(show="*")
    
    #Ingreso de Usuarios
    def Ingresar_command(self):
        usuario=self.sUsuario.get()
        clave=self.sPass.get()
        self.us=Usuario(usuario,clave)
        
        if self.us.consulta_US():
            cliente=self.us.consultarCliente()
            if self.us.consulta_tipo()==1:
                v=Compra(tk.Tk(), cliente, self.us.id_usuario)
                self.root.destroy()
            if self.us.consulta_tipo()==0:
                v=Lista(tk.Tk())
                self.root.destroy()
        else:
            messagebox.showerror(message="Usuario o contraseña mal ingresados", title="Mensaje") 
        
        
    #Conexion con el Modulo de Registro
    def Registro_command(self):
        v=Registro(tk.Tk(), "Registro", "Registro de Usuario", "Super Market \nBienvenido" )


if __name__ == "__main__":
    root=tk.Tk()
    app = Login(root)
    root.mainloop()
