from datetime import date
atual = date.today().year
dia = date.today()
sexo = str(input('Digite seu sexo ( masculino ou feminino): ')).strip().capitalize()
if sexo in 'Feminino feminino':
    print('Seu alistamento não é necessario!')
    print('Fique bem!')
    print('{}'.format(dia))
    exit()     
if sexo in ' Masculino masculino':
    print('Vamos dar continuidade ao seu alistamento!')
ano = int(input('Digite o ano de seu nascimento:'))
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano,idade,atual))
if idade == 18:
    print('Voce tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade 
    print('Ainda faltam {} anos para o seu alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamenot sera em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voce já deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))    
print('{}'.format(dia))
