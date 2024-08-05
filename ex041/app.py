from datetime import date
ano = date.today().year
nascimento = int(input('Digite o seu ano de nascimento:'))
categoria = ano - nascimento
print('O atleta tem {} anos'.format(categoria))
if categoria <= 9:
    print('categoria Mirim')
elif categoria <= 14:
    print('Categoria Infantil')
elif categoria <= 19:
    print('Categoria Junior')
elif categoria <= 25:
    print('Categoria Senior')
elif  categoria > 25:
    print('Categoria Master')