class Dados:
    def __init__(self):
        self.dado1 = ''
        self.dado2 = ''

    def concatenar(self):
        self.dado1 = input("Digite o primeiro dado: ")
        self.dado2 = input("Digite o segundo dado: ")
        
        result = self.dado1 + self.dado2
        print(f'Resultado da concatenacao: {result}')


d1 = Dados()
d1.concatenar()
