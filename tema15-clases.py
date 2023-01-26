# Definimos una clase con la palabra reservada class
class OperasBas:
    # Propiedades de clase
    n1 = 0
    n2 = 0
    res =  0
    # Constructor de la clase
    def __init__(self, a,b):
        self.n1 = a
        self.n2 = b

    # Métodos de la clase
    def suma(self):
        self.res = self.n1 + self.n2
        print(self.res)
        
    def resta(self):
        self.res = self.n1 - self.n2
        print(self.res)
    
def main():
    obj=OperasBas(3,2)
    obj.suma()
    print("La suma es: {}".format(obj.res))

if __name__ == '__main__':
    main()