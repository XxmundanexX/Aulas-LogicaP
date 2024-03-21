#**Problema -2)**
#Faça um programa que calcule a quantidade de ração que sobra ao final de um período de dias tratando de três gatos famintos. Defina o peso do saco comprado e as quantidades diárias, almoço e jantar, dos seus bichanos.

g1 = float(input('Digite a quantidade de ração que o gato 1 come: '))
g2 = float(input('Digite a quantidade de ração que o gato 2 come: '))
g3 = float(input('Digite a quantidade de ração que o gato 3 come: '))

qtd_dias = int(input('Quantidade de dias que os gatos estão sendo alimentados: '))
peso_saco = float(input('Digite o peso do saco de ração comprado: '))

racao_comida = (g1 + g2 + g3) * (qtd_dias)
print(f'A quantidade total comida em {qtd_dias} dias foi de {racao_comida}')

resultado = peso_saco - racao_comida
print(f'A quantidade total de ração que sobrou ao final de {qtd_dias} dias foi de {resultado}')
