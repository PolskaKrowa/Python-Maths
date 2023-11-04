from mpmath import mp

def calculate_e(decimal_places):
    mp.dps = decimal_places  # Set the precision to the desired number of decimal places
    e = mp.exp(1)
    return e

decimal_places = int(input("Enter the number of decimal places for 'e': "))
result = calculate_e(decimal_places)

# Save the result to a file named "e.txt"
with open(r"Python-Maths\Results\e\e.txt", "w") as file:
    file.write(f"{result} \n\n Digits: {decimal_places}")

print("Result has been saved to 'e.txt' at the program directory.")
