def generate_fibonacci(limit):
    fibonacci_sequence = [0, 1]

    while True:
        next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        if next_fib > limit:
            break
        fibonacci_sequence.append(next_fib)

    return fibonacci_sequence

# Set the limit for generating Fibonacci numbers
limit = int(input("Enter the limit for Fibonacci numbers: "))

if limit < 0:
    print("Limit must be a non-negative number.")
else:
    fibonacci_numbers = generate_fibonacci(limit)
    print("Fibonacci numbers up to", limit, "are:")
    print(fibonacci_numbers)
