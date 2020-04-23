# GC content function
# Writing a function to calculate GC content in random sequence
# Nan Hu
# Apr. 15, 2020

#######Function#######
def GCcontent(seq):
	""" This is a function to calculate GC content in given DNA seqence
	Noticed that GC content = (G + C) / total bases"""
	num_g = seq.count("G")
	num_c = seq.count("C")
	gc_content = (num_g + num_c)/len(seq)
	return(gc_content)
#####End Function#####

# Generate a random sequence 
import random
bases = ["A", "C", "T", "G"]
sequence = ""
for i in range(0,5000):
    sequence+=random.choice(bases)

seq_parts = [sequence[base:base+100] for base in range(0, 5000, 100)]
seq_parts_gc = [GCcontent(sub_seq) for sub_seq in seq_parts]
print("GC content for each parts are:")
for sub_seq in seq_parts_gc:
	print(sub_seq)