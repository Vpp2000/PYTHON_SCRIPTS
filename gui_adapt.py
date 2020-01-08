import tkinter as tk

class Abstract_Adapter():

    def get(self,i,j):
        pass



class Adaptee:  # VECTOR
    """
    The Adaptee contains some useful behavior, but its interface is incompatible
    with the existing client code. The Adaptee needs some adaptation before the
    client code can use it.
    """
    def __init__(self,arreglo):
        self.arreglo = arreglo

    def get(self,i):
        return self.arreglo[i]


class Adapter(Abstract_Adapter):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface.
    """
    def __init__(self, adaptee,fil,col):
        self.filas= fil
        self.col=col
        self.adaptee = adaptee

    def get(self,i,j):
        return j-1+(i-1)*(self.col)




class Aplicacion:
    def __init__(self):
        self.x = [1,2,3,4,5,6,7,8,9,10,11,12]
        self.ventana1=tk.Tk()
        self.label1=tk.Label(text="X:")
        self.label1.grid(column=0, row=0)
        self.dato=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=10, textvariable=self.dato)
        self.entry1.grid(column=1, row=0)

        self.label2=tk.Label(text="Y")
        self.label2.grid(column=0, row=1)
        self.dato2=tk.StringVar()
        self.entry2=tk.Entry(self.ventana1, width=10, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1)



        self.boton1=tk.Button(self.ventana1, text="Obtener", command=self.calcularcuadrado)
        self.boton1.grid(column=2, row=0)
        self.label3=tk.Label(text="Rpta:")
        self.label3.grid(column=2, row=1)
        self.ventana1.mainloop()


    def calcularcuadrado(self):
        adaptee = Adaptee(self.x) # ESTE ES EL VECTOR
        adapter = Adapter(adaptee,3,4)
        
        pos = adapter.get(int(self.dato.get()),int(self.dato2.get()))
        result = adaptee.get(pos)
        
        self.label3.configure(text=str(result))

aplicacion1=Aplicacion()   