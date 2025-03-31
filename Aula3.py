##Controle de Fluxo

#if, elif, else
idade = int(input("Digite sua idade: "))

if idade >= 18:
  print("Você é maior de idade.")
  #esse espaço é chamado de identação
  #indentação é o espaço que fica antes de uma linha de código
  #é importante para saber o que está dentro do if, elif e else
  #o espaço é importante para o python saber onde o código termina
  print("Você é maior de idade. Tambem pode beber.")
elif idade >= 16:
  #a seção elif é executada se a condição do if for falsa e pode ter várias elifs
  print("Você é menor de idade, mas pode votar.")
else:
  print("Você é menor de idade.")

#Operadores Lógicos

#and, or, not
#and: todas as condições precisam ser verdadeiras para que o código dentro
#or: basta que uma das condições seja verdadeira para que o código dentro seja executado
#not: inverte o valor lógico da condição

renda_acima_5mil = True
nome_limpo = False
if renda_acima_5mil and not nome_limpo:
  print("Financiamento aprovado.")
else:
  print("Financiamento negado.")

#Multiplos operadores de comparação

valor = int(input("Digite o valor do produto: "))

# é possível encadear vários operadores de comparação

if 20 <= valor < 40:
  print("Produto foi aceito.")
else:
  print("Produto não aceito.")

#For Loop - Utilizando números

#imprimir de 1 a 5
"""
range(start, stop, step)
start: valor inicial
stop: valor final
step: pular de quanto em quanto
o valor final não é incluso
o valor inicial é opcional, quando não é informado, o valor inicial é 0
"""

for numero in range(1, 6, 2):
  print(numero)

#For Loop - Utilizando Strings
"""
Ao utilizar strings, o for loop irá percorrer cada letra 
"""

palavra = "Google"

for letra in palavra:
  print(f'{letra} está dentro da palavra {palavra}')

#For Loop - Utilizando If e Else

compra_confirmada = True
dados_compra = "Compra no valor de R$12.50 e entrega confirmada"
for enviar in range(3):
  if compra_confirmada:
    print(dados_compra)
    print("Detalhes enviados para o seu email.")
    break  #para o loop
  else:
    print("Falha na compra.")
    break

#For Loop - Nested Loops

#outer loop
#inner loop

for numero1 in range(1, 6):
  print(numero1)
  for numero2 in range(5):
    print(numero1, numero2)

#For Loop - Separando Strings
#modificar de FANTASTICO para F A N

palavra = 'FANTASTICO'
#end=' ' faz com que o print não pule linha o espáço entre as letras é o que está entre aspas
for espaco in palavra:
  print(f'{espaco} ', end='')

#For Loop - Criando um Retângulo

linhas = 6
colunas = 3
simbolo = '@'

for line in range(linhas):
  for col in range(colunas):
    print(simbolo, end='')
  print()

#While Loop
#Excelente para loops dependentes de uma condição
#Criar uma promoção para um produto no valor de R$100

valor = 100
dia = 0
while valor > 20:
  dia += 1
  print(f'No dia {dia} o produto vai ser vendido por R${valor}')
  valor -= 5

#Diferença entre For Loop e While Loop
#For Loop: para um número de vezes definido
#While Loop: para uma condição

#Criando condições com While Loop
#Publicar um produto com comissão de 10% se for acima de R$20
valor = int(input('Digite o valor do seu produto:\tR$'))

while valor > 20:
  valor = (valor * 0.10) + valor
  print(f'O valor final do seu produto será de R${valor}')
  brea