print("cuantas piezas cumplen con las caracteristicas")
x=1
cantidad=int(input("Ingrese la cantidad de piezas a evaluar : "))
while x <=cantidad:
    pieza=float(input("Ingrese la medida de la pieza " + str(x) + " : "))
    x=x+1
    if pieza<=1.3 and pieza>=1.2:
        print("la pieza cumplen con la condición ")
    else:
            print("La pieza no cumple con las condiciones")


#---------fibonacci

a, b = 0, 1
while a<10:
    print( a, end=",")
    a, b = b, a+b