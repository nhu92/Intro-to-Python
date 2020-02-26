# AT Content
# Feb. 26, 2020
# Nan Hu

####################################
# Basic Steps
####################################
# 1. Get a sequence
# 2. Count A & T numbers
# 3. Calculate AT content

####################################
# Detailed Steps
####################################
# 1. Get a sequence
#	- the sequece is prepared
# 2. Count A & T numbers
#	- count A and T separately
# 3. Calculate AT content
#	- Total base number
#	- Calculate percentage of ATs

sequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
print("Input DNA sequence is:" + sequence)

# Count the number of As and Ts
Anum = sequence.count("A")
Tnum = sequence.count("T")
Totalnum = len(sequence)
print("There are "+str(Anum)+" As.")
print("There are "+str(Tnum)+" Ts.")
print("Total base number is: "+str(Totalnum))

# Count the AT content
AT_content = (Anum + Tnum) / Totalnum
print("AT content is:" + str(AT_content))