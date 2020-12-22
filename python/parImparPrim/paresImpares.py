class Numeros:
    def __init__(self):
        self.lista=[]
        self.numInicio=int(input("Ingrese el número inicial de la lista "))
        self.numFinal=int(input("Ingrese el número final de la lista "))
        self.lista.append(self.numInicio)

    def cargar(self):
        for self.numInicio in self.lista:
            if self.numInicio<self.numFinal:
                self.numInicio=self.lista.append(self.numInicio + 1)
        print("La lista es: ",self.lista)

    def pares(self):
        par=[]
        for self.numInicio in self.lista:
            if self.numInicio%2==0:
                par.append(self.numInicio)
        print(par)
            
    def imPares(self):
        imPar=[]
        for self.numInicio in self.lista:
            if self.numInicio%2==1:
                imPar.append(self.numInicio)
        print(imPar)

    def primos(self):
        primo=[]
        for self.numInicio in range(2,len(self.lista)):
            for i in range(2,self.numInicio):
                if self.numInicio%i !=0:
                    continue
                else:
                    break
            else:
                primo.append(self.numInicio)
        print(primo)
                



"""
datos postulante 
nombre sin números o simbolos
apellido
documento
celular
altura peso
"""