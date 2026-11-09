# reversaComplementaria2
print('Ingrese secuencia de ADN:')
adn = input()
adnc = ''

complementario = {
    'A':'T',
    'T':'A',
    'C':'G',
    'G':'C'
}

for letra in reversed(adn):
    adnc += complementario[letra]

print()
print('Secuncia reversa complementaria:')
print(adnc)
