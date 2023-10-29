def print_positive_numbers(input_list):
    positive_numbers = [num for num in input_list if num > 0]
    return positive_numbers

# Input list
list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

# Print positive numbers from list1
output1 = print_positive_numbers(list1)
print("Input:", list1)
print("Output:", output1)

# Print positive numbers from list2
output2 = print_positive_numbers(list2)
print("\nInput:", list2)
print("Output:", output2)
