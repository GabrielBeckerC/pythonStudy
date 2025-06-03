"""
Calculo de IMC

IMC = peso / altura^2

Qual a sua altura em cm:
Qual o seu peso em kg:

MENOR QUE 18,5	MAGREZA
ENTRE 18,5 E 24,9	NORMAL
ENTRE 25,0 E 29,9	SOBREPESO
ENTRE 30,0 E 39,9	OBESIDADE
MAIOR QUE 40,0	OBESIDADE GRAVE
"""

from funcDir import calcIMC

altura = float(input("Qual a sua altura em cm: "))
peso =  float(input("Qual o seu peso em kg: "))

imc = calcIMC.calculo_imc(altura, peso)

if imc <= 18.5:
    print(f"Seu IMC é {imc:.2f} e você está com MAGREZA")
elif imc <= 24.9:
    print(f"Seu IMC é {imc:.2f} e você está com NORMAL")
elif imc <= 29.9:
    print(f"Seu IMC é {imc:.2f} e você está com SOBREPESO")
    print("Cuidado, você está acima do peso")
elif imc <= 39.9:
    print(f"Seu IMC é {imc:.2f} e você está com OBESIDADE")
    print("Cuidado, você está acima do peso")
    print("Procure um médico")
elif imc >= 40:
    print(f"Seu IMC é {imc:.2f} e você está com OBESIDADE GRAVE")
    print("Cuidado, você está acima do peso")
    print("Procure um médico")
    print("Procure um nutricionista")
    print("Procure um endocrinologista")

