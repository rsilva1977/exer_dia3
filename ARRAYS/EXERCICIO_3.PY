# INÍCIO

# Declarar o array original
array = [1, 2, 3, 4, 5]

# Criar o array invertido
array_invertido = [0] * 5

# Copiar os elementos pela ordem inversa
for i in range(5):
    array_invertido[4 - i] = array[i]

# Mostrar o resultado
print("Array invertido:", array_invertido)

# FIM