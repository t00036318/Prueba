

class Calculadora:
    def __init__(self, op, num1, num2):
        self.op = op
        self.num1 = num1
        self.num2 = num2

    def suma(self):
        return self.num1 + self.num2

    def resta(self):
        return self.num1 - self.num2

    def multiplicacion(self):
        return self.num1 * self.num2

    def division(self):
        return self.num1 / self.num2

    def __del__(self):
        self.op = None
        self.num1 = None
        self.num2 = None