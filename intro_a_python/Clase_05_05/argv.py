import math
import sys

inputs = sys.argv # es un tipo de lista
g = float(inputs[1])
R = int(inputs[2])*1000
v_e = math.sqrt(2*g*R)
print(f'La velocidad de escape es {v_e:.1f}')
