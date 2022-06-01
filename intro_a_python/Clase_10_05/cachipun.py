import sys
import random

jugador = sys.argv[1].lower()
mano = ['papel', 'piedra', 'tijera']

if jugador not in mano:
	print(f"Argumento inválido: Debe ser: {', '.join(mano[:-1])} o {mano[-1]}")
else:
	print(f'Tu jugaste {jugador}')
	computador = random.choice(mano)
	print(f'Computador jugó {computador}')
	if jugador == computador:
		print("Empate")
	elif (jugador == 'papel' and computador == 'piedra') or \
		(jugador == 'piedra' and computador == 'tijera') or \
		(jugador == 'tijera' and computador == 'papel'):
		print('Ganaste!!')
	else:
		print('Perdiste!!')