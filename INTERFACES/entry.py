import tkinter as tk

class Aplicacion:
    def __init__(self):
        ########################   DEFINICION DE LA VENTANA  ##########################################
        self.ventana1=tk.Tk()
        ######################### LABEL QUE SERVIRÁ DE AYUDA PARA EL USUARIO ##########################
        self.label1=tk.Label(text="Ingrese un número:")
        self.label1.grid(column=0, row=0)
        self.label1=tk.Label(text="Ingrese el otro número:")
        self.label1.grid(column=0, row=2)
        ###################### ASÍ SE PONEN LAS VARIABLES QUE MANEJA LA APP ###########################
        self.dato1=tk.StringVar()
        self.dato2=tk.StringVar()
        ####################### LOS ENTRY SERÁN COMO TEXTFIELDS DONDE SE PIDEN ENTRADAS ###############
        self.entry1=tk.Entry(self.ventana1, width=10, textvariable=self.dato1)
        self.entry1.grid(column=0, row=1)
        self.entry2=tk.Entry(self.ventana1, width=10, textvariable=self.dato2)
        self.entry2.grid(column=0, row=3)
        ################# SE DEFINE EL BOTÓN Y EN EL EL MÉTODO QUE ACTIVARA ###########################
        self.boton1=tk.Button(self.ventana1, text="Calcular suma de numeros", command=self.calcularcuadrado)
        self.boton1.grid(column=0, row=4)
        ######################### LABEL QUE SERVIRÁ DE AYUDA PARA EL USUARIO ##########################
        self.label2=tk.Label(text="resultado")
        self.label2.grid(column=0, row=5)
        ########################## EL BUCLE TAL Y COMO VIMOS EN GRÁFICA ###############################
        self.ventana1.mainloop()

    def calcularcuadrado(self):
        valor1=int(self.dato1.get())
        valor2=int(self.dato2.get())
        suma=valor1+valor2
        self.label2.configure(text=suma)

aplicacion1=Aplicacion()     
