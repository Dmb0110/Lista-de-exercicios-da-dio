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
        

m1 = Media()
m1.media()
