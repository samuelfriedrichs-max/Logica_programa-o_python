class Cachorro:

    def __init__(self, nome, raca, idade, pode_latir=True):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.pode_latir = pode_latir

    def latir(self):
        if self.pode_latir:
            print(f"{self.nome} diz: Au Au!")
        else:
            print(f"{self.nome} não late.")

    def mostrar_info(self):
        print(self.nome)
        print(self.raca)
        print(self.idade)


# Exemplo de uso:
Cachorro1 = Cachorro("Rex", "Pitbull", 3, pode_latir=True)
Cachorro1.mostrar_info()
Cachorro1.latir()  # Saída: Rex diz: Au Au!

Cachorro2 = Cachorro("Soneca", "Buldogue", 5, pode_latir=False)
Cachorro2.mostrar_info()
Cachorro2.latir()  # Saída: Soneca não late.

Cachorro2.idade = 7
Cachorro2.mostrar_info()