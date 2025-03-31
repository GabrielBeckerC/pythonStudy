# Isso é um comentário usado para explicar o código com a marcação de #
'''Isso é um comentário usado para explicar o código com a marcação de 3 aspas simples'''

#Exemplo de saída de dados com print
print("Hello World!")
'''
Data Types são divididos em:
Text Type: str
Numeric Types: int, float, complex
Bolean Type: bool
'''

#Exemplo de variáveis
'''
Variáveis são criadas com o nome da variável e o sinal de igual e o valor da variável. Exemplo: x = 5.
Podendo ser de qualquer tipo
'''
x = 5
print(x)
print(x + x)

#Modificando o tipo de dados
'''
Para modificar o tipo de dados basta usar a função str(), int(), float().
Para verificar o tipo de dado basta usar a função type().
'''
x = str(3)
print(x)
print(type(x))

#Praticar com strings e integers
#Frase: O Gabriel tem 32 anos de idade e mora na cidade de Santa Maria.
nome = 'Gabriel'
idade = 32
cidade = 'Santa Maria'

print('O ' + nome + ' tem ' + str(idade) +' anos de idade e mora na cidade de ' + cidade + '.')

#Usando f-strings
#F-strings são usadas para inserir variáveis dentro de strings.

print(f'O {nome} tem {idade} anos de idade e mora na cidade de {cidade}')

#Adicionado input
#input é usado para receber dados do usuário.
sobrenome = input('Qual é o seu sobrenome?\t ')
print(f'O {nome} {sobrenome} tem {idade} anos de idade e mora na cidade de {cidade}')

ano_nascimento = input('Digite o ano em que você nasceu:\t')
print(type(ano_nascimento))
idade_calculada = 2025 - int(ano_nascimento)
print(f'Você tem {idade_calculada} anos de idade')

#Entendo o Slice

#O slice é usado para extrair um determinado caractere de uma string.

#Exemplo:
fruta = 'Abacate'
#index   0123456
print(fruta[2:6])
#Utilizando números negativos no index, o Python conta a partir do final da string
print(fruta[-1])

valor = 99.75
#index  01234
valor = str(valor)
print(valor[3:5])


#Metodos para strings
'''
As strings são imutáveis, ou seja, não podem ser alteradas.
No entanto, podemos criar novas strings a partir de strings existentes.
Utilizando diversos métodos para strings.
'''

mensagem = 'Eu adoro comida caseira'

print(mensagem.lower())
print(mensagem.upper())
print(mensagem.capitalize())
print(mensagem.find('c'))
print(mensagem.replace('a', 'e'))
print(mensagem.replace('caseira', 'feita em casa'))
print(mensagem.strip())