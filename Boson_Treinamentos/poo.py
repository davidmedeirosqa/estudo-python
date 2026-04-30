# Orientação a Objetos: Paradigma de Programação
# Classes e Objetos

class Veiculo:
    def movimentar(self):
        print('Sou um veículo e me desloco')

    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante # __ - Encapsulamento, ou seja, está privado
        self.__modelo = modelo # __ - Encapsulamento, ou seja, está privado
        self.__num_registro = None # __ - Encapsulamento, ou seja, está privado

    # Setter - Permite gravar dado em um elemento dentro da classe
    def set_num_registro(self, registro):
        self.__num_registro = registro

    # Getter - Permite acessar os atributos direto da classe
    def get_fabr_modelo(self):
        print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante}.\n')
    
    def get_num_registro(self):
        return self.__num_registro

class Carro(Veiculo):
    # Método __init__ será herdado
    def movimentar(self):
        print('Sou um carro e ando pelas ruas')

class Motocicleta(Veiculo):
    def movimentar(self):
        print('Sou uma motocicleta')

class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.__cat = categoria
        super().__init__(fabricante, modelo)

    def get_categoria(self):
        return self.__cat
    
    def movimentar(self):
        print('Eu voo alto')

if __name__ == '__main__':
    # meu_veiculo = Veiculo('GM', 'Cadillac Escalade')
    # meu_veiculo.movimentar() 
    # meu_veiculo.get_fabr_modelo()
    # meu_veiculo.set_num_registro('490321-1')
    # print(f'Registro: {meu_veiculo.get_num_registro()}\n')

    # meu_carro = Carro('Volkswagen', 'Polo')
    # meu_carro.movimentar()
    # meu_carro.get_fabr_modelo()

    # seu_carro = Carro('Audi', 'A5')
    # meu_carro.movimentar()
    # meu_carro.get_fabr_modelo()

    # moto = Motocicleta('Harley-Davidson', 'Nighster Special')
    # moto.movimentar()
    # moto.get_fabr_modelo()

    meu_aviao = Aviao('Boeing', '747', 'Comercial')
    meu_aviao.movimentar()
    meu_aviao.get_fabr_modelo()
    print(f'Categoria: {meu_aviao.get_categoria()}')