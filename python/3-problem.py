"""
prime factorization needs to
try to divide by two or more iteracting
"""

def get_factors(number):
    actual_number = number
    factors = []
    while actual_number != 1:
        try_number = 2
        condition = True
        while condition:
            if actual_number % try_number == 0:
                factors.append(try_number)
                actual_number = actual_number / try_number
                condition = False
            try_number += 1
    return factors


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def get_primes(number_list):
    primes = []
    for item in number_list:
        if is_prime(item):
            primes.append(item)
    return primes


def get_largest_prime_factor(number):
    factors = get_factors(number)
    primes = get_primes(factors)
    return max(primes)


if __name__ == "__main__":
    print(get_largest_prime_factor(600851475143))
