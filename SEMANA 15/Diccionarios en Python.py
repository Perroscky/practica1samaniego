#TRABAJANDO CON DICCIONARIOS EN PYTHON
#CREO UN DICCIONARIO LLAMADO información_personal QUE CONTIENE INFORMACIÓN FICTICIA SOBRE UNA PERSONA.
informacion_personal = {
    "nombre": "Pepe Zarate",
    "edad": 40,
    "ciudad": "Guayaquil",
    "profesion": "Mecanico",
    "deporte favorito": "futbol",
}

# INGRESO AL VALOR ASOCIADO CON LA CLAVE "ciudad"
ciudad_actual = informacion_personal["ciudad"]
print(f"La ciudad actual es: {ciudad_actual}")

# MODIFICO EL VALOR ASOCIADO CON LA CLAVE "ciudad"
informacion_personal["ciudad"] = "Esmeraldas"
print(f"La ciudad nueva es: {informacion_personal['ciudad']}")

# AGREGO UNA NUEVA CLAVE-VALOR AL DICCIONARIO MISMO REPRESENTA LA "profesion" DE PEPE ZARATE
informacion_personal["profesion"] = "Ingeniero Automotriz"
print(f"La profesión actual es: {informacion_personal['profesion']}")

# VERIFICO SI LA CLAVE "telefono" EXISTE EN EL DICCIONARIO
if "celular" not in informacion_personal:
    informacion_personal["celular"] = "0996229789"
    print("Se agrego la clave 'celular' con un número de celular ficticio")

# ELIMINO LA CLAVE "edad" DEL DICCIONARIO
del informacion_personal["edad"]
print("Se elimino la clave 'edad' del diccionario")

#IMPRIMO EL DICCIONARIO FINAL CON LOS CAMBIOS EFECTUADOS
print("diccionario final:")
print(informacion_personal)
