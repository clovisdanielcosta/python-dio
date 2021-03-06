class Televisao:

    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1


if __name__ == '__main__':
    televisao = Televisao()

    televisao.power()
    print('A Televisão está ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('A Televisão está ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('A Televisão está ligada: {}\n'.format(televisao.ligada))

    print('A Televisão está ligada: {}'.format(televisao.ligada))
    print('Canal: {}'.format(televisao.canal))
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('Canal: {}'.format(televisao.canal))
    televisao.diminui_canal()
    print('Canal: {}'.format(televisao.canal))

