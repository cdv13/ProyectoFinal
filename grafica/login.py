from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import BooleanVar
from tkinter import IntVar
from compra import Compra
from registro import Registro
from lista_prod import Lista

import sys
sys.path.append('d:\\00_CURSOS\\2022_Curso_Python_SALTA\\ProyectoFinal\\clases')
from usuario import Usuario

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

        
        #Creo StringVar para administrar las entry
        self.sUsuario=tk.StringVar()
        self.sPass=tk.StringVar()
                
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


    def check_click(self):
        if (self.mostrar_pass.get()==1):
            self.contrasenaEntry.config(show="")
        else:
            self.contrasenaEntry.config(show="*")
            
    def Ingresar_command(self):
        us=self.usuarioEntry.get()
        clave=self.contrasenaEntry.get()

        self.u=Usuario("NULL", us, clave)
        
        if self.u.consulta_US():
            if self.u.consulta_tipo()==1:
                v=Compra(tk.Tk())
                self.root.destroy()
            if self.u.consulta_tipo()==0:
                v=Lista(tk.Tk())
                self.root.destroy()
        else:
            messagebox.showerror(message="Usuario o contraseña mal ingresados", title="Mensaje") 
        #print("consulta", self.u.consulta_US())
        #print("tipo", self.u.consulta_tipo())
        #print(password)

    def Registro_command(self):
        v=Registro(tk.Tk())
        
        


if __name__ == "__main__":
    root=tk.Tk()
    app = Login(root)
    root.mainloop()
