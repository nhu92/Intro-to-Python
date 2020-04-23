# Count elements in given string 
# Using both for loop and list comprehension
# Nan Hu
# Apr. 12, 2020

given_string = "The quick brown fox jumped over the lazy dog"

# Count the number of spaces in the above string. 
string_list = list(given_string)
space_sum = 0
print("Number of spcaces in my string is:")
for item in string_list:
	if item == " ":
		space_sum +=1
print(space_sum)

print("Number of spcaces in my string is (by list comprehension):")
sub_string = [item for item in string_list if item == " "]
print(len(sub_string))

# Find all the words that have the letter “o” in the above string  
string_list = given_string.split(" ")
print("All the words that have the letter \"o\":")
for item in string_list:
	if item.find("o") != -1:
		print(item)

print("All the words that have the letter \"o\" (by list comprehension):")
sub_string = [item for item in string_list if item.find("o") != -1]
for item in sub_string:
	print(item)
	
# Find all the words that have at least 5 letters in the above string
string_list = given_string.split(" ")
print("All the words that have at lest 5 letters:")
for item in string_list:
	if len(item) >= 5:
		print(item)

print("All the words that have at lest 5 letters (by list comprehension):")
sub_string = [item for item in string_list if len(item) >= 5]
for item in sub_string:
	print(item)

# Find all the numbers from 1 to 1000 that have a “3” in it. Ex: 23, 37, 903
# create a list of numbers from 1 to 1000
number_list = range(1, 1000)
# for loops
print("All the numbers from 1 to 100 that have a \"3\":")
for item in number_list:
	if str(item).find("3") != -1:
		print(item, end = ",")

print("\nAll the numbers from 1 to 100 that have a \"3\" (by list conmprehension):")
sub_list = [item for item in number_list if str(item).find("3") != -1]
for item in sub_list:
	print(item, end = ",")