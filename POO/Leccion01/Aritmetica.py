class Aritmetica:
    """
    Clase aritmética para realizar operaciones matemáticas
    """

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA-self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(3, 5)
print(f'Suma: {aritmetica1.sumar()}')
print(f'Restar: {aritmetica1.restar()}')
print(f'Multiplicar: {aritmetica1.multiplicar()}')
print(f'Dividir: {aritmetica1.dividir():.2f}')