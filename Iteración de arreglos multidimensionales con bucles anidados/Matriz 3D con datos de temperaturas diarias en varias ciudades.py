import random

# PARÁMETROS: CIUDADES, DÍAS Y SEMANAS
ciudades = 3
dias_semana = 7
semanas = 2

# NOMBRES DE DÍAS Y SEMANAS
nombres_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
nombres_semanas = ["Semana 1", "Semana 2"]
nombres_ciudades = ["Guayaqiuil", "Esmeraldas", "Machala"]

# MATRIZ 3D PARA ALMACENAR TEMPERATURAS
temperaturas = [[[random.uniform(15, 35) for _ in range(dias_semana)] for _ in range(semanas)] for _ in range(ciudades)]

# MOSTRAR LA MATRIZ 3D DE LAS TEMPERATURAS
print("Matriz 3D de Temperaturas:")
for semana_idx in range(semanas):
    print(f"\n{nombres_semanas[semana_idx]}:")
    for ciudad_idx in range(ciudades):
        print(f"  {nombres_ciudades[ciudad_idx]}:")
        for dia_idx in range(dias_semana):
            print(f"    {nombres_dias[dia_idx]}: {temperaturas[ciudad_idx][semana_idx][dia_idx]:.2f} °C")

# PROMEDIO DE TEMPERATURAS POR CIUDAD POR CADA SEMANA
for ciudad_idx in range(ciudades):
    print(f"\nPromedio de temperaturas para la {nombres_ciudades[ciudad_idx]}:")
    for semana_idx in range(semanas):
        suma_temperaturas = sum(temperaturas[ciudad_idx][semana_idx])
        promedio = suma_temperaturas / dias_semana
        print(f"  {nombres_semanas[semana_idx]}: {promedio:.2f} °C")
