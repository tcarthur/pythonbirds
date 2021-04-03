class Pessoa:
    olhos = 2


    def __init__(self, *filhos, nome = None, idade = 25):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    bernardo = Pessoa(nome='Bernardo')
    arthur = Pessoa(bernardo, nome='Arthur')
    print(Pessoa.cumprimentar(arthur))
    print(id(arthur))
    print(arthur.cumprimentar())
    print(arthur.nome)
    print(arthur.idade)
    for filho in arthur.filhos:
        print(filho.nome)
    arthur.sobrenome = 'Tavares'
    del arthur.filhos
    arthur.olhos = 1
    del arthur.olhos
    print(arthur.__dict__)
    print(bernardo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(arthur.olhos)
    print(bernardo.olhos)
    print(id(Pessoa.olhos), id(bernardo.olhos), id(arthur.olhos))