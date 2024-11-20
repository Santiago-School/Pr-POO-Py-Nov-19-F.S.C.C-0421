class Fabrica():
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

class Moto(Fabrica):
    def informacion(self):
        print(f"La moto tiene {self.llantas} llantas, color {self.color}, precio {self.precio}")

class Carro(Fabrica):
    def informacion(self):
        print(f"El carro tiene {self.llantas} llantas, color {self.color}, precio {self.precio}")

moto = Moto(2, "Verde Neon", "$29999")
moto.informacion()

carro = Carro(4, "Grus", "$24999")
carro.informacion()