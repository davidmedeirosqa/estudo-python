# # while

# num = 1

# while (num <= 10): # Pré-teste
#     print(num)
#     num += 1 # num = num + 1

# print('Laço encerrado')

# nome = None

# while True: # Pós-teste
#     print('Digite seu nome, ou X para parar')
#     nome = input()

#     if nome == "x" or nome == "X":
#         print('Você parou')
#         break

#     print(f'Bem vindo, {nome}')

#########################################################

# # For

# # Sintaxe: for item in sequência:

# lista = [2, 6, 9, 4, 0, 12, 3, 7]

# for item in lista:
#     print(item)

# palavra = 'Python'

# for letra in palavra:
#     print(letra)

# for num in range(0,11):
#     print(num)

# nome = input('Digite seu nome: ')

# for x in range(10):
#     print(f'{x+1} {nome}')

# range(valor_inicial, valor_final, incremento)
# for x in range(2, 20, 2):
#     print(x)

pedras = ('Rubi', 'Esmeralda', 'Quartzo', 'Safira', 'Diamante', 'Turmalina')

for pedra in pedras:
    if pedra == 'Quartzo':
        continue
    print(pedra)