def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"Valor {valor} encontrado en la posición ({i}, {j})"
    return f"Valor {valor} no encontrado en la matriz"

#DEFINICION DE LA MATRIX 3X3

matriz = [
    [101, 304, 700],
    [120, 910, 430],
    [280, 621, 810]
]

# VALOR A BUSCAR
valor_a_buscar = 910

# LLAMAMOS A LA FUNCION Y MOSTRAMOS EL RESULTADO
resultado = buscar_valor(matriz, valor_a_buscar)
print(resultado)