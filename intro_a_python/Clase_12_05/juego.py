import sys,os
import random
os.chdir(sys.path[0])
jugador = sys.argv[1].lower()
mano = ['papel', 'piedra','tijera']
while jugador not in mano:
	jugador = input(f"Argumento inválido. Debe ingresar {', '.join(mano[:-1])} o {mano[-1]}: ")
else:
	computador = random.choice(mano)
	print(f'Tu jugaste jugador {jugador}')
	print(f'El computador jugó: {computador}')

	if jugador == computador:
		print('Empate')
	elif (jugador == 'tijera' and computador == 'papel') or \
		(jugador == 'piedra' and computador == 'tijera') or \
		(jugador == 'papel' and computador == 'piedra'):
		print('Ganaste!!')
	else:
		print('Perdiste!!')