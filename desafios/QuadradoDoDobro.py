from funcDir.Operacoes import exponenciacao, dobrofunc

num = int(input('Digite um número:'))

def quadradododobro(numero):
    quadrado_do_dobro = exponenciacao(dobrofunc(numero))
    return quadrado_do_dobro

print(f"O quadrado do dobro é: {quadradododobro(num)}")