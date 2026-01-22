def DNA_strand(dna):
    x=str.maketrans('ATCG', 'TAGC')
    return dna.translate(x)