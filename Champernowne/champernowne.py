from mpmath import mp
import time

def champernowne_constant(digits):
    mp.dps = digits  # Set the desired number of decimal places
    constant = ""
    
    for i in range(1, digits + 2):
        constant += mp.nstr(i, digits * 10)
    
    return mp.nstr("0." + constant, digits * 10)

# Define the number of decimal places you want
decimal_places = int(input("Specify the amount of digits of champernowne's constant you would like:\n> "))

# Calculate Champernowne's Constant and measure the time
start_time = time.time()
result = champernowne_constant(decimal_places)
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Format the elapsed time
if elapsed_time > 60:
    minutes, seconds = divmod(elapsed_time, 60)
    if minutes > 60:
        hours, minutes = divmod(minutes, 60)
        time_str = f"{int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds"
    else:
        time_str = f"{int(minutes)} minutes, {int(seconds)} seconds"
else:
    time_str = f"{int(elapsed_time)} seconds"

result = result.replace("'", "")

with open(r"Python-Maths\Results\Champernowne\champernowne.txt", "w") as file:
    file.write(result)

print("Champernowne's Constant to", decimal_places, "decimal places have been saved to champernowne.txt")
print(f"\nCalculation took {time_str}.")