from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox

from registro import Registro



class Cuenta():
    def __init__(self, root):
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
        self.perfil=tk.Button(self.frame1,text="Perfil",command=self.pantallaPerfil)
        self.direccion=tk.Button(self.frame1,text="Direccion",command=self.pantallaDireccion)
        self.pedidos=tk.Button(self.frame1,text="Pedidos",command=self.pantallaPedidos)
        self.comprobantes=tk.Button(self.frame1,text="Comprobantes",command=self.pantallaComprobantes)
        self.perfil.place(relx=0.1, rely=0, width=140, height=30)
        self.direccion.place(relx=0.1, rely=0.25, width=140, height=30)
        self.pedidos.place(relx=0.1, rely=0.5, width=140, height=30)
        self.comprobantes.place(relx=0.1, rely=0.75, width=140, height=30)

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
        self.nombre=tk.Label(self.p2, text="Nombre")
        self.nombre.pack(expand=1)

        self.dni=tk.Label(self.p2, text="DNI")
        self.dni.pack(expand=1)

        self.correo=tk.Label(self.p2, text="Correo Electronico")
        self.correo.pack(expand=1)

        self.editar=tk.Button(self.p2, text="Editar", command=self.irRegistro)
        self.editar.pack(expand=1)

        #Ventana Direccion
        self.dir=tk.Label(self.p3, text="Direccion")
        self.dir.pack(expand=1)

        self.editar=tk.Button(self.p3, text="Editar", command=self.editDir)
        self.editar.pack(expand=1)
        
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
    
    def irRegistro(self):
        v=Registro(tk.Tk(), "Editar Datos", "Edicion",  "Super Market \n Perfil Usuario" )

    def editDir(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app=Cuenta(root)
    root.mainloop()