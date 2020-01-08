import tkinter as tk

def convertir(cadena):
    tmp=cadena.split(",")
    return map(float,tmp)


class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=tk.Label(text="Ingrese nombre de usuario:")
        self.label1.grid(column=2, row=0)
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=30, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)
        self.label2=tk.Label(text="Ingrese clave:")
        self.label2.grid(column=0, row=1)
        self.dato2=tk.StringVar()
        self.entry2=tk.Entry(self.ventana1, width=30, textvariable=self.dato2, show="*")
        self.entry2.grid(column=1, row=1)
        self.boton1=tk.Button(self.ventana1, text="Ingresar", command=self.ingresar)
        self.boton1.grid(column=1, row=2)
        self.ventana1.mainloop()

    def ingresar(self):
        x=convertir(self.dato1.get())
        y=convertir(self.dato2.get())
        graphic=plt.plot(x, y, 'o')
        self.label1.image=graphic

aplicacion1=Aplicacion() 

