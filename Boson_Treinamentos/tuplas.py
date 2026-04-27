# São imutáveis

# tupla = (2, 4, 6, 7, 9)
# # tupla[1] = 5 # TypeError 
# print(tupla)

halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres
# t1 = (5, 2, 6, 8, 4, 5, 6, 4, 0, 12, 22, 3, 4, 5)
# print(t1.count(5)) # Contar quantas vezes aparece o número 5
# print(halogenios[0:2]) # Slice
# print('Fe' in halogenios)
# print(elementos)
# print(len(halogenios))
# print(halogenios[3])
# print(halogenios[-1])

# # Operações não disponíveis em tuplas: .sort(), append(), .reverse(), pop() ... 

# for elemento in elementos:
#     print(f'Elemento químico: {elemento}')

# grupo17 = list(halogenios) # Criando uma lista a partir de uma tupla
# grupo17[0] = 'H' # Adicionando valores na lista
# print(grupo17)

grupo1 = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
alcalinos = tuple(grupo1) # Criando uma tupla a partir de uma lista
print(type(alcalinos))

print(sorted(alcalinos)) # Ordenar em ordem crescente, sorted != sort