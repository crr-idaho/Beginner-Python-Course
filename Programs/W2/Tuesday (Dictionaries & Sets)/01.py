# Write a function that takes a sentence and returns the number of unique words.
def unique_word_counter(sentence):
    return len(set(sentence.split()))

print(unique_word_counter("hello world hello again"))