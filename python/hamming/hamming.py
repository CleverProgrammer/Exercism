def distance(strand_1, strand_2):
    hamming_distance = 0
    for index, nucleotide in enumerate(strand_1):
        if strand_2[index] != nucleotide:
            hamming_distance += 1
    return hamming_distance
