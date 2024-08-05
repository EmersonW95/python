produto = float(input('Digite o valor do produto R$'))
print('''Insira a forma de pagamento:
[1] à vista dinheiro/cheque 
[2] à vistao no cartão 
[3] 2x no cartão 
[4] 3x ou mais com juros''')
pagamento = input('Digite qual é a opção de pagamento:')
if pagamento == '1':
    dinheiro = produto - ( produto * 10 / 100)
    print('O valor do produto é  R${} e com o desconto fica R${}'.format(produto,dinheiro))
elif pagamento == '2':
    cartao = produto - ( produto * 5 / 100)
    print('O valor do produto é R${} e fica por R${}'.format(produto,cartao))
elif pagamento == '3':
    parcelado = produto / 2
    print('Preço normal, fica R${}'.format(parcelado))
elif pagamento == '4':
    parceladcomjuros = produto + (produto * 20 / 100)
    parc = int(input('Quantas parcelas deseja pagar?'))
    total = parceladcomjuros / parc
    print('O preço do produto era de R${} e vai ficar por R${} dividido em {} parcelas e vai ficar todo mês por {:.2f}'.format(produto,parceladcomjuros,parc,total))