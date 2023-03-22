brasil = []
while True:
    estado = str(input('Digite o estado: ')).title().strip()
    sigla = str(input('Digite a Sigla: ')).upper()
    temp = {'uf': estado, 'sigla': sigla}
    brasil.append(temp)

    perg = str(input('Quer continuar? (S/N): '))
    if perg in 'nN':
        break
print(brasil)

