def fibonacci_max_value(max_val):
    sequence = []
    a, b = 0, 1
    while a < max_val:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example: Generate Fibonacci numbers less than 50
print(fibonacci_max_value(50))
