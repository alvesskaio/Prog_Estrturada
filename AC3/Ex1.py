"""
1- Uma empresa resolveu dar um aumento de salário aos seus colaboradores e lhe
contrataram para desenvolver o programa que calculará os reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo a
tabela a seguir, baseado no salário atual. Após o aumento ser realizado,
informe na tela:

O salário antes do reajuste;
O percentual de aumento aplicado;
O valor do aumento;
O novo salário, após o aumento.
"""

def cal_reajustes(salario):

    if salario >= 1500:
        percentual = 5
    elif salario > 700 and salario < 1500:
        percentual = 10
    elif salario > 280 and salario < 700:
        percentual = 15
    elif salario <= 280:
        percentual = 20

    valor_reajustado = ((salario / 100) * percentual)
    salario_reajustato = salario + valor_reajustado

    print(f'Salário= R${salario}, '
        f'Percentual de aumento= {percentual}%, '
        f'Valor a reajustar= R${valor_reajustado}, '
        f'Salário reajustado= R${salario_reajustato}')


cal_reajustes(200)