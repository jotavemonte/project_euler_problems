def is_palindromic(number):
    unicode_number = str(number)
    if unicode_number == unicode_number[::-1]:
        return True
    return False


def get_3_digit_bigger_palindromic():
    palindromics = []
    for i in range(999, 1, -1):
        for j in range(999, 1, -1):
            if is_palindromic(i * j):
                palindromics.append(i * j)
    if not palindromics:
        raise ValueError('No result found')
    else:
        return max(palindromics)


if __name__ == "__main__":
    print(get_3_digit_bigger_palindromic())
