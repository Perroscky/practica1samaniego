def calcular_promedio_temperaturas(temperaturas_esmeraldas, temperaturas_guayaquil, temperaturas_machala):

  # CANTIDAD DE SEMANAS
  if len(temperaturas_esmeraldas) != 4 or len(temperaturas_guayaquil) != 4 or len(temperaturas_machala) != 4:
    raise ValueError

  # CALCULO DE PROMEDIOS
  promedio_Esmeraldas = sum(temperaturas_Esmeraldas) / len(temperaturas_Esmeraldas)
  promedio_Guayaquil = sum(temperaturas_Guayaquil) / len(temperaturas_Guayaquil)
  promedio_Machala = sum(temperaturas_Machala) / len(temperaturas_Machala)

  # RETORNO DE RESULTADOS
  return {
    "Esmeraldas": promedio_Esmeraldas,
    "Guayaquil": promedio_Guayaquil,
    "Machala": promedio_Machala
  }

# TEMPERATURAS
temperaturas_Esmeraldas = [30, 32, 29, 28]
temperaturas_Guayaquil = [34, 30, 33, 35]
temperaturas_Machala = [29, 32, 28, 34]

# IMPRIME PROMEDIO DE TEMPERATURA DURANTE 4 SEMANAS
promedios = calcular_promedio_temperaturas(temperaturas_Esmeraldas, temperaturas_Guayaquil, temperaturas_Machala)
print(promedios)