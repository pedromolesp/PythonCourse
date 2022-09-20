class Aritmetica:
    """
    Clase aritmética para realizar operaciones matemáticas
    """

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB


aritmetica1 = Aritmetica(3, 5)
print(aritmetica1.sumar())
