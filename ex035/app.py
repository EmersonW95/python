reta1 = float(input('Digite o primerio segmento:'))
reta2 = float(input('Digite o segundo segmento:'))
reta3 = float(input('Digite o terceiro segmento:'))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os segmentos acima podem formar um triângulo')
else:
    print('Os segmentos acima não podem formar um triângulo')