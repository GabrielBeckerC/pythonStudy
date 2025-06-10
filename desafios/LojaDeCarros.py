carros = list(('BMW x6', 'BMW i5', 'BMW i8'))

carro_desejado = input('Digite o carro desejado: ')


if carro_desejado in carros:
    print('Este carro está disponível')
else:
    print('Desculpe, este carro não etá disponível')