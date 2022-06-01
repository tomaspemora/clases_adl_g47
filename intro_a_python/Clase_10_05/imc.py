import sys

w = float(sys.argv[1])
h = float(sys.argv[2]) / 100

imc = w / h**2

if imc < 18.5:
	clasificacion = 'está Bajo peso'
elif imc < 25:
	clasificacion = 'está en peso Adecuado'
elif imc < 30:
	clasificacion = 'tiene Sobrepeso'
elif imc < 35:
	clasificacion = 'tiene Obesidad grado I'
elif imc < 40:
	clasificacion = 'tiene Obesidad grado II'
else:
	clasificacion = 'tiene Obesidad grado III'

print(f'El IMC es :{imc:.2f}')
print(f'Según la OMS la clasificación de su IMC indica que ud. {clasificacion}')

