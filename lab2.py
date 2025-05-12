#Вариант3
codon_counts = {
    'A': 4, 'C': 2, 'D': 2, 'E': 2,
    'F': 2, 'G': 4, 'H': 2, 'I': 3,
    'K': 2, 'L': 6, 'M': 1, 'N': 2,
    'P': 4, 'Q': 2, 'R': 6, 'S': 6,
    'T': 4, 'V': 4, 'W': 1, 'Y': 2,
    '*': 3
}
def calculate_mrna_sequences(protein):
    result = 1
    mod = 1000000
    for aa in protein:
        if aa not in codon_counts:
            raise ValueError(f"Invalid amino acid symbol: '{aa}'")
        result = (result * codon_counts[aa]) % mod
    result = (result * codon_counts['*']) % mod
    return result
protein = input().strip()
print(calculate_mrna_sequences(protein))