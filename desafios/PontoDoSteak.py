"""
Criar um programa que dependendo da temperatura (em celsius) do steak ele retorna o ponto de cozimento em portugues. O usuário deverá fornecer a temperatura.

Temperaturas - Cozimento
120°F ou 49°C - Rare (Selada)
130°F ou 54°C - Medium Rare (Ao ponto para o mal)
140°F ou 60°C - Medium (Ao ponto)
150°F ou 66°C - Medium Well (Ao ponto para o bem)
160°F ou 71°C - Well Done (Bem passada)
"""

temperatura = int(input("Informe a temperatura da carne em ºC: "))

if temperatura <= 49:
    print("Rare (Selada)")
elif temperatura <= 54:
    print("Medium Rare (Ao ponto para o mal)")
elif temperatura <= 60:
    print("Medium (Ao ponto)")
elif temperatura <= 65:
    print("Medium Well (Ao ponto para o bem)")
else:
    print("Well Done (Bem passada)")