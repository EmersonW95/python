import random
a1 = str(input('Digite seu nome:'))
a2 = str(input('Digite o seu nome:'))
a3 = str(input('Digite o nome:'))
a4 = str(input('Digite o seu nome:'))
sorteio = [a1, a2, a3, a4]
sequencia = random.shuffle(sorteio)
print('A sequencia será')
print(sorteio) 