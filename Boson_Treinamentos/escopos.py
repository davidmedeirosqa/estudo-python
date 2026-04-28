# Escopo local e global

var_global = 'Curso Python'

def escreve_texto():
    global var_global
    var_global = 'Banco de dados com SQL'
    var_local = 'David'
    print(f'Variável global: {var_global}')
    print(f'Variável local: {var_local}')

if __name__ == '__main__':
    print(f'Executar a função escreve_texto()')
    escreve_texto()

    print('Testar acessar as variáveis diretamente')
    print(f'Variável global: {var_global}')