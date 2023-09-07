
def needleman_wunsch(seq1, seq2, match_score=1, mismatch_score=-1, gap_penalty=-1):
    # Inicializar la matriz de puntuación
    n = len(seq1)
    m = len(seq2)
    score_matrix = [[0] * (m + 1) for _ in range(n + 1)]

    # Inicializar la primera fila y columna de la matriz de puntuación
    for i in range(n + 1):
        score_matrix[i][0] = i * gap_penalty
    for j in range(m + 1):
        score_matrix[0][j] = j * gap_penalty

    # Llenar la matriz de puntuación utilizando las reglas de alineamiento global
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match = score_matrix[i - 1][j - 1] + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_score)
            delete = score_matrix[i - 1][j] + gap_penalty
            insert = score_matrix[i][j - 1] + gap_penalty
            score_matrix[i][j] = max(match, delete, insert)

    # Realizar el seguimiento de la alineación
    aligned_seq1, aligned_seq2 = [], []
    i, j = n, m
    while i > 0 or j > 0:
        if i > 0 and score_matrix[i][j] == score_matrix[i - 1][j] + gap_penalty:
            aligned_seq1.append(seq1[i - 1])
            aligned_seq2.append('-')
            i -= 1
        elif j > 0 and score_matrix[i][j] == score_matrix[i][j - 1] + gap_penalty:
            aligned_seq1.append('-')
            aligned_seq2.append(seq2[j - 1])
            j -= 1
        else:
            aligned_seq1.append(seq1[i - 1])
            aligned_seq2.append(seq2[j - 1])
            i -= 1
            j -= 1

    aligned_seq1.reverse()
    aligned_seq2.reverse()

    return ''.join(aligned_seq1), ''.join(aligned_seq2), score_matrix[n][m]

# # Ejemplo de uso:
# seq1 = "AAAC"
# seq2 = "AGC"
# aligned_seq1, aligned_seq2, score = needleman_wunsch(seq1, seq2)
# print(f"Secuencia 1 alineada: {aligned_seq1}")
# print(f"Secuencia 2 alineada: {aligned_seq2}")
# print(f"Puntuación del alineamiento: {score}")

# Función para cargar secuencias desde un archivo
def load_sequences_from_file(filename):
    sequences = []
    with open(filename, 'r') as file:
        sequence = ""
        for line in file:
            if not line.strip().startswith("Bacteria") and not line.strip().startswith("Sars-Cov") and not line.strip().startswith("Influenza"):
                sequence += line.strip()
            else:
                if sequence:
                    sequences.append(sequence)
                sequence = ""
    return sequences

# Cargar secuencias desde el archivo
sequences = load_sequences_from_file("input.txt")

# Ejecutar el algoritmo de alineamiento global para cada par de secuencias
for i in range(len(sequences)):
    for j in range(i + 1, len(sequences)):
        seq1 = sequences[i]
        seq2 = sequences[j]
        aligned_seq1, aligned_seq2, score = needleman_wunsch(seq1, seq2)
        print(f"Alineamiento de secuencia {i + 1} y secuencia {j + 1}:")
        print(f"Secuencia 1 alineada: {aligned_seq1}")
        print(f"Secuencia 2 alineada: {aligned_seq2}")
        print(f"Puntuación del alineamiento: {score}")
        print("\n")
