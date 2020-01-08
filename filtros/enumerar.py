
import re

def desordenar_codigo(cadena):
    patron = "[\S\t ]+\n?"


    matches = re.findall(patron,cadena)

    texto_new = ""


    for i in range(len(matches)):
        texto_new = texto_new+str(i+1)+" "+matches[i]    

    return texto_new


cadena = "if45 32 \n agg\n gaaa\n else \n\n print\n for \n"
print(cadena)
print(desordenar_codigo(cadena)) 
