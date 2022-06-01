# Se obtiene la entrada del usuario a través de input y se valida si es un numero entero. 
rut = input("Ingrese su rut sin puntos ni dígito verificador: ")
while not rut.isnumeric():
	# Si no es valida, se vuelve a preguntar hasta que el usuario ingrese un rut valido
	rut = input("Entrada incorrecta. Ingrese su rut sin puntos ni dígito verificador (solo numeros): ")
# Se transforma la entrada desde un string a una lista de numeros enteros. Cada elemento de la lista será un digito del rut.
rut_numerico = [int(x) for x in list(rut)]
# Se crea una lista con la serie numerica que se usara para aplicar el algoritmo
serie_numerica = [2, 3, 4, 5, 6, 7]
serie_numerica.extend(serie_numerica)
# Se itera conjuntamente sobre el rut y la serie numerica extendida. Sobre el rut iteramos en reversa, tal como lo indica el algoritmo.
# Luego se suma todo lo obtenido.
dv = sum(s*r for (s,r) in zip(serie_numerica,rut_numerico[::-1]))
# Se calcula el módulo 11 de la suma acumulada
dv = dv % 11
# Se reparan los casos de dv = k y dv = 0
dv = 0 if 11 - dv == 11 else 'k' if 11 - dv == 10 else 11 - dv
# Se imprime el rut completo con digito verificador incluido
print(f'El rut completo es: {rut}-{dv}')