from utils import MENU_MASA

def elegir_masa(pizza, opcion):
	while opcion not in ['T', 'D', 'B']:
		print('Tipo de masa no válido. Ingrese una opción válida')
		opcion = input(MENU_MASA).upper()
	else:
		if opcion == 'T':
			pizza['masa'] = 'Traidicional'
		elif opcion == 'D':
			pizza['masa'] = 'Delgada'
		elif opcion == 'B':
			pizza['masa'] = 'Bordes de queso'
	return pizza


if __name__ == '__main__':
	import os
	os.system('cls')
	
	pizza = {'masa': 'Tradicional',
          'salsa': 'Salsa Barbecue',
          'ingredientes': ['Queso', 'Tomate', 'Peperoni', 'Pimiento', 'Champiñones', 'Aceitunas', 'Cebolla', 'Pollo', 'Pavo', 'Salchicha']
          }

	opcion = input(MENU_MASA).upper()
	pizza = elegir_masa(pizza, opcion)
	print(pizza)

