from mpmath import mp

def fibonacci(n):
    a, b = mp.mpf(0), mp.mpf(1)  # Initialize the first two Fibonacci numbers
    for _ in range(n):
        a, b = b, a + b
    return a

n = int(input("Enter the Nth fibonacci number you would like this program to calculate\n>"))
mp.dps = n
result = mp.mpf(fibonacci(n))

with open(r"Python-Maths\Results\fibonacci\fibbo.txt", "w") as file:
    file.write(format(result) + "\n\n")