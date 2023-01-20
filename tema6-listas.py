# Listas: permiten diferentes tipos de datos

nombres = ["Juan", "Mario", "Laura"]
numeros = [1,2,3,4,5]

datos = [1,2.5,"Mario", True]

nombres[0] = "Roberto" # Sustituir el elemento de la lista
print(nombres)
print(nombres[2])
print(nombres[:3])
print(nombres[1:])

nombres.append("Dario") # Agrega un elemento al final de la lista
nombres.insert(2, "Laura") # Con el insert, asignamos la posición donde se agregará el elemento de la lista 

print(nombres)

nombres.extend(["chencha", 2, 23, 5]) # El extend agrega varios elementos dentro de la vista
print(nombres)
nombres.remove("chencha")
nombres.pop() # Eliminar el último elemento
print(nombres)

n = ["juan"]
n2 = n*5 # Múltiplica el elemento n veces 
print(n2)

del nombres[0] # Eliminar un elemento seleccionando una pos.
print(nombres)