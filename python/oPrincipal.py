# solicitar lista por consola, sumar todo, imprimir lista, el mayor y el menor

def cargar():
    lista=[]
    cantidad=int(input("Indique la cantidad de elementos que contendra la lista "))
    i=1
    while i<=cantidad:
        lista.append(int(input("Ingrese un valor: ")))
        i=i+1
    print("La lista ingresada es: ", lista)
    return lista

def suma(lista):
    suma=0
    for x in lista:
        suma=suma+x
    print("La suma de los elementos es: ", suma)
       
def mayor(lista):
    may=lista[0]
    for x in range(1,len(lista)):
        if lista[x]> may:
            may=lista[x]
    print("El número mayor de la lista es: ", may)

def menor(lista):
    men=lista[0]
    for x in range(1,len(lista)):
        if lista[x]< men:
            men=lista[x]
    print("El número menor es: ", men)