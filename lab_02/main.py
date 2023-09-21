def smith_waterman(seq1, seq2, match_score=1, mismatch_score=-1, gap_penalty=-1):
    # Inicializar la matriz de puntuación
    n = len(seq1)
    m = len(seq2)
    score_matrix = [[0] * (m + 1) for _ in range(n + 1)]

    # Inicializar la puntuación máxima y las coordenadas de la celda correspondiente
    max_score = 0
    max_i, max_j = 0, 0

    # Llenar la matriz de puntuación utilizando las reglas de alineamiento local
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match = score_matrix[i - 1][j - 1] + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_score)
            delete = score_matrix[i - 1][j] + gap_penalty
            insert = score_matrix[i][j - 1] + gap_penalty
            score_matrix[i][j] = max(0, match, delete, insert)

            # Actualizar la puntuación máxima y las coordenadas de la celda correspondiente
            if score_matrix[i][j] > max_score:
                max_score = score_matrix[i][j]
                max_i, max_j = i, j

    # Realizar el seguimiento de la subsecuencia local óptima
    aligned_seq1, aligned_seq2 = [], []
    i, j = max_i, max_j
    while i > 0 and j > 0 and score_matrix[i][j] > 0:
        if score_matrix[i][j] == score_matrix[i - 1][j - 1] + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_score):
            aligned_seq1.append(seq1[i - 1])
            aligned_seq2.append(seq2[j - 1])
            i -= 1
            j -= 1
        elif score_matrix[i][j] == score_matrix[i - 1][j] + gap_penalty:
            aligned_seq1.append(seq1[i - 1])
            aligned_seq2.append('-')
            i -= 1
        else:
            aligned_seq1.append('-')
            aligned_seq2.append(seq2[j - 1])
            j -= 1

    aligned_seq1.reverse()
    aligned_seq2.reverse()

    return ''.join(aligned_seq1), ''.join(aligned_seq2), max_score

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

# Ejecutar el algoritmo de alineamiento local para cada par de secuencias
for i in range(len(sequences)):
    for j in range(i + 1, len(sequences)):
        seq1 = sequences[i]
        seq2 = sequences[j]
        aligned_seq1, aligned_seq2, score = smith_waterman(seq1, seq2)
        print(f"Alineamiento local de secuencia {i + 1} y secuencia {j + 1}:")
        print(f"Subsecuencia local 1: {aligned_seq1}")
        print(f"Subsecuencia local 2: {aligned_seq2}")
        print(f"Puntuación del alineamiento local: {score}")
        print("\n")
