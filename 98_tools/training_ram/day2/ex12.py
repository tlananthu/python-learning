#map from dna to rna

'''
Blood Group: A B AB O
DNA: A T C G combination
RNA: U,A, G, C combination respectively to DNA

input: ATTCG
output:UAAGC
'''

rna_map={'A':'U','T':'A','C':'G','G':'C'}
#dna=input('Enter DNA: ')
dna="ATTCG"
op=""

for l in dna:
    op+=rna_map.get(l)
print(op)