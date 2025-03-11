import random

def decision_prisionero():
    return random.choice(["callar", "confesar"])

def simular_dilema():
    prisionero1 = decision_prisionero()
    prisionero2 = decision_prisionero()
    
    if prisionero1 == "callar" and prisionero2 == "callar":
        condena1, condena2 = 1, 1
    elif prisionero1 == "confesar" and prisionero2 == "confesar":
        condena1, condena2 = 5, 5
    elif prisionero1 == "confesar" and prisionero2 == "callar":
        condena1, condena2 = 0, 20
    else:  # prisionero1 calla y prisionero2 confiesa
        condena1, condena2 = 20, 0
    
    print(f"Prisionero 1 decide {prisionero1}, Prisionero 2 decide {prisionero2}")
    print(f"Condena: Prisionero 1 = {condena1} años, Prisionero 2 = {condena2} años")
    
    return condena1, condena2

# Simulación de múltiples rondas
def simular_varias_veces(n):
    resultados = {"(callar, callar)": 0, "(confesar, confesar)": 0, "(confesar, callar)": 0, "(callar, confesar)": 0}
    
    for _ in range(n):
        prisionero1 = decision_prisionero()
        prisionero2 = decision_prisionero()
        clave = f"({prisionero1}, {prisionero2})"
        resultados[clave] += 1
    
    print("Resultados tras", n, "simulaciones:")
    for key, value in resultados.items():
        print(f"{key}: {value} veces ({(value/n)*100:.2f}%)")

# Ejecución de una simulación individual
simular_dilema()

# Ejecución de múltiples simulaciones
simular_varias_veces(10000)
