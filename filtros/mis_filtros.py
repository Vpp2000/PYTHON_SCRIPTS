import re

def max_word(cadena):
	patron = "\w{4,}"
	matches = re.findall(patron,cadena)
	count = {}
	for match in matches:
		count.setdefault(match, 0)
		count[match] = count[match] + 1
	more_frequent = []
	maximo = max(count.values())
	for word,rep in count.items():
		if rep==maximo:
			more_frequent.append(word)
	    
	return more_frequent

def remove_tags(cadena):
	patron = "<[^>]*>"
	new = re.sub(patron,"",cadena)
	return new

def capital(cadena):
	return cadena.capitalize()
	
def SolToDol(cadena):
	conv = lambda x: str(float(x)*3.5)
	patron = "([Ss]\/\.)[\t ]*(\d+)"
	elementos = re.findall(patron,cadena)
	print(f"matches son {elementos}")
	for simbolo,cantidad in elementos:
		cadena = cadena.replace(simbolo,"$/.")
		cadena = cadena.replace(cantidad,conv(cantidad))

	return cadena

def aprobados(cadena):
    patron = "(\w+)[\t ]+(\d){1,2}"
    
def find_comments(cadena):    
    patron = "(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)"

print(max_word("Eresa una vez unas princesas con unas casas en unas pelicuas con unas buenas criticas"))
print(SolToDol("El pan cuesta S/. 45 y el atun cuesta s/. 2 tambien."))
