# Write a function that checks if an argument is a palindrome.
def is_palindrome(word):
    # Reverse the word and compare it
    return word == word[::-1]

# Test it:
print(is_palindrome("madam"))   # True
print(is_palindrome("hello"))   # False