# Population estimation
# Calculate Population after years
# Nan Hu
# Jan. 29, 2020

# import modules
# Add any variables
# Ask for input
# Calculation of population
# Print results

birth_rate = 7
death_rate = 13
immigrant_rate = 35
current_pop = 307357870

print("Current population:", current_pop)

# input year
year_input = input("How many years? ")
year_int = int(year_input)

future_population = year_int * 365 * 24 * 60 * 60 * (1/birth_rate - 1/death_rate + 1/immigrant_rate) + current_pop
print("After", year_input, " years, the population is:", future_population)