temp = {}
nome = str(input('Digite o Nome: ')).strip().title()
media = int(input('Digite a média: '))
if media >= 7:
    sit = 'Aprovado'
else:
    sit = 'Reprovado'
temp = {'nome': nome, 'media': media, 'situaçao': sit}
print(temp)
for k, v in temp.items():
    print(f'O {k} é igual a {v}')
