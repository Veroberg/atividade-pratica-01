# Atividade Prática 01 - Questão 4
#
# Desenvolva um programa que calcule o preço total de uma compra. Use as seguintes informações:
# Nome do produto: "Cadeira Infantil"
# Preço unitário: R$ 12.40
# Quantidade: 3
# O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.
#
# -----------------------------------------------------------------

# Exemplo resolvido:
produto = "Cadeira Infantil"
preco_unitario = 12.40
quantidade = 3

preco_total = preco_unitario * quantidade

print("Exemplo resolvido:")
print("Produto:", produto)
print("Preço unitário: R$", preco_unitario)
print("Quantidade:", quantidade)
print("Preço total: R$", round(preco_total, 2))
print("-" * 20)

# Código interativo:
print("Opção para o professor testar outros valores:")
produto = input("Digite o nome do produto: ")
preco_unitario = float(input("Digite o preço unitário (ex: 12.40): "))
quantidade = int(input("Digite a quantidade: "))
preco_total = preco_unitario * quantidade
print("Preço total da nova compra: R$", round(preco_total, 2))
