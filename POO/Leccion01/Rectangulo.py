class Rectangulo:
    def __init__(self, base, altura):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.altura * self.base


base = int(input("Proporciona la base: "))
altura = int(input("Proporciona la altura: "))
rectangulo1 = Rectangulo(base,altura)
print(f'El área del rectángulo de altura: {rectangulo1.altura} y de base {rectangulo1.base} es igual a: {rectangulo1.calcular_area()}')