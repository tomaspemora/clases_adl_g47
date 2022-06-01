
#En primer lugar se define la primera variable que considera el rut ingresado por el usuario:
rut = list(input("Ingresa tu rut sin puntos ni dígito verificador: ")) 

#Se define una segunda variable que corresponde a una lista de la serie númerica y un extend() para que la serie se vuelva a repetir (según el ejemplo):
serie = [2,3,4,5,6,7]
serie.extend(serie)

#Se invierte la variable rut de acuerdo al ejemplo
rut.reverse()                     


#Con las variables rut y serie ya definidas se construye la variable "módulo 11", realizando una iteración en la que se recorra cada elemento de "rut" 
#multiplicandolo por su par correspondiente de la serie.
#Luego se suma la lista con los productos, se obtiene el módulo al dividir por 11, y se sustrae de 11 (siguiendo el ejemplo del ejercicio):
módulo_11 = 11-(sum([int(rut[i]) * int(serie[i]) for i in range(len(rut))]) % 11)      

#Finalmente se definen las condiciones para el digito verificador, en función del valor obtenido de la variable anterior ("módulo_11"):
if módulo_11 == 10:
    print ("Su digito verificador es K")
elif módulo_11 == 11:
    print("Su digito verificador es 0")
else:
    print (f"Su digito verificador es {módulo_11}")





























