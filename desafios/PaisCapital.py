paisCapital = dict(
    Brasil = 'Brasilia',
    Inglaterra = 'Londres',
    Russia = 'Moscou')

pais = input('Digite uma pais: ')
capital = paisCapital.get(pais.capitalize(),f'Desculpe, não temos informações sobre a capital do pais {pais}')

if pais.capitalize() in paisCapital:
    print(f' A capital do pais {pais.capitalize()} é {capital}')
else:
    print(capital)
