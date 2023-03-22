galera = []
dado = []
totmaior = totmenor = 0
for c in range(3):
    dado.append(str(input('Nome: '.title().strip())))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        totmaior += 1
        print(f'{p[0]} é maior de idade.')
    else:
        totmenor += 1
        print(f'{p[0]} é menor de idade.')

print(f'Conteúdo da lista galera: {galera}.')
print(f'Conteúdo da lista dados: {dado}.')
print(f'O total de maiores é {totmaior} e o total de menores é {totmenor}.')



#galera1 = [['Joao', 19], ['Ana', 33], ['joaquim', 13], ['Maria', 45]]
#print(galera1[2][0])
#for c in galera1:
#    if 'o' in c[0]:
        #print(c[0])

