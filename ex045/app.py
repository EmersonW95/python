from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Vamos jogar?
[0]Pedra
[1]Papel
[2]Tesoura''')
jogador = int(input('Digite um numero:'))
print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOURA')
sleep(1)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR GANHOU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('ALGO DEU ERRADO. TENTE NOVAMENTE')
elif computador == 1:
    if jogador == 1:
        print('EMPATE')
    elif jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('ALGO DEU ERRADO. TENTE NOVAMENTE')
elif computador == 2:
    if jogador == 2:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 0:
        print('COMPUTADOR VENCE')
    else:
        print('ALGO DEU ERRADO. TENTE NOVAMENTE')