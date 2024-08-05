peso = float(input('Digite seu peso:Kg'))
altura = float(input('Digite seu altura:'))
massa = peso / altura
total = massa / altura
print('Seu peso segundo a tabela IMC é de {:.1f}'.format(total))

if total < 18.5:
    print('Você esta abaixo do peso')

elif 18.5 <= total < 25:
    print('Seu peso é o ideal')

elif 25 <= total < 30:
    print('Você esta com sobrepeso')

elif 30 <= total < 40:
    print('Você esta obeso')

elif total > 40:
    print('Obeso mórbido')