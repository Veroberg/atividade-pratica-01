# Atividade Prática 01 - Questão 5
#
# Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).
# Saída: Imprima a mensagem "DIFERENCA = " com todas as letras maiúsculas.
#
# -----------------------------------------------------------------

# Exemplo resolvido:
A = 5
B = 6
C = 7
D = 8

DIFERENCA = (A * B - C * D)

print("Exemplo resolvido:")
print("Valores informados: A =", A, "B =", B, "C =", C, "D =", D)
print("DIFERENCA =", DIFERENCA)
print("-" * 20)

# Código interativo:
print("Opção para testar outros valores:")
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))
DIFERENCA = (A * B - C * D)
print("DIFERENCA =", DIFERENCA)
