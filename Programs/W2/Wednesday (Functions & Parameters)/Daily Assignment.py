# Write a function that checks if an argument is a palindrome.
def pal_check(word):
    pal = word[::-1]
    print(pal)
    if word == pal:
        return True
    else:
        return False

print(pal_check("racecar"))