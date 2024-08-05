vlr_casa = float(input('Digite qual é o valor da casa:R$'))
slr_comprador = float(input('Digite o salario do comprador:R$'))
qtd_anos = int(input('Digite a quantidade de anos você vai pagar:'))
prestacao =  vlr_casa / (qtd_anos * 12)
minimo = slr_comprador * 30 / 100  

if prestacao <= minimo:
    print('Parabéns, você pode fazer o emprestimo!')
elif prestacao > minimo:
    print('Para pagar uma casa de R${} em {} anos a prestaçao seria de R${:.2f}'.format(vlr_casa,qtd_anos,prestacao))
    print('Você não pode fazer o emprestimo')