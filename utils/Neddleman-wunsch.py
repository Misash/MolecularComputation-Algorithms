# TRACEBACK-->BUSCAR EL MEJOR ALINEAMIENTO

alineamiento_1 = " "
alineamiento_2 = " "



while (i > 0 and j > 0):
    puntuacion = F[j][i]
    puntuacion_diag = F[j - 1][i - 1]

    puntuacion_up = F[j - 1][i]
    puntuacion_left = F[j][i - 1]

    if puntuacion == puntuacion_diag + suma:
        alineamiento_1 = sec1[i - 1] + alineamiento_1
        alineamiento_2 = sec2[j - 1] + alineamiento_2

        i = i - 1
        j = j - 1

    elif puntuacion == puntuacion_left + gap:
        alineamiento_1 = sec1[i - 1] + alineamiento_1
        alineamiento_2 = "-" + alineamiento_2

        i = i - 1

    elif puntuacion == puntuacion_up + gap:
        alineamiento_1 = "-" + alineamiento_1
        alineamiento_2 = sec2[j - 1] + alineamiento_2

        j = j - 1

while (i > 0):
    alineamiento_1 = sec1[i - 1] + alineamiento_1
    alineamiento_2 = "-" + alineamiento_2

    i = i - 1

while (j > 0):
    alineamiento_1 = "-" + alineamiento_1
    alineamiento_2 = sec2[j - 1] + alineamiento_2

    j = j - 1

print
alineamiento_1, alineamiento_2, score