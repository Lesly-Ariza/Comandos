#sumar,restar, multiplicar y dividir dos valores creando una función llamada Main
class Operaciones:

    def __init__ (self):
        self.valor1=0
        self.valor2=0

    def sumar(self):
        suma=self.valor1 + self.valor2
        print("Lasuma de los valores ingresados es: ",suma)

    def restar(self):
        resta=self.valor1-self.valor2
        print("La resta de los valores ingresados es: ",resta)

    def multiplicar(self):
        multi=self.valor1 * self.valor2
        print("La multiplicación de los valores ingresados es: ", multi)

    def dividir(self):
        if self.valor1 >=self.valor2:
            div=self.valor1/self.valor2
            print("La división de ", self.valor1," entre ",self.valor2, "es igual a: ", div)
        else:
            div=self.valor2/self.valor1
            print("La división de ", self.valor2, " entre ", self.valor1, " es igual a: ", div)

    def cargar(self):
        print("********************************")
        print("Se realizará las operaciones básicas con los valores ingresados")
        print("********************************")
        self.valor1=int(input("Ingrese el valor 1 "))
        self.valor2=int(input("Ingrese el valor 2 "))

    def main(self):
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()

operacion1=Operaciones()
operacion1.cargar()
operacion1.main()