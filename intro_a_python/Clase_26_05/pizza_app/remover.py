from utils import MENU_REMOVER

def remover_ingrediente(pizza, opcion):
	ingredientes = ['Tomate', 'Champiñones', 'Aceituna',
                 'Cebolla', 'Pollo', 'Jamón', 'Carne', 'Tocino', 'Queso']
	ingrediente_remover = ingredientes[opcion-1]
	if len(pizza['ingredientes']) == 0:
		print('No hay ingredientes para remover')
	else:
		if ingrediente_remover not in pizza['ingredientes']:
			print('Tu pizza no tiene ese ingrediente')
		else:
			pizza['ingredientes'].remove(ingrediente_remover)
	return pizza


if __name__ == '__main__':

	pizza = {'masa': 'Tradicional',
          'salsa': 'Salsa Barbecue',
          'ingredientes': ['Queso']
          }

	while True:
		opcion = input(MENU_REMOVER)
		if opcion.isnumeric():
			opcion = int(opcion)
			if opcion in list(range(1, 10)):
				break
		print('Ingrese una opción válida')

	print(remover_ingrediente(pizza, opcion))
