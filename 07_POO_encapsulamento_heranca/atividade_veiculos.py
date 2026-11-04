class Veiculo:

    def __init__(self, marca, modelo):
        # Atributos comuns a qualquer veículo
        self.marca = marca
        self.modelo = modelo
        self.ligado = False  #Todo veículo inicia desligado por padrão

    def ligar(self):
        self.ligado = True
        print(f"{self.marca} {self.modelo} ligado.")

    def mostrar_info(self):

        # Valida o estado atual para exibir um texto legível
        status = "ligado" if self.ligado else "desligado"
        print(f"Veículo: {self.marca} {self.modelo} | Status: {status}")



# 2. CLASSES FILHAS (HERANÇA)
class Carro(Veiculo):

    def __init__(self, marca, modelo, portas):

        # super().__init__() executa o construtor da classe mãe (Veiculo),
        # definindo self.marca, self.modelo e self.ligado = False
        super().__init__(marca, modelo)
        self.portas = portas  # Atributo exclusivo da classe Carro

    def abrir_porta_malas(self):

        # Método exclusivo da classe Carro
        print(f"Porta-malas do {self.marca} {self.modelo} aberto com sucesso!")


class Moto(Veiculo):

    def __init__(self, marca, modelo, cilindradas):

        # Reaproveita a inicialização da classe mãe
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas  # Atributo exclusivo da classe Moto

    def empinar(self):

        # Método exclusivo da classe Moto com validação de regra de negócio
        if self.ligado:
            print(
                f"A moto {self.marca} {self.modelo} de {self.cilindradas}cc"
                " está empinando!"
            )
        else:
            print(
                f"Atenção: Não é possível empinar. A {self.marca} {self.modelo}"
                " está desligada!"
            )


# 3. TESTES E EXECUÇÃO

print("--- TESTANDO O CARRO ---")
meu_carro = Carro(marca="Toyota", modelo="Corolla", portas=4)

# Métodos herdados de Veiculo (funcionam mesmo sem estarem escritos em Carro)
meu_carro.mostrar_info()
meu_carro.ligar()
meu_carro.mostrar_info()

#métod0 exclusivo de carro
meu_carro.abrir_porta_malas()


print("\n--- TESTANDO A MOTO ---")
minha_moto = Moto(marca="Honda", modelo="CB 500", cilindradas=500)

# Métodos herdados de Veiculo
minha_moto.mostrar_info()

# Tentativa de empinar com a moto desligada (Validação acionada)
minha_moto.empinar()

# Ligando e empinando
minha_moto.ligar()
minha_moto.empinar()