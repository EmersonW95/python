salario = float(input("Digite seu salario:R$"))

if salario > 1250:
    print('Seu novo salario é de R${:.2f}'.format(salario + (salario * 10 / 100 )))
if salario <=1250:
    print('Seu novo salario é de R${:.2f}'.format(salario + (salario * 15 / 100)))