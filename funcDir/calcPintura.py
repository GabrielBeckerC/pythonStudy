
def calculo_tinta( altura, largura, rendimento):
    area_parede = altura * largura
    total_tinta = area_parede / rendimento
    print(f'Você necessita de {total_tinta} latas de tinta.')
