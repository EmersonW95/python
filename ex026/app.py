frase = str(input('Digite uma frase:')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A aparece primeiro na posição {}'.format(frase.find('A')+1))
print('A ultima vez que aparece a letra A é na posição {}'.format(frase.rfind('A')+1))