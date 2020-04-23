# Large genes on mRNA
# Determine large genes on random mRNA strand
# Nan Hu
# Apr. 12, 2020

# Generate a random sequence 
import random
bases = ["A", "C", "U", "G"]
sequence = ""
for i in range(0,1000):
    sequence+=random.choice(bases)
print(sequence)

# Split sequence with start codon
genes = sequence.split("AUG")
print("Genes are:")
for items in genes:
	print(items)

# Define two lists for large genes and length
large_genes = []
length_genes = []

# Find large genes and their length
for items in genes:
	if len(items) > 50:
		large_genes.append(items)
		length_genes.append(len(items))

# Output results
print("Big genes are:")
for items in large_genes:
	print(items,sep=",")

print("The length of big genes is")
for items in length_genes:
	print(items,sep=",")
	
	

