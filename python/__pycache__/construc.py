#ingresar por consola (nombre, salario, imprimir y validar si debe o no pagar impuesto despues de 300)
class Usuario:

    def __init__ (self):
        self.nombre=""
        self.salario=0

    def cargar(self):
        self.nombre=input("Ingrese el nombre de usuario ")
        self.salario=float(input("Ingrese el salario del usuario "))

    def imprimir(self):
        print("Usuario: ",self.nombre)
        print("Salario: ", self.salario)
    
    def impuesto(self):
        if self.salario >= 300:
            print("El usuario debe pagar impuesto")
        else:
            print("El usuario no debe pagar impuesto")

persona1=Usuario()
persona1.cargar()
persona1.imprimir()
persona1.impuesto()