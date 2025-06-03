"""
Desafio Filtrando funcionários em uma empresa

Criar um programa que gera 3 lista de acordo com a necessidade logo abaixo:

Lista 1 Funcionários que tem carro e trabalham a noite
Lista 2 Funcionários que tem carro e trabalham durante o dia
Lista 3 Funcionários que não tem carro

"""

funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

lista1 = set(tem_carro).intersection(set(turno_noite))

lista2 = set(tem_carro).intersection(set(turno_dia))

lista3 = set(funcionarios).difference(set(tem_carro))


print(f'Funcionários que tem carro e trabalham a noite {lista1}')
print(f'Funcionários que tem carro e trabalham durante o dia {lista2}')
print(f'Funcionários que não tem carro {lista3}')