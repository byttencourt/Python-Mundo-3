def voto(nasc):
    from datetime import datetime
    idade = datetime.now().year - nasc
    if idade < 18:
        return f'Com {idade} anos. Não vota!'
    elif idade >= 18 and idade < 65:
        return f'Com {idade} anos: É Obrigatório votar'
    elif idade >= 18 and idade >= 65:
        return f'Com {idade} anos: É opcional votar'


print('-' * 30)
perg = int(input('Em que ano vc nasceu? '))
print(voto(perg))



