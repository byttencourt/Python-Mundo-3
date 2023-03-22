aluno1 = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
aluno2 = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 40}
lista = []
print(f'O {aluno1["nome"]} tem {aluno1["idade"]} anos e o sexo {aluno1["sexo"]}.')
print(aluno1.keys())
print(aluno1.items())
#del aluno1['sexo']
print('='*20)
for k in aluno1.items():
    print(k)
print('='*20)
aluno1['nome'] = 'Leandro'
for k, v in aluno1.items():
    print(k, v)
print('='*20)
for k in aluno1.keys():
    print(k)
print('='*20)
for k in aluno1.values():
    print(k)
lista.append(aluno1)
lista.append(aluno2)
print(lista)
