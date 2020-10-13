# realizar ingreso de datos por consola
print("Datos de la primera persona")
nombreP=input("Ingrese nombre del cliente")
producto=input("Ingrese nombre del producto")
precioP =int(input("Ingrese el precio del producto"))
producto2=input("Ingrese nombre del producto 2")
precioP2=int(input("Ingrese el precio del producto"))
comparar=precioP>= precioP2
valor=precioP + precioP2
print("Cliente")
print(nombreP)
cabecera=("Producto 1.{0} valor : {1} \n Producto 2.{2} valor: {3}")
print(cabecera.format(producto,precioP,producto2,precioP2))
print("El producto 1 es mayor o igual al producto 2?")
print(comparar)
print("valor total")
print(valor)


