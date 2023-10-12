def find_second_largest(numbers):
    numbers.sort(reverse=True)
    return numbers[1] if len(numbers) >= 2 else None

my_list = [38,45,76,47,89,90,87]
second_largest = find_second_largest(my_list)

print("Second largest number:", second_largest)