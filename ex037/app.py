
num = int(input('Digite um numero inteiro:'))
base = str(input('Digite qual será a base de conversão. 1 para bin, 2 octal e 3 hex:'))

if base  == '1':
    conversao = bin(num)[2:]
elif base == '2':
    conversao = oct(num)[2:]
elif base == '3':
    conversao = hex(num)[2:]
else:
    print('Numero invalido')

print('O numero convertido foi {} a base foi {} e a conversão foi {}'.format(num,base,conversao))