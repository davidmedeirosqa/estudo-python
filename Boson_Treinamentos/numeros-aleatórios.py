import random

# valor = random.randint(1, 20)
# print(valor)

# print('Gerar cinco números aleatórios entre 1 e 50: \n') 
# for i in range(5):
#     n = random.randint(1,50)
#     print(f'Número gerado: {n}')

# valor = random.random()
# print(f'Número gerado: {round(valor * 10, 2)}') # round - arredondar o número

# valor = random.uniform(1, 100)
# print(f'Número: {valor}')

# L = [2, 4, 6, 9, 10, 13, 14,18, 20, 21, 27, 33]
# n = random.choice(L) # random - escolhe um número aleatório da lista
# print(f'Número escolhido: {n}') 

# S = [2, 4, 6, 9, 10, 13, 14,18, 20, 21, 27, 33]
# n = random.sample(S, 3) # sample - escolhe x números aleatórios da lista
# print(f'Números escolhidos: {n}')

# Embaralhar a lista

E = [2, 4, 6, 9, 10, 13, 14,18, 20, 21, 27, 33]
print(f'Lista original: {E}')

random.shuffle(E) # shuffle - embaralha a lista
print (f'Lista embaralhada: {E}')