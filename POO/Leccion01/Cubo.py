class Cubo:
    def __init__(self, base, altura, profundo):
        self.altura = altura
        self.base = base
        self.profundo = profundo

    def calcular_area(self):
        return self.altura * self.base * self.profundo


base = int(input("Proporciona la base: "))
altura = int(input("Proporciona la altura: "))
profundidad = int(input("Proporciona la profundidad: "))
cubo1 = Cubo(base,altura,profundidad)
print(f'El área del cubo de altura: {cubo1.altura}, de base {cubo1.base} y profundidad {cubo1.profundo} es igual a: {cubo1.calcular_area()}')