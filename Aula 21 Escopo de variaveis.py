def funcao(b):
    global a
    a = 8
    b += 4
    c = 2
    print('---')
    print(f'a é igual a {a}')
    print(f'b local é {b}')
    print(f'c é igual a {c}')
    print('---')


a = 2
print(f'a global vale {a}')
funcao(a)
#print(f'No programa principal x vale {x}')
print(f'a global agora vale {a}')




