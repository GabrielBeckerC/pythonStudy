# Erros

# O que são erros?
'''Erros são problemas na execução do programa. Na linguagem de programação Python, existem dois tipos de erros: de sintaxe e de exceção.'''

# Erros de sintaxe
'''
Ocorrem quando o Python encontra um código com problemas de sintaxe. Ou seja, você escreveu algo que o Python não reconhece como parte da linguagem.
'''

# Erros de exceção
'''
Erros de exceção ocorrem quando o programa está sendo executado e encontra um problema. Por exemplo, tentar abrir um arquivo que não existe ou tentar fazer uma divisão por zero.
'''

# Trabalhando com o try e except com uma lista

letras = ['a', 'b', 'c']
try:
    print(letras[3])
except IndexError:
    print('O índice não existe')

    # Trabalhando com o try e except com o input

while True:
    try:
        valor = int(input('Digite o valor do seu produto: '))
        print(valor)
        break
    except ValueError:
        print('Favor digitar um valor em números')

# Adicionado o ELSE e Finally

'''finally é sempre executado, independente de erro ou não. O finally geralmente é utilizado para fechar ou desalocar recursos.'''

while True:
    try:
        valor = int(input('Digite o valor do seu produto: '))
        print(valor)

    except ValueError:
        print('Favor digitar um valor em números')
    # else:
    #   print('Usuário digitou um valor correto')
    #   resultado = valor * 2
    #   print(resultado)
    #   break
    finally:
        print('Código ok')