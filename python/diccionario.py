""" Los diccionarios son objetos que contienen una lista de parejas de elementos. 
De cada pareja un elemento es la clave, que no puede repetirse, y, el otro, un valor asociado. 
La clave que se utiliza para acceder al valor tiene que ser un dato inmutable como una cadena, 
mientras que el valor puede ser un número, una cadena, un valor lógico (True/False), una lista o una tupla.

Los pares clave-valor están separados por dos puntos, las parejas por comas y todo el conjunto se encierra entre llaves.

Ejemplos:

capitales = {'Chile':'Santiago', 'España':'Madrid', 'Francia':'París'}

Para definir un diccionario vacío hay dos opciones:

capitales = {}
capitales = dict() """
opcion=int(input("Ingrese la opción que desea ver:\n 1. Datos tipo diccionario.\n 2. Tipo de datos lista, tupla y diccionario \n 3. Porciones de listas, tuplas y cadenas"))
if opcion == 1:
    #estructura de datos tipo diccionario
    """crear un diccionario en español a ingles donde español sea la llave, al ingresar los datos se 
    preguntará si desea agreagr otra palabra o si desea salir, imprimir dicicionario completo, consultar si la palabra existe"""

    def cargar():
        diccionario={}
        continua="s"
        while continua =="s":
            esp=input("Ingrese la palabra en español: ")
            ing=input("Ingrese su significado en ingles: ")
            diccionario[esp]=ing
            continua=input("Desea agregar otra palabra:s/n")
        return diccionario

    def imprimir(diccionario):
        print("Listado completo del diccionario")
        for ingles in diccionario:
            print(ingles,diccionario[ingles])

    def buscar(diccionario):
        pal=input("Ingrese la palabra que desea consultar: ")
        if pal in diccionario:
            print("En ingles significa: ", diccionario[pal])


    diccionario=cargar()
    imprimir(diccionario)
    buscar(diccionario)

elif opcion ==2:
    """Permite cargar un codigo de producto como clave en un diccionario. Guardar para dicha clave 
    el nombre del producto, su precio y cantidad en stock"""

    def cargar():
        productos={}
        continua="si"
        while continua =="si":
            codigo=int(input("Ingrese el codigo del producto: "))
            nombre=input("Ingrese el nombre del producto: ")
            precio=float(input("Ingrese el precio del producto: "))
            stock=int(input("Ingrese la cantidad del producto: "))
            productos[codigo]=(nombre, precio, stock)
            continua=input("¿Desea ingresar otro producto? si/no: ")
        return productos

    def imprimir(productos):
        for codigo in productos:
            print("Producto: ",productos[codigo][0],"| Precio: ",productos[codigo][1],"| Stock:" , productos[codigo][2])

    def consulta(productos):
        busc=int(input("Indique el codigo del producto que desea consultar: "))
        if busc in productos:
            print("El producto con codigo: ", busc, "es: ")
            print("Producto: ",productos[busc][0], "| Precio: ",productos[busc][1], "| stock: ",productos[busc][2])
        else:
            print("El codigo ingresado no exxiste")

    def existencia(productos):
        print("Los productos sin existencias son: ")
        for codigo in productos:
            if productos[codigo][2]==0:
                print("Producto: ",productos[codigo][0],"| Cantidad: ", productos[codigo][2])
                

    productos=cargar()
    imprimir(productos)
    consulta(productos)
    existencia(productos)
elif opcion ==3:
    selec=int(input("Seleccione la opción que desea: \n 1. Los meses faltantes \n 2. Entre meses \n 3. Los meses transcurridos "))
    if selec ==1:
        def mesesFaltantes(numero):
            meses=("Enero", "Febrero", "Marzo","Abril", "Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre", "Diciembre")
            return meses[numero:]

        print("Imprimir los meses que faltan para terminar el año")
        numero=(int(input("Ingrese el número de mes actual ")))
        mesFalta=mesesFaltantes(numero)
        print(mesFalta)
    elif selec==2:
        def entreMeses(inicio,fin):
            meses=("Enero", "Febrero", "Marzo","Abril", "Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre", "Diciembre")
            return meses[inicio:fin]

        print("Le mostrará los meses entre los solicitados")
        inicio=int(input("Ingrese el numero del mes inicial "))
        fin=int(input("Ingrese el numero del mes final "))
        mesesEntre=entreMeses(inicio,fin)
        print(mesesEntre)
    elif selec==3:
        def mesesTranscurridos(numero):
            meses=("Enero", "Febrero", "Marzo","Abril", "Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre", "Diciembre")
            return meses[:numero]

        print("Mostrará los meses transcurridos asta el momento")
        numero=int(input("Ingrese el mes actual "))
        transcurridos=mesesTranscurridos(numero)
        print(transcurridos)
    else: 
           print("Esta opción no es valida") 
else:
    print("Esta opción no es valida") 