# import os
# print(os.getcwd())

# # Manipulação de arquivos de texto

# Modos de acesso do open() no Python:
# "r"   leitura
# "w"   escrita (sobrescreve)
# "a"   adiciona ao final
# "x"   cria novo arquivo
#
# "r+"  leitura e escrita
# "w+"  leitura e escrita (sobrescreve)
# "a+"  leitura e escrita (adiciona ao final)
#
# "t"   modo texto (padrão)
# "b"   modo binário (ex: "rb", "wb", "r+b", "w+b", "a+b")
# "+"   atualização - leitura e escrita

# manipulador = open(r'C:\Python\Boson_Treinamentos\Manipulação_de_arquivos\arquivo.txt', 'r', encoding='UTF-8')

# print(f'\Método read():\n')
# print(manipulador.read())

# print(f'\Método read():\n')
# print(manipulador.readline())
# print(manipulador.readline())

# print(f'\Método read():\n')
# print(manipulador.readlines())

# texto = input('Qual termo deseja procurar no arquivo? ')

# try:
#     manipulador = open('C:\\Python\\Boson_Treinamentos\\Manipulação_de_arquivos\\arquivo.txt', 'r', encoding='UTF-8')
#     encontrou = False
#     for linha in manipulador:
#         linha = linha.rstrip()
#         if texto in linha:
#             print('A string foi encontrada')
#             encontrou = True
#             print(linha)
#             break
#     if not encontrou:
#         print ('A string não foi encontrada')
        
# except IOError:
#     print('Não foi possível abrir o arquivo')
# else:
#     manipulador.close()

#####################################################

# # Escrever em arquivos de texto

# texto = input('Adicione um texto: ')

# try:
#     manipulador = open('C:\\Python\\Boson_Treinamentos\\Manipulação_de_arquivos\\arquivo.txt', 'a', encoding='UTF-8')
#     # manipulador.write('Python é empregada em IA\n')
#     # manipulador.write('Como criar um arquivo de texto com Python\n')
#     manipulador.write(texto)

# except IOError:
#     print('Não foi possível abrir o arquivo')
# else:
#     manipulador.close()

#################################################################

# Criar e gravar o arquivo

frutas = ['Morango\n', 'Uva\n', 'Caju\n', 'Amora\n', 'Framboesa\n', 'Graviola']

try:
    manipulador = open('C:\\Python\\Boson_Treinamentos\\Manipulação_de_arquivos\\frutas.dat', 'w', encoding='UTF-8')
    manipulador.writelines(frutas)

except IOError:
    print('Não foi possível abrir o arquivo')
else:
    manipulador.close()

    
try:
    manipulador = open('C:\\Python\\Boson_Treinamentos\\Manipulação_de_arquivos\\frutas.dat', 'r', encoding='UTF-8')
    print(manipulador.read())

except IOError:
    print('Não foi possível abrir o arquivo')
else:
    manipulador.close()