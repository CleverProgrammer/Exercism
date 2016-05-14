def to_rna(dna):
    dna_to_rna = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    return ''.join([dna_to_rna[strand] for strand in dna])
