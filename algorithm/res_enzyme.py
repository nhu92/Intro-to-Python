# Restriction Enzyme
# Feb. 26, 2020
# Nan Hu

####################################
# Basic Steps
####################################
# 1. Get a sequence
# 2. Get the restriction enzyme recognition site
# 3. Find the site in given sequence
# 4. Cut the seuqennce
# 5. Calculate the length of fragments
# 6. Output the results

####################################
# Detailed Steps
####################################
# 1. Get a sequence
# 2. Get the restriction enzyme recognition site
# 3. Find the site in given sequence
#	- Using find() to locate the position of restriction enzyme recognition site
# 4. Cut the seuqennce
#	- Split sequence at the right position
# 5. Calculate the length of fragments
# 6. Output the results
#	- Two outputs

sequence = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
res_enz = "GAATTC"
print("The original sequence is: " + sequence)

# Find the position where contains the restriction enzyme recognition site
res_pos = sequence.find(res_enz)

# Define the where to cut 
cut_pos = res_pos+1

# Calculate the length of 2 fragment
subseq1 = sequence[:cut_pos]
subseq2 = sequence[cut_pos:]
size1 = len(subseq1)
size2 = len(subseq2)
print("The first fragment is: "+ subseq1)
print("The size equals to: "+ str(size1))
print("The second fragment is: "+ subseq2)
print("The size equals to: "+ str(size2))
