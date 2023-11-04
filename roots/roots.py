import mpmath

n = int(input("number to rootify.\n> "))

num_digits = int(input("Digits of precision.\n> "))

# Calculate the square root using mpmath
mpmath.mp.dps = num_digits  # Set the desired precision (number of decimal places)
sqrt_result = mpmath.sqrt(n)

# Save the result to a file
file_name = fr"Results\roots\root_{n}.txt"
with open(file_name, "w") as file:
    file.write(str(sqrt_result))

print(f"Square root of {n} with {num_digits} digits saved to {file_name}")