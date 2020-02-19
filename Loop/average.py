# Calculating average from 1 to 20
# Feb. 19, 2020
# Nan Hu

import statistics

# Using for loop to calculate average
sum = 0
for num in range(1,21):
	sum += num
average1 = sum / num
print("The average of 1 to 20 is", average1)

# Using build-in function to calculate average
average2 = statistics.mean(range(1,21))
print("The average of 1 to 20 is", average2)
