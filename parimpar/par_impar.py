class ParImpar:
    def __init__(self):
        self.n = ''

    def par_impar(self):
        
        self.n = int(input("Digite um número inteiro: "))

        if self.n % 2 == 0:
            print('O numero e par')
        else:
            print('O nuemro e impar')
            

p1 = ParImpar()
p1.par_impar()
