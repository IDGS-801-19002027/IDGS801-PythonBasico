num1 = 20
num2 = 0


# Estructura de una excepción en python: Try-Except
try:
    tem = num1/num2
except ZeroDivisionError:
    print("Error en el programa")
finally:
    print("Siempre aparezco")