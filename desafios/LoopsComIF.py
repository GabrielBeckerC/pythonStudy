
frutas = list(('maçã', 'banana', 'maçã', 'pêra', 'uva', 'maçã', 'abacaxi'))
contaMaca = 0
for fruta in frutas:
    print(f'A fruta é: {fruta}')
    if fruta == 'maçã':
        contaMaca += 1

print(f'O número de maçãs na cesta é: {contaMaca}')