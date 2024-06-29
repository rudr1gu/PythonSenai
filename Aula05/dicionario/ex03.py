# Crie um sistema onde a pessoa poderá cadastrar carros. Para cadastrar um carro é necessário fornecer o nome do carro e o preço FIPE deste carro.

carros = {}
def cadastrarCar():
    carro = input('Informe o nome do carro')
    valor = float(input('informe o valor do carro'))
    carros[carro] = valor
    print(carros)

cadastrarCar()