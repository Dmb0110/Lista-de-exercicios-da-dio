class Dados:
    def __init__(self):
        self.dado1 = ''
        self.dado2 = ''

    def concatenar(self):
        self.dado1 = input("Digite o primeiro dado: ")
        self.dado2 = input("Digite o segundo dado: ")
        
        result = self.dado1 + self.dado2
        print(f'Resultado da concatenacao: {result}')

class Media:
    def __init__(self):
        self.nota1 = ''
        self.nota2 = ''
        self.nota3 = ''

    def media(self):
        self.nota1 = float(input("Digite a primeira nota: "))
        self.nota2 = float(input("Digite a segunda nota: "))
        self.nota3 = float(input("Digite a terceira nota: "))

        media = (self.nota1 + self.nota2 + self.nota3)
        print(f'A media das notas e: {media}')
        

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
                
class Palindromo:
    def __init__(self):
        self.palavra = ''

    def verifica(self):
        self.palavra = input('Digite uma palavra: ')
        
        if self.palavra == self.palavra[::-1]:
            print("É um palíndromo!")
        else:
            print("Não é um palíndromo.")

class ParImpar:
    def __init__(self):
        self.n = ''

    def par_impar(self):
        
        self.n = int(input("Digite um número inteiro: "))

        if self.n % 2 == 0:
            print('O numero e par')
        else:
            print('O nuemro e impar')
            
class Texto:
    def __init__(self):
        self.texto = ''
        self.n = ''

    def concatenar(self):
        
        self.texto = input("Digite um texto: ")
        self.n = int(input("Digite um número inteiro: "))

        print(self.texto * self.n)
        

d1 = Dados()
d1.concatenar()
