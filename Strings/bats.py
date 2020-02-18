# Species name output Homework Assignment 1
# Output abbreviate form of species
# Nan Hu
# Feb. 12, 2020

# Input species full name
species1 = input("Type in species 1 name: ")
species2 = input("Type in species 2 name: ")
species3 = input("Type in species 3 name: ")

# split, abbr, uppercase
abbr_sp1 = (species1.split(" ")[0][0:3] + species1.split(" ")[1][0:3]).upper()
abbr_sp2 = (species2.split(" ")[0][0:3] + species2.split(" ")[1][0:3]).upper()
abbr_sp3 = (species3.split(" ")[0][0:3] + species3.split(" ")[1][0:3]).upper()

# output result in one statement
print(abbr_sp1 + "\n" + abbr_sp2 + "\n" + abbr_sp3 + "\n")
