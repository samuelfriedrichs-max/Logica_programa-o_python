# ==========================================
# 1. CADASTRO DE FILMES
# ==========================================

# 1. Criar lista inicial de 5 filmes
filmes = ["Justice League", "Spider-man", "Batman", "Superman", "Iron Man"]

# 2. Exibir todos os filmes
print("\nFilmes cadastrados:")
print(filmes)

# 3. Exibir o primeiro filme
print("\nPrimeiro filme:")
print(filmes[0])

# 4. Exibir o último filme
print("\nÚltimo filme:")
print(filmes[-1])

# 5. Adicionar novo filme ao final
filmes.append("Ant Man")
print("\nApós adicionar Ant Man ao final:")
print(filmes)

# 6. Inserir em posição específica (índice 1)
filmes.insert(1, "Captain America")
print("\nApós inserir Captain America no índice 1:")
print(filmes)

# 7. Remover um filme
filmes.remove("Superman")
print("\nApós remover Superman:")
print(filmes)

# 8. Alterar o nome do primeiro filme
filmes[0] = "Avengers"
print("\nApós alterar o primeiro filme para Avengers:")
print(filmes)

# 9. Exibir quantidade cadastrada
print(f"\nA quantidade total de filmes é: {len(filmes)}")

# 10. Verificar se um filme está presente
if "Batman" in filmes:
    print("\nBatman está na lista")
else:
    print("\nBatman não está na lista")


# ==========================================
# 2. CONTROLE DE NOTAS
# ==========================================

# 1. Criar lista com 5 notas
notas = [8.0, 7.5, 6.0, 9.0, 10.0]

# 2. Exibir todas as notas
print("\nNotas do estudante:")
print(notas)

# 3. Calcular a soma das notas
soma = 0
for nota in notas:
    soma = soma + nota

print(f"\nA soma das notas é: {soma}")

# 4. Calcular a média das notas
media = soma / len(notas)
print(f"\nA média das notas é: {media}")

# 5. Identificar a maior nota
maior = notas[0]
for nota in notas:
    if nota > maior:
        maior = nota

print(f"\nA maior nota é: {maior}")

# 6. Identificar a menor nota
menor = notas[0]
for nota in notas:
    if nota < menor:
        menor = nota

print(f"\nA menor nota é: {menor}")

# 7. Verificar se existe nota igual a 10
if 10 in notas:
    print("\nExiste uma nota igual a 10")
else:
    print("\nNão existe uma nota igual a 10")

# 8 e 9. Informar aprovação ou reprovação (Média >= 7)
if media >= 7:
    print("\nO estudante foi aprovado")
else:
    print("\nO estudante foi reprovado")


# ==========================================
# 3. INFORMAÇÕES DE UM PRODUTO (TUPLA)
# ==========================================

# 1. Tupla do produto (Nome, Categoria, Preço, Código)
produto = ("Notebook", "Informática", 3500, 12345)

# 2. Exibir cada informação individualmente
print("\nNome do produto:")
print(produto[0])

print("\nCategoria:")
print(produto[1])

print("\nPreço:")
print(produto[2])

print("\nCódigo do produto:")
print(produto[3])

# 3. Exibir todas as informações com repetição
print("\nInformações do produto (loop):")
for informacao in produto:
    print(informacao)

# 4. Informar quantidade de informações
print(f"\nQuantidade de informações: {len(produto)}")

# 5. Tentar alterar informação e explicar a imutabilidade
# produto[0] = "Computador"  # Se descomentar esta linha, gerará um TypeError

print("\nNão é possível alterar uma informação da tupla.")
print("As tuplas são imutáveis e não podem ter seus elementos alterados após criadas.")


# ==========================================
# 4. CADASTRO DE FUNCIONÁRIO (DICIONÁRIO)
# ==========================================

# 1. Dicionário do funcionário
funcionario = {
    "nome": "Carlos",
    "idade": 25,
    "cargo": "Programador",
    "salario": 3500,
    "setor": "Tecnologia"
}

# Exibir cada informação
print("\nNome:", funcionario["nome"])
print("Idade:", funcionario["idade"])
print("Cargo:", funcionario["cargo"])
print("Salário:", funcionario["salario"])
print("Setor:", funcionario["setor"])

# 2. Alterar o salário do funcionário
funcionario["salario"] = 4000
print("\nNovo salário:")
print(funcionario["salario"])

# 3. Adicionar nova informação
funcionario["email"] = "carlos@email.com"
print("\nCadastro com nova informação:")
print(funcionario)

# 4. Remover informação do cadastro
funcionario.pop("idade")
print("\nCadastro após remover a idade:")
print(funcionario)

# 5. Verificar se determinada chave existe
if "cargo" in funcionario:
    print("\nA chave 'cargo' existe no cadastro")
else:
    print("\nA chave 'cargo' não existe no cadastro")

# 6. Percorrer o dicionário exibindo chaves e valores
print("\nInformações do funcionário:")
for chave in funcionario:
    print(chave, ":", funcionario[chave])


# ==========================================
# 5. SISTEMA DE ESTOQUE (LISTA DE DICIONÁRIOS)
# ==========================================

# 1. Lista de dicionários
estoque = [
    {
        "nome": "Notebook",
        "categoria": "Informática",
        "preco": 3500,
        "quantidade": 8
    },
    {
        "nome": "Mouse",
        "categoria": "Periféricos",
        "preco": 80,
        "quantidade": 15
    },
    {
        "nome": "Teclado",
        "categoria": "Periféricos",
        "preco": 150,
        "quantidade": 7
    },
    {
        "nome": "Monitor",
        "categoria": "Informática",
        "preco": 1200,
        "quantidade": 12
    },
    {
        "nome": "Headset",
        "categoria": "Periféricos",
        "preco": 200,
        "quantidade": 5
    }
]

# 2. Exibir todos os produtos cadastrados
print("\nProdutos cadastrados:")
print(estoque)

# Exibir nome, preço e quantidade em estoque
print("\nInformações resumidas dos produtos:")
for produto in estoque:
    print("Nome:", produto["nome"])
    print("Preço:", produto["preco"])
    print("Quantidade:", produto["quantidade"])
    print()

# 3. Calcular a quantidade total de itens no estoque
quantidade_total = 0
for produto in estoque:
    quantidade_total = quantidade_total + produto["quantidade"]

print(f"A quantidade total de itens no estoque é: {quantidade_total}")

# 4. Calcular o valor total do estoque
valor_total = 0
for produto in estoque:
    valor = produto["preco"] * produto["quantidade"]
    valor_total = valor_total + valor

print(f"\nO valor total do estoque é: R$ {valor_total}")

# 5. Identificar produtos com menos de 10 unidades
print("\nProdutos com menos de 10 unidades:")
for produto in estoque:
    if produto["quantidade"] < 10:
        print(produto["nome"])

# 6. Verificar se determinado produto está cadastrado
nome_produto = "Mouse"
encontrado = False

for produto in estoque:
    if produto["nome"] == nome_produto:
        encontrado = True

if encontrado:
    print(f"\n{nome_produto} está cadastrado")
else:
    print(f"\n{nome_produto} não está cadastrado")

# 7. Alterar a quantidade em estoque de um produto
for produto in estoque:
    if produto["nome"] == "Mouse":
        produto["quantidade"] = 20

print("\nQuantidade do Mouse alterada.")

# 8. Adicionar um novo produto
novo_produto = {
    "nome": "Webcam",
    "categoria": "Periféricos",
    "preco": 300,
    "quantidade": 6
}
estoque.append(novo_produto)

# 9. Relatório final do estoque
print("\nRelatório final do estoque:")
for produto in estoque:
    print("Nome:", produto["nome"])
    print("Categoria:", produto["categoria"])
    print("Preço:", produto["preco"])
    print("Quantidade:", produto["quantidade"])
    print("-------------------------")