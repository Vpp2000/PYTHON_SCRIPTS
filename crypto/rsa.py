SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
print(len(SYMBOLS))


def text_to_number(string):
	global SYMBOLS
	blockInteger = 0
	ind = 0
	for i in string:
		blockInteger += SYMBOLS.index(i) * (len(SYMBOLS) ** ind)
		ind += 1
	return blockInteger


def encrypt(string,e,n):
	global SYMBOLS
	print(f'Texto sin encriptar:  {string}')
	nmr = text_to_number(string)
	print(f'Texto pasado a numero:  {nmr}')
	enc = pow(nmr,e,n)
	print(f'Texto encriptado: {enc}')
	return enc

def decrypt(nmr,d,n):
	global SYMBOLS
	nmr_dec = pow(nmr,d,n)
	print(f'Texto desencriptado: {nmr_dec}')
	return nmr_dec



# encoding howdy

texto = input("Texto:  ")
texto_encriptado = encrypt(texto,13805220545651593223,116284564958604315258674918142848831759)
texto_desencriptado = decrypt(texto_encriptado,72424475949690145396970707764378340583,116284564958604315258674918142848831759,len(texto))