#RANDOM crea números aleatorios
import random
from math import sqrt as raiz, pow as exponente

def cargar():
    lista=[]
    for x in range(10):
        lista.append(random.randint(0,1000))
    return lista

def imprimir(lista):
    print(lista)
    
def mezclar(lista):
    random.shuffle(lista)

lista=cargar()
print("Lista generada aleatoriamente ")
imprimir(lista)
mezclar(lista)
print("Lista mezclada")
imprimir(lista)

def raizPotencia():
   
    print("A continuación se generará la raiz cuadrada y la potencia de un número")
    dato=int(input("-Ingrese un número entero: "))
    cuadrada=raiz(dato)
    cubo=exponente(dato,3)
    print("La raiz cuadrada de ", dato, " es: ", cuadrada)
    print("El número ", dato, "elevado a la potencia 3 es: ",cubo)
    return dato

dato=raizPotencia()    