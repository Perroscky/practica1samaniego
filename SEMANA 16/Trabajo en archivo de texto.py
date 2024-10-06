# Parte 1
# ABRIR EL ARCHIVO 'my_notes.txt' EN MODO LECTURA
archivo = open('my_notes.txt', 'r')

# LEEMES EL ARCHIVO LINEA POR LINEA Y MUESTRO EL CONTENIDO
for linea in archivo:
    print(linea)

# CIERRO EL ARCHIVO
archivo.close()

# Parte 2:
# ESCRIBO EN EL ARCHIVO "my_notes1"
# ABRIMOS EL ARCHIVO EN MODO ESCRITURA ("w"), CREE EL ARCHIVO QUE NO EXISTIA
archivo_escritura = open('my_notes1.txt', 'w')

# ESCRIBO 3 LINEAS CON DEPORTES EN EL ARCHIVO
archivo_escritura.write("Futbol.\n")
archivo_escritura.write("Natacion.\n")
archivo_escritura.write("Bascket.\n")

# CERRAMOS EL ARCHIVO DE ESCRITURA
archivo_escritura.close()

# Parte 3: LEER EL ARCHIVO
# ABRO EL ARCHIVO EN MODO LECTURA ("r")
archivo_lectura = open('my_notes1.txt', 'r')

# LEEMOS EL ARCHIVO LINEA POR LINEA USANDO READLINE ()
while True:
    linea = archivo_lectura.readline()  # Leemos una línea
    if not linea:  # Si no hay más líneas, salimos del bucle
        break
    print(linea.strip())  # Mostramos la línea en la pantalla, eliminando saltos de línea

# CIERRO EL ARCHIVO DE LECTURA
archivo_lectura.close()
