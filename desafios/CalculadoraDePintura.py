"""
Calculadora para Pintura

Criar um programa que calcula a quantidade de tinta necessária para pintar uma parede. O usuário deverá fornecer as seguintes informações: Rendimento, altura e largura.
O programa deve mostrar na tela a mensagem 'Você necessita de x latas de tinta.'
"""
from funcDir import calcPintura

rendimento = int(input('Qual é o rendimento da lata? '))
altura = int(input('Qual é a altura da parede? '))
largura = int(input('Qual é a largura da parede? '))

calcPintura.calculo_tinta(altura,largura,rendimento)