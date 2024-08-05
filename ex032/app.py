from datetime import date
ano = int(input('Digite um ano:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0:
    print('Ano de {} é bissexto'.format(ano))
else:
    print('Ano de {} é normal'.format(ano))