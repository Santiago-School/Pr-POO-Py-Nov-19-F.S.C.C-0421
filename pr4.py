class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def nombrecompleto(self):
        print(f"{self.nombre} {self.apellido}")

class Estudiante(Persona):
    def __init__(self, nombre, apellido, especialidad):
        super().__init__(nombre, apellido)
        self.especialidad = especialidad

    def especialidad(self):
        print(f"especialidad: {self.especialidad}")


estudiante1 = Estudiante("Maria", "Correa", "Arte y sus variantes")
estudiante1.nombrecompleto()
