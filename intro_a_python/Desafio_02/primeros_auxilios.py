# Con el diagrama de flujo ejemplicado, se define una pregunta de inicio y se van tomando decisiones de acuerdo a las respuestas del usuario a las preguntas (Sí o No):
# Además de definir el inicio del flujo, también se acota a las respuestas comprendidas en el ejemplo y se definen algunas variaciones probables del Sí y el No:
emergencia = input(f'¿Responde a estímulos (Si/No): ').lower()
while emergencia not in ['si', 's', 'no', 'n']:
	emergencia = input(f'Su respuesta anterior fue inválida indique solo sí o no: ¿Responde a estímulos (Si/No): ').lower()

# De aquí en adelante se van enumerando cada uno de los pasos a través de condiciones que reflejan la respuesta y la consecuente acción que se ejecuta:
if emergencia in ['si','s']:
	print(f'Valorar la necesidad de llevarlo al hospital más cercano')
	print(f'fin')
else:
	print(f'Abrir la vía área')
	respirar = input(f'¿Respirar? (Si/No): ').lower()
	while respirar not in ['si','s','no','n']:
		respirar = input(
			f'Su respuesta anterior fue inválida indique solo sí o no: ¿Respirar? (Si/No): ').lower()
	if respirar in ['s','si']:
		print(f'Permitirle posición de suficiente ventilación')
		print(f'fin')
	elif respirar in ['no','n']:
		print(f'Administrar 5 ventilaciones y llamar a ambulancia.')
		signos_vida = input(f'¿Signos de vida? (Si/No): ').lower()
		while signos_vida not in ['si', 's', 'no', 'n']:
			signos_vida = input(f'Su respuesta anterior fue inválida indique solo sí o no: ¿Respirar? (Si/No): ').lower()
		if signos_vida in ['si','s']:
			print(f'Reevaluar a la espera de la ambulancia')
		else:
			print(f'Administrar Compresiones Torácicas hasta que llegue ambulancia')
		llego_ambulancia = input(f'¿Llegó ambulancia? (Si/No): ').lower()
		while llego_ambulancia not in ['si', 's', 'no', 'n']:
			llego_ambulancia = input(f'Su respuesta anterior fue inválida indique solo sí o no: ¿Llegó ambulancia? (Si/No): ').lower()
		if llego_ambulancia in ['s','si']:
			print(f'La ambulancia llegó')
			print(f'fin')
		else:
			while llego_ambulancia in ['no','n']:
				signos_vida = input(f'¿Signos de vida? (Si/No): ').lower()
				while signos_vida not in ['si', 's', 'no', 'n']:
					signos_vida = input(f'Su respuesta anterior fue inválida indique solo sí o no: ¿Signos de vida? (Si/No): ').lower()
				if signos_vida in ['si', 's']:
					print(f'Reevaluar a la espera de la ambulancia')
				else:
					print(f'Administrar Compresiones Torácicas hasta que llegue ambulancia')
				llego_ambulancia = input(f'¿Llegó ambulancia? (Si/No): ').lower()
				while llego_ambulancia not in ['si', 's', 'no', 'n']:
					llego_ambulancia = input(
						f'Su respuesta anterior fue inválida indique solo sí o no: ¿Llegó ambulancia? (Si/No): ').lower()
				if llego_ambulancia in ['s', 'si']:
					print(f'La ambulancia llegó')
					print(f'fin')

	else:
		print(f'Respuesta inválida')
