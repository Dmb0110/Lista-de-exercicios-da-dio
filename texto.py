class Texto:
    def __init__(self):
        self.texto = ''
        self.n = ''

    def concatenar(self):
        
        self.texto = input("Digite um texto: ")
        self.n = int(input("Digite um número inteiro: "))

        print(self.texto * self.n)
        

t1 = Texto()
t1.concatenar()
