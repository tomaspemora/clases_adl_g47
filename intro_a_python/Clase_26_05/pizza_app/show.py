def mostrar_ingredientes(pizza):
	print(f"Su masa es {pizza['masa']}")
	print(f"Su salsa es {pizza['salsa']}")
	print(f"Sus ingredientes son:")
	for ingrediente in pizza['ingredientes']:
		print(f"	- {ingrediente}")


if __name__ == '__main__':
	import os
	os.system('cls')
	pizza = {'masa': 'Tradicional',
			'salsa': 'Salsa Barbecue',
			'ingredientes': ['Queso', 'Tomate', 'Peperoni', 'Pimiento']
			}
	mostrar_ingredientes(pizza)
	