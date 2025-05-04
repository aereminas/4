import math

def is_prime_number(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def prime_number_sequence():
    current_number = 2
    while True:
        if is_prime_number(current_number):
            yield current_number
        current_number += 1

prime_seq = prime_number_sequence()
for _ in range(10):
    print(next(prime_seq))

