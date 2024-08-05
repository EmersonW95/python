v = float(input('Digite a velocidade do carro:')) 
multa = (v - 80) * 7
if v >80:
    print('Você foi multado. Você tem que pagar R${:.2f}'.format(multa))
else:
    print('Tudo certo!. Tenha um bom dia!')