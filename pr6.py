class Marino():
    def hablar(self):
        print("Hola soy un animal marino")

class Cangrejo(Marino):
    def hablar(self):
        print("Hola soy chese y soy un cangrejo")

class Mojarra(Marino):
    def hablar(self, mensaje):
        self.mensaje = mensaje
        print(mensaje)


marino = Marino()
marino.hablar()

pulpo = Cangrejo()
pulpo.hablar()

foca = Mojarra()
foca.hablar("Glu Glu Glu°° ( hola soy una mojarra)")