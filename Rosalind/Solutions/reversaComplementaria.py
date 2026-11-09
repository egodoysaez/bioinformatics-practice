# Obtencion de la reversa complementaria de ADN
print('Ingrese secuencia de ADN:')
adn = input()
adnc = ''

for letra in reversed(adn):
    if letra == 'A':
        adnc += 'T'
    elif letra == 'T':
        adnc += 'A'
    elif letra == 'C':
        adnc += 'G'
    elif letra == 'G':
        adnc += 'C'

print()
print('Secuencia reversa complementaria:')
print(adnc)
