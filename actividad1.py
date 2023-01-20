tabla = [1,2,3,4,5,6,7,8,9,10]
num = int(input('Ingrese el valor a multiplicar: '))

for n in tabla:
    print("{} X {} = {}".format(num, n, (num * n)))

for n in range(1,11):
    print("{} X {} = {}".format(num, n, (num * n)))
    