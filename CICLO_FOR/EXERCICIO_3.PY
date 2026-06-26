# INÍCIO

# Ler o texto
texto = input("Introduza um texto: ")

# Inicializar string invertida
texto_invertido = ""

# Percorrer o texto de trás para a frente
for i in range(len(texto) - 1, -1, -1):
    texto_invertido = texto_invertido + texto[i]

# Mostrar resultado
print("Texto invertido:", texto_invertido)

# FIM