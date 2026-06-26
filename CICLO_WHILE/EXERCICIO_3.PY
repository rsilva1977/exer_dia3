# INÍCIO

# Ler o número
num = int(input("Introduza um número: "))

# Inicializar o multiplicador
multiplicador = 1

# Gerar a tabuada
while multiplicador <= 10:
    resultado = num * multiplicador
    print(num, "x", multiplicador, "=", resultado)
    multiplicador = multiplicador + 1

# FIM