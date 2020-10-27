#ingresar por consola nombre y nota de los alumnos,
#opcion listar alumnos o alumnos  con notas superiores a 4

class Alumnos:
    def __init__(self):
        self.nombre=[]
        self.nota=[]

    def cargar(self):
        continua="si"
        while continua=="si":
            nom=input("Ingrese el nombre del alumno ")
            self.nombre.append(nom)
            no=int(input("Ingrese la nota de 0 a 5 "))
            self.nota.append(no)
            print("******************************************")
            continua=input("Desea agregar otro alumno: si/no ")
            print("******************************************")

    def menu(self):
        opcion=0
        while opcion!=3:
           print("******************************************")
           opcion=int(input("Seleccione la opción que desea: \n1- Listar todos los alumnos \n2- Alumnos con nota igual o superior a 4 \n3- Finalizar programa "))
           if opcion==1:
               self.listar()
           elif opcion ==2:
               self.notasAltas()

    def listar(self):
        print("******************************************")
        print("Los estudiantes registrados son: ")
        print("******************************************")
        for x in range(len(self.nota)):
            print("nombre: ",self.nombre[x],"nota: ",self.nota[x])

    def notasAltas(self):
        print("******************************************")
        print("Los alumnos con notas igual o superior a 4 son: ")
        print("******************************************")
        for x in range(len(self.nota)):
            if self.nota[x]>=4:
                print("nombre: ",self.nombre[x],"nota: ",self.nota[x])

alumnos=Alumnos()
alumnos.cargar()
alumnos.menu()
