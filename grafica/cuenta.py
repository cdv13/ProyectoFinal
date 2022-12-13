from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox



class Cuenta():
    def __init__(self, root):
        self.root=root
        self.root.title("Perfil Usuario")
        #root.geometry("610x400")


        #________________fram3____________para mostrar lo de los botones
        self.frame3=tk.LabelFrame(self.root, text="", width=460, height=500, bg="bisque3")
        self.frame3.pack(ipadx=10, ipady=10, side="right", expand=True, fill="both")

        #___ Frame 1______________________para menu
        self.frame1=tk.LabelFrame(self.root, text="Perfil Usuario", width=150, height=220, bg="bisque3")
        self.frame1.pack(ipadx=10, ipady=10, expand=True, fill="y")

        #___________________Frame2___________ cerrar sesion
        self.frame2=tk.LabelFrame(self.root, text="", width=150, height=70, bg="bisque3")
        self.frame2.pack(ipadx=10, ipady=10, side="bottom")

        #Creo menu lateral
        self.perfil=tk.Button(self.frame1,text="Perfil",command=self.irPerfil)
        self.direccion=tk.Button(self.frame1,text="Direccion",command=self.irDireccion)
        self.pedidos=tk.Button(self.frame1,text="Pedidos",command=self.irPedidos)
        self.comprobantes=tk.Button(self.frame1,text="Comprobantes",command=self.irComprobantes)
        self.perfil.place(relx=0.1, rely=0, width=140, height=30)
        self.direccion.place(relx=0.1, rely=0.25, width=140, height=30)
        self.pedidos.place(relx=0.1, rely=0.5, width=140, height=30)
        self.comprobantes.place(relx=0.1, rely=0.75, width=140, height=30)

        self.activarFrame3()

        #creo boton cerrar sesion
        self.cerrar=tk.Button(self.frame2,text="Cerrar Sesion",command=self.cerrarSesion)
        self.cerrar.place(relx=.5,rely=.5,anchor='center',width=140, height=30)

        
    #creo la funcion para abrir los menus en el frame3
    def activarFrame3(self):
        pass

    def cerrarSesion(self):
        messagebox.askyesno(message="¿Seguro que desea cerrar sesion?")
        self.root.destroy()
        
    def irPerfil(self):
        pass
    def irDireccion(self):
        pass
    def irPedidos(self):
        pass
    def irComprobantes(self):
        pass
        


if __name__ == "__main__":
    root = tk.Tk()
    app=Cuenta(root)
    root.mainloop()