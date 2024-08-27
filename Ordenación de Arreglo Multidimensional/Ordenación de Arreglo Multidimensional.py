def ordenar_fila(matriz, fila):
    # Implementación del algoritmo de ordenación (Bubble Sort en este caso)
    for i in range(len(matriz[fila])):
        for j in range(0, len(matriz[fila]) - i - 1):
            if matriz[fila][j] > matriz[fila][j + 1]:
                # Intercambiar los elementos
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]
    return matriz

# DEFINICION DE LA MATRIZ 3x3
matriz = [
    [101, 304, 700],
    [120, 910, 430],
    [280, 621, 810]
]

# FILA A ORDENAR
fila_a_ordenar = 1

# MOSTRAR MATRIZ ORIGINAL
print("Matriz original:")
for fila in matriz:
    print(fila)

# LLAMAMOS A LA FUNCION PARA ORDENAR LA FILA Y MOSTRAR EL RESULTADO
matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)

# MOSTRAR MATRIZ CION LA FILA ORDENADA
print("\nMatriz con la fila ordenada:")
for fila in matriz_ordenada:
    print(fila)
