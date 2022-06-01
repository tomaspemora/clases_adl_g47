# Se importa el abecedario en minuscula y la librería para input de password
from string import ascii_lowercase
import getpass
# Se pide al usuario que ingrese su contraseña
password = getpass.getpass('Ingrese la contraseña: ').lower().replace('ñ','n')
intentos = 0
# Se itera sobre los caracteres del password
for letra_pass in password:
	# Se define un contador y se usa ese contador para ir iterando sobre las letras del abecedario
	contador_letra = 0
	letra_abc = ascii_lowercase[contador_letra]
	# mientras el caracter seleccionado del password no sea igual al caracter seleccionado del abecedario, sigue iterando y sumando uno a los intentos.
	while letra_pass != letra_abc:
		intentos += 1
		contador_letra+=1
		letra_abc = ascii_lowercase[contador_letra]
	intentos += 1 # este incremento adicional de la variable intentos se colocó porque el while donde se comparan las letras solo cuenta hasta antes de que encuentre la letra coincidente y hay que contar también la iteración donde se encontró.
# imprimir numero de intentos.
print(f'La contraseña fue forzada en {intentos} intentos')
