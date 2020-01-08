def last_element(lista):
	return lista[len(lista)-1]



l1=[3,2,1]
win=[3,2,1]
l2=[]
l3=[]
dic = {1:l1,2:l2,3:l3}
print(dic)
while dic[3] != win:
	source = int(input("Desde: "))
	to = int(input("Hacia: "))
	if len(dic[source])>0:
		if len(dic[to])==0 or last_element(dic[source])<last_element(dic[to]): 
			dic[to].append(dic[source].pop())

	print(dic)