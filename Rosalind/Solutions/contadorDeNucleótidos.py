# Contador de nucleótidos
secuencia = input()
contador_A = 0
contador_C = 0
contador_G = 0
contador_T = 0

for letra in secuencia:
    if letra == 'A':
        contador_A += 1
    elif letra == 'C':
         contador_C += 1
    elif letra == 'G':
        contador_G += 1
    elif letra == 'T':
        contador_T += 1

print(contador_A, contador_C, contador_G, contador_T)
