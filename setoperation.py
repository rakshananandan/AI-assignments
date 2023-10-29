E = {0, 1, 2, 3, 4, 5, 6, 8}
N = {2, 4, 6, 8, 9}

# Calculate and display the union of E and N
union_result = E.union(N)
print(f"Union of E and N is {union_result}")

# Calculate and display the intersection of E and N
intersection_result = E.intersection(N)
print(f"Intersection of E and N is {intersection_result}")

# Calculate and display the difference of E and N (E - N)
difference_result = E.difference(N)
print(f"Difference of E and N is {difference_result}")

# Calculate and display the symmetric difference of E and N
symmetric_difference_result = E.symmetric_difference(N)
print(f"Symmetric difference of E and N is {symmetric_difference_result}")
