# Base count
# Counting numbers of Gs, As, and A+Cs in a random sequence
# Nan Hu
# Feb. 12, 2020

# Generate a random sequence 
import random
bases = ["A", "C", "T", "G"]
sequence = random.choices(bases, k=100)
print(sequence)

# Count the number of bases in sequence
print("There are " + str(sequence.count("G")) + " Gs.\n")
print("There are " + str(sequence.count("A")) + " As.\n")
print("There are " + str(sequence.count("A") + sequence.count("C")) + " A and Cs.")
