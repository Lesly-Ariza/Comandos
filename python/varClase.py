class Cliente:
    suspendidos=[]

    def __init__(self,codigo,nombre):
        self.codigo=codigo
        self.nombre=nombre

    def imprimir(self):
        print("Codigo: ",self.codigo)
        print("Nombre: ", self.nombre)
        self.esta_suspendido()

    def esta_suspendido(self):
        if self.codigo in Cliente.suspendidos:
            print("Esta suspendido")
            print("_____________________")
        else:
            print("No esta suspendido")
            print("_____________________")

    def suspender(self):
        Cliente.suspendidos.append(self.codigo)

cliente1=Cliente(1,"Juan")
cliente2=Cliente(2,"Camilo")
cliente3=Cliente(3,"Andres")
cliente4=Cliente(4,"Fernando")

cliente3.suspender()
cliente4.suspender()

cliente1.imprimir()
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()

print(Cliente.suspendidos)
