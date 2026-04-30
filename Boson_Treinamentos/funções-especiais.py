from functools import reduce

# # Função lambda (anônimas)
# # Sintaxe:
# # lambda argumentos: expressão

# quadrado = lambda x: x ** 2

# for i in range(1, 11):
#     print(quadrado(i))

# par = lambda x: x %2 == 0
# print(par(2))

# f_c = lambda f: (f - 32) * 5/9
# print(f_c(212))

# comp = lambda comp: comp >= 100
# print(comp(99))

#####################################################

# # Função map()
# # Função interna do Python
# # Sintaxe:
# # map(função, iterável)

# num = [1, 2, 3, 4 , 5 , 6, 7, 8]
# dobro = list(map(lambda x: x*2,num)) # Necessário converter para lista
# print(dobro)

# palavras = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']
# maiusculas = list(map(str.title, palavras)) # Necessário converter para lista
# print(maiusculas)

#####################################################

# # Função filter()
# # Sintaxe:
# # filter(função, sequência)

# def numeros_pares(n):
#     return n % 2 == 0

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# num_par = list(filter(numeros_pares, numeros)) # Necessário converter para lista
# print(num_par)

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# num_imp = list(filter(lambda x: x %2 != 0, numeros)) # Necessário converter para lista
# print(num_imp)

#####################################################

# # Função reduce()
# # Sintaxe:
# # reduce(função, sequência, valor_inicial)

# # Necessário importação

# def sum(x, y):
#     return x + y

# numeros = [1, 2, 3, 4, 5, 6, 9]
# total = reduce(sum, numeros)
# print(total)

# Soma acumulativa dos quadrados dos valores, usando a expressão lambda
# ((1² + 2²)² + 3²)² + 4²

numeros = [1, 2, 3, 4]
total = reduce(lambda x, y: x ** 2 + y ** 2, numeros)
print(total)