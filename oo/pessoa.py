class Pessoa:
    def __init__(self,nome = None, idade = 3):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Bernardo')
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Arthur'
    print(p.nome)
    print(p.idade)