def calcular_descuento(cantidad_total, porcentaje_descuento=10):
    # CALCULO DEL DESCUENTO CANTIDAD TOTAL
    descuento = (cantidad_total * porcentaje_descuento) / 100
    return descuento

# LLAMADAS A LA FUNCIÓN
# PRIMERA  LLAMADA: CANTIDAD TOTAL
cantidad1 = 300
descuento1 = calcular_descuento(cantidad1)
cantidad_final1 = cantidad1 - descuento1

print(f"Valor total: ${cantidad1:.2f}")
print(f"Descuento: ${descuento1:.2f} (10%)")
print(f"Valor a pagar: ${cantidad_final1:.2f}")

# SEGUNDA LLAMADA: CANTIDAD TOTAL Y PORCENTAJE DE DESCUENTO
cantidad2 = 500
porcentaje2 = 30
descuento2 = calcular_descuento(cantidad2, porcentaje2)
cantidad_final2 = cantidad2 - descuento2

print(f"\nValor total: ${cantidad2:.2f}")
print(f"Descuento: ${descuento2:.2f} ({porcentaje2}%)")
print(f"Valor a pagar: ${cantidad_final2:.2f}")