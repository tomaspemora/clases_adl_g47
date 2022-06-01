def estimar_tiempo(pizza):
	n_ingredientes = len(pizza['ingredientes'])
	return 20 + 2 * n_ingredientes

if __name__ == '__main__':
	pizza = {'masa': 'Tradicional',
			'salsa': 'Salsa Barbecue',
			'ingredientes': ['Queso']
			}
	print(estimar_tiempo(pizza))
	