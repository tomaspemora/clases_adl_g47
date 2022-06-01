import sys

precios = {'Notebook': 700000,
           'Teclado': 25000,
           'Mouse': 12000,
           'Monitor': 250000,
           'Escritorio': 135000,
           'Tarjeta de Video': 1500000}


umbral = int(sys.argv[1])

def filtrar(precios, umbral, mayor_que = True):
	if mayor_que:
		output = [k for k,v in precios.items() if v > umbral]
		print(f'Los productos mayores al umbral son: {", ".join(output)}')
	else:
		output = [k for k,v in precios.items() if v < umbral]
		print(f'Los productos menores al umbral son: {", ".join(output)}')


if len(sys.argv) == 2:
	filtrar(precios, umbral, mayor_que=True)
elif len(sys.argv) == 3 and sys.argv[2] == 'menor':
	filtrar(precios, umbral, mayor_que=False)
elif len(sys.argv) == 3 and sys.argv[2] == 'mayor':
	filtrar(precios, umbral, mayor_que=True)
else:
	print('Lo sentimos, no es una operación válida')

