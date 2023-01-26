import os

class OperasBas:
    def __init__(self, a, b):
        self.n1 = a
        self.n2 = b

    def suma(self): 
        self.res = self.n1 + self.n2
        return self.res

    def resta(self):
        self.res = self.n1 - self.n2
        return self.res

    def multiplicacion(self):
        self.res = self.n1 * self.n2
        return self.res

    def division(self): 
        self.res = self.n1 / self.n2
        return self.res

def main():
    opt = 5
    while opt != -1:
        
        if (opt == 0):
            print('Adiós')
            break
        #os.system('clear')

        else:
            print("Ingrese alguna de las siguientes opciones:")
            opt = int(input('1. -Suma\n 2.- Resta\n 3.- Multiplicación\n 4.- División\n 0.- Salir \n'))
            n1 = int(input('Ingrese el primer número: '))
            n2 = int(input('Ingrese el segundo número: '))
            ob = OperasBas(n1,n2)
            if (opt == 1):
                res = ob.suma()
            elif (opt == 2):
                res = ob.resta()
            elif (opt == 3):
                res = ob.multiplicacion()
            elif (opt == 4):
                res = ob.division()
            print('El resultado de la operación es: {}'.format(res))

if __name__ == '__main__':
    main()
    
  