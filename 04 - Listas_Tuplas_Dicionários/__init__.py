# Listas, Tuplas e Dicionários

# 1. Listas
# Listas são utilizadas para armazenar vários valores numa única variável
nomes = ["ana", "Carlos", "João", "Maria"]
print(nomes)

# 2. Acedendo aos elementos da lista
print(nomes[0])
# Podemos aceder ao último elemento usando o -1
print(nomes[-1])

# 3. Alterando elementos
nomes[0] = "Pedro"
print(nomes)

# 4. Adicionar elementos
# append() adiciona um elemento ao final da lista
nomes.append("Lucas")
print(nomes)

# insert() adiciona um elemento numa posição específica
nomes.insert(1, "Mariana")
print(nomes)

# 5. Removendo elementos
# remove() remove um elemento pelo valor (deve corresponder exatamente a maiúsculas/minúsculas)
nomes.remove("Lucas")
print(nomes)

# pop() remove um elemento pelo índice
nomes.pop(0)
print(nomes)

# 6. Tamanho da lista
# len() informa a quantidade de elementos
print(len(nomes))

# 7. Percorrendo uma lista
for nome in nomes:
    print(nome)

# 8. Verificando se um elemento existe
if "João" in nomes:
    print("João está na lista")
else:
    print("João não está na lista")

# 9. Lista com diferentes tipos de dados
dados = ["João", 18, 1.75, True]
print(dados)

# 10. Lista de números
notas = [7.5, 8.0, 6.5, 9.0]
soma = 0
for nota in notas:
    soma = soma + nota

media = soma / len(notas)
print(f"Média: {media}")

# 11. Tuplas
coordenadas = (10, 20)
print(coordenadas)

# 12. Dicionários
# Dicionários armazenam informações no formato: chave: valor
aluno = {
    "nome": "Carlos",
    "idade": 17,
    "nota": 8.5
}
print(aluno)

# 13. Acedendo aos valores do dicionário
print(aluno["nome"])
print(aluno["idade"])
print(aluno["nota"])

# 14. Alterando os valores
aluno["nota"] = 9.0
print(aluno)

# 15. Adicionando novos dados
aluno["curso"] = "Informática"
print(aluno)

# 16. Removendo dados
del aluno["curso"]
print(aluno)

# 17. Percorrendo um dicionário
for chave in aluno:
    print(chave)

# Podemos aceder à chave e ao valor ao mesmo tempo.
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")