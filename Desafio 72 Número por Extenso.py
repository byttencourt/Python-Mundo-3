tupla = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', \
    'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte'
while True:
    escolha = int(input('Digite o valor que vc deseja vizualizar de 0 a 20: '))
    if escolha > 20 or escolha < 0:
        break
    print(tupla[escolha])
print('Fim!')