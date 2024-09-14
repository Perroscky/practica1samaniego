def calcular_promedio_temperaturas(temperaturas_esmeraldas, temperaturas_guayaquil, temperaturas_machala):
#Esta línea define una nueva función llamada, esta función tomará tres listas de temperaturas como entrada, una para cada ciudad.

  # CANTIDAD DE SEMANAS
  if len(temperaturas_esmeraldas) != 4 or len(temperaturas_guayaquil) != 4 or len(temperaturas_machala) != 4:
    raise ValueError
#Aquí se verifica que cada lista de temperaturas tenga exactamente 4 elementos

  # CALCULO DE PROMEDIOS
  promedio_Esmeraldas = sum(temperaturas_Esmeraldas) / len(temperaturas_Esmeraldas)
  promedio_Guayaquil = sum(temperaturas_Guayaquil) / len(temperaturas_Guayaquil)
  promedio_Machala = sum(temperaturas_Machala) / len(temperaturas_Machala)
#Aqui cuanta los elementos, suma y divide para sacar el promedio

  # RETORNO DE RESULTADOS
  return {
    "Esmeraldas": promedio_Esmeraldas,
    "Guayaquil": promedio_Guayaquil,
    "Machala": promedio_Machala
  }
#Aqui la función devuelve un diccionario donde las claves son los nombres de las ciudades y los valores son los promedios de temperatura calculados

# TEMPERATURAS
temperaturas_Esmeraldas = [30, 32, 29, 28]
temperaturas_Guayaquil = [34, 30, 33, 35]
temperaturas_Machala = [29, 32, 28, 34]
#Aqui se detalla las temperaturas de las 4 semanas

# IMPRIME PROMEDIO DE TEMPERATURA DURANTE 4 SEMANAS
promedios = calcular_promedio_temperaturas(temperaturas_Esmeraldas, temperaturas_Guayaquil, temperaturas_Machala)
print(promedios)