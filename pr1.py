class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"Nombre: {self.nombre} \nNota: {self.nota}")

    def resultados(self):
        if self.nota >= 6:
            print("es tu obligacion")
        else:
            print("hechele ganas mijo")

estudiante1 = Estudiante("santiago", 8)
estudiante1.imprimir()
estudiante1.resultados()

estudiante2 = Estudiante("diana", 6)
estudiante2.imprimir()
estudiante2.resultados()