from Bio import pairwise2
from Bio.pairwise2 import format_alignment

# Función para realizar el alineamiento de un conjunto de secuencias
def perform_alignment(sequences):
    alignments = []

    # Realizar alineamientos de todas las combinaciones posibles
    for i in range(len(sequences)):
        for j in range(i + 1, len(sequences)):
            alignment = pairwise2.align.globalxx(sequences[i], sequences[j], one_alignment_only=True, score_only=True)
            alignments.append((i, j, alignment))

    # Ordenar los alineamientos por score descendente
    alignments.sort(key=lambda x: x[2], reverse=True)

    return alignments

# Definir las secuencias directas y reversas
direct_sequences = [
    "TGCCGGCAGGGATGTGCTTG",
    "GTTTAGGTTTTTGCTTATGCAGCATCCA",
    "GGAAAAGCACAGAACTGGCCAACA",
    "GCCAGTTGGTTGATTTCCACCTCCA",
    "ACCCCCGACATGCAGAAGCTG",
    "TGACGTGTCTGCTCCACTTCCA"
]

reverse_sequences = [
    "TGCTTGCAGTTTGCTTTCACTGATGGA",
    "TCAGGTACCCTGACCTTCTCTGAAC",
    "GTGGGTTGTAAAGGTCCCAAATGGT",
    "TGCCTTGGGTCCCTCTGACTGG",
    "GTGGTGCATTGATGGAAGGAAGCA",
    "AGTGAGAGGAGCTCCCAGGGC"
]

# Realizar alineamientos
direct_alignments = perform_alignment(direct_sequences)
reverse_alignments = perform_alignment(reverse_sequences)
all_alignments = perform_alignment(direct_sequences + reverse_sequences)

# Imprimir resultados
print("Alineamiento de secuencias directas:")
for alignment in direct_alignments:
    i, j, score = alignment
    seq1 = direct_sequences[i]
    seq2 = direct_sequences[j]
    alignment_str = format_alignment(seq1, seq2, score, 0, len(seq1))
    print(alignment_str)

print("\nAlineamiento de secuencias reversas:")
for alignment in reverse_alignments:
    i, j, score = alignment
    seq1 = reverse_sequences[i]
    seq2 = reverse_sequences[j]
    alignment_str = format_alignment(seq1, seq2, score, 0, len(seq1))
    print(alignment_str)

print("\nAlineamiento de todas las secuencias juntas:")
for alignment in all_alignments:
    i, j, score = alignment
    seq1 = (direct_sequences + reverse_sequences)[i]
    seq2 = (direct_sequences + reverse_sequences)[j]
    alignment_str = format_alignment(seq1, seq2, score, 0, len(seq1))
    print(alignment_str)
