# # Match Case

# dia = int(input("Digite o dia da semana: "))

# match dia:
#     case 1:
#         print("Domingo")
#     case 2:
#         print("Segunda-feira")
#     case 3:
#         print("Terça-feira")
#     case 4:
#         print("Quarta-feira")
#     case 5:
#         print("Quinta-feira")
#     case 6:
#         print("Sexta-feira")
#     case 7:
#         print("Sábado")
#     case _:    
#         print("Dia da semana inválido")

######################################################################################################################

# # While

# senha_atual = "123"
# senha_digitada = ""

# senha_digitada = input("Digite sua senha:")

# if senha_digitada != senha_atual:
#         print("Senha incorreta!")

# while senha_digitada != senha_atual:
#     senha_digitada = input("Digite novamente sua senha sua senha:")
#     if senha_digitada != senha_atual:
#         print("Senha incorreta!")

# print("Acesso liberado")

######################################################################################################################

# senha_atual = "123"
# senha_digitada = ""
# tentativa = 3

# while tentativa > 0:
#     senha_digitada = input("Digite sua senha:")
#     if senha_digitada == senha_atual:
#         print("Login efetuado com sucesso")
#         break
#     else:
#         tentativa -=1
#         print("Senha errada, você possui {} tentativa".format(tentativa))

# if tentativa == 0:
#     print("Você bloqueou seu acesso")

######################################################################################################################

# For

# Times = ["Flamengo", "Vasco", "Fluminense", "Botafogo"]

# for time in Times:
#     print(Times)

# for item in range(11):
#     print(item)

# for item in range(10,-1,-1):
#     print(item)

######################################################################################################################

# for numero in range(0,11):
#     if numero == 5:
#         print(numero)
#         continue
#     else:
#         print("Laço concluído sem interrupção - número não encontrado")

######################################################################################################################

# try:
#     x = int(input("Digite um número: "))
#     y = int(input("Digite outro número: "))
#     resultado = x / y
# except ZeroDivisionError:
#     print("Erro: Não é possível dividir por zero!")
# except ValueError:
#     print("Erro: Entrada inválida! Por favor, digite um número.")
# else:
#     print(f"O resultado é: {resultado}")

######################################################################################################################

# i = 10

# while i > 0:
#     print("Contagem:", i)
#     i -= 1