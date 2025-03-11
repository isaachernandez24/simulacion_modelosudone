import random

def explorar_petróleo():
    """Simula una exploración petrolera con una probabilidad del 40% de éxito."""
    return random.random() < 0.40  # 40% de probabilidad de éxito

def calcular_ganancia():
    """Calcula la ganancia neta de una exploración exitosa."""
    barriles = 300000
    precio_por_barril = 150
    ingreso_total = barriles * precio_por_barril
    ganancia_empresa = ingreso_total * 0.60  # La empresa se queda con el 60%
    return ganancia_empresa

def simular_exploraciones(n):
    """Simula n exploraciones petroleras y analiza el umbral de éxito."""
    costo_exploracion = 1000000
    exitos = 0
    ganancia_total = 0
    
    for _ in range(n):
        if explorar_petróleo():
            exitos += 1
            ganancia_total += calcular_ganancia() - costo_exploracion
        else:
            ganancia_total -= costo_exploracion
    
    porcentaje_exito = (exitos / n) * 100
    print(f"Exploraciones exitosas: {exitos} de {n} ({porcentaje_exito:.2f}%)")
    print(f"Ganancia total después de {n} exploraciones: ${ganancia_total:,.2f}")
    
    umbral_exito = costo_exploracion / calcular_ganancia()
    print(f"Para no perder dinero, se necesita al menos un {umbral_exito * 100:.2f}% de éxito.")

# Ejecutar simulación con 1,000,000 de exploraciones
simular_exploraciones(1000000)
