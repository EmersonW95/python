from random import choice
aluno1 = str(input('Digite aqui seu nome:'))
aluno2 = str(input('Digite o seu nome:'))
aluno3 = str(input('Digite seu nome:'))
aluno4 = str(input('Digite seu nome:'))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista)
print('O aluno (a) escolhido foi {}'.format(escolhido))