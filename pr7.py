class Universidad():
    def __init__(self, nombre):
        self.nombre = nombre

class Carrera():
    def asignar_carrera(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carrera):
    def mostrar_datos(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"el estudiante {self.nombre} tiene {self.edad} años, esta cursando {self.especialidad} en la universidad {self.nombre}")


persona = Estudiante("universidad De Chihuahua")
persona.asignar_carrera("Abogado")
persona.mostrar_datos("Carlos Maldonado", 26)