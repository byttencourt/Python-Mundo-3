times = 'América-MG', 'Athletico-PR', 'Atlético-MG', 'Bahia', 'Botafogo', 'Bragantino', 'Corinthians', 'Coritiba', \
    'Cruzeiro', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Grêmio', 'Internacional', 'Palmeiras', \
    'Santos', 'São Paulo', 'Vasco'
print('Cinco primeiros times: {}.'.format(times[0:5]))
print('Quatro últimos times: {}.'.format(times[-4:]))
print('Times em ordem alfabética: {}'.format(sorted(times)))
print('O time Cruzeiro está na {}º colocação.'.format(1 + times.index('Cruzeiro')))


