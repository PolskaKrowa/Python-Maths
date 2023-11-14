<<<<<<< HEAD
from mpmath import mp
import time

# Set the number of decimal places
mp.dps = int(input("Specify the amount of digits of Euler's Constant (Gamma) to calculate:\n> "))

# Start the timer
start_time = time.time()

# Calculate Euler's constant
gamma = mp.euler()

# Stop the timer
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Save the result and elapsed time to a file
with open(r"Python-Maths\Results\Gamma\gamma.txt", "w") as file:
    file.write(format(gamma) + "\n\n")
    file.write("Time taken to calculate (seconds): {:.4f}".format(elapsed_time))

print("Euler's constant:", gamma)
=======
from mpmath import mp
import time

# Set the number of decimal places
mp.dps = int(input("Specify the amount of digits of Euler's Constant (Gamma) to calculate:\n> "))

# Start the timer
start_time = time.time()

# Calculate Euler's constant
gamma = mp.euler()

# Stop the timer
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Save the result and elapsed time to a file
with open(r"Python-Maths\Results\Gamma\gamma.txt", "w") as file:
    file.write(format(gamma) + "\n\n")
    file.write("Time taken to calculate (seconds): {:.4f}".format(elapsed_time))

print("Euler's constant:", gamma)
>>>>>>> 542dfd1ec557abe77e3cf2f63ed3497a60b186e7
print("Time taken to calculate (seconds):", elapsed_time)