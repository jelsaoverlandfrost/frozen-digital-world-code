def get_base_counts(dna):
    sequenceDNA = {}
    count = [0] * 4
    name = ['A','C','G','T']
    validity = True
    for i in range(len(dna)):
        if dna[i] == 'A':
            count[0] += 1
        elif dna[i] == 'C':
            count[1] += 1
        elif dna[i] == 'G':
            count[2] += 1
        elif dna[i] == 'T':
            count[3] += 1
        else:
            validity = False
    if validity:
        for i in range(len(count)):
            if count[i] != 0:
                sequenceDNA[name[i]] = count[i]
        return sequenceDNA
    else:
        return 'The input DNA string is inValid'

stringdna = "Aa"
print get_base_counts(stringdna)