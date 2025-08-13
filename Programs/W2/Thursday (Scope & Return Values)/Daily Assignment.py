# Modify the palindorme checker to ignore capitalization and spaces
def is_palindrome(word):
    clean_word = word.lower().replace(" ", "")
    return clean_word == clean_word[::-1]

print(is_palindrome("Race Car"))
print(is_palindrome("Big Dog"))