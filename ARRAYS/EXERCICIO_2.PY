# INÍCIO

# Declarar o array
array = [15, 7, 22, 3, 19]

# Inicializar a variável maior
maior = array[0]

# Percorrer o array
for i in range(1, len(array)):
    if array[i] > maior:
        maior = array[i]

# Mostrar o resultado
print("O maior elemento é:", maior)

# FIM