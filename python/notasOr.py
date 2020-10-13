print("Promedio comparación or")
nota4=int(input("Ingrese la nota 1 :"))
nota5=int(input("Ingrese la nota 2 :"))
nota6=int(input("ingrese la nota 3 :"))
total2=(nota4+nota5+nota6)/3
if total2 ==9 or total2 ==10:
    print("Excelente : " + str(total2))
elif total2 ==8 or total2 ==7:
    print("sobresaliente : " + str(total2))
elif total2 ==6:
    print("Bien : " + str(total2))
elif total2 ==5:
    print ("Aceptable: "  + str(total2))
else:
    print("Reprobado : " +str(total2))