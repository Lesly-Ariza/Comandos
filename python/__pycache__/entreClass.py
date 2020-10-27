import random

opcion=int(input("Colaboracioón entre clases \n1- Banco \n2- Dados\n3- Club "))
#crear clase usuario (depositar,extraer,retornar monto,imprimir)
#clase banco(operar, depositos totales)
if opcion==1:
    class Cliente:
        def __init__(self, nombre):
            self.nombre=nombre
            self.monto=0
        
        def depositar(self,monto):
            self.monto=self.monto+monto

        def extraer(self,monto):
            self.monto=self.monto-monto

        def retornar_monto(self):
            return self.monto

        def imprimir(self):
            print(self.nombre," Tiene como saldo: ", self.monto) 

    class Banco:
        def __init__(self):
            self.cliente1=Cliente("Les")
            self.cliente2=Cliente("Mau")
            self.cliente3=Cliente("Ant")

        def operar(self):
            self.cliente1.depositar(100)
            self.cliente2.depositar(200)
            self.cliente3.depositar(300)

        def depositos_totales(self):
            total=self.cliente1.retornar_monto()+self.cliente2.retornar_monto(),self.cliente3.retornar_monto()
            print("El total de dinero del banco es: ", total)
            self.cliente1.imprimir()
            self.cliente2.imprimir()
            self.cliente3.imprimir()

    banco1=Banco()
    banco1.operar()
    banco1.depositos_totales()

elif opcion==2:  
      #lanzar 3 datos en caso de los 3 tener el mismo número gano de lo contrario perderá
    class Dados:
        print("se lanzarán 3 dados con resultados aleatorios, en caso de que los 3 tengan el mismo valor ganarás, de lo contrario perderás")
        def tirar(self):
            self.valor=random.randint(1,6)

        def imprimir(self):
            print("El valor es: ",self.valor)
        
        def retornar_valor(self):
            return self.valor
    
    class Jugar_dados:
        def __init__(self):
            self.dado1=Dados()
            self.dado2=Dados()
            self.dado3=Dados()

        def jugar(self):
                self.dado1.tirar()
                self.dado1.imprimir()
                self.dado2.tirar()
                self.dado2.imprimir()
                self.dado3.tirar()
                self.dado3.imprimir()
                if self.dado1.retornar_valor()==self.dado2.retornar_valor()and self.dado1.retornar_valor()==self.dado3.retornar_valor():
                    print("Ganaste")
                else:
                    print("Perdiste")
    
    jugar_dados=Jugar_dados()
    jugar_dados.jugar()
elif opcion==3:
    """Plantear una clase Club y otra clase Socio.
La clase Socio debe tener los siguientes atributos: nombre y la antigüedad en el club (en años).
En el método __init__ de la clase Socio pedir la carga por teclado del nombre y su antigüedad.
La clase Club debe tener como atributos 3 objetos de la clase Socio.
Definir una responsabilidad para imprimir el nombre del socio con mayor antigüedad en el club."""
    class Socio:
        def __init__(self):
            self.nombre=[]
            self.antiguedad=[]

        def cargar(self):
            continua="si"
            while continua == "si":
                nom=input("Ingrese el nombre del socio ")
                self.nombre.append(nom)
                antig=int(input("Ingrese en años la antiguedad del socio "))
                self.antiguedad.append(antig)
                continua=input("Desea ingresar otro socio: si/no")

        def imprimir(self):
            for x in range(len(self.nombre)):
                print("Nombre: ", self.nombre[x])

    class Club:
        def __init__(self):
            self.socio=Socio()

        def Mayor_antiguedad(self):
            self.socio.cargar()
            self.socio.imprimir()
            mayor=0
            for x in range(len(self.socio.antiguedad)):
                if self.socio.antiguedad[x]>mayor:
                    mayor=self.socio.antiguedad[x]
            print("El socio con mayor antiguedad es: ", self.socio.nombre[x], self.socio.antiguedad[x])

    club=Club()
    club.Mayor_antiguedad()
    
   