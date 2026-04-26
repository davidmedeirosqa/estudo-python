# # Simples, composto ou encadeado

###########################################

# # Simples

# n1 = n2 = 0.0
# media = 0.0

# n1 = float(input('Digite a primeira nota: '))
# n2 = float(input('Digite a segunda nota: '))

# media = (n1 + n2) / 2

# if (media >= 7):
#     print('Aprovado')

# print('Sua média é {}'.format(media)) # Formatação de strings

###########################################

# # Composto

# n1 = n2 = 0.0
# media = 0.0

# n1 = float(input('Digite a primeira nota: '))
# n2 = float(input('Digite a segunda nota: '))

# media = (n1 + n2) / 2

# if (media >= 7):
#     print('Aprovado')
# else:
#     print('Reprovado')

# print('Sua média é {}'.format(media))

###########################################

# Encadeado

n1 = n2 = 0.0
media = 0.0

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if (media >= 7):
    print('Aprovado')
elif (media >= 5):
    print('Recuperação')
else:
    print('Reprovado')

print('Sua média é {}'.format(media))