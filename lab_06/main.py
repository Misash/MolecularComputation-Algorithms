import numpy as np

# Secuencias
seq1 = "ATCGTACGTTA"
seq2 = "ACGTGACGT"

# Modelo HMM más complejo
# Estados: M (Match), I (Insertion), D (Deletion)
states = ['M', 'I', 'D']

# Probabilidades de transición
trans_prob = {
    'M': [0.7, 0.2, 0.1],
    'I': [0.1, 0.8, 0.1],
    'D': [0.1, 0.1, 0.8]
}

# Probabilidades de emisión
emit_prob = {
    'M': {'A': 0.3, 'T': 0.2, 'C': 0.3, 'G': 0.2},
    'I': {'A': 0.25, 'T': 0.25, 'C': 0.25, 'G': 0.25},
    'D': {'-': 1.0}
}

# algoritmo de Viterbi para HMM
def viterbi_advanced(seq1, seq2, states, trans_prob, emit_prob):
    len_seq1 = len(seq1) + 1
    len_seq2 = len(seq2) + 1
    dp = np.zeros((len_seq1, len_seq2, len(states)))
    path = np.zeros((len_seq1, len_seq2, len(states)), dtype=int)

    # Inicialización de la matriz
    dp[0, 0, :] = 1

    # Relleno de la matriz
    for i in range(1, len_seq1):
        for j in range(1, len_seq2):
            for k, state in enumerate(states):
                max_prob = 0
                max_state = 0
                for l, prev_state in enumerate(states):
                    prob = 0
                    if state == 'M':
                        prob = dp[i-1, j-1, l] * trans_prob[prev_state][k] * emit_prob[state][seq1[i-1]]
                    elif state == 'I':
                        prob = dp[i-1, j, l] * trans_prob[prev_state][k] * emit_prob[state][seq1[i-1]]
                    elif state == 'D':
                        prob = dp[i, j-1, l] * trans_prob[prev_state][k] * emit_prob[state]['-']

                    if prob > max_prob:
                        max_prob = prob
                        max_state = l

                dp[i, j, k] = max_prob
                path[i, j, k] = max_state

    # Recuperación del camino más probable
    align_seq1 = ""
    align_seq2 = ""
    i, j = len_seq1 - 1, len_seq2 - 1
    state = np.argmax(dp[i, j])
    while i > 0 and j > 0:
        if states[state] == 'M':
            align_seq1 = seq1[i-1] + align_seq1
            align_seq2 = seq2[j-1] + align_seq2
            i -= 1
            j -= 1
        elif states[state] == 'I':
            align_seq1 = seq1[i-1] + align_seq1
            align_seq2 = '-' + align_seq2
            i -= 1
        elif states[state] == 'D':
            align_seq1 = '-' + align_seq1
            align_seq2 = seq2[j-1] + align_seq2
            j -= 1
        state = path[i, j, state]

    return align_seq1, align_seq2


print(viterbi_advanced(seq1, seq2, states, trans_prob, emit_prob))
