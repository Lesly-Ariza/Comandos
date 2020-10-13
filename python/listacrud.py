lista=[]
cantidad=int(input("ingrese la cantidad de elementos que desea registrar"))
i=1
while i <= cantidad:
    #append agrega elementos en la siguiente posición
    lista.append(input("Ingrese el valor : "))
    i= i+1
#end permite imprimir los valores en una misma linea
print(lista, end=',')
print("Elija una de las siguientes opciones")
opcion=int(input("1. Modificar \n2. Agregar \n3.Eliminar \n4.Buscar"))
if opcion ==1:
    indice=int(input("\n Ingrese el indice del elemento a modificar"))
    indice= indice-1
    valor=input("Ingrese el nuevo valor")
    lista[indice]=valor
    print("los elementos de la lista son : ", str(lista), end=',')
elif opcion ==2:
    indice=int(input("\n Ingrese el indice del elemento a agregar"))
    indice= indice-1
    valor=input("Ingrese el valor")
    lista.insert(indice, valor)
    print(lista, end=',')
elif opcion ==3:
    valor=input("\n Ingrese el valor del elemento a eliminar")
    lista.remove(valor)
    print("los elementos de la lista son : ", str(lista), end=',')
elif opcion ==4:
    valor=input("\n Ingrese el valor del elemento a buscar")
    resultado = (valor in lista)
    if resultado:
        print("El indice del elemento es: ", str((lista.index(valor)+1)))
    else:
        print("el elemento no existe en la lista")
else:
    print("Esta opción no esta disponible")