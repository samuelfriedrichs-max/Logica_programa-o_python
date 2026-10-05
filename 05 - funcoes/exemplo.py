#O que é uma função?

#Uma função é um bloco de código criado para realizar uma determinada tarefa.
# Ela permite organizar e reutilizar código.

#1. Criando uma função
#utilizar a palavra def para uma função

def saudacao():
        print("Olá seja bem-vindo!")

saudacao()

#2. Criando uma função com parâmetro

#parâmetros permitem enviar informações para a função
def saudacao():
        print(f"olá {nome}")

saudacao("Ana")
saudacao("João")

#3. Mais um parâmetro
def apresentar()
        print(f"nome: {nome}")
        print(f"idade: {idade}")

apresentar("Maria", 17)
apresentar("joao", 20)

#4. Função com calculo

def somar(num1, num2):
    resultado = num1 + num2
    print(f"Resultado {resultado}")
somar(num1 = 10, num2 = 20)
somar(num1 = 10, num2 = 90)


#5. Retornando um valor
#return devolve um valor par ao local onde a função foi chamada
def somar(num1, num2):
    return num1 + num2


print(somar(num1 = 10, num2 = 5))

# 6. funçãocom condição
def verificarIdade(idade):
        if idade >= 18:
            return "Maior de idade"
        else:
            return "Menor de idade"
print(verificarIdade(20))

#7 Parâmetro com valor padrão
def saudacao(nome="Aluno"):
    print(f"Ola {nome}")


saudacao("Joao")
saudacao()

#8. Função utilizando lista
def calcularMedia():
    for nota in notas:
        soma += nota
    return soma / len(notas)


notas = [8, 7, 9, 10]
media = calcularMedia(notas)
print(f"média: {media}")