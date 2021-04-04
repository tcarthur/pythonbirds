"""
Você deve criar uma classe carro que vai
possuir dois atributos compostos por duas classes:

1) Motor
2) Direção

O Motor terá a responsabilidade de controlar a velocidadeEle oferece os seguinte atributos:
1) Atribyto de dado velocidade
2) Método acelerar, que deverá incrementar a velocidade de uma unidade.
3) Método frear que deverá decrementar a velocidade em duas unidades

A direção terá a responsabilidade de controlar a direção. ela oferece os seguintes atributos:
1) Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste.
2) Método girar_a_direita
3) Método girar_a_esquerda

  N
O   L
  S

  Exemplo:
  # Testando motor
  >>>motor = Motor()
  >>>motor.velocidade
  0
  >>>motor = acelerar()
  >>>motor.velocidade
  1
  >>>motor = acelerar()
  >>>motor.velocidade
  2
  >>>motor = acelerar()
  >>>motor.velocidade3
  3
  >>>motor = frear()
  >>>motor.velocidade

  >>> # Testando Direção
  >>> direcao  = Direcao()
  >>> direcao.valor
  'Norte'
  >>> direcao.girar_a_direita()
  >>> direcao.valor
  'leste'
  >>> direcao.girar_a_direita()
  >>> direcao.valor
  'Sul'
  >>> direcao.girar_a_direita()
  >>> direcao.valor
  'Oeste'
  >>> direcao.girar_a_direita()
  >>> direcao.valor
  'Norte'
  >>> direcao.girar_a_esquerda()
  >>> direcao.valor
  'Oeste'
  >>> direcao.girar_a_esquerda()
  >>> direcao.valor
  'Sul'
  >>> direcao.girar_a_esquerda()
  >>> direcao.valor
  'Leste'
  >>> direcao.girar_a_esquerda()
  >>> direcao.valor
  'Norte'
  >>> carro = Carro(direcao,motor)
  >>> carro.calcular_velocidade()
  >>>0
  >>> carro.acelerar()
  >>> carro.calcular_velocidade()
  >>>1
  >>>carro.acelerar()
  >>>carro.calcular_velocidade()
  2
  >>>carro.frear()
  >>>carro.calcular_velocidade()
  0
  >>>carro.calcular_direcao()
  'Norte'
  >>>carro.girar_a_direita()
  >>>carro.calcular_direcao()
  'Leste'
  >>>carro.girar_a_esquerda()
  >>>carro.calcular_direcao()
  'Norte'
  >>>carro.girar_a_direita()
  >>>carro.calcular_direcao()
  'Oeste'
"""


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.acelerar += 1

    def frear(self):
        self.frear -= 2
        self.velocidade = max(0, self.velocidade)


NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'


class Direcao(object):
    rotacao_a_direita_dct = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    rotacao_a_esquerda_dct = {NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL}

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]
