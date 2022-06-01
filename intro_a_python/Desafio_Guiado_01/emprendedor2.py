u1 = int(input("Ingrese el número de usuarios normales: "))
u2 = int(input("Ingrese el número de usuarios premium: "))
p1 = int(input("Ingrese el precio normal: "))
p2 = 1.5 * p1 # precio premium
gt = int(input("Ingrese el gasto total: "))

utilidades = u1*p1 + u2*p2 - gt

print(f'Las utilidades considerando usuarios premium es: ${int(utilidades)} ')