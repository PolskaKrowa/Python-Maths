<<<<<<< HEAD
def calculate_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def save_factors_to_file(number):
    factors = calculate_factors(number)
    with open(fr'Python-Maths\Results\factors\factors_{number}.txt', 'w') as file:
        file.write('Factors of ' + str(number) + ' are:\n')
        for factor in factors:
            file.write(f"\n{factor}")

# Ask the user to specify value to get the factors of.
your_number = int(input("State the number that you want to get the factors of.\n>"))

save_factors_to_file(your_number)
=======
def calculate_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def save_factors_to_file(number):
    factors = calculate_factors(number)
    with open(fr'Python-Maths\Results\factors\factors_{number}.txt', 'w') as file:
        file.write('Factors of ' + str(number) + ' are:\n')
        for factor in factors:
            file.write(f"\n{factor}")

# Ask the user to specify value to get the factors of.
your_number = int(input("State the number that you want to get the factors of.\n>"))

save_factors_to_file(your_number)
>>>>>>> 542dfd1ec557abe77e3cf2f63ed3497a60b186e7
print(f'Factors of {your_number} have been saved to factors_{your_number}.txt')