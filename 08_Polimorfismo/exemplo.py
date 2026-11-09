# 3 Polimorfismo
# O mesmo mé
todo pode existir em várias classes mas apresentar comportamentos diferentes dependendo
# do objeto que está executando esse mé
todo
from encapsulamento.exemplo import Funcionario


class Gerente(Funcionario):
    def __init__(self, nome, salario, equipe ):
        super().__init__(nome, salario)
        self.equipe = equipe


    def bonus(self):
        return self.salario * 0.20 + self.equipe *
100
class Estagiario(Funcionario):
    def __init__(self, nome, salario, curso):
        super().__init__(nome, salario)
        self.curso = curso


    def bonus(self):
        return 200

print("\n ============== POLIMORFISMO ==============")


equipe = [
    Funcionario("Funcionario", 200),
    Gerente("Gerente", 200),
    Estagiario("Estagiario", 200)
]


for funcionario in equipe:
    print(f"{funcionario.nome}: R$ {funcionario.bonus()}")