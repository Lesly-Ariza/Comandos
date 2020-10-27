# registrar información de los alumnos(nombre puntuacion), 
# determinar calificación
 
class alumno:

    def cargar(self,documento,nombre,puntuacion):
        self.documento=documento
        self.nombre=nombre
        self.puntuacion=puntuacion
           
        return alumno
    
    def imprimir(self):
        print("Nombre: ",self.nombre)
        print("nota: ", self.puntuacion)

    def promedio(self):
        if self.puntuacion<=3.4:
            print("Insuficiente")
        elif self.puntuacion<=4:
            print("Aceptable")
        elif self.puntuacion<=4.5:
            print("Sobresaliente")
        elif self.puntuacion<=5:
            print("Excelente")
        else:
            print("La nota ingresada no es valida debe estar entre 0 a 5")



alumno1=alumno()
alumno1.cargar(1234,"les",5)
alumno1.imprimir()
alumno1.promedio()