from masa import elegir_masa
from salsa import elegir_salsa
from agregar import agregar_ingrediente
from remover import remover_ingrediente
from show import mostrar_ingredientes
from tiempo import estimar_tiempo
from utils import MENU_REMOVER, MENU_AGREGAR, MENU_MASA, MENU_PRINCIPAL, MENU_SALSA
import os
os.system('cls')

pizza = {'masa': 'Tradicional',
        'salsa': 'Salsa Tomate',
        'ingredientes': ['Queso']
        }

print('Bienvenido a Pizza Jat')
while True:
    opcion = input(MENU_PRINCIPAL)
    if opcion.isnumeric():
        opcion = int(opcion)
        if opcion in list(range(0, 6)):
            if opcion == 1:
                eleccion = input(MENU_MASA)
                pizza = elegir_masa(pizza, eleccion)
            elif opcion == 2:
                eleccion = input(MENU_SALSA)
                pizza = elegir_salsa(pizza, eleccion)
            elif opcion == 3:
                while True:
                    eleccion = input(MENU_AGREGAR)
                    if eleccion.isnumeric():
                        eleccion = int(eleccion)
                        if eleccion in list(range(1, 10)):
                            pizza = agregar_ingrediente(pizza, eleccion)
                            break
            elif opcion == 4:
                while True:
                    eleccion = input(MENU_REMOVER)
                    if eleccion.isnumeric():
                        eleccion = int(eleccion)
                        if eleccion in list(range(1, 10)):
                            pizza = remover_ingrediente(pizza, eleccion)
                            break
            elif opcion == 5:
                tiempo = estimar_tiempo(pizza)
                print(f'Su pizza se preparará en {tiempo} minutos')
                ordenar = input('Desea ordenar ahora? S/N ').upper()
                if ordenar == 'S':
                    print('Gracias por ordenar  en Pizza Jat')
                    print('Disfrute su pizza')
                    exit()
            elif opcion == 0:
                mostrar_ingredientes(pizza)
                input()
        else:
            print('Ingrese una opción válida')
    os.system('cls')



