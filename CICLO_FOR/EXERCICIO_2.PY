# INÍCIO

import math

# Ler o número
num = int(input("Introduza um número: "))

# Verificar se o número é primo
if num <= 1:
    print("O número não é primo.")
else:
    primo = True

    # Testar divisores de 2 até à raiz quadrada de num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            primo = False
            break

    if primo:
        print("O número é primo.")
    else:
        print("O número não é primo.")

# FIM