# Calculadora de Volume de uma Caixa Retangular

# Atividade Prática 01 - Questão 3
#
# Crie um programa que calcule o volume de uma caixa retangular.
# Use as seguintes dimensões:
# Comprimento: 12 cm
# Largura: 14 cm
# Altura: 20 cm
# O programa deve calcular o volume e exibir o resultado em cm³.
#
# -----------------------------------------------------------------

# Exemplo resolvido:
comprimento = 12
largura = 14
altura = 20

volume = comprimento * largura * altura

print("Exemplo resolvido:")
print("Dimensões da caixa:")
print("Comprimento:", comprimento, "cm")
print("Largura:", largura, "cm")
print("Altura:", altura, "cm")
print("Volume =", volume, "cm³")
print("-" * 20)

# Código interativo:
print("Opção para o professor testar outros valores:")
comprimento = int(input("Digite o comprimento (cm): "))
largura = int(input("Digite a largura (cm): "))
altura = int(input("Digite a altura (cm): "))
volume = comprimento * largura * altura
print("Volume da nova caixa =", volume, "cm³")
