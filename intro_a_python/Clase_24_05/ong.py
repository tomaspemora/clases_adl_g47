
def productoria(lista):
	# El factorial(n) no es más que la productoria la de lista de 1 a n
	resultado = 1
	for numero in lista:
		resultado *= numero
	return resultado

def calcular(**operaciones):
	for k,v in operaciones.items():
		if 'fact' in k and isinstance(v,int):
			print(f'El factorial de {v} es {productoria(range(1,v+1))}')
		elif 'prod' in k and isinstance(v,list):
			print(f'La productoria de {v} es {productoria(v)}')
		else:
			print(f'Hay una operación no válida definida como {k}')


calcular(fact_1=5, prod_1=[3, 6, 4, 2, 8], fact_2=6)
# print(factorial(5))