def maior(lista):
	a=lista[0]
	for i in range(len(lista)):		
		if lista[i]>lista[i+1]:
			a=lista[i]
		return a