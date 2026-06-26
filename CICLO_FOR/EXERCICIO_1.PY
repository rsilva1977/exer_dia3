# INÍCIO

# Ler o número de notas
N = int(input("Quantas notas pretende introduzir? "))

# Inicializar a soma
soma = 0

# Ler as notas e acumular a soma
for i in range(1, N + 1):
    nota = int(input(f"Introduza a nota {i}: "))
    soma = soma + nota

# Calcular a média
media = soma / N

# Mostrar o resultado
print("A média é:", media)

# FIM