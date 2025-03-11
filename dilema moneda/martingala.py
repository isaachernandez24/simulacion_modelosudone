import random

def lanzar_dado():
    return random.randint(1, 6)  # Número entre 1 y 6

def lanzar_moneda():
    return random.choice(['cara', 'cruz'])  # Cara o cruz

def jugar_ronda():
    dado = lanzar_dado()
    moneda = lanzar_moneda()
    return moneda == 'cara' and dado % 2 == 0  # Ganas si es cara y número par

def estrategia_martingala(saldo_inicial, apuesta_inicial, rondas):
    saldo = saldo_inicial
    apuesta = apuesta_inicial
    for i in range(rondas):
        if saldo < apuesta:
            print("Saldo insuficiente para continuar la estrategia.")
            break
        
        resultado = jugar_ronda()
        if resultado:
            saldo += apuesta  # Ganas la apuesta
            apuesta = apuesta_inicial  # Reinicias la apuesta
        else:
            saldo -= apuesta  # Pierdes la apuesta
            apuesta *= 2  # Duplicas la apuesta
        
        print(f"Ronda {i+1}: Saldo = {saldo}, Apuesta = {apuesta}")
    return saldo

def probar_probabilidad(intentos):
    exitos = sum(jugar_ronda() for _ in range(intentos))
    probabilidad = (exitos / intentos) * 100
    print(f"Probabilidad de ganar basada en {intentos} intentos: {probabilidad:.2f}%")

# Parámetros iniciales
saldo_final = estrategia_martingala(saldo_inicial=100, apuesta_inicial=1, rondas=10)
print(f"Saldo final después de la estrategia: {saldo_final}")

# Probar la tasa de éxito sin el sistema de apuestas
probar_probabilidad(10000)
