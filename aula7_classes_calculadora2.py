# Sem passar valores pelo init
class Calculadora:

    # def __init__(self):
    #     pass

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

if __name__ == '__main__':
    # Instanciando uma classe
    calculadora = Calculadora()

    print(calculadora.soma(10, 2))
    print(calculadora.subtracao(10, 2))
    print(calculadora.multiplicacao(10, 2))
    print(calculadora.divisao(10, 2))