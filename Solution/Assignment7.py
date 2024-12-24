n = int(input("Enter the number of lines: "))

for i in range(1, n + 1):
    # Generate the numbers for the current row
    numbers = [str(j) for j in range(1, 2 * i)]
    # Add spaces and join
    print(" " * (n - i) + " ".join(numbers))
