
frutas = list(('maçã', 'banana', 'manga','uva'))

print(f'Minha cesta de frutas tem: {frutas}')
print(f'A fruta que mais gosta da minha cesta é: {frutas[1]}')
print(f'Mas também gosto de: {frutas[-1]}')
print(f'Metade da cesta é: {frutas[2:4]}')
frutas.append('goiaba')
print(frutas)
frutas.pop()
print(frutas)
frutas.remove("uva")
print(frutas)

for fruta in frutas:
    print(f'{fruta} é bom pra saúde!')

    

frutas[2] = 'abacaxi'
print(frutas)
frutas.append('goiaba')
frutas.append('manga')
print(frutas)