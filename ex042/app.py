reta1 = float(input('Digite o primerio segmento:'))
reta2 = float(input('Digite o segundo segmento:'))
reta3 = float(input('Digite o terceiro segmento:'))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta3:
    print('Forma um triangulo,', end=' ')
    if reta1 == reta2 == reta3:
        print('triangulo Equilatero')
    elif reta1 != reta2 != reta3 != reta1:
        print('triangulo escaleno')
    else:
        print('triangulo isosceles')
else:
    print('Não pode forma um triangulo')