nota1=int(input("Ingrese la nota 1 :"))
nota2=int(input("Ingrese la nota 2 :"))
nota3=int(input("ingrese la nota 3 :"))
total=(nota1+nota2+nota3)/3
if total >=7:
    print("Aprobado : " + str(total))
else:
    if total >=4:
        print("Aceptable : " + str(total))
    else:
        print("Reprobado : " + str(total))

