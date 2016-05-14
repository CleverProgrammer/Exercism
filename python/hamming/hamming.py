def distance(strand_1, strand_2):
    hamming_distance = 0
    for nucleotide_1, nucleotide_2 in zip(strand_1, strand_2):
        if nucleotide_1 != nucleotide_2:
            hamming_distance += 1
    return hamming_distance
