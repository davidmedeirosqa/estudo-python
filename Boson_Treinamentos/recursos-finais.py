# Trocar valores entre duas variáveis
# var1 = 12
# var2 = 31

# var2, var1 = var1, var2

# print(var1, var2)

###############################

# Operador Condicional Ternário
# var1 = 12
# var2 = 31

# menor = var1 if var1 < var2 else var2
# print(menor)

###############################

# Generators
# valores = [1, 3, 5, 7, 8]
# quadrados = (item ** 2 for item in valores)
# print(quadrados)

###############################

# Função enumerate()
# bebidas = ['Café', 'Chá', 'Água', 'Suco', 'Refrigerante']
# for i, item in enumerate(bebidas):
#     print(f'Índice: {i}, Item: {item}')

# temperaturas = [-1, 10, 5, -3, 8, 4, -2, -5, 7]
# total = 0

# for i, t in enumerate(temperaturas):
#     if t < 0:
#         total += 1

# print(f'Há {total} temperaturas negativas nas amostras')

# for i, t in enumerate(temperaturas):
#     if t < 0:
#         print(f'A temperatura em {i} é negativa, com {t} ºC.')

###############################

# Gerenciamento de contexto com with 

with open('C:\\Python\\Boson_Treinamentos\\Manipulação_de_arquivos\\frutas.dat', 'r', encoding='UTF-8') as a:
    for linha in a:
        print(linha, end='-')