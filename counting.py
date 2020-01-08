from pprint import pprint

texto = input("Ingresa algo: ")
count = {}
for match in texto:
	count.setdefault(match, 0)
	count[match] = count[match] + 1

pprint(count)