qtd_km = float(input('Digite a quantidade de km percorridos:Km'))
qtd_dias= int(input('Digite a quantidade de dias alugado:'))
carro = 60 * qtd_dias
rodado = qtd_km * 0.15 
total = carro + rodado
print('O total a pagar é de R${:.2f}'.format(total))