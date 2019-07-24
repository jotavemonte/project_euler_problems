def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def get_prime(number_ranking):
    counter = 1
    number = 2
    prime_number = 0
    while counter <= number_ranking:
        if is_prime(number):
            prime_number = number
            counter += 1
        number += 1
    return prime_number


if __name__ == "__main__":
    print(get_prime(10001))
