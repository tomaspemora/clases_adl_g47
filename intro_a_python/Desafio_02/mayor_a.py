import sys
# En primer lugar se importa la libreria sys para poder ingresar los valores a través del terminal y se define la variable ventas (diccionario):
umbral = int(sys.argv[1]) 

ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}

#Se utiliza un python comprehension a través de la variable ventas_filtrado para poder determinar los meses que superen el umbral ingresado por el usuario al terminal
ventas_filtrado = {mes:venta for mes,venta in ventas.items() if venta > umbral}
print(ventas_filtrado)
