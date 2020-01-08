import random
import re

def desordenar_codigo(cadena):
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


cadena = "if \n agg\n gaaa\n else \n print\n for \n"
print(cadena)
print(desordenar_codigo(cadena)) 
