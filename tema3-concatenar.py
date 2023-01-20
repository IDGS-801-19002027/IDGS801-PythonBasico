# Concatenación de str

texto1 ="Hola"
texto2 = "Mundo!!"

# Tipos de concatenación 
textoFinal = texto1 + " " + texto2
print(textoFinal)

print("El saludo es: %s %s" % (texto1,texto2)) 

cadena = "Saludar dos: {0} {1} ".format(texto1, texto2) # {1-0} para seleccionar cual orden tomará la cadena
print(cadena)


