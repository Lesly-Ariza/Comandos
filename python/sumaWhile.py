print("Sumará 10 valores ingresados por consola")
x=1
suma=0
while x<=10:
    valor=int(input("Ingrese el valor " + str(x)))
    suma=suma+valor
    x=x+1
promedio=suma/10
print("El promedio es : " + str(promedio))
print("La suma es : " + str(suma))
