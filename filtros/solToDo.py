# -*- coding: utf-8 -*-


import re
"""
def dolToSol(cadena):		
		numero = re.findall(r"([+-]?\d+(\.\d+)?)(\s*)(dolares|dólares|dolar|dólar)",cadena)		
		numero = ["{0:.2f}".format(float(a[0])*0.2958579881656805) for a in numero]			
		cadena = re.sub(r"([+-]?\d+(\.\d+)?)(\s*)(dolares|dólares|dolar|dólar)",
		lambda match: str(numero.pop(0)+" soles"),
		cadena)		

		numero = re.findall(r"\$\s*([+-]?\d+(\.\d+)?)",cadena)
		numero = ["{0:.2f}".format(float(a[0])*0.2958579881656805) for a in numero]		
		cadena = re.sub(r"\$\s*([+-]?\d+(\.\d+)?)",
		lambda match: str("S./ "+numero.pop(0)),
		cadena)
		
		return cadena
"""

def solToDol(cadena):
	numero = re.findall(r"(S\/\.|s\/\.)\s*([+-]?\d+(\.\d+)?)",cadena)
	print(numero)
	dinero = [(float(item[1])*3.25) for item in numero]
	print(dinero)
	cadena = re.sub(r"(S\/\.|s\/\.)\s*([+-]?\d+(\.\d+)?)",lambda match: "$ "+ str(dinero.pop(0)),cadena)

	return cadena	

#print(dolToSol("El pan cuesta $ 45 y el atun cuesta $ 2 tambien. Ademas el pollo cuesta $ 45.50"))

print(solToDol("El pan cuesta S/. 45 y el atun cuesta s/. 2 tambien. Ademas el pollo cuesta S/. 45.50"))

