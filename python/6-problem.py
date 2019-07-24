def sum_square_difference():
    squares_sum = sum(map(lambda x: x ** 2, range(1, 101)))
    square_of_sum = sum(range(1, 101)) ** 2
    return square_of_sum - squares_sum


if __name__ == "__main__":
    print(sum_square_difference())