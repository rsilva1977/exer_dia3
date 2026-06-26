# INÍCIO

# Inicializar a soma
soma = 0

# Ler o primeiro número
num = int(input("Introduza um número (0 para terminar): "))

# Repetir enquanto o número for diferente de 0
while num != 0:
    soma = soma + num
    num = int(input("Introduza um número (0 para terminar): "))

# Mostrar o resultado
print("A soma é:", soma)

# FIM