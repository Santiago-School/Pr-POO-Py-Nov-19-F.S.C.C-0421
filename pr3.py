class Calculadora():
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2

    def suma(self):
        resultado = self._num1 + self._num2
        print(f"el resultado de la suma es: {self._num1} + {self._num2} = {resultado}")

    def resta(self):
        resultado = self._num1 - self._num2
        print(f"el resultado de la resta es: {self._num1} - {self._num2} = {resultado}")

    def division(self):
        resultado = self._num1 / self._num2
        print(f"el resultado de la division es: {self._num1} / {self._num2} = {resultado}")

    def multiplicacion(self):
        resultado = self._num1 * self._num2
        print(f"el resultado de la multiplicacion es: {self._num1} * {self._num2} = {resultado}")

operacion = Calculadora(2, 4)
operacion.suma()

operacion = Calculadora(8, 6)
operacion.resta()

operacion = Calculadora(14, 6)
operacion.division()

operacion = Calculadora(2, 8)
operacion.multiplicacion()