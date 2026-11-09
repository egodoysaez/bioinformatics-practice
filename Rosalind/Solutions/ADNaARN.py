# Cambio ADN a ARN
print('Ingrese secuencia de ADN:')
adn = input()
arn = ''

for letra in adn:
    if letra == 'T':
        arn += 'U'
    else:
        arn += letra

print()
print('Secuencia transcrita:')
print(arn)
