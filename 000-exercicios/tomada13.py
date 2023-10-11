# Ler 4 números inteiros positivos t1,t2,t3,t4
#

tomada_regua = input()

num_tomada = tomada_regua.split(" ")

t1,t2,t3,t4 = [int(x) for x in num_tomada]

print(t1,t2,t3,t4 - 3)
