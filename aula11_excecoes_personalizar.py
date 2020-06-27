class Error(Exception):
    pass # Usado para a classe passar mesmo sem nada

class InputError(Error):

    # Criando um construtor
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input('Digite uma nota de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser maior que 10')
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0')
        break
    except ValueError:
        print('Valor inválido. Deve-se digitar apenas números.')
    except InputError as ex:
        print(ex)