#conocer las palabras reservadas
help("keywords")
print(dir(__builtins__))
print("----------------------------------------")
x = 2 # tipo int
y = 1.5 # tipo float
z = 5j # tipo complex

#Conversión de int a float:
a = float(x)

#Conversión de float a int:
b = int(y)

#Conversion de int a complex:
c = complex(x)

print(a) #Retorna: 2.0
print(b) #Retorna: 1
print(c) #Retorna: (2+0j)

print(type(a)) #Retorna: <class 'float'>
print(type(b)) #Retorna: <class 'int'>
print(type(c)) #Retorna: <class 'complex'> 
print("----------------------------------------")
var1 = 'Python es increible'
print ('Antes de ser actualizado:', var1)

var1 = var1[:10] + 'el mejor' 
# En la anterior línea cambiamos los valores del
# string después del caracter número 10

print ('Después de ser actualizado:', var1)
print("--------------------------")
a = """Este es un
texto con,
varios saltos
de línea"""

b = '''Este texto
tiene un salto'''

print('Texto1: '+a)
print('Texto2: '+b)
print("-------------------")
txt="estacio entre\tun Tab"
txt="un renglon de \btexto"
txt="\110\145\154\154\157"
txt="\x48\x64\x6c\x6c\x6f"
print(txt)
x = bool([''])
print(x)
linea = "Saludos a todos"
print(linea[10:].upper()) 
print("-----------------")
lista1 = [-1, 0, 1 ,2 ,3]
lista2 = ['Manzana', 'Uva', 'Mora']
x=lista1.copy()
print(x)
print("-----------------")
tupleConstr2 = ('Index0',)
print(type(tupleConstr2))
print("-----------------")
dicc =	{
  "nombre": "Países Bajos",
  "continente": "Europa",
  "coord": "52°19′00″N,5°33′00″E"
}

for x in dicc:
  print(dicc[x])
for x in dicc.values():
  print(x)
print("-------------")
print("AGREGAR")

dicc["bandera"] = ["Rojo","Blanco","Azul"]

for x, y in dicc.items():
  print(x,':', y)
print("-------------")
print(dicc)
x = 'abcd'
for i in range(len(x)):
    print(i)  
print("-------------")  
a="un,formato,csv"   
print(a.split(","))
nums = len(set([1,1,2,3,3,3,4,4]))
print(nums)
tupla1 = (1, 2, 3, 4)
#tupla1.append(5)
print(tupla1)
print("---------------------------")
class Persona:
    
    cedula = "1022457235"
    nombre = "Hermann"
    apellido = "Hauptmann"
    sexo = "M"

    def __str__(self):
        """Devuelve una cadena representativa de Persona"""
        return ("%s, %s %s, %s." % (str(self.cedula), self.nombre, 
            self.apellido, self.sexo))
       
       
a= Persona()
print(a.__str__())

class B(object):

    def first(self):
        print("Llamando al primer método...")
    
    @staticmethod
    def second():
        print("Llamando al segundo método...")

ob = B()

B.first(ob)
B.second()
print("--------------------------")
try:
  print(x)
except:
  print("Ocurrió una excepción")
  print("--------------------------")
try:
  print(n)
except NameError:
  print("La variable x no está definida")
except:
  print("Algo más salió mal")
print("------------------------")
try:
  print("Hola")
except:
  print("Ocurrió un error")
else:
  print("No hubo errores")
print("------------------------")
x = 1

if x < 0:
  raise Exception("No se permiten números menores a cero")
print("----------------")
x = 1

if not type(x) is int:
  raise TypeError("Sólo se perminten enteros")
x = 50
def func():
    global x
    print('El valor de x es:', x)
    x = 2
    print('La variable global x cambio a:', x)
func()
print('El valor de x es:', x)
def func1():
    
    global x
    x-=1
    print(x)
    
x=20

print(x)
func1()

def func():
    try:
        print(1)
    finally:
        print(2)
func()

def f(): 
    x=4
    
x=1
f()
print(x)
class test:
    
    def __init__(self):
        self.variable = 'Valor antiguo'
        self.Change(self.variable)
        
    def Change(self, var):
        var = 'Valor nuevo'
        
obj=test()
print(obj.variable)
value = [1, 2, 3, 4] 
data = 0
try: 
    data = value[4] 
    print(data)
except IndexError: 
    print('Ocurrió un error al hallando el índice') 
except: 
    print('Ocurrió un error en el proceso') 

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

txt = "The rain in Spain"
x = re.search("\s", txt)

print("El primer espacio en blanco está en la posición:", x.start())