def filter_even_numbers(list_numbers):
    filtered_numbers = []
    for number in list_numbers:
        if number % 2 == 0:
            filtered_numbers.append(number)
    return filtered_numbers

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = filter_even_numbers(original_list)
print("Original list:", original_list)
print("List with even numbers only:", filtered_list)