# Métodos para cadenas (str)

cadena = "universidad Tecnológica de León"

print(cadena)

print(cadena.lower()) # Convierte el texto completo a minúsculas
print(cadena.upper()) # Convierte el texto completo a mayúsculas
print(cadena.title()) # Convierte la primera letra de una palabra a mayúsculas

print(cadena.find("de")) 
print(cadena.count("a")) # Contar cuántas letras se repiten en el texto

textoFinal = cadena.replace("a", "4") # Remplazar un caracter por otro
print(textoFinal)

cadenaNueva = cadena.split(" ") # Separación en palabras de una cadena en un array
print(cadenaNueva)