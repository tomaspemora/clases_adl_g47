from string import ascii_lowercase
import getpass

from sqlalchemy import asc
password = getpass.getpass('Ingrese la contraseña: ').lower().replace('ñ','n')
intentos = 0

for letra_pass in password:
	contador_letra = 0
	letra_abc = ascii_lowercase[contador_letra]
	while letra_pass != letra_abc:
		print(f'letra_pass es : {letra_pass} y letra_abc es : {letra_abc}')
		intentos += 1
		contador_letra+=1
		letra_abc = ascii_lowercase[contador_letra]
	intentos += 1 # esta incremento adicional de la variable intentos se colocó porque el while donde se comparan las letras solo cuenta hasta antes de que encuentre la letra coincidente y hay que contar también la iteración donde se encontró.

print(f'La contraseña fue forzada en {intentos} intentos')
