def pattern_alphabets(n):
    for i in range(n):
        spaces = " " * (n - i - 1) * 4
        left = [chr(65 + j) for j in range(i + 1)]
        right = [chr(65 + j) for j in range(i - 1, -1, -1)]
        print(spaces + "   ".join(left + right))

# Example usage
pattern_alphabets(5)
