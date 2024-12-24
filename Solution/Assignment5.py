def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Normalize the string
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True

# Example usage
print(is_palindrome("radar"))  # True
print(is_palindrome("world"))  # False
