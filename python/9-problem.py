import math

def special_pythagorean_triplet():
    """
    constaints
    a < b < c
    a² + b² = c²
    a + b + c = 1000
    find a * b * c
    """
    a = 1
    b = 2
    while True:
        c = math.sqrt(a ** 2 + b ** 2)
        if a + b + c < 1000:
            b += 1
        elif a + b + c > 1000:
            a += 1
            b = a + 1
        else:
            return a * b * c


if __name__ == "__main__":
    print(special_pythagorean_triplet())
