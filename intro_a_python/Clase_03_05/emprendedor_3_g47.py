p = int(input('Ingrese el precio: '))
u = int(input('Ingrese el número de usuarios: '))
gt = int(input('Ingrese el gasto total: '))
u_ant = int(input("""Ingrese las utilidades del año anterior\n(no puede ser 0): """))

utilidades_actuales = p*u - gt
razon = utilidades_actuales / u_ant
print(f'Las utilidades actuales son: ${int(utilidades_actuales)}')
print(f'La razón entre las utilidades es: {razon:.2f}')
