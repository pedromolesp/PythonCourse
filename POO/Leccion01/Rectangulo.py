class Rectangulo:
    def __init__(self, base, altura):
        self.altura = altura
        self.base = base

    def calcularArea(self):
        return self.altura * self.base


rectangulo1 = Rectangulo(3,7)
print(f'El área del rectángulo de altura: {rectangulo1.altura} y de base {rectangulo1.base} es igual a: {rectangulo1.calcularArea()}')