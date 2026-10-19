def sum_two_smallest_numbers(numbers):
    numbers.sort()

    return numbers[0] + numbers[1]
print(sum_two_smallest_numbers([1, 2, 3, 4, 5]))

