# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import scrolledtext as st
import re


class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
                
        self.label1=tk.Label(text="Ingrese patrón:")
        self.label1.grid(column=0, row=0)
        

        self.dato=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=20, textvariable=self.dato)
        self.entry1.grid(column=1, row=0)
        
        self.label2=tk.Label(text="Ingrese texto a analizar:")
        self.label2.grid(column=0, row=1)

        self.scrolledtext2=st.ScrolledText(self.ventana1, width=50, height=10)
        self.scrolledtext2.grid(column=1,row=1, padx=10, pady=10)

        self.scrolledtext3=st.ScrolledText(self.ventana1, width=30, height=10)
        self.scrolledtext3.grid(column=0,row=4, padx=10, pady=10,rowspan=2)

        self.label3=tk.Label(text="ListBox:")
        self.label3.grid(column=0, row=3)

        self.boton1=tk.Button(self.ventana1, text="MATCH", command=self.ingresar)
        self.boton1.grid(column=1, row=3)
        
        self.boton2=tk.Button(self.ventana1, text="REPLACE", command=self.replace)
        self.boton2.grid(column=1, row=4)


        self.label4=tk.Label(text="# of matches: ")
        self.label4.grid(column=1, row=6)


        self.ventana1.mainloop()
    def get_data(self,matches):
        cadena = ""
        for el in matches: 
            cadena = cadena + el + "\n"
        return cadena        


    def ingresar(self):
        texto = self.scrolledtext2.get("0.0",tk.END)
        match = re.findall(self.entry1.get(),texto)
        while '' in match:
            match.remove('')
        self.scrolledtext3.insert(tk.INSERT, self.get_data(match))
        print(self.get_data(match))
        self.label4.configure(text="# of matches: "+str(len(match)))

    def replace(self):
        texto = self.scrolledtext2.get("0.0",tk.END)
        match = re.sub(self.entry1.get(),"aeape",texto)
        self.scrolledtext3.insert(tk.INSERT, match)


aplicacion1=Aplicacion()        