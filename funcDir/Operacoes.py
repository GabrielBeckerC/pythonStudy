
def soma(a, b):
  print('soma')
  return print(a + b)


def multiplicacao(a, b):
  print('multiplicacao')
  return print(a * b)

def subtracao(a, b):
  print('subtracao')
  return print(a - b)

def divisao(divisor, dividendo):
  print('divisao')
  return print(divisor / dividendo)

def exponenciacao(base, expoente = 2):
  print('exponenciacao')
  return print(base ** expoente)

def fatorial(a):
  if a == 0:
    return 1
  else:
    return a * fatorial(a-1)
