from functools import reduce

def divide_all(numbers, divisor):
    new_numbers = []
    for i in numbers:
        if i % divisor == 0:
            new_numbers.append(i//divisor)
        else:
            new_numbers.append(i)
    return new_numbers


def mmc():
    numbers = list(range(2, 21))
    index = 0
    mmc_numbers = []
    result = 1
    while index < 19:
        mmc_numbers.append(numbers[index])
        numbers = divide_all(numbers, numbers[index])
        index += 1
    return reduce(lambda x, y: x * y, mmc_numbers)


if __name__ == "__main__":
    print(mmc())
