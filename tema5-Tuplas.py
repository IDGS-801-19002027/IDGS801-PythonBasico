# Dentro de una tupla no se puede remplazar los elementos, no se puede editar, es una constante
tupla = (1,2,3)
print(tupla)
print(type(tupla))

tupla2 = (7, "Roberto", True, 23.8, 16+7j)
print(tupla2[1])
print(tupla2[4]) # Imprimir el último elemento
print(tupla2[-1]) # Imprimir el último elemento

print(tupla2[0:3]) # Seleccionar un rango para mostrar dichos elementos de la tupla
print(tupla2[:3]) 

a, b, c = tupla # Cada elemento de la tupla se dividirá (asociará) en las variables declaradas
print(a)
print(b)
print(c)

tuplaN = tupla+tupla2 # Sumar tuplas
print(tuplaN)

print(tupla.count(2)) # El método de count cuenta el número de veces que se encuentra n elemento en la tupla

# tupla[2]=23 ERR- no se pueden editar, las tuplas son estáticas


