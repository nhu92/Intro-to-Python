# Large genes on mRNA - Comprehension
# Determine large genes on random mRNA strand using list comprehension
# Nan Hu
# Apr. 15, 2020

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

large_genes = []
# Find large genes and their length (Using list comprehension)
large_genes = [items for items in genes if len(items)>50]

# Output results
print("Big genes are:")
for items in large_genes:
	print(items,sep=",")

print("The length of big genes is")
for items in large_genes:
	print(len(items),sep=",")
	