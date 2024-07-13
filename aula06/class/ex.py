#orientação Objeto 
class cachorro:
    def __init__(self, nome, raca, idade, cor, peso):
        self.setNome(nome)
        self.setRaca(raca)
        self.setIdade(idade)
        self.setCor(cor)
        self.setPeso(peso)
    
    def latir(self):
        print('Au au')
    
    def getNome(self):
        return self.nome
    def setNome(self, nome):
        self.nome = nome

    def getRaca(self):
        return self.raca
    def setRaca(self, raca):
        self.raca = raca
    
    def getIdade(self):
        return self.idade
    def setIdade(self, idade):
        self.idade = idade
    
    def getCor(self):
        return self.cor
    def setCor(self, cor):
        self.cor = cor
    
    def getPeso(self):
        return self.peso
    def setPeso(self, peso):
        self.peso = peso


cachorro1 = cachorro('Rex', 'vira-lata', 5, 'Caramelo', 10)
print(cachorro1.nome)
cachorro1.latir()

cachorro1.setNome('djaaa')
print(cachorro1.getNome())

        