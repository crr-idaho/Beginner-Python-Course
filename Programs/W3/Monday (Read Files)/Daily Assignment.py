def word_counter(file):
    with open(file, "r") as f:
        text = f.read()
        word = text.split()
        return len(word)

print(word_counter("C:/Users/itzco/Downloads/sample_text.txt"))