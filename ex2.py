"""
2 -Faça um programa que receba o valor de uma dívida e mostre as opções de parcelamento.

O resultado final deve conter as opções de 1, 3, 6, 9 ou 12 parcelas,
e o percentual de juros para cada parcela deve ser determinado conforme a primeira tabela, abaixo.

O relatório com as opções de pagamento deve conter os seguintes dados:
valor dos juros, valor total da dívida (incluindo juros),
quantidade de parcelas e valor da parcela.

A segunda tabela, abaixo, mostra um exemplo de como o resultado deve ser exibido.
 No momento, não é necessário formatar os valores.

Quantidade de Parcelas            % de Juros sobre o valor inicial da dívida
 1                                  0
 3                                  10
 6                                  15
 9                                  20
 12                                 25

Valor dos Juros   Valor Total      Quantidade de Parcelas   Valor da Parcela
 0                 R$ 1.000,00      1                        R$  1.000,00
 R$ 100,00         R$ 1.100,00      3                        R$    366,00
 R$ 150,00         R$ 1.150,00      6                        R$    191,67

"""

# Não consegui fazer


def pula_linha():
  print("\n")

def mostra_parcelamento(valor_divida):

  tabela_juros = {
      1: 0,
      3: 10,
      6: 15,
      9: 20,
      12: 25
  }

  for i in range(6):
    tabela_juros.split(",")
    print()


mostra_parcelamento(1000)

  # for op in range(1, 13):
  #   print(f"valor dos juros = {} \n"
  #         f"valor total da dívida = {} \n"
  #         f"quantidade de parcelas = {} \n"
  #         f"valor da parcela = {}")












mostra_parcelamento()