class operacion:
    def __init__(self):
        self.valor1=0
        self.valor2=0
        self.resultado=0

    def cargar(self):
        self.valor1=int(input("Ingrese el valor 1 "))
        self.valor2=int(input("Ingrese el valor 2 "))

    def imprimir(self):
        print(self.resultado)

class suma(operacion):
    def sumar(self):
        self.resultado=self.valor1+self.valor2

class resta(operacion):
    def restar(self):
        self.resultado=self.valor1-self.valor2

sumar1=suma()
sumar1.cargar()
sumar1.sumar()
print("La suma de los valores es: ")
sumar1.imprimir()

restar1=resta()
restar1.cargar()
restar1.restar()
print("La resta de los valores es: ")
restar1.imprimir()

