# Contenido de GC en secuencia
#sin considerar el FASTA todavía
import sys

print('Ingrese secuencia FASTA:')
fasta = sys.stdin.read()
lineas_fasta = fasta.splitlines()

secuencias = {}

for linea in lineas_fasta:
    if linea.startswith('>'):
        secuencia = ''
        lineas = linea[1:]
    else:
        secuencia += linea
        secuencias[lineas] = secuencia

Porcentaje = 0
mayorPorcentaje = ''
for etiqueta, secuen in secuencias.items():
    total = 0
    GC = 0
    for letra in secuen:
        if letra in 'CG':
            total += 1
            GC += 1
        elif letra in 'AT':
            total += 1
    porcentajeGC = (GC/total)*100
    if porcentajeGC > Porcentaje:
        Porcentaje = porcentajeGC
        mayorPorcentaje = etiqueta
    print(f'Para {etiqueta} el porcentaje es {porcentajeGC:.4f}%')

print()
print(f'La secuencia con mayor %GC es {mayorPorcentaje} con un {Porcentaje:.4f}%')
