import pprint
# import pprint para imprimir arreglos mas ordenadamente
pp = pprint.PrettyPrinter(indent=4).pprint
recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
				['2021-05-01', "15:00", "No trabajar"],
				['2021-07-15', "13:00", "No hacer nada es feriado"],
				['2021-09-18', "16:00", "Ramadas"],
				['2021-12-25', "00:00", "Navidad"]]

# Output
print("::::::::::::ANTES:::::::::")
pp(recordatorios)

# Primer cambio
recordatorios.insert(1, ['2021-01-02','06:00','Empezar el Año.'])

# Segundo cambio
recordatorios[3][0] = '2021-07-16'

# Tercer cambio
recordatorios.pop(2)

# Cuarto cambio
recordatorios.insert(4,['2021-12-24', '22:00', 'Cena de Navidad'])
recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo'])

# Print de la lista recordatorios después de todos los cambios
print("::::::::::::DESPUES:::::::::")
pp(recordatorios)
