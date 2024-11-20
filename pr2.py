class Persona:
    def __init__(self, n, e):
        self.nombre = n
        self.edad = e

    def cumpleaños(self):
        self.edad += 1

nombre = input("ingresa tu nombre: ")
edad = int(input("ingresa tu edad: "))
persona = Persona(nombre, edad)
persona.cumpleaños()
persona.cumpleaños()
persona.edad -=1
print(f"{persona.nombre} ahora tiene {persona.edad} años")