#A Classe: O modelo (a planta)
class celular:
    def __init__(self, marca, modelo, cor, bateria = 100 ):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.bateria = bateria
        self.ligado = False

    def ligar(self):
        if self.bateria == 0:
            print("Sem bateria! Coloque para carregar")
        else:
            self.ligado = True
            print(f"{self.modelo} Ligado!")

#Os objetos Criados apartir da classe (as "casas")
celular1 = celular("Samsung", "Galaxy a23", "preto")
celular2 = celular("motorola", "Moto-G", "azul", 30)

#Acessando e alterando atributos
print(celular2.marca)

#também podemos alterar diretamente
celular1.cor = "branco"
print(celular1.cor)

#chamando métodos
celular2.ligar()
