"""Una tupla permite tener agrupados un conjunto inmutable de elementos, es decir, en una tupla no es posible 
    agregar ni eliminar elementos. Las tuplas se declaran separando los elementos por comas y éstos, opcionalmente, 
    pueden ir entre paréntesis. Se recomienda el uso de paréntesis para evitar ambigüedades del tipo:
    print(9, 8, 7) y print((9, 8, 7)).

    TuplaDiasSemana = (“LU”, “MA”, “MI”, “JU”, “VI”, “SA”, “DO”)  # Declara tupla"""
def solicitarFecha():
    print("ingrese la fecha en el siguiente orden")
    dd=input("Ingrese el día: ")
    mes=input("ingrese el mes: ")
    anio=input("Ingrese el añio: ")
    tupla = (dd, mes, anio)
    return tupla
def imprimirFecha(fecha):
    print(fecha[0],fecha[1],fecha[2], sep="/" )

fecha=solicitarFecha()
imprimirFecha(fecha)

#combinación tupla y lista 
"""ingresar por consola país y cantidad de población, almacenarlo en una dupla,
imprimir los paises y la cantidad, indicar país con mayor población"""

def solicitarPais():
  paises=[]
  num=int(input("Indique la cantidad de paises que desea registrar: "))
  for x in range(num):
    pais=input("Ingrese el país: ")
    cant=input("Ingrese la cantidad de habitantes: ")
    paises.append((pais, cant))
  return paises

def imprimirPais(paises):
  print("paises y su población")
  for x in range(len(paises)):
    print(paises[x][0],paises[x][1])  

def masPoblacion(paises):
  may=0
  for x in range(1,len(paises)):
    if paises[x][1]>paises[may][1]:
      may=x
  print("El pais con mayor población es: ", paises[may][0])    

paises=solicitarPais()
imprimirPais(paises)
masPoblacion(paises)