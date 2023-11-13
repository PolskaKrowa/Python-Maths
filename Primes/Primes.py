import time

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_primes(limit):
    prime_list = []
    num = 2
    start_time = time.time()  # Record the start time
    while len(prime_list) < limit:
        if is_prime(num):
            prime_list.append(num)
        num += 1
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time
    
    return prime_list, elapsed_time

def format_time(elapsed_time):
    if elapsed_time < 1:
        return f"{int(elapsed_time * 1000)} milliseconds"
    elif elapsed_time < 60:
        seconds = int(elapsed_time)
        milliseconds = int((elapsed_time - seconds) * 1000)
        return f"{seconds} second(s) {milliseconds} millisecond(s)"
    else:
        minutes = int(elapsed_time / 60)
        seconds = int(elapsed_time % 60)
        return f"{minutes} minute(s) {seconds} second(s)"

def save_to_file(filename, primes):
    with open(filename, 'w') as file:
        file.write('\n'.join(map(str, primes)))

if __name__ == '__main__':
    try:
        limit = int(input("Enter the number of prime numbers you want to generate: "))
        if limit <= 0:
            print("Please enter a positive number.")
        else:
            primes, elapsed_time = generate_primes(limit)
            print(f"Calculation time: {format_time(elapsed_time)}")
            
            filename = r"Python-Maths\Results\primes\primes.txt"
            
            save_to_file(filename, primes)
            print(f"The results have been saved to '{filename}' at the 'Python Maths' folder on your system disk.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")