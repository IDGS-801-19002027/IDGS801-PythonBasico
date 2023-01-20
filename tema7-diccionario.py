# Diccionarios: Permite almacenar diferentes tipos de datos a través de una key:value

miDiccionario = {"Matricula":12345, "Nombre":"Dario", "edad": 23}

print(type(miDiccionario))
print(miDiccionario)

miDiccionario["Nombre"]="Panfilo" # Modificar dato
print(miDiccionario)

print(miDiccionario["edad"]) # Imprimir solamente una llave:valor del diccionario
print(miDiccionario.values) # Imprimir solamente los valores
print(miDiccionario.keys()) # Imprimir solamente las llaves


