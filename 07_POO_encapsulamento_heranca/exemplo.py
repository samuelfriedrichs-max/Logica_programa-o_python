# 1. Encapsulamento
# Proteger o salário para que so mude seguindo regras
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario


    # privado: dois sublinhados
    def apresentar(self):
        print(f"Sou {self.nome} e ganho R${self.__salario:.2f}")


    # deixa ler o salario como se fosse um atributo
    @property
    def salario(self):
        return self.__salario


    def dar_aumento(self, porcentagem):
        if porcentagem <= 0:
            print(f"Aumento invalido par {self.nome}")
            return
        self.__salario = self.__salario * (1 + porcentagem / 100)
        print(f"{self.nome} recebeu {porcentagem}% de aumento")


##################################################################################
ana = Funcionario(nome='Ana', salario=3000)
ana.__salario = 4000
print(ana.salario)
ana.apresentar()
ana.dar_aumento(20)
ana.apresentar()


ana.__salario = 5000
ana.apresentar()


# 0 try/except é um bloco usado em programação para tra
try:
    ana.salario = 10000
except AttributeError:
    print("Não é permitido alterar o salário diretamente")


try:
    print(ana.__salario)
except AttributeError:
    print("O atributo __salario nao pode ser acessado de fora")

# Herança
class Gerente(Funcionario):

    # 1. Adicionado o parâmetro 'equipe'
    def __init__(self, nome, salario, equipe):
        super().__init__(nome, salario)
        self.equipe = equipe

    # 2. Indentação recuada (agora é um metodo da classe Gerente)
    def mostrar_equipe(self):
        print(f"{self.nome} gerencia {self.equipe}")

class Estagiario(Funcionario):
    def __init__(self, nome, salario, curso):
        super().__init__(nome, salario)
        self.curso = curso

print("\n======== Herança ========")

bruno = Gerente("Bruno" , 8000, 5)
caio = Estagiario("Caio", 1500, "Análise de sistemas")

bruno.apresentar()
caio.apresentar()

bruno.mostrar_equipe()
