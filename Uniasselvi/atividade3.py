# n1 = float(input("Digite a nota 1 do aluno: "))
# n2 = float(input("Digite a nota 2 do aluno: "))
# frequencia = int(input("Digite a frequência do aluno: "))

# m = (n1 + n2)/2


# if m >= 7.0 and frequencia >= 75:
#     print(f"Média do aluno é: {m} e a frequência é de: {frequencia} e situação do aluno: aprovado ")
# elif m >= 5.0 and m < 7.0 and frequencia >= 75:
#     print(f"Média do aluno é: {m} e a frequência é de: {frequencia} e situação do aluno: recuperação ")
# else:
#     print(f"Média do aluno é: {m} e a frequência é de: {frequencia} e situação do aluno: reprovado ")

while True:
    try:
        # Entradas
        n1 = float(input("Digite a nota 1 do aluno: "))
        n2 = float(input("Digite a nota 2 do aluno: "))
        frequencia = int(input("Digite a frequência do aluno: "))

        # Validação de números negativos
        if not (0 <= n1 <= 10) or not (0 <= n2 <= 10) or not (0 <= frequencia <= 100):
            print("Valores fora do intervalo permitido. Tente novamente.\n")
            continue

        break

    # Validação de casos de entradas inválidas
    except ValueError:
        print("Entrada inválida! Digite apenas números.\n")

# Cálculo da média
m = (n1 + n2) / 2

# Condição
if m >= 7.0 and frequencia >= 75:
    print(f"Média do aluno é: {m} e a frequência é de: {frequencia}% e situação do aluno: aprovado")
elif 5.0 <= m < 7.0 and frequencia >= 75:
    print(f"Média do aluno é: {m} e a frequência é de: {frequencia}% e situação do aluno: recuperação")
else:
    print(f"Média do aluno é: {m} e a frequência é de: {frequencia}% e situação do aluno: reprovado")