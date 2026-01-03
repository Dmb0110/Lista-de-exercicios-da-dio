class Operacao:
    def __init__(self):
        self.n1 = ''
        self.n2 = ''
        self.op = ''

    def resultado(self):
        
        self.n1 = float(input("Digite o primeiro número: "))
        self.n2 = float(input("Digite o segundo número: "))
        self.op = input('Digite o operador: ')

        if self.op == '+':
            result = self.n1 + self.n2
            print(f'{result} = {self.n1} + {self.n2}')

        elif self.op == '-':
            result = self.n1 - self.n2
            print(f'{result} = {self.n1} - {self.n2}')
        
        elif self.op == '*':
            result = self.n1 * self.n2
            print(f'{result} = {self.n1} * {self.n2}')
        
        elif self.op == '/':
            if self.n2 == 0:
                return {'Divisao por zero nao permitido'}
            else:
                result = self.n1 / self.n2
                print(f'{result} = {self.n1} / {self.n2}')
                

op1 = Operacao()
op1.resultado()
