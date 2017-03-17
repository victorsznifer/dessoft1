
def maior(lista):
	a=lista[0]
	for i in range(len(lista)):
		if lista[i]>a:
		a=lista[i]
	return a
