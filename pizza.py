# -*- coding: utf-8 -*-
import tkinter as tk
from abc import ABC, abstractmethod


class Abstract_Pizza:

	def precio(self):
		pass 


class Base_Jamon(Abstract_Pizza):
	
	def precio(self):
         return 10

class Vegana(Abstract_Pizza):
	
	def precio(self):
         return 9

class Full_Meats(Abstract_Pizza):
	
	def precio(self):
         return 12


class Abstract_Pizza_Decorator(Abstract_Pizza):
	def __init__(self,_mi_pizza):
		self._mi_pizza = _mi_pizza

	def precio(self):
		return self._mi_pizza.precio()
	



class Chorizo(Abstract_Pizza_Decorator):
	def __init__(self,_mi_pizza):
		Abstract_Pizza_Decorator.__init__(self,_mi_pizza)

	def precio(self):
		return self._mi_pizza.precio()+5


class Jamón(Abstract_Pizza_Decorator):
	def __init__(self,_mi_pizza):
		Abstract_Pizza_Decorator.__init__(self,_mi_pizza)

	def precio(self):
		return self._mi_pizza.precio()+4

class Xqueso(Abstract_Pizza_Decorator):
	def __init__(self,_mi_pizza):
		Abstract_Pizza_Decorator.__init__(self,_mi_pizza)

	def precio(self):
		return self._mi_pizza.precio()+3

class Peperoni(Abstract_Pizza_Decorator):
	def __init__(self,_mi_pizza):
		Abstract_Pizza_Decorator.__init__(self,_mi_pizza)

	def precio(self):
		return self._mi_pizza.precio()+2


class Piña(Abstract_Pizza_Decorator):
	def __init__(self,_mi_pizza):
		Abstract_Pizza_Decorator.__init__(self,_mi_pizza)

	def precio(self):
		return self._mi_pizza.precio()+1

class Pizza_descuento(Abstract_Pizza_Decorator):
	def __init__(self,_mi_pizza):
		Abstract_Pizza_Decorator.__init__(self,_mi_pizza)

	def precio(self):
		return self._mi_pizza.precio()*0.8



class Aplicacion:
	def __init__(self):
		self.ventana1=tk.Tk()
		self.seleccion1=tk.IntVar()
		self.seleccion2=tk.IntVar()
		self.seleccion3=tk.IntVar()
		self.seleccion4=tk.IntVar()        
		self.seleccion5=tk.IntVar()        
		self.dato=tk.StringVar()
		
		self.label_pizza=tk.Label(text="Tipo de pizza")
		self.label_pizza.grid(column=0, row=0)

		
		self.boton1=tk.Button(self.ventana1, text="Crear Base_Jamon", command=self.crear_Jamon)
		self.boton1.grid(column=0, row=1)

		
		self.boton2=tk.Button(self.ventana1, text="Crear Vegana", command=self.crear_Vegana)
		self.boton2.grid(column=0, row=2)

		self.boton3=tk.Button(self.ventana1, text="Crear Full_Meats", command=self.crear_Fullmeat)
		self.boton3.grid(column=0, row=3)

		

		self.label1=tk.Label(text="Ingrediente")
		self.label1.grid(column=0, row=4)

		self.check1=tk.Checkbutton(self.ventana1,text="Chorizo", variable=self.seleccion1, command=self.add_chorizo)
		self.check1.grid(column=0, row=5)

		self.check2=tk.Checkbutton(self.ventana1,text="Jamón", variable=self.seleccion2,command=self.add_jamón)
		self.check2.grid(column=0, row=6)

		self.check3=tk.Checkbutton(self.ventana1,text="Xqueso", variable=self.seleccion3,command=self.add_xqueso)
		self.check3.grid(column=0, row=7)

		self.check4=tk.Checkbutton(self.ventana1,text="Peperoni", variable=self.seleccion4,command=self.add_peperoni)
		self.check4.grid(column=0, row=8)     

		self.check5=tk.Checkbutton(self.ventana1,text="Piña", variable=self.seleccion5,command=self.add_piña)
		self.check5.grid(column=0, row=9)           

		
		
		self.precio_pizzas=tk.Label(text="Precio")
		self.precio_pizzas.grid(column=1, row=0)

		self.precio_jamon=tk.Label(text="10 soles")
		self.precio_jamon.grid(column=1, row=1)

		self.precio_vegana=tk.Label(text="9 soles")
		self.precio_vegana.grid(column=1, row=2)

		self.precio_fullmeat=tk.Label(text="12 soles")
		self.precio_fullmeat.grid(column=1, row=3)




		self.label2=tk.Label(text="Precio")
		self.label2.grid(column=1, row=4)

		self.label3=tk.Label(text="5 soles")
		self.label3.grid(column=1, row=5)

		self.label4=tk.Label(text="4 soles")
		self.label4.grid(column=1, row=6)

		self.label3=tk.Label(text="3 soles")
		self.label3.grid(column=1, row=7)

		self.label3=tk.Label(text="2 soles")
		self.label3.grid(column=1, row=8)		

		self.label4=tk.Label(text="1 soles")
		self.label4.grid(column=1, row=9)         

		

		self.label5=tk.Label(text="El precio total de la pizza: ")
		self.label5.grid(column=3, row=0)

		self.boton4=tk.Button(self.ventana1, text="Precio", command=self.calcular_precio)
		self.boton4.grid(column=3, row=1)
		
		self.label_descuento=tk.Label(text="DESCUENTO:")
		self.label_descuento.grid(column=3, row=4)
		self.entry1=tk.Entry(self.ventana1, width=10, textvariable=self.dato)
		self.entry1.grid(column=3, row=5)
		self.boton_descuento=tk.Button(self.ventana1, text="ACTIVAR DESCUENTO", command=self.descuento_pizza)
		self.boton_descuento.grid(column=3, row=6)

		

		self.ventana1.mainloop()



	def crear_Jamon(self):
		self.pizza_krusty=Base_Jamon()
		print(self.pizza_krusty.precio())

	def crear_Vegana(self):
		self.pizza_krusty=Vegana()
		print(self.pizza_krusty.precio())
		
	def crear_Fullmeat(self):
		self.pizza_krusty=Full_Meats()
		print(self.pizza_krusty.precio())			

	def calcular_precio(self):
		print(self.pizza_krusty.precio())
		self.label5.configure(text="El precio total de la pizza:"+str(self.pizza_krusty.precio()))
		return self.pizza_krusty.precio()



	def add_chorizo(self):
		self.pizza_krusty = Chorizo(self.pizza_krusty)

	def add_xqueso(self):
		self.pizza_krusty = Xqueso(self.pizza_krusty)

	def add_jamón(self):
		self.pizza_krusty = Jamón(self.pizza_krusty)

	def add_peperoni(self):
		self.pizza_krusty = Peperoni(self.pizza_krusty)

	def add_piña(self):
		self.pizza_krusty = Piña(self.pizza_krusty)

	def descuento_pizza(self):
		valor= self.dato.get()
		print(valor)
		if valor == 'UNI1234':
			self.pizza_krusty = Pizza_descuento(self.pizza_krusty)



aplicacion1=Aplicacion() 

