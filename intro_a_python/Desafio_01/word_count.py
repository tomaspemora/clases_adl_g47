with open("lorem_ipsum.txt", "r") as file:
	# Leo el archivo y lo almaceno en la variable texto como un string.
	texto = file.read()
# Creo una estructura set a partir del string texto que contiene el contenido de lorem_ipsum.txt. Este set contendrá todos los carácteres distintos del string.
caracteres_distintos = set(texto)
# Luego, imprimo el largo de ese set para mostrar el número de caracteres distintos.
print(f"El número de caracteres distintos es: {len(caracteres_distintos)}")
# Creo una estructura set a partir de la variable texto, pero separándola por espacios, de tal manera que contenga todas las palabras de lorem_ipsum.txt. Este set contendrá todas las palabras distintas del string.
palabras_distintas = set(texto.split(' '))
# Luego, imprimo el largo de ese set para mostrar el número de palabras distintas.
print(f"El número de palabras distintas es: {len(palabras_distintas)}")
