viagem = float(input('Qual a distancia da vigem em km? '))
print('Você esta preste a começar um viagem de {}km'.format(viagem))
viagem_curta = viagem * 0.50
viagem_longa =  viagem * 0.45
if viagem <= 200:
    print('O preço da passagem é de R${:.2f}'.format(viagem_curta))
elif viagem >200:
    print('O preço da passagem é de R${:.2f}'.format(viagem_longa))

print('Boa viagem!')