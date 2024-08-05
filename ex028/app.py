from random import randint
from time import sleep
computador = randint(0,5) # Faz o computador pensar
print('-=-' * 20)
print('Vou pensar em numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jodador = int(input('Em que numero eu pensei?'))
print('PROCESSANDO...')
sleep(2)
if jodador == computador:
    print('Parabéns você venceu!')
else:
    print('Voce perdeu, eu pensei no numero {}!'.format(computador))