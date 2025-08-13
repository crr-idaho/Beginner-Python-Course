# Write a function that counts how many times each word appears in a sentence.
def word_frequencies(text):
    sp_text = text.split()
    word_count = {}
    for w in sp_text:
        word_count[w] = word_count.get(w, 0) + 1
    return word_count

print(word_frequencies("cat dog cat bird"))
# Expected: {'cat': 2, 'dog': 1, 'bird': 1}