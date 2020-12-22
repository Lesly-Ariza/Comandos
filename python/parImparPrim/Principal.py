import paresImpares

print("este programa identifica los números pares, impares y primos de una lista")
continua=1
while continua ==1:
    numero=paresImpares.Numeros()
    numero.cargar()
    opcion=int(input("Ingrese la opción que desea ver:\n1.Números pares \n2.Números impares \n3.Números primos "))
    if opcion==1:
        numero.pares()
        continua=int(input("0. para salir\n1.Volver al menu\n"))
    elif opcion ==2:
        numero.imPares()
        continua=int(input("0. para salir\n1.Volver al menu\n"))
    elif opcion ==3:
        numero.primos()
        continua=int(input("0. para salir\n1.Volver al menu\n"))
    else:
        print("La opción ingresada no es valida")
        continua=int(input("0. para salir \n1.Volver al menu\n "))

