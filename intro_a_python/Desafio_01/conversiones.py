import sys
inputs = sys.argv
# pos 0 conversiones.py pos 1 sol pos 2 ars pos 3 usd pos 4 clp

# Defino las variables que voy a imprimir, realizando las conversiones a numeros y las conversiones de divisa.
clp = int(inputs[4])
clp_sol = float(inputs[1]) * clp
clp_ars = float(inputs[2]) * clp
clp_usd = float(inputs[3]) * clp

# Imprimo las variables como se solicita.
print(f"Los {clp} pesos equivalen a:")
print(f"{clp_sol} Soles")
print(f"{clp_ars} Pesos Argentinos")
print(f"{clp_usd} Dólares")
