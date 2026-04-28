# nome = 'David'
# sobrenome = 'Medeiros'
# letra = nome[2]
# print(letra)
# print(len(nome))
# print(nome + ' ' + sobrenome)

# frase = "Vamos aprender Python hoje"
# # palavras = frase.split()
# # print(palavras)

# # for palavra in palavras:
# #     print(palavra)

# # for letra in frase:
# #     print(letra)

# print(frase[0:5])

# email = input('Digite seu endereço de e-mail: ')
# arroba = email.find('@')
# print(arroba)

# usuario = email[0:arroba]
# dominio = email[arroba+1:]

# print(usuario)
# print(dominio)

# produtos = 'carbonato de sódio e óxido de zinco'
# print('sódio' in produtos)
# print('magnésio' not in produtos)

# item = 'hipoclorito'
# pos = item.find('clor')
# print(pos)
# pos = item.find('flu')
# print(pos)

# objeto_celeste = 'galáxia esPiral M31'
# print(objeto_celeste.upper())
# print(objeto_celeste.lower())
# print(objeto_celeste.capitalize())
# print(objeto_celeste.title())

# suplemento = 'cloreto de magnésio'
# n_suplemento = suplemento.replace('magnésio', 'zinco')
# print(suplemento)
# print(n_suplemento)

# frase = '   Vários espaços no início   '
# print(frase)
# print(frase.lstrip())
# print(frase.rstrip())
# print(frase.strip())

# fruta = 'Abacate'
# print(fruta)
# print(fruta.ljust(20))
# print(fruta.rjust(20))
# print(fruta.center(20))
# print(fruta.center(20, '-'))

p = 'Treinamento Python'
print(p.startswith('Tr'))
print(p.endswith('on'))

# Docstrings

"""
Docstrings é uma espécie de documentação
que podemos inserir dentro de um módulo, função ou classe
no Python, entre outros locais.
    Respeita deslocamento do texto e é multilinhas.
"""