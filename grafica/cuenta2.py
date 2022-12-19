from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox,StringVar,IntVar

from registro import Registro
from ventanadir import VentanaDir

#Importacio de modulos propios
#from pathlib import Path
#import sys
#sys.path.append(str(Path(__file__).parent.parent.parent))



class Cuenta(tk.Frame):
    def __init__(self, root,cliente, correo):
        self.root=root
        self.root.title("Mi Cuenta")
        #setting window size
        width=600
        height=500
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)
        self.cliente=cliente
        self.correo=correo


        #________________fram3____________para mostrar lo de los botones
        self.frame3=tk.LabelFrame(self.root, text="", width=460, height=500, bg="bisque3")
        self.frame3.pack(ipadx=10, ipady=10, side="right", expand=True, fill="both")

        #___ Frame 1______________________para menu Lateral
        self.frame1=tk.LabelFrame(self.root, text="Perfil Usuario", width=150, height=220, bg="bisque3")
        self.frame1.pack(ipadx=10, ipady=10, expand=True, fill="y")

        #___________________Frame2___________ cerrar sesion
        self.frame2=tk.LabelFrame(self.root, text="", width=150, height=70, bg="bisque3")
        self.frame2.pack(ipadx=10, ipady=10, side="bottom")

        #Creo menu con notebook
        #Creo los Botones
        self.etiquetaUS=tk.Label(self.frame1, text=f"{self.correo}")
        self.perfil=tk.Button(self.frame1,text="Perfil",command=self.pantallaPerfil)
        self.direccion=tk.Button(self.frame1,text="Direccion",command=self.pantallaDireccion)
        self.pedidos=tk.Button(self.frame1,text="Pedidos",command=self.pantallaPedidos)
        self.comprobantes=tk.Button(self.frame1,text="Comprobantes",command=self.pantallaComprobantes)
        self.etiquetaUS.place(relx=0.1, rely=0.1, width=140, height=30)
        self.perfil.place(relx=0.1, rely=0.3, width=140, height=30)
        self.direccion.place(relx=0.1, rely=0.5, width=140, height=30)
        self.pedidos.place(relx=0.1, rely=0.7, width=140, height=30)
        self.comprobantes.place(relx=0.1, rely=0.9, width=140, height=30)

        #creo el panel notebook
        self.panel=ttk.Notebook(self.frame3, style="TNotebook")
        self.panel.pack(fill="both", expand=True)

        #Estilo de panel y pestañas(para q no se vean)
        estilo_panel=ttk.Style()
        estilo_panel.configure("TNotebook", background="bisque3", foreground="bisque3", padding=0, borderwidth=0)
        estilo_panel.theme_use("default")
        estilo_panel.configure("TNotebook",background="bisque3",foreground="bisque3", borderwidth=0)
        estilo_panel.configure("TNotebook.Tab",background="bisque3",foreground="bisque3", borderwidth=0)
        estilo_panel.map("TNotebook",background=[("selected", "bisque3")])
        estilo_panel.map("TNotebook.Tab",background=[("selected", "bisque3")], foreground=[("selected", "bisque3")])
        
        #Creo las pestañas del panel
        self.p1=tk.Frame(self.panel, background="bisque3")
        self.p2=tk.Frame(self.panel, background="bisque3")
        self.p3=tk.Frame(self.panel, background="bisque3") 
        self.p4=tk.Frame(self.panel, background="bisque3")
        self.p5=tk.Frame(self.panel, background="bisque3")

        #Agrego las pestañas al panel
        self.panel.add(self.p1, text="Pestaña 1")
        self.panel.add(self.p2, text="Pestaña 2")
        self.panel.add(self.p3, text="Pestaña 3")
        self.panel.add(self.p4, text="Pestaña 4")
        self.panel.add(self.p5, text="Pestaña 5")

        self.panel.pack(padx=10, pady=10)
        
        #Agrego los elementos en cada pestaña(funcionalidades)
        #Ventana principal
        self.titulo=tk.Label(self.p1,text="Ventana Usuario", bg="bisque3")
        self.titulo.pack(expand=1)

        #Ventana perfil
        self.sNombre=StringVar(self.p2)
        self.sDni=IntVar(self.p2)
        self.sCorreo=StringVar(self.p2)

        self.nombre=tk.Label(self.p2, text="Nombre")
        self.nombreEntry=tk.Entry(self.p2, textvariable=self.sNombre)
        self.dni=tk.Label(self.p2, text="DNI")
        self.dniEntry=tk.Entry(self.p2, textvariable=self.sDni)
        self.correo=tk.Label(self.p2, text="Correo Electronico")
        self.correoEntry=tk.Entry(self.p2, textvariable=self.sCorreo)
        self.editar=tk.Button(self.p2, text="Editar", command=self.irRegistro)

        self.nombre.grid(row=0,column=0,ipadx=2, ipady=2, pady=2)
        self.nombreEntry.grid(row=1,column=0,ipadx=2, ipady=2,pady=2)
        self.dni.grid(row=2,column=0,ipadx=2, ipady=2,pady=2)
        self.dniEntry.grid(row=3,column=0,ipadx=2, ipady=2,pady=2)
        self.correo.grid(row=4,column=0,ipadx=2, ipady=2,pady=2)
        self.correoEntry.grid(row=5,column=0,ipadx=2, ipady=2,pady=2)
        self.editar.grid(row=6,column=0,ipadx=2, ipady=2,pady=2)

        #Ventana Direccion
        self.sCalle=StringVar(self.p3)
        self.sAltura=IntVar(self.p3)
        self.sLocalidad=StringVar(self.p3)
        self.sProvincia=StringVar(self.p3)
        self.sPostal=StringVar(self.p3)

        self.dir=tk.Label(self.p3, text="Direccion de Usuario")
        self.calle=tk.Label(self.p3, text="Calle")
        self.calleEntry=tk.Entry(self.p3, textvariable=self.sCalle)
        self.altura=tk.Label(self.p3, text="Altura")
        self.alturaEntry=tk.Entry(self.p3, textvariable=self.sAltura)
        self.localidad=tk.Label(self.p3, text="Localidad")
        self.localidadEntry=tk.Entry(self.p3, textvariable=self.sLocalidad)
        self.provincia=tk.Label(self.p3,text="Provincia")
        self.provinciaEntry=tk.Entry(self.p3, textvariable=self.sProvincia)
        self.postal=tk.Label(self.p3,text="Codigo Postal")
        self.postalEntry=tk.Entry(self.p3, textvariable=self.sPostal)
        self.editar=tk.Button(self.p3, text="Editar", command=self.editDir)
        
        self.dir.grid(row=0,column=0,ipadx=2, ipady=2,pady=2)
        self.calle.grid(row=1,column=0,ipadx=2, ipady=2,pady=2)
        self.calleEntry.grid(row=2,column=0,ipadx=2, ipady=2,pady=2)
        self.altura.grid(row=3,column=0,ipadx=2, ipady=2,pady=2)
        self.alturaEntry.grid(row=4,column=0,ipadx=2, ipady=2,pady=2)
        self.localidad.grid(row=5,column=0,ipadx=2, ipady=2,pady=2)
        self.localidadEntry.grid(row=6,column=0,ipadx=2, ipady=2,pady=2)
        self.provincia.grid(row=7,column=0,ipadx=2, ipady=2,pady=2)
        self.provinciaEntry.grid(row=8,column=0,ipadx=2, ipady=2,pady=2)
        self.postal.grid(row=9,column=0,ipadx=2, ipady=2,pady=2)
        self.postalEntry.grid(row=10,column=0,ipadx=2, ipady=2,pady=2)
        self.editar.grid(row=11,column=0,ipadx=2, ipady=2,pady=2)
        
        #Ventana Pedidos
        self.pedidos=tk.Label(self.p4, text="Listado de Pedidos")
        self.pedidos.pack(expand=1)
        
        #Ventana Comprobantes
        self.comprobantes=tk.Label(self.p5, text="Lista de Comprobantes")
        self.comprobantes.pack(expand=1)

        #creo boton cerrar sesion
        self.cerrar=tk.Button(self.frame2,text="Cerrar Sesion",command=self.cerrarSesion)
        self.cerrar.place(relx=.5,rely=.5,anchor='center',width=140, height=30)


    def cerrarSesion(self):
        messagebox.askyesno(message="¿Seguro que desea cerrar sesion?")
        self.root.destroy()

    def pantallaPerfil(self):
        self.panel.select([self.p2])
        
    def pantallaDireccion(self):
        self.panel.select([self.p3])

    def pantallaPedidos(self):
        self.panel.select([self.p4])

    def pantallaComprobantes(self):
        self.panel.select([self.p5])
    
    def mostrarDir(self):
        pass

    def irRegistro(self):
        v=Registro(tk.Tk(), "Editar Datos", "Edicion",  "Super Market \n Perfil Usuario" )

    def editDir(self):
        v=VentanaDir(tk.Tk())

'''
if __name__ == "__main__":
    root = tk.Tk()
    cliente=Cliente(0,"","",0,"")
    app=Cuenta(root,cliente,correo)
    root.mainloop()
'''