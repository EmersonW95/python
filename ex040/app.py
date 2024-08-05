n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('Digite sua segunda nota:'))
soma = (n1 + n2) / 2

if soma >= 7:
    print('APROVADO. Sua media foi {:.1f}'.format(soma))
elif soma < 5:
    print('REPROVADO. Sua media foi {:.1f}'.format(soma))
elif soma > 5:
    print('RECUPERAÇÃO. Sua media foi {:.1f}'.format(soma))
