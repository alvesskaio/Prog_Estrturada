"""
Monte uma função que recebe um salário por hora e o número de horas trabalhadas
no mês, e retorne o salário a ser recebido.

"""

def salarioReceber (salarioHora, horasTrabalhadas):
    return salarioHora * horasTrabalhadas

def main():
    print(salarioReceber(50,10))

main()