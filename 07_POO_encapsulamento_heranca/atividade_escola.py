# ==============================================================================
# 1. CLASSE MÃE (BASE)
# ==============================================================================
class Pessoa:

    def __init__(self, nome, idade):
        # Atributos básicos compartilhados por qualquer pessoa na escola
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, eu sou {self.nome} e tenho {self.idade} anos.")


# ==============================================================================
# 2. CLASSES FILHAS (HERANÇA)
# ==============================================================================
class Aluno(Pessoa):

    def __init__(self, nome, idade, matricula):
        # super().__init__() envia nome e idade para a classe mãe Pessoa
        super().__init__(nome, idade)
        self.matricula = matricula
        self.notas = []  # Todo aluno começa com uma lista de notas vazia

    def adicionar_nota(self, nota):
        self.notas.append(nota)
        print(f"Nota {nota} adicionada para o aluno {self.nome}.")

    def media(self):
        # Proteção para evitar divisão por zero se a lista estiver vazia
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)


class Professor(Pessoa):

    def __init__(self, nome, idade, disciplina):
        # Reaproveita a inicialização de nome e idade da classe Pessoa
        super().__init__(nome, idade)
        self.disciplina = disciplina  # Atributo exclusivo do Professor

    def dar_aula(self):
        print(f"Prof. {self.nome} está dando aula de {self.disciplina}.")


# ==============================================================================
# 3. TESTES E EXECUÇÃO
# ==============================================================================
print("--- TESTANDO O ALUNO ---")
aluno1 = Aluno(nome="Lucas", idade=17, matricula="2026-001")

# Método herdado da classe Pessoa
aluno1.apresentar()

# Média antes de adicionar notas (deve retornar 0)
print(f"Média inicial (sem notas): {aluno1.media()}")

# Adicionando notas
aluno1.adicionar_nota(8.5)
aluno1.adicionar_nota(9.0)
aluno1.adicionar_nota(7.5)

# Exibindo a média final
print(f"Média do aluno {aluno1.nome}: {aluno1.media():.2f}")


print("\n--- TESTANDO O PROFESSOR ---")
prof1 = Professor(nome="Helena", idade=35, disciplina="Python")

# Método herdado da classe Pessoa
prof1.apresentar()

# Método exclusivo da classe Professor
prof1.dar_aula()