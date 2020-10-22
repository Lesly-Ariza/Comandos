print("Se realiza muestra de los diferentes tipos de funciones")
opcion=int(input("Seleccione la opción que desea: \n 1. Parametros\n 2. Retorno de datos\n 3. Parametros por defecto u omisión \n 4. Parametros arbitrarios \n 5. Parametros de lista \n 6. Retorno de lista \n 7. Parametros tipo lista: "))
if opcion ==1:
    #PARAMETROS
    def mostrarMensajes(mensaje):
        print("*****************")
        print(mensaje)
        print("*****************")
    def sumar():
        valor1=int(input("Ingrese el valor 1: "))
        valor2=int(input("Ingrese el valor 2: "))
        sum=valor1+valor2
        print("la suma de los valores es: ", str(sum))
    mostrarMensajes("sumará dos valores ingresados por consola")
    sumar()
elif opcion==2:
    #RETORNO DE DATOS
    def areaCuadrado(lado):
        area=lado*lado
        return area
    print("*******************")
    print("Calculará el area de un cuadrado")
    print("*******************")
    va=int(input("Ingrese el lado del cuadrado: "))
    superficie=areaCuadrado(va)
    print("El area del cuadrado es: ", str(superficie))
elif opcion==3:
    #PARAMETRO POR DEFECTO U OMISIÓN
    def saludar(nombre, mensaje="hola"):
        print(mensaje, nombre)
    saludar("Lesly")
    #saludar("lesly", "Buenos días")
elif opcion ==4:
    #PARAMETROS ARBITRARIOS
    print("*******************")
    print("Sumar valores sin limite")
    print("*******************")

    def sumarLista(v1, v2, *lista):
        suma1=v1+v2
        for x in range(len(lista)):
            suma1=suma1+lista[x]
        return suma1
    print("suma de dos valores")
    print(sumarLista(1, 2))
    print("suma de cuatro valores")
    print(sumarLista(1, 2, 3, 4))
    print("suma de diez valores")
    print(sumarLista(1, 2, 3, 4, 5, 6, 7, 8, 9, 0))
elif opcion ==5:
    #PARAMETROS DE LISTA
    def suma2(lista):
        suma3=0
        for x in range(len(lista)):
            suma3=suma3+lista[x]
        return suma3
    def mayor(lista):
        mayor=lista[0]
        for x in range(len(lista)):
            if lista[x]>mayor:
                mayor=lista[x]
        return mayor
    def menor(lista):
        menor=lista[0]
        for x in range(len(lista)):
            if lista[x]<menor:
                menor=lista[x]
        return menor 
    listaValores=[10, 20, 30, 40, 50, 60, 70] 
    print("*******************")
    print("Parametros de lista")
    print("*******************")
    print("Lista completa ")
    print(listaValores)
    print("La suma de los valores es: ", suma2(listaValores))
    print("El número mayor es: ", mayor(listaValores))
    print("El número menor es: ", menor(listaValores))
elif opcion ==6:
    #RETORNO DE LISTA 
    def cargar_lista():
        li=[]
        for x in range(5):
            valor=int(input("Ingrese el valor: "))
            li.append(valor)
        return li
    def imprimir(li):
        ("Los números  mayores a 10 son : ")
        for x in range(len(li)):
            if li[x]>10:
                print(li[x], end=', ')
    print("*******************")
    print("Ingrese 5 números y se validará cuales son mayores a 10")
    print("*******************")
    lista=cargar_lista()
    imprimir(lista)

elif opcion ==7:
    #FUNCION PARAMETROS TIPO LISTA
    
    def suma4(lista):
        suma= 0
        for x in range(len(lista)):
            suma=suma+lista[x]
        return suma

    def mayor(lista):
        mayor=lista[0]
        for x in range(1,len(lista)):
            if lista[x]>mayor:
                mayor=lista[x]
        return mayor

    def menor(lista):
        menor=lista[0]
        for x in range(1, len(lista)):
            if lista[x] < menor:
                menor=lista[x]
        return menor
    datos=[12,13,14,15,23,45,60]
    print("Los valores de la lista son: ", datos)
    print("La suma de los valores es: ", suma4(datos))
    print("El número mayor es: ", mayor(datos))
    print("El número menor es: ", menor(datos))
            
else:
    print("La opción selecionada no existe")