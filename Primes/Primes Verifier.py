import time

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True

def find_correction(number):
    lower_limit = number - 1
    upper_limit = number + 1

    for num in range(lower_limit, upper_limit + 1):
        if is_prime(num):
            return num

def mark_primes(filename):
    correct_primes = 0
    incorrect_primes = 0
    total_numbers = 0
    incorrect_positions = []

    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for i, line in enumerate(lines, start=1):
            number = int(line.strip())
            if is_prime(number):
                file.write(f"{number} V\n")
                correct_primes += 1
            else:
                suggested_correction = find_correction(number)
                if suggested_correction == None:
                    file.write(f"{number} X (Remove)\n")
                    incorrect_primes += 1
                    incorrect_positions.append(i)
                elif suggested_correction != number:
                    file.write(f"{suggested_correction} V (Corrected)\n")
                    correct_primes += 1
            total_numbers += 1
        accuracy = (correct_primes / total_numbers) * 100
        file.write(f"\n\nVerified accuracy: {accuracy:.10f}%")

    if total_numbers > 0:
        accuracy = (correct_primes / total_numbers) * 100
        print(f"Correct Primes: {correct_primes}")
        print(f"Incorrect Primes: {incorrect_primes}")
        print(f"Accuracy: {accuracy:.10f}%")

    if incorrect_primes > 0:
        print("Inaccurate Prime(s) at position(s):", incorrect_positions)
    else:
        print("Well done!")

# Example usage
filename = r"Python-Maths\Results\primes\primes.txt"  # Replace with your file path
mark_primes(filename)
time.sleep(5)
exit(69)