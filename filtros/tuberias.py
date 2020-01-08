import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
import re
import random

class Tuberia:
    def __init__(self):
        self.lista_filtros=[]


    def add_filter(self,filtro):
        self.lista_filtros.append(filtro)

    def clear_lista(self):
        self.lista_filtros = []

    def filtrar(self,cadena):
        new_cadena = cadena
        for filtro in self.lista_filtros: 
            new_cadena = filtro.filter(new_cadena)

        return new_cadena

class Abstract_filter:

    def filter(self,cadena):
        pass



class Capitalize(Abstract_filter):
	
	def filter(self,cadena):
		return cadena.capitalize()


class Reverse(Abstract_filter):
	
	def filter(self,cadena):
		return cadena[::-1]


class DeleteSpaces(Abstract_filter):

    def filter(self,cadena):
        return re.sub(r'[\t ]+',' ',cadena)


class SolesToDolars(Abstract_filter):

    def filter(self,cadena):
        numero = re.findall(r"([+-]?\d+(\.\d+)?)(\s*)(soles|sol|nuevo sol)",cadena)     
        numero = ["{0:.2f}".format(float(a[1])*3.38) for a in numero]       
        cadena = re.sub(r"([+-]?\d+(\.\d+)?)(\s*)(soles|sol|nuevo sol)",
        lambda match: str(numero.pop(0)+" dólares"),
        cadena)     

        numero = re.findall(r"(S\/\.|s\/\.)\s*([+-]?\d+(\.\d+)?)",cadena)
        numero = ["{0:.2f}".format(float(a[1])*3.38) for a in numero]
        cadena = re.sub(r"(S\/\.|s\/\.)\s*([+-]?\d+(\.\d+)?)",
        lambda match: str("US$ "+numero.pop(0)),
        cadena)

        return cadena

class Todomayusc(Abstract_filter):
    
    def filter(self,cadena):
        return cadena.upper()

class Todominusc(Abstract_filter):
    
    def filter(self,cadena):
        return cadena.lower()

class Desorden(Abstract_filter):
    def filter(self,cadena):
        patron = "[\S ]+\n|[\S ]+"


        matches = re.findall(patron,cadena)

        texto_new = ""

        lista = []
        while len(lista)<len(matches):
            r=random.randint(0,len(matches)-1)
            if r not in lista: lista.append(r)

        print(f"matches es {matches}")
        print(f"Len matches es {len(matches)}")
        print(f"La lista es {lista}")

        for i in range(len(matches)):
            texto_new = texto_new + matches[lista[i]]    

        return texto_new

class Enumeracion(Abstract_filter):
    def filter(self,cadena):
        patron = "[\S\t ]+\n?"

        matches = re.findall(patron,cadena)

        texto_new = ""


        for i in range(len(matches)):
            texto_new = texto_new+str(i+1)+" "+matches[i]    

        return texto_new

class Busca_comentarios(Abstract_filter):
    def filter(cadena):    
        patron = "(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)"
        coincidencia = re.findall(patron,cadena)
        print(coincidencia)


class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.pipe = Tuberia()

        self.texto_label="Filtros:\n"
        self.label1=tk.Label(self.ventana1, text=self.texto_label)
        self.label1.grid(column=0, row=6)


        self.scrolledtext1=st.ScrolledText(self.ventana1, width=50, height=10)
        self.scrolledtext1.grid(column=2,row=0, columnspan=3,rowspan=4,padx=10, pady=10)

        self.seleccion1=tk.IntVar()
        self.boton1=tk.Button(self.ventana1,text="Capitalize", command=self.mayusculas)
        self.boton1.grid(column=0, row=0)

        self.boton2=tk.Button(self.ventana1,text="Reverse", command=self.inversa)
        self.boton2.grid(column=0, row=1)

        self.boton3=tk.Button(self.ventana1,text="Delete Spaces", command=self.espacios)
        self.boton3.grid(column=0, row=2)

        self.boton4=tk.Button(self.ventana1,text="Soles To Dolars", command=self.SolToDol)
        self.boton4.grid(column=0, row=3)

        self.boton5=tk.Button(self.ventana1,text="Upper", command=self.toupper)
        self.boton5.grid(column=1, row=0)

        self.boton6=tk.Button(self.ventana1,text="Lower", command=self.tolower)
        self.boton6.grid(column=1, row=1)

        self.boton7=tk.Button(self.ventana1,text="Desorden", command=self.desordenar)
        self.boton7.grid(column=1, row=2)

        self.boton8=tk.Button(self.ventana1,text="Enumera", command=self.enumerar)
        self.boton8.grid(column=1, row=3)


        self.boton5_filtra=tk.Button(self.ventana1,text="Filtrar", command=self.filtrar_todo)
        self.boton5_filtra.grid(column=2, row=4)

        self.boton6_filtra=tk.Button(self.ventana1,text="Limpiar", command=self.limpiar_filtros)
        self.boton6_filtra.grid(column=2, row=5)


        self.scrolledtext2=st.ScrolledText(self.ventana1, width=50, height=10)
        self.scrolledtext2.grid(column=2,row=6, padx=10, pady=10)
        self.ventana1.mainloop()
        

    def mayusculas(self):
        obj = Capitalize()
        self.pipe.add_filter(obj)
        self.texto_label=self.texto_label+"Mayusculas\n"
        self.label1.configure(text=self.texto_label)

    def inversa(self):
        obj = Reverse()
        self.pipe.add_filter(obj)
        self.texto_label=self.texto_label+"Inversa\n"        
        self.label1.configure(text=self.texto_label)


    def espacios(self):
        obj = DeleteSpaces()
        self.pipe.add_filter(obj)
        self.texto_label=self.texto_label+"ESpacios\n"        
        self.label1.configure(text=self.texto_label)

    def SolToDol(self):
        obj = SolesToDolars()
        self.pipe.add_filter(obj)
        self.texto_label=self.texto_label+"SolToDO\n"        
        self.label1.configure(text=self.texto_label)

    def toupper(self):
        obj = Todomayusc()
        self.pipe.add_filter(obj)
        self.texto_label=self.texto_label+"Todo a mayuscula\n"        
        self.label1.configure(text=self.texto_label)

    def tolower(self):
        obj = Todominusc()
        self.pipe.add_filter(obj)
        self.texto_label=self.texto_label+"Todo a minuscula\n"        
        self.label1.configure(text=self.texto_label)

    def desordenar(self):
        obj = Desorden()
        self.pipe.add_filter(obj)
        self.texto_label=self.texto_label+"Desordenar lineas\n"        
        self.label1.configure(text=self.texto_label)

    def enumerar(self):
        obj = Enumeracion()
        self.pipe.add_filter(obj)
        self.texto_label=self.texto_label+"Enumerar lineas\n"        
        self.label1.configure(text=self.texto_label)




    def limpiar_filtros(self):
        self.pipe.clear_lista()
        self.texto_label="Filtros:\n"
        self.label1.configure(text=self.texto_label)

    def filtrar_todo(self):
        self.scrolledtext2.delete('1.0',tk.END)		
        entrada = self.saveText = self.scrolledtext1.get("1.0",tk.END)
        nuevo_texto = self.pipe.filtrar(entrada)
        self.scrolledtext2.insert("1.0", nuevo_texto)

aplicacion1=Aplicacion() 
