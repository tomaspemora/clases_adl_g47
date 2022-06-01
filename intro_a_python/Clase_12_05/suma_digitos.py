# te doy un numero por ejemplo 5432
# 5 + 4 + 3 + 2 = 14

# Nivel sencillo
# n = input(f'Ingrese un numero ')
# suma = 0
# for letter in n:
# 	suma += int(letter)
# print(f'La suma de los dígitos es: {suma}')

# Segundo approach
# n = input(f'Ingrese un numero ')
# largo = len(n)
# suma = 0
# suma_alt = 0
# lista = []
# for item in range(largo - 1, -1, -1):
# 	suma += int(n[item])
# 	# print(int(int(n)/10**item))
# 	val = int(int(n)/10**item)
# 	lista.append(val)
# 	suma_alt = int(suma_alt)-val*10**item
# 	print(val * 10 ** item)
# print(f'La suma de los dígitos es: {suma}')
# print(f'La suma de los dígitos es: {lista}')

# tercer approach
n = input(f'Ingrese un numero ')
print(f'La suma de los dígitos es: {sum([(int(i)) for i in n])}')
