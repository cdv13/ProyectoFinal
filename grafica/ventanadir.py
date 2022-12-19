import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox, StringVar, IntVar


#importacion de modulos propios de otra carpeta
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from clases.cliente import Cliente
from clases.usuario import Usuario


class VentanaDir(tk.Toplevel):
    def __init__(self, root):
        #setting title
        self.root=root
        self.root.title("Edicion Direccion")
        #setting window size
        width=450
        height=360
        
                
        #________________frame1___________________
        font_f1=("Helvetica", 14, "bold")

        self.frame1=tk.LabelFrame(self.root, width=350, height=100, bg="bisque3" )
        self.frame1.pack()

        self.titulo=tk.Label(self.frame1, text="Super Market")
        self.titulo.config(font=font_f1)
        self.titulo.place(rely=0.5, relx=0.5, anchor="center")
        
        #________________frame2______________________
        font_f2=("Helvetica", 10)

        self.frame2=tk.LabelFrame(self.root, text="Editar Direccion", width=350, height=350, bg="bisque3" )
        self.frame2.config(font=font_f2)
        self.frame2.pack()

        
        #Creo Variables de control para administrar las entry
        self.aCalle=StringVar()
        self.sAltura=IntVar()
        self.sLocalidad=StringVar()
        self.sProvincia=StringVar()
        self.sPostal=StringVar()
        
        
        #Creo los Widgets
        self.calle=tk.Label(self.frame2, text="Calle")
        self.calle.config(font=font_f2)
        self.calle.place(x=10,y=10,width=70,height=25)

        self.calleEntry=tk.Entry(self.frame2, textvariable=self.aCalle)
        self.calleEntry.config(font=font_f2)
        self.calleEntry.place(x=100,y=10,width=171,height=25)

        self.altura=tk.Label(self.frame2, text="Altura")
        self.altura.config(font=font_f2)
        self.altura.place(x=10,y=50,width=70,height=25)

        self.alturaEntry=tk.Entry(self.frame2, textvariable=self.sAltura)
        self.alturaEntry.config(font=font_f2)
        self.alturaEntry.place(x=100,y=50,width=171,height=25)

        self.localidad=tk.Label(self.frame2, text="Localidad")
        self.localidad.config(font=font_f2)
        self.localidad.place(x=10,y=100,width=70,height=25)

        self.localidadEntry=tk.Entry(self.frame2, textvariable=self.sLocalidad)
        self.localidadEntry.config(font=font_f2)
        self.localidadEntry.place(x=100,y=100,width=171,height=25)

        self.provincia=tk.Label(self.frame2, text="Provincia")
        self.provincia.config(font=font_f2)
        self.provincia.place(x=10,y=150,width=70,height=25)

        self.provinciaEntry=tk.Entry(self.frame2, textvariable=self.sProvincia)
        self.provinciaEntry.config(font=font_f2)
        self.provinciaEntry.place(x=100,y=150,width=171,height=25)

        self.postal=tk.Label(self.frame2, text="Codigo Postal")
        self.postal.config(font=font_f2)
        self.postal.place(x=10,y=200,width=70,height=25)

        self.postalEntry=tk.Entry(self.frame2, textvariable=self.sPostal)
        self.postalEntry.config(font=font_f2)
        self.postalEntry.place(x=100,y=200,width=171,height=25)

        self.Cancel=tk.Button(self.frame2, text="Cancelar")
        self.Cancel.config(font=font_f2)
        self.Cancel.place(x=110,y=250,width=70,height=25)
        self.Cancel["command"] = self.cancelar

        self.Crear=tk.Button(self.frame2, text="Guardar")
        self.Crear.config(font=font_f2)
        self.Crear.place(x=200,y=250,width=70,height=25)
        self.Crear["command"] = self.editar

        

    def cancelar(self):
        self.root.destroy()


    def editar(self):
        try:
            self.dir=Direccion("NULL", self.aCalle.get(),self.sAltura.get(),self.sLocalidad.get(),self.sProvincia.get(),self.sPostal.get())
            self.dir.insertar_DR()
            self.cliente.modificar_CLDir()
            messagebox.showinfo(message="Registro insertado con exito")
            
            self.root.destroy()
        except:
            messagebox.showwarning(message="No se guardo la Direccion, intente nuevamente")
            self.root.destroy()

'''
if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaDir(root)
    root.mainloop()
'''