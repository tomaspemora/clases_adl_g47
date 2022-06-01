import math
g = float(input("Ingrese el valor de g: "))
r = int(input("Ingrese el valor de r: ")) * 1000
v_e = math.sqrt(2 * g * r)
print(f"La velocidad de escape es {v_e:.1f} [m/s] ")