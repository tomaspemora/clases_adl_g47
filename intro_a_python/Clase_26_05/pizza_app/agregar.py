from utils import MENU_AGREGAR

def agregar_ingrediente(pizza, opcion):
	ingredientes = ['Tomate', 'Champiñones', 'Aceituna', 'Cebolla', 'Pollo', 'Jamón', 'Carne', 'Tocino', 'Queso']
	nuevo_ingrediente = ingredientes[opcion-1]
	if nuevo_ingrediente in pizza['ingredientes']:
		print('Ese ingrediente ya es parte de tu pizza')
	else:
		pizza['ingredientes'].append(nuevo_ingrediente)
	return pizza

if __name__ == '__main__':
	
	pizza = {'masa': 'Tradicional',
			'salsa': 'Salsa Barbecue',
			'ingredientes': ['Queso']
			}

	while True:
		opcion = input(MENU_AGREGAR)
		if opcion.isnumeric():
			opcion = int(opcion)
			if opcion in list(range(1, 10)):
				break
		print('Ingrese una opción válida')

	print(agregar_ingrediente(pizza, opcion))