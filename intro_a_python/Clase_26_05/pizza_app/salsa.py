from utils import MENU_SALSA

def elegir_salsa(pizza, opcion):
	while opcion not in ['T', 'A', 'B', 'P']:
		print('Salsa no válida. Ingrese una salsa válida')
		opcion = input(MENU_SALSA).upper()
	else:
		if opcion == 'T':
			pizza['salsa'] = 'Salsa de Tomate'
		elif opcion == 'A':
			pizza['salsa'] = 'Salsa Alfredo'
		elif opcion == 'B':
			pizza['salsa'] = 'Salsa Barbecue'
		elif opcion == 'P':
			pizza['salsa'] = 'Salsa Pesto'
	return pizza


if __name__ == '__main__':
	import os
	os.system('cls')

	pizza = {'masa': 'Tradicional',
          'salsa': 'Salsa Barbecue',
          'ingredientes': ['Queso', 'Tomate', 'Peperoni', 'Pimiento', 'Champiñones', 'Aceitunas', 'Cebolla', 'Pollo', 'Pavo', 'Salchicha']
          }

	opcion = input(MENU_SALSA).upper()

	pizza = elegir_salsa(pizza, opcion)
	print(pizza)
