class Palindromo:
    def __init__(self):
        self.palavra = ''

    def verifica(self):
        self.palavra = input('Digite uma palavra: ')
        
        if self.palavra == self.palavra[::-1]:
            print("É um palíndromo!")
        else:
            print("Não é um palíndromo.")


p1 = Palindromo()
p1.verifica()
